---
layout: post
title: "\"Very Rare\": Does the Catalogue Agree With Crawford?"
date: 2026-11-24
description: "Do auction catalogues' scarce, rare and very rare line up with Crawford's die counts? A check of 309 Republican denarius lots."
tags: [rarity, die-counts, auction-catalogues]
published: false   # DRAFT: remove this line (or set true) to publish
---
<!-- DRAFT. Imported verbatim from crawford-bot research/rarity_study_v2/blog_post.md (commit 2e57c12, figures regenerated 2026-11-24 after the Crawford DB fixes). Data, scripts and t-tests live in that repo. -->

Open any auction catalogue of Roman Republican denarii and you will find the same small vocabulary: *scarce*, *rare*, *very rare*. The cataloguers are experts, and the words are not idle. They are also a sales tool. So I asked a simple question: **do those words line up with something the market cannot talk up?**

The yardstick is Michael Crawford's *Roman Republican Coinage* (1974), which estimates how many obverse dies were used to strike each issue. Fewer dies means a smaller issue, and a smaller issue ought to be harder to find. If the words mean anything, lots described as "very rare" should come from issues with fewer dies.

## What I did

I took 536 auction lots of Republican denarii from the ACSearch archive and matched each lot's Crawford number to Crawford's die count. 309 lots (182 different issues) could be matched. I sorted them by the strongest rarity word in the description and compared die counts across the groups.

Because die counts are heavily skewed (a few huge issues, many small ones), I compared them on a log scale, using the *geometric mean*: the typical multiplicative level of a group, not an ordinary average that one 750-die issue can drag around.

| Lot description | Lots | Median dies | Average ± std dev | Geometric mean |
|---|---|---|---|---|
| "Very rare" / "extremely rare" | 41 | 20 | 27 ± 36 | 17 |
| "Rare" | 27 | 30 | 27 ± 19 | 22 |
| "Scarce" | 34 | 32 | 48 ± 35 | 39 |
| No rarity word | 207 | 73 | 121 ± 142 | 72 |

## What it shows

- **The words mean something.** Lots with any rarity word cite issues with about **a third as many dies** as lots with none. That holds when each issue is counted only once, and within a single auction house.
- **There are about three tiers, not four.** "Very rare" and "rare" cannot be told apart statistically. "Scarce" sits between them and silence, with about twice the dies of "rare", although that gap gets thin once each issue is counted once.
- **Groups, not coins.** A random "very rare" lot has fewer dies than a random unlabelled one about 85% of the time. Between "very rare" and "rare" it is 63%, barely better than a coin flip. You cannot read a coin's word off its die count.
- **Silence says little.** Of the 207 lots with no rarity word, 15 cite issues with ten or fewer dies.

## Why not to over-read it

- **Dies are production, not survival.** Rarity is how many coins were struck *and* how many survived 2,000 years. Crawford's die counts, many of them rounded estimates, only speak to the first part.
- **Houses write differently.** In this sample "scarce" never came from the biggest house, and about nine in ten "rare" lots did. House style and coin are tangled together.
- **Same coin, different verdict.** One 10-die issue turns up once as "scarce" and once with no word at all.
- **It's a convenience sample.** The lot text I had was cut off at 350 characters, so some rarity words were missed. That pushes results toward finding *no* difference, so the pattern above is, if anything, understated. The p-values show the pattern is not chance *within this sample*. They do not extend to the market at large.

## How I got here, and what I corrected

My first pass at this, done earlier, did not survive an audit. It compared against a sample that was mostly "coins we never saw", counted the same issue under different labels, and wrongly called "rare" and "scarce" a clean ladder. I rebuilt the comparison from the underlying data: one die count per issue, tests on logs, and each issue counted once as a check.

## Next steps

A better test would use survival evidence: how often an issue turns up in sales per year, or in hoards. That is a bigger job, and it is the natural sequel.

**Bottom line:** believe "very rare" and "rare". Treat "scarce" as a hint. And do not read much into a catalogue that says nothing.
