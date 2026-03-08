---
layout: homepage
title: Aletheia Blog
permalink: /blog/
---

<h1>Aletheia Blog</h1>
<hr>

<div class="blog-posts">
  {% for post in site.posts %}
    <div class="post-item" style="margin-bottom: 1.8rem;">
      <h2 style="margin-bottom: 0.3rem; font-size: 1.2rem;">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      <p class="post-metadata" style="color: var(--sidebar-text); font-size: 0.85rem; margin-bottom: 0.5rem;">
        {{ post.date | date: "%B %d, %Y" }}
        {% if post.categories %} • {{ post.categories | join: ", " }}{% endif %}
      </p>
      <p class="post-excerpt" style="font-size: 0.9rem; line-height: 1.4; margin-bottom: 0;">
        {% if post.description %}
          {{ post.description | truncatewords: 20 }}
        {% else %}
          {{ post.content | strip_html | truncatewords: 20 }}
        {% endif %}
        <a href="{{ post.url | relative_url }}" style="font-weight: 500; font-size: 0.9rem; margin-left: 5px;">Read more &rarr;</a>
      </p>
    </div>
  {% endfor %}
</div>
