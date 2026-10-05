# Blog

Blog posts hold stories that cut across coins. Coin pages stay focused on one coin; posts link to several.

## Adding a post

Create `_posts/YYYY-MM-DD-short-title.md`:

```yaml
---
layout: post
title: "Post title"
date: 2026-10-05
description: "One sentence shown on the blog roll."
tags: [grain, senatus-consultum-ultimum]   # shown as filter buttons on /blog/
coins: [saturnius, capio_piso]             # slugs = filenames in _coins/ without .md
---
```

- `coins:` shows thumbnails on the blog roll and a "Coins in this post" strip on the post.
- Each listed coin page automatically gets a "Featured in" link back to the post.
- Footnotes, `{% include figure.liquid %}` and blockquotes work as on coin pages.
- Link to a coin in text with `[Saturnius](/coins/saturnius/)`.

## Promoting a coin essay to a post

Long coin write-ups live better as posts. The coin page keeps only its metadata and a "Related stories" list.

1. Copy the essay (body, footnotes, figures) into a new `_posts/` file, verbatim.
2. Give it `layout: post`, a `title`, a `date` (the original coin post's date works), a one-sentence `description`, and `coins: [slug]`.
3. Delete the body from the coin file, leaving only the front matter.
4. Add `coin_header: true` if the essay was written assuming the coin is on the page; it repeats the obverse and reverse at the top of the post. Skip it for posts written to stand alone.
5. Change relative links such as `../julius_caesar` to `/coins/julius_caesar/`. Relative links break under `/blog/YEAR/`.

The coin page picks up the link automatically; no coin front matter changes.

## Promoted so far

| Post | Coin |
|---|---|
| `2026-01-05-pompey-the-great.md` | faustus_sulla |
| `2026-02-22-who-is-on-the-aqua-marcia-statue.md` | l_marcius_philippus |

## Candidates

- **saturnius** (~3,800 words, 23 footnotes): the largest essay, but still a draft with open `@claude` notes, commented-out sections and uncommitted changes. Promote once finished.
- **Mid-length essays with a single through-line (350–650 words):** julius_caesar, sulla, brutus_ahala, p_licinius_nerva, p_porcius_laeca, neria, pansa_brutus, aemilia_denarius, cassius_longinus_voting, the titurius trio. Short enough that leaving them on the coin page is reasonable.
- Imperial posts (augustus through commodus, ~300–400 words each) read as short biographies; promote only if you want them in the blog roll.

## Not done yet

- RSS: `jekyll-feed` is installed but commented out in `_config.yml` plugins.
- Home page: `latest_posts` in `_pages/about.md` can show recent posts (currently disabled).
