#!/usr/bin/env python3
"""
Add a book to the bookshelf collection.
Fetches metadata from Open Library API using ISBN or OCLC identifier.

Usage:
    python tools/add_book.py <isbn_or_oclc>
    python tools/add_book.py 9780393635720
    python tools/add_book.py oclc/1195449792
"""

import sys
import re
import json
import urllib.request
import urllib.parse
import ssl
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

# Create SSL context that doesn't verify certificates (for local testing)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


class ISBNSearchParser(HTMLParser):
    """Parse isbnsearch.org HTML to extract book metadata."""
    def __init__(self):
        super().__init__()
        self.data = {}
        self.current_tag = None
        self.in_title = False
        self.in_author = False
        self.in_publisher = False
        self.in_year = False
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'h1' and attrs_dict.get('class') == 'book-title':
            self.in_title = True
        elif tag == 'div' and attrs_dict.get('class') == 'book-author':
            self.in_author = True
        elif tag == 'span' and 'year' in attrs_dict.get('class', ''):
            self.in_year = True
            
    def handle_data(self, data):
        data = data.strip()
        if data:
            if self.in_title:
                self.data['title'] = data
            elif self.in_author:
                if 'by ' in data.lower():
                    self.data['author'] = data.replace('by ', '').replace('By ', '')
                elif 'author' not in self.data:
                    self.data['author'] = data
            elif self.in_year and data.isdigit():
                self.data['year'] = data
                
    def handle_endtag(self, tag):
        if tag in ['h1', 'div', 'span']:
            self.in_title = False
            self.in_author = False
            self.in_year = False


def fetch_isbnsearch(isbn):
    """Fetch book data from isbnsearch.org as fallback."""
    isbn = re.sub(r'[^\d]', '', isbn)
    url = f"https://isbnsearch.org/isbn/{isbn}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10, context=ssl_context) as response:
            html = response.read().decode('utf-8')
        
        # Extract title
        title = 'Unknown Title'
        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', html)
        if title_match:
            title = title_match.group(1).strip()
        
        # Extract author
        author = 'Unknown Author'
        author_match = re.search(r'<strong>Author[s]?:</strong>\s*([^<]+)', html, re.IGNORECASE)
        if author_match:
            author = author_match.group(1).strip()
        
        # Extract year
        year = ''
        year_match = re.search(r'<strong>Published:</strong>\s*([^<]+)', html, re.IGNORECASE)
        if year_match:
            year_text = year_match.group(1).strip()
            year_num = re.search(r'\d{4}', year_text)
            if year_num:
                year = year_num.group(0)
        
        # Try to extract cover image URL
        cover_url = None
        # Look for isbndb.com cover URLs
        cover_match = re.search(r'(https?://[^"\']*isbndb\.com[^"\']*covers[^"\']*\.jpg)', html, re.IGNORECASE)
        if not cover_match:
            # Look for img tags with cover-related attributes
            cover_match = re.search(r'<img[^>]+src="([^"]*book[^"]*cover[^"]*)"', html, re.IGNORECASE)
        if not cover_match:
            cover_match = re.search(r'<img[^>]+class="[^"]*cover[^"]*"[^>]+src="([^"]+)"', html, re.IGNORECASE)
        if not cover_match:
            # Look for any img src with cover in the URL
            cover_match = re.search(r'<img[^>]+src="([^"]*cover[^"]*\.jpg)"', html, re.IGNORECASE)
        if cover_match:
            cover_url = cover_match.group(1)
            if not cover_url.startswith('http'):
                cover_url = 'https://isbnsearch.org' + cover_url
        
        if title != 'Unknown Title' or author != 'Unknown Author':
            return {
                'title': title,
                'author': author,
                'isbn': isbn,
                'publish_year': year,
                'cover_url': cover_url,
                'olid': None
            }
        
        return None
    except Exception as e:
        print(f"Error fetching from ISBNSearch: {e}")
        return None


def slugify(text):
    """Convert text to a valid filename slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '_', text)
    return text.strip('_')


def fetch_openlibrary_by_isbn(isbn):
    """Fetch book data from Open Library using ISBN."""
    isbn = re.sub(r'[^\d]', '', isbn)  # Remove any dashes or spaces
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    
    try:
        with urllib.request.urlopen(url, timeout=10, context=ssl_context) as response:
            data = json.loads(response.read().decode())
            
        # Get work data for additional info
        if 'works' in data and data['works']:
            work_key = data['works'][0]['key']
            work_url = f"https://openlibrary.org{work_key}.json"
            with urllib.request.urlopen(work_url, timeout=10, context=ssl_context) as response:
                work_data = json.loads(response.read().decode())
        else:
            work_data = {}
        
        # Get author data
        authors = []
        if 'authors' in data:
            for author_ref in data['authors']:
                author_url = f"https://openlibrary.org{author_ref['key']}.json"
                with urllib.request.urlopen(author_url, timeout=10, context=ssl_context) as response:
                    author_data = json.loads(response.read().decode())
                    authors.append(author_data.get('name', 'Unknown'))
        
        return {
            'title': data.get('title', work_data.get('title', 'Unknown Title')),
            'author': authors[0] if authors else 'Unknown Author',
            'isbn': isbn,
            'publish_year': data.get('publish_date', '').split()[-1] if data.get('publish_date') else '',
            'olid': data.get('key', '').split('/')[-1] if 'key' in data else None
        }
    except Exception as e:
        print(f"Error fetching from Open Library: {e}")
        return None


def fetch_openlibrary_by_oclc(oclc):
    """Fetch book data from Open Library using OCLC number."""
    oclc = re.sub(r'[^\d]', '', oclc)  # Extract just the number
    url = f"https://openlibrary.org/search.json?q=oclc:{oclc}"
    
    try:
        with urllib.request.urlopen(url, timeout=10, context=ssl_context) as response:
            data = json.loads(response.read().decode())
        
        if data.get('numFound', 0) == 0:
            print("No book found with that OCLC number")
            return None
        
        # Get first result
        book = data['docs'][0]
        
        # Try to get ISBN
        isbn = None
        if 'isbn' in book and book['isbn']:
            isbn = book['isbn'][0]
        
        return {
            'title': book.get('title', 'Unknown Title'),
            'author': book.get('author_name', ['Unknown Author'])[0] if book.get('author_name') else 'Unknown Author',
            'isbn': isbn,
            'publish_year': book.get('first_publish_year', ''),
            'olid': book.get('edition_key', [None])[0]
        }
    except Exception as e:
        print(f"Error fetching from Open Library: {e}")
        return None


def download_cover_image(url, filename):
    """Download cover image from URL."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10, context=ssl_context) as response:
            image_data = response.read()
        
        with open(filename, 'wb') as f:
            f.write(image_data)
        
        return True
    except Exception as e:
        print(f"Error downloading cover image: {e}")
        return False


def create_book_markdown(book_data, books_dir, assets_dir):
    """Create a markdown file for the book."""
    # Generate filename
    author_slug = slugify(book_data['author'].split()[-1])  # Last name
    title_slug = slugify(book_data['title'][:30])  # First 30 chars of title
    filename = f"{author_slug}_{title_slug}.md"
    filepath = books_dir / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"Book file already exists: {filepath}")
        overwrite = input("Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Aborted.")
            return None
    
    # Get current date for the date field
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Build frontmatter
    frontmatter = f"""---
layout: book-review
title: "{book_data['title']}"
author: {book_data['author']}"""
    
    if book_data.get('isbn'):
        frontmatter += f"\nisbn: {book_data['isbn']}"
    elif book_data.get('olid'):
        frontmatter += f"\nolid: {book_data['olid']}"
    
    # Handle cover image download if URL provided
    if book_data.get('cover_url'):
        cover_filename = f"{author_slug}_{title_slug}_cover.jpg"
        cover_path = assets_dir / cover_filename
        print(f"Downloading cover image...")
        if download_cover_image(book_data['cover_url'], cover_path):
            frontmatter += f"\ncover: assets/img/book_covers/{cover_filename}"
            print(f"✓ Cover image saved")
        else:
            # Use default cover if download fails
            frontmatter += f"\ncover: assets/img/book_covers/default_cover.jpg"
            print(f"✓ Using default cover (download failed)")
    else:
        # No cover URL available, use default cover
        frontmatter += f"\ncover: assets/img/book_covers/default_cover.jpg"
        print(f"✓ Using default cover (no cover URL found)")
    
    frontmatter += f"""
categories: 
tags: 
date: {current_date}"""
    
    if book_data.get('publish_year'):
        frontmatter += f"\nreleased: {book_data['publish_year']}"
    
    frontmatter += "\n---\n\n"
    
    # Placeholder content
    content = f"A book by {book_data['author']}.\n"
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write(content)
    
    return filepath


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/add_book.py <isbn_or_oclc>")
        print("Examples:")
        print("  python tools/add_book.py 9780393635720")
        print("  python tools/add_book.py oclc/1195449792")
        sys.exit(1)
    
    identifier = sys.argv[1]
    
    # Determine if it's OCLC or ISBN
    if 'oclc' in identifier.lower():
        print(f"Fetching book data for OCLC: {identifier}...")
        book_data = fetch_openlibrary_by_oclc(identifier)
    else:
        print(f"Fetching book data for ISBN: {identifier}...")
        book_data = fetch_openlibrary_by_isbn(identifier)
        
        # If Open Library fails or returns incomplete data, try ISBNSearch
        if not book_data or book_data.get('author') == 'Unknown Author':
            print("Trying ISBNSearch.org as fallback...")
            isbn_data = fetch_isbnsearch(identifier)
            if isbn_data:
                # Merge data, preferring ISBNSearch for missing fields
                if not book_data:
                    book_data = isbn_data
                else:
                    if book_data.get('author') == 'Unknown Author' and isbn_data.get('author'):
                        book_data['author'] = isbn_data['author']
                    if not book_data.get('publish_year') and isbn_data.get('publish_year'):
                        book_data['publish_year'] = isbn_data['publish_year']
                    if isbn_data.get('cover_url'):
                        book_data['cover_url'] = isbn_data['cover_url']
    
    if not book_data:
        print("Could not fetch book data. Please check the identifier.")
        sys.exit(1)
    
    # Display found data
    print("\nFound book:")
    print(f"  Title: {book_data['title']}")
    print(f"  Author: {book_data['author']}")
    if book_data.get('isbn'):
        print(f"  ISBN: {book_data['isbn']}")
    if book_data.get('olid'):
        print(f"  OLID: {book_data['olid']}")
    if book_data.get('publish_year'):
        print(f"  Published: {book_data['publish_year']}")
    
    # Confirm
    confirm = input("\nCreate book entry? (y/n): ").lower()
    if confirm != 'y':
        print("Aborted.")
        sys.exit(0)
    
    # Get path to _books directory
    script_dir = Path(__file__).parent
    repo_dir = script_dir.parent
    books_dir = repo_dir / '_books'
    assets_dir = repo_dir / 'assets' / 'img' / 'book_covers'
    
    if not books_dir.exists():
        print(f"Creating _books directory at {books_dir}")
        books_dir.mkdir(parents=True)
    
    if not assets_dir.exists():
        print(f"Creating book_covers directory at {assets_dir}")
        assets_dir.mkdir(parents=True)
    
    # Create markdown file
    filepath = create_book_markdown(book_data, books_dir, assets_dir)
    
    if filepath:
        print(f"\n✓ Created: {filepath.relative_to(repo_dir)}")
        print("\nYou can now edit the file to add categories, tags, and description.")


if __name__ == '__main__':
    main()
