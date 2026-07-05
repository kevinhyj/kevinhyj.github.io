---
layout: default
title: Home
description: "Yanjie Huang's visual garden for AI4Bio research, projects, and field notes."
---

{% assign settings = site.data.settings %}

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-image">
        <img src="{{ settings.hero.image | relative_url }}" alt="{{ settings.author.name }}'s picture">
      </div>
      <div class="hero-copy">
        <h1>{{ settings.hero.title }}</h1>
        {% if settings.hero.description %}
          <p>{{ settings.hero.description }}</p>
        {% endif %}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <h2>{{ settings.projects.title }}</h2>
        {% if settings.projects.description %}<p>{{ settings.projects.description }}</p>{% endif %}
      </div>
      <a href="{{ '/projects/' | relative_url }}">See all</a>
    </div>

    <div class="project-grid">
      {% assign sorted_works = site.works | sort: "order" %}
      {% for work in sorted_works limit:6 %}
        <a class="project-card project-card-{{ work.slug }}" href="{{ work.url | relative_url }}">
          {% if work.image %}<img src="{{ work.image | relative_url }}" alt="{{ work.title }} visual">{% endif %}
          <div class="card-content">
            <p>{{ work.kind }}</p>
            <h3>{{ work.title }}</h3>
            <span>{{ work.subtitle }}</span>
          </div>
        </a>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <h2>{{ settings.blog.title }}</h2>
        {% if settings.blog.description %}<p>{{ settings.blog.description }}</p>{% endif %}
      </div>
      <a href="{{ '/blog/' | relative_url }}">See all</a>
    </div>

    <div class="post-card-grid">
      {% assign recent_posts = site.posts | sort: "date" | reverse %}
      {% for post in recent_posts limit:3 %}
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
  </div>
</section>
