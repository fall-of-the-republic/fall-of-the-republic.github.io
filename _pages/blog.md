---
layout: page
title: Blog
permalink: /blog/
description: Stories that cut across coins — people, institutions, and ideas that don't fit on a single coin page.
nav: true
nav_order: 3
---

{% assign all_tags = site.posts | map: "tags" | join: "," | split: "," | uniq | sort %}

{% if site.posts.size > 0 %}
  {% if all_tags.size > 1 %}
  <div class="blog-filters">
    <button class="filter-btn active" data-filter="all">All</button>
    {% for tag in all_tags %}{% if tag != "" %}
    <button class="filter-btn" data-filter="{{ tag | slugify }}">{{ tag }}</button>
    {% endif %}{% endfor %}
  </div>
  {% endif %}

  <ul class="blog-roll">
    {% for post in site.posts %}
    <li class="blog-roll-item" {% if post.tags %}data-tag-list="{% for t in post.tags %}{{ t | slugify }}{% unless forloop.last %},{% endunless %}{% endfor %}"{% endif %}>
      <div class="blog-roll-text">
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="blog-roll-meta">
          {{ post.date | date: "%B %-d, %Y" }}
          {% if post.tags.size > 0 %}&middot; {{ post.tags | join: ", " }}{% endif %}
        </p>
        {% if post.description %}<p class="blog-roll-desc">{{ post.description }}</p>{% endif %}
      </div>
      {% if post.coins.size > 0 %}
      <div class="blog-roll-coins">
        {% for slug in post.coins limit: 3 %}
          {% assign coin = site.coins | where: "slug", slug | first %}
          {% if coin and coin.image_obverse %}
            <a href="{{ coin.url | relative_url }}" title="{{ coin.title }}">
              <img src="{{ coin.image_obverse | prepend: '/assets/img/' | relative_url }}" alt="{{ coin.title }}" loading="lazy">
            </a>
          {% endif %}
        {% endfor %}
      </div>
      {% endif %}
    </li>
    {% endfor %}
  </ul>
{% else %}
  <p class="blog-empty">No posts yet.</p>
{% endif %}

<style>
.blog-filters {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.blog-filters .filter-btn {
  padding: 0.35rem 1rem;
  border: 2px solid var(--global-theme-color);
  background: transparent;
  color: var(--global-theme-color);
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
}

.blog-filters .filter-btn:hover,
.blog-filters .filter-btn.active {
  background: var(--global-theme-color);
  color: white;
}

.blog-roll {
  list-style: none;
  padding: 0;
  margin: 0;
}

.blog-roll-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid var(--global-divider-color);
}

.blog-roll-item h3 {
  margin: 0 0 0.25rem;
  font-size: 1.4rem;
}

.blog-roll-meta {
  margin: 0 0 0.5rem;
  font-size: 0.9rem;
  color: var(--global-text-color-light);
}

.blog-roll-desc {
  margin: 0;
  line-height: 1.6;
}

.blog-roll-coins {
  display: flex;
  gap: 0.5rem;
  flex-shrink: 0;
}

.blog-roll-coins img {
  width: 64px;
  height: 64px;
  object-fit: contain;
  background: #000;
  border-radius: 50%;
  padding: 3px;
}

.blog-empty {
  text-align: center;
  font-style: italic;
  color: var(--global-text-color-light);
}

@media (max-width: 576px) {
  .blog-roll-item {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const btns = document.querySelectorAll('.blog-filters .filter-btn');
  const items = document.querySelectorAll('.blog-roll-item');

  btns.forEach(btn => {
    btn.addEventListener('click', function() {
      btns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      const filter = this.dataset.filter;
      items.forEach(item => {
        const tags = (item.dataset.tagList || '').split(',');
        item.style.display = (filter === 'all' || tags.includes(filter)) ? 'flex' : 'none';
      });
    });
  });
});
</script>
