# Adding Coins - AI Assistant Quick Reference

This document is for reminding you (as an AI assistant) about the current best practices for adding coins to the Fall of the Republic collection.

## Standard Workflow (Manual - Preferred)

1. **Create directory:**
   ```bash
   mkdir -p assets/img/coins/coin-name
   ```

2. **Copy images with consistent naming:**
   - `coin-name-obverse.png` (or .jpeg)
   - `coin-name-reverse.png` (or .jpeg)

3. **Create aligned image:**
   ```bash
   python3 tools/align_coin_images.py \
     assets/img/coins/coin-name/coin-name-obverse.png \
     assets/img/coins/coin-name/coin-name-reverse.png \
     assets/img/coins/coin-name/coin-name-aligned.png \
     --bg-color black
   ```

4. **Create markdown file** in `_coins/coin_name.md` with:
   - Correct `period`: `Greek`, `Republican`, `Imperatorial`, or `Imperial`
   - Numeric `sort_date`: negative for BC/BCE, positive for AD/CE
   - Reference link: CRRO for Republican coins, RIC/plain text for Imperial
   - Image paths: `coins/coin-name/coin-name-obverse.png` (no `/assets/img/` prefix)
   - `featured: true` to show in collection

## Critical Details

### sort_date Field
- **Type:** Float (supports decimals)
- **BC/BCE:** Negative value (e.g., `-101` for 101 BC)
- **AD/CE:** Positive value (e.g., `69` for 69 AD)
- **Same year coins:** Use decimals for ordering (69.1, 69.2, 69.3)
- **JavaScript uses:** `parseFloat()` - NOT `parseInt()`

### Period Field (Must Match Exactly)
- `Greek` - Ancient Greek coins
- `Republican` - Roman Republic era (pre-27 BC)
- `Imperatorial` - Roman civil wars/transition period (49-27 BC)
- `Imperial` - Roman Empire (27 BC onwards)

### Reference Links
**Republican & Imperatorial coins:**
```html
<a href="http://numismatics.org/crro/id/rrc-317.3">Crawford 317/3b</a>; BMCRR Rome 1548
```
Only the Crawford number gets the href link.

**Imperial coins:**
```html
RIC I 189; BMCRE 6
```
No href links for Imperial coins.

## Recent Fixes Applied

1. **sort_date field name:** All coins use `sort_date` (not `date_sorted`)
2. **JavaScript parsing:** Updated collection.md to use `parseFloat()` instead of `parseInt()`
3. **Image alignment:** Fixed scripts to preserve fractional sort_date values

## Common sort_date Examples

- Saturnius: `-101` (101 BC)
- Galba: `69.1` (69 AD)
- Otho: `69.2` (69 AD)
- Vitellius: `69.3` (69 AD)

## File Locations

- Coin entries: `_coins/coin_name.md`
- Images: `assets/img/coins/coin-name/`
- Collection page: `_pages/collection.md` (has sorting JS)
- Alignment tool: `tools/align_coin_images.py`
- Automated script: `tools/add_coin.py` (available but manual is faster)

## Checklist for Each Coin

- [ ] Images copied to `assets/img/coins/coin-name/` with correct naming
- [ ] Aligned image created via `align_coin_images.py`
- [ ] Markdown file created in `_coins/`
- [ ] `period` is one of: Greek, Republican, Imperatorial, Imperial
- [ ] `sort_date` is numeric (negative for BC, positive for AD, decimals for same year)
- [ ] Image paths start with `coins/` (no `/assets/img/` prefix)
- [ ] Reference links properly formatted with `<a href>` for Republican coins
- [ ] `featured: true` set if coin should appear in collection
