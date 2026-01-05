---
layout: page
title: Collection
permalink: /collection/
description: Browse the complete Fall of the Republic Collection
nav: false
nav_order: 1
published: false
---

<div class="collection-intro">
  <p></p>
</div>

<div class="collection-filters">
  <button class="filter-btn active" data-filter="all">All Coins</button>
  <button class="filter-btn" data-filter="greek">Greek</button>
  <button class="filter-btn" data-filter="republican">Republican</button>
  <button class="filter-btn" data-filter="imperial">Imperial</button>
</div>

<div class="coin-grid">
  {% assign sorted_coins = site.coins | sort: "date_minted" | reverse %}
  {% for coin in sorted_coins %}
    <div class="coin-card" data-period="{{ coin.period | downcase }}">
      <a href="{{ coin.url | relative_url }}">
        <div class="coin-card-images">
          {% if coin.image_aligned %}
            <img src="{{ coin.image_aligned | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }}" style="width: 100%; height: auto;">
          {% else %}
            <div class="coin-card-image">
              {% if coin.image_obverse %}
                <img src="{{ coin.image_obverse | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }} - Obverse">
              {% endif %}
            </div>
            <div class="coin-card-image">
              {% if coin.image_reverse %}
                <img src="{{ coin.image_reverse | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }} - Reverse">
              {% endif %}
            </div>
          {% endif %}
          {% if coin.featured %}
            <span class="featured-badge">★ Featured</span>
          {% endif %}
        </div>
        <div class="coin-card-content">
          <h3 class="coin-card-title">{{ coin.title }}</h3>
        </div>
      </a>
    </div>
  {% endfor %}
</div>

<style>
.collection-intro {
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

.coin-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.coin-card {
  background: var(--global-bg-color);
  border: 1px solid var(--global-divider-color);
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.coin-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.coin-card a {
  text-decoration: none;
  color: inherit;
}

.coin-card-images {
  position: relative;
  display: flex;
  width: 100%;
  background: #f8f8f8;
  gap: 0;
}

.coin-card-image {
  position: relative;
  width: 50%;
  padding-top: 50%;
  overflow: hidden;
}

.coin-card-image img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
}

.featured-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  background: var(--global-theme-color);
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
}

.coin-card-content {
  padding: 1rem;
}

.coin-card-title {
  font-size: 1.1rem;
  margin: 0 0 0.5rem;
  font-weight: 600;
}

.coin-card-description {
  font-size: 0.9rem;
  color: var(--global-text-color-light);
  margin: 0.5rem 0 0;
  line-height: 1.5;
}

.coin-period {
  display: inline-block;
  padding: 0.1rem 0.5rem;
  background: var(--global-theme-color);
  color: white;
  border-radius: 3px;
  font-size: 0.75rem;
  margin-right: 0.5rem;
}

@media (max-width: 768px) {
  .coin-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const coinCards = document.querySelectorAll('.coin-card');
  
  filterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // Update active button
      filterBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      
      const filter = this.dataset.filter;
      
      // Filter coins
      coinCards.forEach(card => {
        if (filter === 'all' || card.dataset.period === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
});
</script>
