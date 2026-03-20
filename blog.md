---
layout: homepage
title: Blog
permalink: /blog/
---

<h1>Blog</h1>
<hr>

<div class="blog-list">
  {% for post in site.posts %}
    <div class="blog-list-item">
      <span class="blog-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      <a href="{{ post.url | relative_url }}" class="blog-title">{{ post.title }}</a>
    </div>
  {% endfor %}
</div>

<style>
.blog-list {
  margin-top: 1rem;
}
.blog-list-item {
  display: flex;
  align-items: baseline;
  gap: 1.2rem;
  padding: 0.45rem 0;
  border-bottom: 1px solid var(--border-color, #eee);
}
.blog-list-item:last-child {
  border-bottom: none;
}
.blog-date {
  font-family: 'Courier New', Courier, monospace;
  font-size: 0.82rem;
  color: #888;
  white-space: nowrap;
  flex-shrink: 0;
  letter-spacing: 0.03em;
}
.blog-title {
  font-size: 0.97rem;
  color: var(--link-color, #1a0dab);
  text-decoration: none;
  line-height: 1.4;
}
.blog-title:hover {
  text-decoration: underline;
}
[data-theme="dark"] .blog-date { color: #888; }
[data-theme="dark"] .blog-title { color: #8ab4f8; }
[data-theme="dark"] .blog-list-item { border-color: #333; }
</style>
