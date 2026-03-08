<div class="pub-row" style="display: flex; flex-direction: row; margin-bottom: 1.5rem;">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 15px;padding-left: 15px;">
    {% if link.image %}
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width: 100px; height: auto;">
    {% if link.conference_short %}
    <abbr class="badge">{{ link.conference_short }}</abbr>
    {% endif %}
    {% endif %}
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
    <div class="title" style="font-weight: bold;">
      <a href="{% if link.html %}{{ link.html }}{% elsif link.doi %}https://doi.org/{{ link.doi }}{% else %}{{ link.pdf }}{% endif %}" target="_blank">
        {{ link.title }}
      </a>
    </div>
    <div class="author" style="font-size: 0.9rem;">
      {{ link.authors | replace: "Paul, S.K.", "<strong>Paul, S.K.</strong>" | replace: "Paul, S. K.", "<strong>Paul, S. K.</strong>" | replace: "Shamrat Kumar Paul", "<strong>Shamrat Kumar Paul</strong>" }}
    </div>
    <div class="periodical" style="font-size: 0.9rem;">
      <em>{{ link.conference }}</em> {% if link.year %}({{ link.year }}){% endif %}
    </div>
    <div class="links" style="margin-top: 5px;">
      {% if link.pdf %}
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">PDF</a>
      {% endif %}
      {% if link.doi %}
      <a href="https://doi.org/{{ link.doi }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">DOI</a>
      {% endif %}
      {% if link.bibtex %}
      <a class="bibtex btn btn-sm z-depth-0" role="button" onclick="toggleBibtex('{{ link.title | slugify }}')" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px; cursor: pointer;">BibTeX</a>
      {% endif %}
      {% if link.code %}
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">Code</a>
      {% endif %}
      {% if link.page %}
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px;">Project Page</a>
      {% endif %}
      {% if link.notes %}
      <strong> <i style="color:#e74d3c; margin-left: 5px;">{{ link.notes }}</i></strong>
      {% endif %}
    </div>

    {% if link.bibtex %}
    <div id="{{ link.title | slugify }}" class="bibtex-hidden" style="display: none; margin-top: 10px; padding: 10px; background: rgba(0,0,0,0.05); border-radius: 5px; font-family: monospace; font-size: 0.85rem; white-space: pre-wrap; border: 1px solid var(--border-color);">{{ link.bibtex }}</div>
    {% endif %}
  </div>
</div>
