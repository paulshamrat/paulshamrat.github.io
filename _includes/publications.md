<h2 id="publications" style="margin: 2px 0px -15px;">Publications</h2>
<div class="publications">
  <div class="pub-table-header">
    <div class="header-title">Title</div>
    <div class="header-citations">Cited by</div>
    <div class="header-year">Year</div>
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
