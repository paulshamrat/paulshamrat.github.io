---
layout: homepage
title: News
permalink: /news/
---

# News

<ul class="news-list" style="list-style: none; padding: 0;">
  {% assign news_items = site.data.news | sort: 'date' | reverse %}
  {% for item in news_items %}
  <li style="margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid var(--border-color);">
    <strong style="display: block; margin-bottom: 5px; color: var(--accent-color);">{{ item.date | date: "%B %d, %Y" }}</strong>
    {{ item.text }}
  </li>
  {% endfor %}
</ul>
