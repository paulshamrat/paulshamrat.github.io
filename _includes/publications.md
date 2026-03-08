<h2 id="publications" style="margin: 2px 0px -15px;">Publications</h2>
<div class="publications">
  <ol class="bibliography">
    {% for link in site.data.publications.main %}
<li>
  {% include publication_single.md %}
</li>
{% endfor %}
</ol>
</div>

{% include bibtex_script.md %}
