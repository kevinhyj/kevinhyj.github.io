---
title: Projects
permalink: /projects/
eyebrow: Projects
subtitle: "AI4Bio systems, generative models, and scientific agents."
---

<section class="section page-section">
  <div class="container">
    <div class="project-grid all-projects">
      {% assign sorted_works = site.works | sort: "order" %}
      {% for work in sorted_works %}
        {% unless work.hidden %}
          <a class="project-card project-card-{{ work.slug }}" href="{{ work.url | relative_url }}">
            {% if work.image %}<img src="{{ work.image | relative_url }}" alt="{{ work.title }} visual">{% endif %}
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
