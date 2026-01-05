# Adding New Coins to the Collection

## Quick Start

Use the automated script to add a new coin:

```bash
python tools/add_coin.py \
    "/path/to/Coins/Collection/CoinName/Notes.docx" \
    "/path/to/Coins/Collection/CoinName/Photography/obverse.png" \
    "/path/to/Coins/Collection/CoinName/Photography/reverse.png"
```

## What the Script Does

1. **Extracts text** from your Notes.docx file
2. **Parses metadata** (title, ruler, mint, date, reference, weight, grade, period)
3. **Copies images** to `assets/img/coins/` with standardized naming
4. **Creates aligned image** (side-by-side obverse/reverse on black background)
5. **Generates markdown file** in `_coins/` with all metadata and content

## Manual Process (if needed)

### 1. Prepare Your Materials

- **Notes.docx**: Coin description and metadata
- **obverse.png**: Obverse (front) image
- **reverse.png**: Reverse (back) image

### 2. Copy Images

```bash
cp "/path/to/obverse.png" "assets/img/coins/coin-name-obv.png"
cp "/path/to/reverse.png" "assets/img/coins/coin-name-rev.png"
```

### 3. Create Aligned Image

```bash
python tools/align_coin_images.py \
    assets/img/coins/coin-name-obv.png \
    assets/img/coins/coin-name-rev.png \
    assets/img/coins/coin-name-aligned.png \
    --bg-color black
```

### 4. Create Coin Entry

Create `_coins/coin_name.md`:

```yaml
---
layout: coin
title: "Coin Title Here"
period: Republican           # Greek, Republican, or Imperial
ruler: "Ruler Name"
mint: Rome
denomination: Denarius
date_minted: "110-109 BCE"
reference: "Crawford 301/1"
metal: Silver
weight: "3.99g"
grade: "gVF"
image_obverse: coins/coin-name-obv.png
image_reverse: coins/coin-name-rev.png
image_aligned: coins/coin-name-aligned.png
featured: true              # Shows in showcase and home page
---

Write your coin description here. This is the main content that appears on the coin's detail page.

Add multiple paragraphs with historical context, significance, and interesting details about the coin.
```

## Field Guidelines

### Required Fields
- `layout`: Always use `coin`
- `title`: Full descriptive title
- `period`: `Greek`, `Republican`, or `Imperial` (used for filtering)
- `mint`: City where coin was minted
- `featured`: Set to `true` to show in galleries

### Image Fields
- `image_obverse`: Obverse (front) image
- `image_reverse`: Reverse (back) image  
- `image_aligned`: Combined side-by-side image (created by script)

### Metadata Fields
- `ruler`: Ruler, moneyer, or issuing authority
- `denomination`: Denarius, Aureus, Drachma, etc.
- `date_minted`: Date range or specific date
- `reference`: Crawford, RIC, or other catalog reference
- `metal`: Gold, Silver, Bronze, etc.
- `weight`: With unit (e.g., "3.99g")
- `grade`: Numismatic grade (VF, EF, etc.)

## Notes Document Format

Your `Notes.docx` should follow this structure for best automation:

```
Coin Title – Mint – Date Range

Main descriptive content about the coin's historical significance
and context. Multiple paragraphs are fine.

More historical details and analysis.

Obverse: Description of obverse
Reverse: Description of reverse
Crawford 301/1; BMCRR Rome 526
gVF; 3.99g
```

## Tips

- Use **background-removed images** for best results with aligned images
- The script uses black background by default (use `--bg-color white` for white)
- Filenames are auto-generated from titles (lowercase, underscores)
- Review the generated markdown file and add/edit content as needed
- Only coins with `featured: true` appear on home page and showcase (limit: 6 most recent)

## Display Order

Coins on the home page appear in **reverse chronological order** (newest first), showing the 6 most recently added coins with `featured: true`.

## Example Workflow

```bash
# 1. Navigate to project
cd /Users/jforsyth/Documents/GitHub/photo

# 2. Activate Python environment
source .venv/bin/activate

# 3. Run the automated script
python tools/add_coin.py \
    "/Users/jforsyth/Library/CloudStorage/Dropbox/Coins/Collection/Augustus/Notes.docx" \
    "/Users/jforsyth/Library/CloudStorage/Dropbox/Coins/Collection/Augustus/Photography/obverse.png" \
    "/Users/jforsyth/Library/CloudStorage/Dropbox/Coins/Collection/Augustus/Photography/reverse.png"

# 4. Review generated file
code _coins/augustus_aureus.md

# 5. Test locally
docker compose up

# 6. Commit and push
git add _coins/ assets/img/coins/
git commit -m "Add Augustus Aureus coin"
git push
```
