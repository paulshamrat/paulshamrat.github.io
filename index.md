---
layout: homepage
---

## Bio

I am a PhD student in Medical Biophysics at Clemson University. I specialize in computational biophysics and the thermodynamics of biomolecules, with a dedicated focus on developing therapeutics for rare diseases—principally **CDKL5 deficiency disorder**.

I developed and maintain [ColabMDA](https://github.com/paulshamrat/ColabMDA) and am a core contributor to [SAMPDI-3Dv2](https://github.com/delphi001/sampdi3dv2).

## Research Interests

- **Rare-Disease Therapeutics**: Investigating the molecular mechanisms of CDKL5 deficiency to identify novel treatment pathways.
- **Computational Biophysics & Thermodynamics**: Modeling biomolecular interactions to understand stability and binding affinity.
- **Open-Source Tool Development**: Creating accessible, high-performance workflows for the scientific community.
<br>

<h2 id="selected-publications" style="margin: 2px 0px -15px;">Selected Publications</h2>
<div class="publications">
  <ol class="bibliography">
    {% for link in site.data.publications.main limit:3 %}
    <li>
      <div class="pub-row" style="display: flex; flex-direction: row; margin-bottom: 1.5rem;">
        <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 0px;">
          <div class="title" style="font-weight: bold;"><a href="{{ link.pdf }}">{{ link.title }}</a></div>
          <div class="author" style="font-size: 0.9rem;">{{ link.authors }}</div>
          <div class="periodical" style="font-size: 0.9rem;"><em>{{ link.conference }} ({{ link.year }})</em> </div>
          <div class="links" style="margin-top: 5px;">
            {% if link.pdf %} 
            <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px; margin-right: 5px;">PDF</a>
            {% endif %}
            {% if link.page %} 
            <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px; border: 1px solid var(--border-color); padding: 2px 8px; border-radius: 4px;">Journal</a>
            {% endif %}
          </div>
        </div>
      </div>
    </li>
    {% endfor %}
  </ol>
</div>

<p><a href="{{ "/publications/" | relative_url }}" style="font-weight: 500;">View all publications &rarr;</a></p>

## News

- **Aug 2025**: Paper on CDKL5 Deficiency Disorder published in [**IJMS**](https://www.mdpi.com/1422-0067/26/17/8399).
- **Dec 2024**: SAMPDI-3Dv2 paper published in [**Genes**](https://www.mdpi.com/2073-4425/16/1/101).
