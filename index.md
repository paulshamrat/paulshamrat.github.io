---
layout: homepage
---

## Bio

<p>
  I am a PhD student in Medical Biophysics at Clemson University. I specialize in computational biophysics and the thermodynamics of biomolecules, with a dedicated focus on developing therapeutics for rare diseases—principally <strong>CDKL5 deficiency disorder</strong>.
  <span id="more-dots">...</span>
  <span id="more-bio" style="display: none;">
    I also hold an MS in Medical Biophysics from Clemson University and a BSc in Biochemistry from BSMRSTU, Bangladesh. My background spans molecular biology, physical chemistry, and computational modeling, which I combine to study biomolecular systems. My doctoral research investigates how missense variants alter protein stability and partner binding, curates large variant datasets, and translates structure- and energy-based insights into ideas for variant-guided small-molecule discovery. I also work on machine-learning approaches to predict mutation effects on biomolecular interactions. I recently presented a CDKL5 variant reclassification framework named <a href="https://github.com/paulshamrat/cdkl5-variants" target="_blank">cdkl5-variants</a> that links variant impacts of folding and binding energetics to pathogenicity and highlights potential avenues for targeted therapy design. My work has been supported by several fellowships, including the Clemson Graduate Education Program Quasi‑Endowment (College of Science fellowship) and the Pearce Center Grad WAC Fellowship. Earlier, I received a GRIESHMA research fellowship at IIT Madras and was joint second runner‑up at the BAUET Tech Fair for a project combining quantum chemistry with docking.
  </span>
  <a href="javascript:void(0)" onclick="toggleBio()" id="read-more-btn" style="color: var(--link-color); font-weight: 500; text-decoration: none;">[Read More]</a>
</p>

I developed and maintain [ColabMDA](https://github.com/paulshamrat/ColabMDA) and am a core contributor to [SAMPDI-3Dv2](https://github.com/delphi001/sampdi3dv2).

<script>
function toggleBio() {
  var dots = document.getElementById("more-dots");
  var moreText = document.getElementById("more-bio");
  var btnText = document.getElementById("read-more-btn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "[Read More]";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "[Show Less]";
    moreText.style.display = "inline";
  }
}
</script>

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
