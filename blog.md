---
title: Blog
permalink: /blog/
eyebrow: Blog
subtitle: "Photo notes, research fragments, and a little everyday life."
---

<section class="section page-section">
  <div class="container">
    {% assign published_posts = site.posts | sort: "date" | reverse %}
    {% if published_posts.size > 0 %}
      <div class="post-card-grid blog-grid">
        {% for post in published_posts %}
          <a class="post-card" href="{{ post.url | relative_url }}">
            {% if post.image %}<img src="{{ post.image | relative_url }}" alt="{{ post.title }} cover">{% endif %}
            <div>
              <p class="post-card-tags">{{ post.tags | join: " / " }}</p>
              <h3>{{ post.title }}</h3>
              <p>{{ post.excerpt | strip_html | truncate: 120 }}</p>
            </div>
          </a>
        {% endfor %}
      </div>
    {% else %}
      <div class="empty-state">
        <h2>The notebook is open, but the ink is still drying.</h2>
        <p>Research logs, paper notes, and life fragments will live here.</p>
      </div>
    {% endif %}
  </div>
</section>
