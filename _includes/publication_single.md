<div class="pub-row" data-doi="{{ link.doi }}" data-title="{{ link.title }}">
  <div class="pub-info">
    <div class="title">
      <a href="{% if link.html %}{{ link.html }}{% elsif link.doi %}https://doi.org/{{ link.doi }}{% else %}{{ link.pdf }}{% endif %}" target="_blank">
        {{ link.title }}
      </a>
    </div>
    <div class="author">
      {{ link.authors | replace: "Paul, S.K.", "<strong>Paul, S.K.</strong>" | replace: "Paul, S. K.", "<strong>Paul, S. K.</strong>" | replace: "Shamrat Kumar Paul", "<strong>Shamrat Kumar Paul</strong>" }}
    </div>
    <div class="periodical">
      <em>{{ link.conference }}</em>
    </div>
    <div class="links">
      {% if link.pdf %}
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">PDF</a>
      {% endif %}
      {% if link.doi %}
      <a href="https://doi.org/{{ link.doi }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">DOI</a>
      {% endif %}
      {% if link.bibtex %}
      <a class="bibtex btn btn-sm z-depth-0" role="button" onclick="toggleBibtex('{{ link.title | slugify }}')" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px; cursor: pointer;">BibTeX</a>
      {% endif %}
      {% if link.supplementary %}
      <a class="btn btn-sm z-depth-0" role="button" onclick="toggleBibtex('{{ link.title | slugify }}-supp')" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px; cursor: pointer;">Supplementary</a>
      {% endif %}
      {% if link.code %}
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">Code</a>
      {% endif %}
      {% if link.notes %}
      <strong> <i style="color:#e74d3c; margin-left: 5px;">{{ link.notes }}</i></strong>
      {% endif %}
    </div>

    {% if link.bibtex %}
    <div id="{{ link.title | slugify }}" class="bibtex-hidden" style="display: none; margin-top: 10px; padding: 10px; background: rgba(0,0,0,0.05); border-radius: 5px; font-family: monospace; font-size: 0.85rem; white-space: pre-wrap; border: 1px solid var(--border-color);">{{ link.bibtex }}</div>
    {% endif %}
    {% if link.supplementary %}
    <div id="{{ link.title | slugify }}-supp" style="display: none; margin-top: 10px; padding: 10px; background: rgba(0,0,0,0.05); border-radius: 5px; font-size: 0.85rem; border: 1px solid var(--border-color);">
      <strong>Supplementary Materials:</strong>
      <ul style="margin: 5px 0 0 20px; padding: 0;">
        {% for item in link.supplementary %}
        <li>
          <a href="{{ item.url | relative_url }}" target="_blank">{{ item.name }}</a>
          <a href="https://docs.google.com/viewer?url={{ site.url }}{{ item.url | relative_url }}" target="_blank" style="margin-left: 10px; color: #777; font-size: 0.75rem;">[View]</a>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endif %}
  </div>

  <div class="pub-citations">
    <span class="citation-label">Cited by:</span>
    {% if link.doi %}
    <a href="https://scholar.google.com/scholar?q={{ link.doi }}" target="_blank" class="citation-count" id="cite-{{ link.doi | slugify }}">
      <span class="count-value">{% if link.manual_citations %}{{ link.manual_citations }}{% else %}...{% endif %}</span>
    </a>
    {% else %}
    <a href="https://scholar.google.com/scholar?q={{ link.title | url_encode }}" target="_blank" class="citation-count" id="cite-{{ link.title | slugify }}">
      <span class="count-value">{% if link.manual_citations %}{{ link.manual_citations }}{% else %}...{% endif %}</span>
    </a>
    {% endif %}
  </div>

  <div class="pub-year">
    {{ link.year }}
  </div>
</div>
