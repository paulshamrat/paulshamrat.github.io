---
layout: homepage
title: CDKL5 Research Hub
description: A constantly updating feed of the latest CDD research, clinical trials, and community news.
permalink: /cdkl5/
published: false
---

<!-- 1. The Newsletter Subscription Box (Clean & Minimal) -->
<div class="newsletter-box text-center" style="background: var(--global-bg-color); border: 1px solid var(--global-divider-color); padding: 20px; border-radius: 8px; margin-bottom: 30px;">
    <h5>Subscribe to the Weekly CDKL5 Digest</h5>
    <p style="font-size: 0.9em; color: var(--global-text-color-light);">Get the top 5 most important updates emailed directly to you every Friday.</p>
    <form action="#" method="post">
        <input type="email" placeholder="Your email address" style="padding: 10px; width: 60%; max-width: 300px; border-radius: 4px; border: 1px solid #ccc;">
        <button type="submit" class="btn btn-primary" style="padding: 10px 20px;">Subscribe</button>
    </form>
</div>

<!-- 2. The Filter Tabs -->
<div class="text-center mb-4">
    <button class="btn btn-sm btn-outline-primary active">All Updates</button>
    <button class="btn btn-sm btn-outline-secondary">🔬 Research Papers</button>
    <button class="btn btn-sm btn-outline-secondary">📰 News & Trials</button>
    <button class="btn btn-sm btn-outline-secondary">🗣️ Community</button>
</div>

<!-- 3. The Content Feed (The Cards) -->
<div class="card-columns">

  {% assign cdkl5_posts = site.cdkl5 | sort: 'date' | reverse %}
  {% if cdkl5_posts.size > 0 %}
    <ul class="list-unstyled mt-3">
    {% for post in cdkl5_posts %}
      <li class="py-2 border-bottom" style="display: flex; align-items: baseline;">
          <!-- Date on the left -->
          <span class="text-muted mr-4" style="font-family: monospace; font-size: 0.9em; min-width: 190px;">
              {{ post.date_range }}
          </span>
          
          <!-- Clickable Title to read the whole story -->
          <h6 class="mb-0" style="font-size: 1.1rem; font-weight: 500;">
            <a href="{{ post.url | relative_url }}" style="color: var(--global-theme-color);">
                {{ post.title }}
            </a>
          </h6>
      </li>
    {% endfor %}
    </ul>
  {% else %}
    <p class="text-center text-muted col-12 mt-4">No digests found. The bot will automatically generate bi-weekly digests here!</p>
  {% endif %}

</div>
