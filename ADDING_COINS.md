# Adding New Coins to the Collection

## Quick Reference: Manual Workflow

For most cases, **manually add coins** using this streamlined process:

```bash
# 1. Create directory
mkdir -p assets/img/coins/coin-name

# 2. Copy images with standardized naming
cp "/path/to/obverse.png" "assets/img/coins/coin-name/coin-name-obverse.png"
cp "/path/to/reverse.png" "assets/img/coins/coin-name/coin-name-reverse.png"

# 3. Create aligned image for grid display
python3 tools/align_coin_images.py \
    assets/img/coins/coin-name/coin-name-obverse.png \
    assets/img/coins/coin-name/coin-name-reverse.png \
    assets/img/coins/coin-name/coin-name-aligned.png \
    --bg-color black

# 4. Create markdown file (see template below)
nano _coins/coin_name.md

# 5. Test and commit
git add _coins/ assets/img/coins/
git commit -m "Add [Coin Name] coin"
git push
```

## Why Manual is Better

The `add_coin.py` script is available but manual addition is faster for our workflow because:
- You control metadata accuracy without parsing text
- Image naming is consistent (`coin-name-obverse.png`, `coin-name-reverse.png`)
- Reference links are precisely formatted
- You can add detailed descriptions directly
- Works with any image format (JPEG, PNG)

## Manual Process (if needed)

### 1. Prepare Your Materials

- **Obverse image**: Front of coin (PNG or JPEG, background removed preferred)
- **Reverse image**: Back of coin (PNG or JPEG, background removed preferred)
- **Metadata**: Title, ruler, mint, date, references, weight, diameter, grade

### 2. Create Directory & Copy Images

```bash
mkdir -p assets/img/coins/coin-name
cp "/source/path/obverse.png" "assets/img/coins/coin-name/coin-name-obverse.png"
cp "/source/path/reverse.png" "assets/img/coins/coin-name/coin-name-reverse.png"
```

**Image naming convention:** `coin-name-obverse.png`, `coin-name-reverse.png`

### 3. Create Aligned Image

```bash
python3 tools/align_coin_images.py \
    assets/img/coins/coin-name/coin-name-obverse.png \
    assets/img/coins/coin-name/coin-name-reverse.png \
    assets/img/coins/coin-name/coin-name-aligned.png \
    --bg-color black
```

This creates a side-by-side image used in the collection grid.

### 4. Create Coin Markdown Entry

Create `_coins/coin_name.md` with this template:

---
layout: coin
title: "Denarius of Julius Caesar"
period: Imperatorial          # Greek, Republican, Imperatorial, or Imperial
ruler: Julius Caesar
mint: Rome
denomination: Denarius
date_minted: "Jan/Feb 44 BCE"
sort_date: -44               # Numeric year (negative for BC/BCE). Use decimals for coins in same year: 69.1, 69.2, 69.3
reference: '<a href="http://numismatics.org/crro/id/rrc-480.5">Crawford 480/5b</a>'  # Link for Republican coins
metal: Silver
weight: "3.80g"
diameter: "19mm"
grade: "Fine"                # Numismatic grade (EF, gVF, VF, Fine, etc.)
image_obverse: coins/coin_name/coin_name-obverse.png
image_reverse: coins/coin_name/coin_name-reverse.png
image_aligned: coins/coin_name/coin_name-aligned.png
obverse_description: "Wreathed head of Caesar right; star behind; CAESAR IM[P]"
reverse_description: "Venus standing left, holding Victory; P SEPVLLIVS behind"
featured: true               # true = shows in collection grid
---

Historical description and context here. Write multiple paragraphs about the coin, its significance, historical context, and any interesting details.

You can use markdown formatting like **bold** and *italic* for emphasis.

## Critical Fields

### Required
- `layout`: Always `coin`
- `title`: Descriptive title (e.g., "Denarius of Julius Caesar")
- `period`: Must be one of: `Greek`, `Republican`, `Imperatorial`, `Imperial`
- `sort_date`: Numeric value for chronological ordering
  - **Negative** for BC/BCE (e.g., `-44` for 44 BC)
  - **Positive** for AD/CE (e.g., `69` for 69 AD)
  - **Decimals** for ordering coins within same year (e.g., `69.1`, `69.2`, `69.3`)

### Image Paths (relative to `/assets/img/`)
- `image_obverse`: `coins/coin-name/coin-name-obverse.png`
- `image_reverse`: `coins/coin-name/coin-name-reverse.png`
- `image_aligned`: `coins/coin-name/coin-name-aligned.png` (auto-generated)

### Reference Links

**For Republican & Imperatorial coins** (CRRO database link on Crawford number only):
```yaml
reference: '<a href="http://numismatics.org/crro/id/rrc-317.3">Crawford 317/3b</a>; BMCRR Rome 1548; RBW 1170'
```

**For Imperial coins** (plain text, no links):
```yaml
reference: 'RIC I 189; BMCRE 6'
```

### Other Important Fields
- `featured`: `true` to include in collection galleries
- `grade`: Numismatic grade (EF = Extremely Fine, VF = Very Fine, Fine, etc.)
- `obverse_description` & `reverse_description`: Brief text describing each side

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

## Quick Reference: Common sort_date Values

Use these for same-year coins (fractional sort_date):
- **69 AD**: Galba (69.1), Otho (69.2), Vitellius (69.3)
- **70 AD**: First coin (70.0), Second coin (70.1), etc.

## Troubleshooting

### Coins not appearing in collection
- Verify `featured: true` is set
- Check `period` matches exactly: `Greek`, `Republican`, `Imperatorial`, or `Imperial`
- Ensure image paths are correct (no `/assets/img/` prefix, always start with `coins/`)

### Sort order is wrong
- Check `sort_date` is numeric (not a string)
- Negative values for BC/BCE: `-101` not `101`
- Use decimals to order multiple coins from same year: `69.1`, `69.2`, etc.

### Images not displaying
- Verify file exists at correct path
- Image path should be: `coins/coin-name/coin-name-obverse.png`
- Restart Jekyll or rebuild with `docker compose up`

### Reference links not working
- For Republican: `http://numismatics.org/crro/id/rrc-317.3` (URL-encoded, match the RRC number)
- For Imperial: RIC references typically don't have URLs, use plain text
- Always wrap in `<a href="...">text</a>` tags
