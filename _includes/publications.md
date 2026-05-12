<h2 id="publications" style="margin: 2px 0px -15px;">Publications</h2>
<div class="publication-stats">
  <div class="stat-item">
    <i class="fa-solid fa-book-open"></i>
    <span class="stat-value">{{ site.data.publications.main | size }}</span>
    <span class="stat-label">Publications</span>
  </div>
  <div class="stat-divider"></div>
  <div class="stat-item">
    <i class="fa-solid fa-quote-left"></i>
    <span class="stat-value" id="total-citations-value">
      {% assign total_manual_cites = 0 %}
      {% for pub in site.data.publications.main %}
        {% if pub.manual_citations %}{% assign total_manual_cites = total_manual_cites | plus: pub.manual_citations %}{% endif %}
      {% endfor %}
      {{ total_manual_cites }}
    </span>
    <span class="stat-label">Citations</span>
  </div>
</div>
<div class="publications">
  <div class="pub-table-header">
    <div class="header-title sortable" id="sort-title" onclick="sortPublications('title')">
      Title <i class="fa-solid fa-sort-down sort-icon"></i>
    </div>
    <div class="header-citations sortable" id="sort-citations" onclick="sortPublications('citations')">
      Cited by <i class="fa-solid fa-sort sort-icon" style="opacity: 0.3;"></i>
    </div>
    <div class="header-year sortable" id="sort-year" onclick="sortPublications('year')">
      Year <i class="fa-solid fa-sort sort-icon" style="opacity: 0.3;"></i>
    </div>
  </div>
  <ol class="bibliography">
    {% for link in site.data.publications.main %}
    <li>
      {% include publication_single.md %}
    </li>
    {% endfor %}
  </ol>
</div>

{% include bibtex_script.md %}
