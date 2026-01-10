#!/usr/bin/env python3
"""
Automated coin addition script for the Jekyll coin collection.

Usage:
    # Process entire folder from Dropbox collection
    python tools/add_coin.py "/path/to/Coins/Collection/CoinName"
    
    # Or process individual files (legacy)
    python tools/add_coin.py <notes_docx> <obverse_image> <reverse_image>

Example:
    python tools/add_coin.py "/Users/jforsyth/Library/CloudStorage/Dropbox/Coins/Collection/AP+MA"
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from PIL import Image
import yaml


def extract_text_from_docx(docx_path):
    """Extract text from a Word document using textutil."""
    result = subprocess.run(
        ['textutil', '-convert', 'txt', '-stdout', docx_path],
        capture_output=True,
        text=True
    )
    return result.stdout


def find_docx_in_folder(folder_path):
    """Find a Word document in the folder."""
    folder = Path(folder_path)
    docx_files = list(folder.glob('*.docx'))
    if not docx_files:
        return None
    return str(docx_files[0])


def find_images_in_photography(folder_path):
    """Find obverse and reverse images in Photography, Media, Photos subfolders, or root folder."""
    folder = Path(folder_path)
    
    # Try multiple possible subdirectories, plus the root folder
    search_dirs = [
        folder / 'Photography',
        folder / 'Media',
        folder / 'Photos',
        folder  # Root folder as fallback
    ]
    
    images = []
    for search_dir in search_dirs:
        if search_dir.exists():
            for file in search_dir.rglob('*') if search_dir != folder else search_dir.glob('*'):
                if file.is_file() and file.suffix.lower() in ['.png', '.jpg', '.jpeg']:
                    images.append((file.name.lower(), str(file)))
    
    if not images:
        return None, None
    
    # Look for background-removed versions first, then any obverse/reverse
    obverse = None
    reverse = None
    
    for img_lower, img_path in sorted(images):
        if 'obverse' in img_lower or 'obv' in img_lower:
            if 'background' in img_lower and not obverse:
                obverse = img_path
            elif not obverse or 'background' not in obverse:
                obverse = img_path
        
        if 'reverse' in img_lower or 'rev' in img_lower:
            if 'background' in img_lower and not reverse:
                reverse = img_path
            elif not reverse or 'background' not in reverse:
                reverse = img_path
    
    return obverse, reverse


def parse_coin_metadata(text):
    """Parse coin metadata from the document text."""
    metadata = {}
    
    # Extract title (first line pattern: "Name – Location – Date")
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]
    if lines:
        first_line = lines[0]
        
        # Try to parse components from first line
        parts = [p.strip() for p in first_line.split('–')]
        if len(parts) >= 3:
            metadata['ruler'] = parts[0]
            metadata['mint'] = parts[1]
            metadata['date_minted'] = parts[2]
        elif len(parts) >= 1:
            metadata['ruler'] = parts[0]
        
        # Extract denomination from first line
        denomination = 'Denarius'  # Default
        if 'denarius' in first_line.lower():
            denomination = 'Denarius'
        elif 'aureus' in first_line.lower():
            denomination = 'Aureus'
        elif 'as' in first_line.lower() and 'cassius' not in first_line.lower():
            denomination = 'As'
        elif 'sestertius' in first_line.lower():
            denomination = 'Sestertius'
        elif 'tetradrachm' in first_line.lower():
            denomination = 'Tetradrachm'
        
        # Generate title as "<denomination> of <ruler>"
        ruler = metadata.get('ruler', parts[0] if parts else 'Unknown')
        metadata['title'] = f"{denomination} of {ruler}"
    
    # Extract reference (RIC, Crawford, etc.)
    ric_match = re.search(r'RIC\s+([^\s]+)\s+(\d+[a-z]?)', text, re.IGNORECASE)
    crawford_match = re.search(r'Crawford\s+(\d+/\d+[a-z]?)', text, re.IGNORECASE)
    
    if ric_match:
        metadata['reference'] = f"RIC {ric_match.group(1)} {ric_match.group(2)}"
    elif crawford_match:
        metadata['reference'] = f"Crawford {crawford_match.group(1)}"
    
    # Extract weight, diameter, and grade from patterns
    weight_match = re.search(r'(\d+\.\d+)g', text)
    if weight_match:
        metadata['weight'] = f"{weight_match.group(1)}g"
    
    diameter_match = re.search(r'(\d+)mm', text)
    if diameter_match:
        metadata['diameter'] = f"{diameter_match.group(1)}mm"
    
    grade_match = re.search(r'\b([gv]?[VEF]{1,3}|EF|VF|Fine|Good Very Fine)\b', text, re.IGNORECASE)
    if grade_match:
        grade_text = grade_match.group(1)
        # Standardize common grades
        grade_map = {
            'ef': 'EF',
            'vf': 'VF',
            'gvf': 'gVF',
            'fine': 'Fine',
            'good very fine': 'Good Very Fine'
        }
        metadata['grade'] = grade_map.get(grade_text.lower(), grade_text)
    
    # Extract period - check for Imperatorial first (more specific)
    if re.search(r'\bImperatorial\b', text, re.IGNORECASE):
        metadata['period'] = 'Imperatorial'
    elif re.search(r'\b(Republic|Republican)\b', text, re.IGNORECASE):
        metadata['period'] = 'Republican'
    elif re.search(r'\bImperial\b', text, re.IGNORECASE):
        metadata['period'] = 'Imperial'
    elif re.search(r'\bGreek\b', text, re.IGNORECASE):
        metadata['period'] = 'Greek'
    
    # Extract obverse and reverse descriptions (from "Obverse:", "Obv:", "Reverse:", "Rev:" patterns)
    obv_match = re.search(r'(?:Obverse|Obv)[:\s]+(.+?)(?=(?:Reverse|Rev)[:\s]|$)', text, re.IGNORECASE | re.DOTALL)
    rev_match = re.search(r'(?:Reverse|Rev)[:\s]+(.+?)(?=Crawford|RIC|VF|EF|Fine|Grade|$)', text, re.IGNORECASE | re.DOTALL)
    
    if obv_match:
        metadata['obverse_description'] = obv_match.group(1).strip()
    
    if rev_match:
        metadata['reverse_description'] = rev_match.group(1).strip()
    
    return metadata


def extract_main_content(text):
    """Extract the main descriptive content from the document, keeping it close to source."""
    lines = text.strip().split('\n')
    
    content_lines = []
    in_content = False
    skip_line_patterns = [
        r'^Obverse:',
        r'^Reverse:',
        r'^Crawford',
        r'^RIC',
        r'^VF|^EF|^Fine',
        r'^Notes?:?$',
        r'^References?:?$',
        r'^\d+g|^\d+mm',
    ]
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Skip first line (title)
        if i == 0:
            continue
        
        # Skip empty lines at start
        if not in_content and not line_stripped:
            continue
        
        # Skip metadata and reference lines
        if any(re.match(pattern, line_stripped, re.IGNORECASE) for pattern in skip_line_patterns):
            continue
        
        # Skip bullet points and notes
        if line_stripped.startswith('•') or line_stripped.startswith('-'):
            continue
        
        # Collect content paragraphs
        if len(line_stripped) > 30:
            in_content = True
            content_lines.append(line_stripped)
    
    # Join with paragraph breaks, keep close to source
    return '\n\n'.join(content_lines)


def create_aligned_image(obv_path, rev_path, output_path, bg_color='black'):
    """Create side-by-side aligned image using PIL with no spacing."""
    # Load images
    obv_img = Image.open(obv_path).convert('RGBA')
    rev_img = Image.open(rev_path).convert('RGBA')
    
    # Use minimum height to match aspect ratios
    target_height = min(obv_img.height, rev_img.height)
    obv_ratio = target_height / obv_img.height
    rev_ratio = target_height / rev_img.height
    
    obv_width = int(obv_img.width * obv_ratio)
    rev_width = int(rev_img.width * rev_ratio)
    
    obv_resized = obv_img.resize((obv_width, target_height), Image.Resampling.LANCZOS)
    rev_resized = rev_img.resize((rev_width, target_height), Image.Resampling.LANCZOS)
    
    # Create side-by-side image with NO spacing (touching)
    total_width = obv_width + rev_width
    total_height = target_height
    
    aligned_img = Image.new('RGB', (total_width, total_height), color=bg_color)
    
    # Paste images side-by-side with no gap
    aligned_img.paste(obv_resized, (0, 0), obv_resized)
    aligned_img.paste(rev_resized, (obv_width, 0), rev_resized)
    
    # Save
    aligned_img.save(output_path, 'PNG')
    return total_width, total_height


def generate_filename(title, folder_name=None, max_length=80):
    """Generate a filename from the coin title or folder name.
    
    Args:
        title: The coin title
        folder_name: Optional folder name to use as fallback if title is too long
        max_length: Maximum filename length (default 80)
    """
    # Remove special characters, convert to lowercase, replace spaces with underscores
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '_', filename)
    
    # If filename is too long, try folder name or truncate
    if len(filename) > max_length:
        if folder_name:
            # Use folder name instead
            filename = re.sub(r'[^\w\s-]', '', folder_name.lower())
            filename = re.sub(r'[-\s]+', '_', filename)
        
        # Still too long? Truncate intelligently at word boundaries
        if len(filename) > max_length:
            filename = filename[:max_length].rsplit('_', 1)[0]
    
    return filename


def generate_sort_date(date_minted_str):
    """Generate a numeric sort_date from date_minted string.
    
    Args:
        date_minted_str: Date string like "101/102 AD", "89 BC", "60* BCE"
    
    Returns:
        Integer sort date (negative for BC/BCE, positive for AD)
    """
    if not date_minted_str:
        return 0
    
    # Extract first number from the string
    year_match = re.search(r'(\d+)', date_minted_str)
    if not year_match:
        return 0
    
    year = int(year_match.group(1))
    
    # Check if BC/BCE (negative) or AD (positive)
    if 'BC' in date_minted_str.upper() or 'BCE' in date_minted_str.upper():
        return -year
    else:
        return year


def load_progress():
    """Load progress tracking file."""
    progress_file = Path(__file__).parent.parent / 'tools' / 'coins_progress.json'
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            return json.load(f)
    return {
        'coins_completed': [],
        'coins_in_progress': [],
        'coins_pending': [],
        'coins_failed': []
    }


def save_progress(progress):
    """Save progress tracking file."""
    progress_file = Path(__file__).parent.parent / 'tools' / 'coins_progress.json'
    with open(progress_file, 'w') as f:
        json.dump(progress, f, indent=2)


def update_progress(coin_name, status):
    """Update progress for a coin."""
    progress = load_progress()
    
    # Remove from other lists
    for key in ['coins_completed', 'coins_in_progress', 'coins_pending', 'coins_failed']:
        if coin_name in progress[key]:
            progress[key].remove(coin_name)
    
    # Add to appropriate list
    if status == 'completed':
        progress['coins_completed'].append(coin_name)
    elif status == 'in_progress':
        progress['coins_in_progress'].append(coin_name)
    elif status == 'failed':
        progress['coins_failed'].append(coin_name)
    
    save_progress(progress)


def main():
    parser = argparse.ArgumentParser(
        description='Add coins to the collection (folder or legacy mode)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process coin folder (new method)
  python tools/add_coin.py "/path/to/Coins/Collection/CoinName"
  
  # Legacy method with individual files
  python tools/add_coin.py notes.docx obverse.png reverse.png
        """)
    
    parser.add_argument('input', help='Coin folder path OR path to notes.docx file')
    parser.add_argument('obverse', nargs='?', help='(Legacy) Path to obverse image')
    parser.add_argument('reverse', nargs='?', help='(Legacy) Path to reverse image')
    parser.add_argument('--bg-color', default='black', choices=['black', 'white', 'gray'],
                       help='Background color for aligned image (default: black)')
    parser.add_argument('--force', action='store_true',
                       help='Force reprocessing of already completed coins')
    
    args = parser.parse_args()
    
    # Detect mode: folder vs legacy
    input_path = Path(args.input)
    is_folder = input_path.is_dir()
    is_docx = input_path.suffix.lower() == '.docx'
    
    if is_folder:
        # Folder mode - new workflow
        process_coin_folder(input_path, args.bg_color, force=args.force)
    elif is_docx and args.obverse and args.reverse:
        # Legacy mode - individual files
        process_legacy_mode(args.input, args.obverse, args.reverse, args.bg_color)
    else:
        print("❌ Invalid input. Use either:")
        print("   1. Folder: python tools/add_coin.py /path/to/CoinFolder")
        print("   2. Legacy: python tools/add_coin.py notes.docx obverse.png reverse.png")
        sys.exit(1)


def process_coin_folder(folder_path, bg_color, force=False):
    """Process a coin folder from Dropbox collection."""
    folder_path = Path(folder_path)
    coin_name = folder_path.name
    
    print(f"\n🪙  Processing: {coin_name}")
    
    # Load progress
    progress = load_progress()
    
    # Check if already completed
    if not force and coin_name in progress['coins_completed']:
        print(f"✅ Already completed. Skipping.")
        return
    
    # Mark as in progress
    update_progress(coin_name, 'in_progress')
    
    # Find files
    print("🔍 Finding files...")
    docx_path = find_docx_in_folder(folder_path)
    obv_path, rev_path = find_images_in_photography(folder_path)
    
    if not docx_path:
        print(f"❌ No Word document found in {folder_path}")
        update_progress(coin_name, 'failed')
        return
    
    if not obv_path or not rev_path:
        print(f"❌ Could not find both obverse and reverse images in Photography folder")
        print(f"   Obverse: {obv_path}, Reverse: {rev_path}")
        update_progress(coin_name, 'failed')
        return
    
    try:
        # Extract and parse
        print("📄 Extracting text...")
        text = extract_text_from_docx(docx_path)
        
        print("🔍 Parsing metadata...")
        metadata = parse_coin_metadata(text)
        content = extract_main_content(text)
        
        # Ask user for filename
        print(f"\n📋 Coin title: {metadata.get('title', coin_name)}")
        print(f"📁 Suggested from folder: {coin_name.lower().replace(' ', '_').replace('+', '_')}")
        filename = input("\n✏️  Enter filename for .md file and media folder (e.g., 'titus' or 'trajan'): ").strip()
        
        if not filename:
            print("❌ No filename provided. Using folder name as fallback.")
            filename = coin_name.lower().replace(' ', '_').replace('+', '_')
        
        # Clean filename
        filename = re.sub(r'[^\w\s-]', '', filename.lower())
        filename = re.sub(r'[-\s]+', '_', filename)
        
        # Setup paths
        project_root = Path(__file__).parent.parent
        coins_dir = project_root / '_coins'
        img_dir = project_root / 'assets' / 'img' / 'coins' / filename
        
        coins_dir.mkdir(exist_ok=True)
        img_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy images
        print("🖼️  Copying images...")
        obv_dest = img_dir / f"{filename}-obv.png"
        rev_dest = img_dir / f"{filename}-rev.png"
        aligned_dest = img_dir / f"{filename}-aligned.png"
        
        shutil.copy(obv_path, obv_dest)
        shutil.copy(rev_path, rev_dest)
        
        # Create aligned image
        print("⚙️  Creating aligned image...")
        width, height = create_aligned_image(str(obv_dest), str(rev_dest), str(aligned_dest), bg_color)
        
        # Create markdown
        print("📝 Creating markdown file...")
        md_path = coins_dir / f"{filename}.md"
        
        # Extract denomination and metal from title or default
        denomination = 'Denarius'  # Default
        if 'denarius' in metadata.get('title', '').lower():
            denomination = 'Denarius'
        elif 'aureus' in metadata.get('title', '').lower():
            denomination = 'Aureus'
        elif 'as' in metadata.get('title', '').lower():
            denomination = 'As'
        
        metal = 'Silver'  # Default
        if 'gold' in text.lower() or 'aureus' in metadata.get('title', '').lower():
            metal = 'Gold'
        elif 'bronze' in text.lower() or 'copper' in text.lower() or 'as' in metadata.get('title', '').lower():
            metal = 'Bronze'
        
        # Generate sort_date for chronological ordering
        sort_date = generate_sort_date(metadata.get('date_minted', ''))
        
        # Build frontmatter using proper YAML escaping
        frontmatter_dict = {
            'layout': 'coin',
            'title': metadata.get('title', 'Unknown Coin'),
            'period': metadata.get('period', 'Imperial'),
            'ruler': metadata.get('ruler', ''),
            'mint': metadata.get('mint', 'Rome'),
            'denomination': denomination,
            'date_minted': metadata.get('date_minted', ''),
            'sort_date': sort_date,
            'reference': metadata.get('reference', ''),
            'metal': metal,
            'weight': metadata.get('weight', ''),
            'diameter': metadata.get('diameter', ''),
            'grade': metadata.get('grade', ''),
            'image_obverse': f"coins/{filename}/{obv_dest.name}",
            'image_reverse': f"coins/{filename}/{rev_dest.name}",
            'image_aligned': f"coins/{filename}/{aligned_dest.name}",
            'obverse_description': metadata.get('obverse_description', ''),
            'reverse_description': metadata.get('reverse_description', ''),
            'featured': True
        }
        
        # Use yaml.dump for proper formatting, then wrap with --- markers
        yaml_content = yaml.dump(frontmatter_dict, default_flow_style=False, allow_unicode=True, sort_keys=False)
        frontmatter = f"---\n{yaml_content}---\n"
        
        # Add content without section headers (keep simple)
        if content:
            frontmatter += content.strip()
            frontmatter += '\n'
        
        md_path.write_text(frontmatter)
        
        print(f"\n✅ Successfully added: {metadata.get('title')}")
        print(f"   Coin: {filename}")
        print(f"   Markdown: {md_path.relative_to(project_root)}")
        print(f"   Images: {obv_dest.name}, {rev_dest.name}, {aligned_dest.name} ({width}x{height}px)")
        
        # Update progress
        update_progress(coin_name, 'completed')
        print(f"\n📊 Progress saved!")
        
    except Exception as e:
        print(f"\n❌ Error processing {coin_name}: {e}")
        import traceback
        traceback.print_exc()
        update_progress(coin_name, 'failed')


def process_legacy_mode(docx_path, obv_path, rev_path, bg_color):
    """Legacy mode - process individual files."""
    print("⚠️  Using legacy mode (individual files)")
    
    # Validate input files exist
    for path in [docx_path, obv_path, rev_path]:
        if not os.path.exists(path):
            print(f"Error: File not found: {path}")
            sys.exit(1)
    
    # Extract and parse
    print("📄 Extracting text...")
    text = extract_text_from_docx(docx_path)
    
    print("🔍 Parsing metadata...")
    metadata = parse_coin_metadata(text)
    content = extract_main_content(text)
    
    # Generate filename
    filename = generate_filename(metadata.get('title', 'unknown'))
    
    # Setup paths
    project_root = Path(__file__).parent.parent
    coins_dir = project_root / '_coins'
    img_dir = project_root / 'assets' / 'img' / 'coins' / filename
    
    coins_dir.mkdir(exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy images
    print("🖼️  Copying images...")
    obv_dest = img_dir / f"{filename}-obv.png"
    rev_dest = img_dir / f"{filename}-rev.png"
    aligned_dest = img_dir / f"{filename}-aligned.png"
    
    shutil.copy(obv_path, obv_dest)
    shutil.copy(rev_path, rev_dest)
    
    # Create aligned image
    print("⚙️  Creating aligned image...")
    create_aligned_image(str(obv_dest), str(rev_dest), str(aligned_dest), bg_color)
    
    # Create markdown
    print("📝 Creating markdown file...")
    md_path = coins_dir / f"{filename}.md"
    
    # Build frontmatter using proper YAML escaping
    frontmatter_dict = {
        'layout': 'coin',
        'title': metadata.get('title', 'Unknown Coin'),
        'period': metadata.get('period', 'Imperial'),
        'ruler': metadata.get('ruler', ''),
        'mint': metadata.get('mint', 'Rome'),
        'denomination': 'Denarius',
        'date_minted': metadata.get('date_minted', ''),
        'reference': metadata.get('reference', ''),
        'metal': 'Silver',
        'weight': metadata.get('weight', ''),
        'diameter': metadata.get('diameter', ''),
        'grade': metadata.get('grade', ''),
        'image_obverse': f"coins/{filename}/{obv_dest.name}",
        'image_reverse': f"coins/{filename}/{rev_dest.name}",
        'image_aligned': f"coins/{filename}/{aligned_dest.name}",
        'obverse_description': metadata.get('obverse_description', ''),
        'reverse_description': metadata.get('reverse_description', ''),
        'featured': True
    }
    
    # Use yaml.dump for proper formatting, then wrap with --- markers
    yaml_content = yaml.dump(frontmatter_dict, default_flow_style=False, allow_unicode=True, sort_keys=False)
    frontmatter = f"---\n{yaml_content}---\n"
    
    if content:
        frontmatter += content.strip() + '\n'
    
    md_path.write_text(frontmatter)
    
    print(f"\n✅ Successfully added coin: {metadata.get('title')}")
    print(f"   Markdown file: {md_path.relative_to(project_root)}")
    print(f"   Images: {obv_dest.name}, {rev_dest.name}, {aligned_dest.name}")


if __name__ == '__main__':
    main()
