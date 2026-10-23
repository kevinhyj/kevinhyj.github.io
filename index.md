---
layout: default
title: Home
description: "Yanjie Huang (黄䶮杰) is an undergraduate researcher at Shanghai Jiao Tong University building self-improving AI systems for automated research through post-training, synthetic data, test-time search, and experimental feedback."
---

{% assign settings = site.data.settings %}

<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-image">
        {% capture hero_alt %}{{ settings.author.name }}'s picture{% endcapture %}
        {% include responsive-photo.html src=settings.hero.image alt=hero_alt sizes="(max-width: 900px) 100vw, 42vw" fetchpriority="high" %}
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

<section class="section research-intro" aria-labelledby="research-statement">
  <div class="container">
    <p class="eyebrow">Research interests</p>
    <h2 id="research-statement">I build self-improving AI systems for automated research.</h2>
    <p class="research-summary">My work connects algorithm design with scientific discovery, from multimodal generation and ML engineering to biomolecular design.</p>
    <div class="research-directions">
      <div>
        <h3>Learning from generated experience</h3>
        <p>How can self-generated feedback and synthetic data improve models through post-training?</p>
      </div>
      <div>
        <h3>Scaling computation at test time</h3>
        <p>How can search and computation scale efficiently for reasoning, design, and optimization?</p>
      </div>
      <div>
        <h3>Learning through interaction</h3>
        <p>How can computational and experimental feedback enable continual model improvement and scientific discovery?</p>
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
        {% unless work.hidden %}
          <a class="project-card project-card-{{ work.slug }}" href="{{ work.url | relative_url }}">
            {% if work.image %}{% include project-card-image.html src=work.image alt=work.title %}{% elsif work.status == "In progress" %}<div class="project-placeholder" role="img" aria-label="{{ work.title }} image coming soon">?</div>{% endif %}
            <div class="card-content">
              <p>{{ work.kind }}{% if work.status == "In progress" %}<span class="project-status">In progress</span>{% endif %}</p>
              <h3>{{ work.title }}</h3>
              <span>{{ work.subtitle }}</span>
            </div>
          </a>
        {% endunless %}
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
          {% if post.image %}{% include responsive-photo.html src=post.image alt=post.title sizes="(max-width: 560px) 100vw, (max-width: 900px) 50vw, 33vw" %}{% endif %}
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
