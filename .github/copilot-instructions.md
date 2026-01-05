# Ancient Coin Collection Website - AI Coding Instructions

## Project Overview
This is a Jekyll-based coin collection showcase website, adapted from the al-folio academic theme. It displays ancient Greek and Roman coins with image galleries, detailed metadata, and filtering capabilities.

## Architecture & Key Components

### Jekyll Core Structure
- **Liquid templates** in `_includes/` and `_layouts/` render content
- **Coins collection** in `_coins/` - main content type (markdown files with coin metadata)
- **Custom coin layout** `_layouts/coin.liquid` displays individual coin pages with obverse/reverse images
- **Configuration** `_config.yml` - Central config for site metadata and collections

### Content Organization
- **Coins** (`_coins/*.md`): Individual coin entries with frontmatter metadata and descriptions
- **Pages** (`_pages/*.md`): Main site pages (home, collection, showcase, about)
- **Images** (`assets/img/coins/`): Coin photographs (obverse, reverse, details)
- **Configuration** (`_config.yml`): Site settings, collection config

### Coin Entry Format
Each coin is a markdown file in `_coins/` with this structure:

```yaml
---
layout: coin
title: "Denarius of Julius Caesar"
period: Imperatorial          # Greek, Republican, Imperatorial, or Imperial
ruler: Julius Caesar
mint: Rome
denomination: Denarius
date_minted: "Jan/Feb 44 BC"
reference: '<a href="...">Crawford 480/5b</a>'  # Can include HTML links
metal: Silver
weight: "3.80g"
diameter: "19mm"
grade: "Fine"                 # Numismatic grade (EF, gVF, Fine, etc.)
image_obverse: coins/julius_caesar/caesar-obv.png
image_reverse: coins/julius_caesar/caesar-rev.png
image_aligned: coins/julius_caesar/caesar-aligned.png  # Side-by-side obverse/reverse
obverse_description: "Wreathed head of Caesar right; star behind; CAESAR IM[P]"
reverse_description: "Venus standing left, holding Victory; P SEPVLLIVS behind"
featured: true                # Shows in showcase and featured galleries
---

Historical description and context here. Can include HTML embeds like videos and figures.
```

**Field Notes:**
- `image_obverse`/`image_reverse`: Required for detail pages (uses `coin.liquid` layout)
- `image_aligned`: Optional but recommended for collection grid display (side-by-side on black background)
- `period`: Must match filter values exactly (`Greek`, `Republican`, `Imperatorial`, `Imperial`). Note: `Imperatorial` is the transition period between Republican and Imperial eras (late Roman civil wars).
- `reference`: Use standard numismatic citations; can include HTML `<a>` tags for linking
- Markdown body supports HTML: videos (`video.liquid`), figures (`figure.liquid`), blockquotes

### Site Pages
Three main pages in `_pages/`:
- `about.md` - Homepage with collection overview
- `collection.md` - Featured coins gallery and main entry point; `_collection.md` (unpublished) has full collection with filtering
- `about-collection.md` - About the collection and collecting philosophy

## Python Automation Tools

The project includes two powerful Python scripts in `tools/` to streamline coin additions:

### `add_coin.py` - Complete Coin Addition
Extracts metadata from Word documents, processes images, and generates markdown:
```bash
python tools/add_coin.py <notes_docx> <obverse_image> <reverse_image>
```
**Workflow:** Reads Notes.docx (coin description + metadata) → Parses fields → Copies/processes images → Generates aligned coin image → Creates `_coins/coinname.md`

### `align_coin_images.py` - Image Processing
Creates side-by-side obverse/reverse images on black background (required for grid display):
```bash
python tools/align_coin_images.py obverse.png reverse.png output.png --bg-color black
```

**Integration:** `add_coin.py` calls this automatically; manual use only if updating images after coin creation.

## Development Workflows

### Local Development
**Docker (recommended):**
```bash
docker compose pull
docker compose up  # Site at http://localhost:8080
```
Slim image: `docker compose -f docker-compose-slim.yml up`

**Manual (legacy, not recommended):**
```bash
bundle install
bundle exec jekyll serve  # Site at http://localhost:4000
```

**Live reload:** Docker setup includes `--livereload` and watches `_config.yml` changes (auto-restarts Jekyll)

### Making Changes
- **Config changes** (`_config.yml`): Require Jekyll restart or rebuild
- **Content/template changes**: Auto-reload in Docker, or refresh browser
- **Before committing**: Code is auto-formatted by Prettier via GitHub Actions (`.github/workflows/prettier.yml`)

### Deployment
- **GitHub Actions** (`.github/workflows/deploy.yml`): Auto-deploys on push to main/master
- Builds site → pushes to `gh-pages` branch → GitHub Pages serves it
- Deployment takes ~4 min; then `pages-build-deployment` action (~45s) finalizes
- **Critical config**: Set `url` to `https://<username>.github.io`, leave `baseurl` empty for user/org sites

## Project-Specific Patterns

### Adding a New Coin
1. Create markdown file in `_coins/` (e.g., `hadrian_denarius.md`)
2. Add coin images to `assets/img/coins/`
3. Fill out frontmatter with metadata (see format above)
4. Write description in markdown body
5. Set `featured: true` to show in showcase gallery

### Filtering System
The collection page uses JavaScript to filter coins by period:
- **Coin frontmatter:** Period stored as capitalized values (`Greek`, `Republican`, `Imperatorial`, `Imperial`)
- **HTML attribute:** `data-period="{{ coin.period | downcase }}"` converts to lowercase for matching
- **Filter buttons:** Target lowercase values (`greek`, `republican`, `imperial`)
- **JavaScript logic:** `if (filter === 'all' || card.dataset.period === filter)` matches button clicks
- **Add new period:** Update frontmatter in coins + add filter button in `_pages/_collection.md` + update JavaScript

### Image Display
- **Grid view**: `coin-card-image` CSS creates square containers with centered images
- **Individual pages**: Side-by-side obverse/reverse display in `coin.liquid` layout
- **Responsive**: Images scale on mobile, cards stack vertically

### Styling Conventions
- Coin-specific CSS embedded in page files (collection.md, showcase.md)
- Layout styling in `_layouts/coin.liquid`
- Uses CSS variables: `--global-theme-color`, `--global-bg-color`, `--global-text-color`
- Dark/light mode support inherited from al-folio theme

## Common Tasks

### Add Multiple Coins
1. For each coin, create `_coins/coinname.md` with proper naming: lowercase, underscores (e.g., `tiberius_tribute.md`)
2. Copy images to `assets/img/coins/coin-name/` subdirectory
3. Set appropriate `period` for filtering (must exactly match one of: Greek, Republican, Imperatorial, Imperial)

### Customize Colors
- Theme color: Edit `--global-theme-color` in `_sass/_themes.scss`
- Period-specific styles: Defined in collection grid `_collection.md`
- Card hover effects: Modify `.coin-card:hover` styling

## Disabled Features

These al-folio features are turned off:
- ❌ Blog posts / pagination
- ❌ Publications / bibliography
- ❌ CV page
- ❌ News announcements  
- ❌ Projects collection
- ❌ External RSS feeds
- ❌ Social media integrations
- ❌ Comments (Giscus/Disqus)
- ❌ Newsletter signup

## Troubleshooting

### Images Not Showing
- Verify image path starts with `coins/` (relative to `/assets/img/`)
- Check file exists: `assets/img/coins/filename.jpg`
- Image paths in frontmatter shouldn't include `/assets/img/` prefix

### Filters Not Working
- Check `data-period` attribute matches filter values exactly
- Ensure JavaScript is loading (check browser console)
- Period must be lowercase: `greek`, `republican`, `imperial`

### Card Layout Issues
- Grid uses CSS Grid with `repeat(auto-fill, minmax(280px, 1fr))`
- Adjust minmax value in collection.md for different card sizes
- Cards auto-wrap on narrow screens

## Key Files Reference
- [_config.yml](../_config.yml) - Site configuration
- [_layouts/coin.liquid](../_layouts/coin.liquid) - Individual coin page template
- [_pages/collection.md](../_pages/collection.md) - Main collection grid
- [_coins/](../_coins/) - Coin markdown entries directory
- [assets/img/coins/](../assets/img/coins/) - Coin images directory

## Additional Resources
- [Jekyll Collections](https://jekyllrb.com/docs/collections/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Original al-folio Theme](https://github.com/alshedivat/al-folio)
