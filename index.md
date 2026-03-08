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

## News

- **Feb 2026**: Invited to present research on CDKL5 deficiency disorder at [**ACS Spring 2026**](https://www.acs.org/meetings/acs-meetings/spring-2026.html) (March 22-26) in the COMP Division.
- **Aug 2025**: Paper on CDKL5 Deficiency Disorder published in [**IJMS**](https://www.mdpi.com/1422-0067/26/17/8399).
- **Dec 2024**: SAMPDI-3Dv2 paper published in [**Genes**](https://www.mdpi.com/2073-4425/16/1/101).

<h2 id="selected-publications" style="margin: 2px 0px -15px;">Selected Publications</h2>
<div class="publications">
  <ol class="bibliography">
    {% assign selected_pubs = site.data.publications.main | where: "selected", true %}
    {% for link in selected_pubs %}
    <li>
      {% include publication_single.md %}
    </li>
    {% endfor %}
  </ol>
</div>

{% include bibtex_script.md %}

<p><a href="{{ "/publications/" | relative_url }}" style="font-weight: 500;">View all publications &rarr;</a></p>
