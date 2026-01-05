---
layout: about
title: Home
permalink: /
subtitle: 

selected_papers: false
social: true

announcements:
  enabled: false

latest_posts:
  enabled: false
---
## Introduction and Welcome
This collection and blog are an extension of the work on our [Instagram](https://www.instagram.com/jasonsancientcoins/). Often, when composing those posts, I find that significant historical and numismatic information cannot be included within the 2,000-character limit. Here, we have no such limits and can explore the deep connections between ancient Roman coins, primary sources, and modern scholarship.

This collection was originally inspired by Suetonius' Twelve Caesars, and completing that set of coins was the first goal. Over time, we have focused on the late Republic as it offers an expressive numismatic template that revels in its ancestral history, engages with the challenges of its day, and provides intriguing scholarship and narrative for today. The parameters of the forthcoming collection will be tentatively from the Gracchi (~133 BCE) to Caesar (~49 BCE); however, already completed sets and other coins of interest will be included.

Our work is inspired by several sources. We strive to provide accessible and intelligent historical writing following [Garrett Ryan's Toldinstone](https://toldinstone.com/) and [Gareth Harney's Moneta](https://www.harneycoins.com/), while grounding everything in the latest scholarship and led by primary sources like [Liv Yarrow's Adventures in My Head](https://livyarrow.org/). The narrative format with extensive footnotes follows [Bret Devereaux's A Collection of Unmitigated Pedantry](https://acoup.blog/). Insights into the modern coin trade are from [Aaron Berk's Ancient Coin Podcast](https://www.youtube.com/playlist?list=PLi8uAYychtLcENn1Xo4NrBTN9m1GC8tDu).

Below are some well-documented coins within the collection. All coins are available on the [Collection](collection/) page. All images and text are copyright the author, unless otherwise indicated. 

<div class="showcase-gallery">
  {% assign featured_coins = site.coins | where: "featured", true %}
  {% for coin in featured_coins %}
    <div class="showcase-item" data-sort-date="{{ coin.sort_date }}">
      <a href="{{ coin.url | relative_url }}">
        {% if coin.image_aligned %}
          <img src="{{ coin.image_aligned | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }}">
        {% elsif coin.image_obverse %}
          <img src="{{ coin.image_obverse | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }}">
        {% endif %}
        <div class="showcase-overlay">
          <h3>{{ coin.title }}</h3>
          <p>{{ coin.date_minted }} • {{ coin.reference }}</p>
        </div>
      </a>
    </div>
  {% endfor %}
</div>

<div style="text-align: center; margin-top: 3rem;">
  <a href="{{ '/collection/' | relative_url }}" class="btn" style="display: inline-block; padding: 0.75rem 2rem; background: #3b82f6; color: white; text-decoration: none; border-radius: 4px; font-weight: 600;">Browse the Collection</a>
</div>

<style>
.showcase-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.showcase-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
  background: #000000;
  padding: 1rem;
}

.showcase-item:hover {
  transform: scale(1.02);
}

.showcase-item img {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
}

.showcase-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: #ffffff !important;
  padding: 2rem 1rem 1rem;
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.showcase-item:hover .showcase-overlay {
  transform: translateY(0);
}

.showcase-overlay h3 {
  margin: 0 0 0.5rem;
  font-size: 1.2rem;
  color: #ffffff !important;
}

.showcase-overlay p {
  margin: 0;
  font-size: 0.9rem;
  opacity: 0.9;
  color: #ffffff !important;
}

.showcase-item a {
  text-decoration: none;
  color: inherit;
}

@media (max-width: 768px) {
  .showcase-gallery {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const showcaseGallery = document.querySelector('.showcase-gallery');
  const showcaseItems = Array.from(document.querySelectorAll('.showcase-item'));
  
  // Sort coins by sort_date numerically (oldest to newest)
  showcaseItems.sort((a, b) => {
    const dateA = parseInt(a.dataset.sortDate);
    const dateB = parseInt(b.dataset.sortDate);
    return dateA - dateB;
  });
  
  // Re-append items in sorted order
  showcaseItems.forEach(item => showcaseGallery.appendChild(item));
});
</script>
