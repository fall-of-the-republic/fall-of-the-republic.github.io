---
layout: page
title: Collection
permalink: /collection/
description: Browse the complete Fall of the Republic Collection
nav: true
nav_order: 2
---

<div class="showcase-intro">
  <p></p>
</div>

<div class="collection-filters">
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="republican">Republican</button>
  <button class="filter-btn" data-filter="imperatorial">Imperatorial</button>
  <button class="filter-btn" data-filter="imperial">Imperial</button>
</div>

<div class="showcase-gallery">
  {% assign featured_coins = site.coins %}
  {% for coin in featured_coins %}
    <div class="showcase-item" data-sort-date="{{ coin.sort_date }}" data-period="{{ coin.period | downcase }}">
      <a href="{{ coin.url | relative_url }}">
        {% if coin.image_aligned %}
          {% assign img_path = coin.image_aligned | remove: '.png' | remove: '.jpg' %}
          <picture>
            <source
              srcset="{% for i in site.imagemagick.widths %}{{ img_path | prepend: '/assets/img/' | relative_url }}-{{ i }}.webp {{ i }}w,{% endfor %}"
              type="image/webp"
              sizes="700px"
            >
            <img src="{{ coin.image_aligned | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }}" width="700" height="350" loading="lazy">
          </picture>
        {% elsif coin.image_obverse %}
          {% assign img_path = coin.image_obverse | remove: '.png' | remove: '.jpg' %}
          <picture>
            <source
              srcset="{% for i in site.imagemagick.widths %}{{ img_path | prepend: '/assets/img/' | relative_url }}-{{ i }}.webp {{ i }}w,{% endfor %}"
              type="image/webp"
              sizes="400px"
            >
            <img src="{{ coin.image_obverse | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }}" width="400" height="400" loading="lazy">
          </picture>
        {% endif %}
        <div class="showcase-overlay">
          <h3>{{ coin.title }}</h3>
          <p>{{ coin.date_minted }} • {{ coin.reference }}</p>
        </div>
      </a>
    </div>
  {% endfor %}
</div>

<style>
.showcase-intro {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 3rem;
  font-size: 1.1rem;
  color: var(--global-text-color-light);
}

.collection-filters {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.5rem 1.5rem;
  border: 2px solid var(--global-theme-color);
  background: transparent;
  color: var(--global-theme-color);
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
}

.filter-btn:hover,
.filter-btn.active {
  background: var(--global-theme-color);
  color: white;
}

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
  border: none;
  padding: 1rem;
  aspect-ratio: 2 / 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.showcase-item:hover {
  transform: scale(1.02);
}

.showcase-item img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  content-visibility: auto;
}

.showcase-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: #ffffff;
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
    const dateA = parseFloat(a.dataset.sortDate);
    const dateB = parseFloat(b.dataset.sortDate);
    return dateA - dateB;
  });
  
  // Re-append items in sorted order
  showcaseItems.forEach(item => showcaseGallery.appendChild(item));
  
  // Filter functionality
  const filterBtns = document.querySelectorAll('.filter-btn');
  
  filterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // Update active button
      filterBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      
      const filter = this.dataset.filter;
      
      // Filter coins
      showcaseItems.forEach(item => {
        if (filter === 'all' || item.dataset.period === filter) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
});
</script>
