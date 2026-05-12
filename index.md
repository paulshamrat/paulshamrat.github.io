---
layout: homepage
is_home: true
---

## Bio

<div id="bio-short">
  <p>
    I am a PhD student in Medical Biophysics at Clemson University. I specialize in computational biophysics and the thermodynamics of biomolecules, with a dedicated focus on developing therapeutics for rare diseases, principally <strong>CDKL5 deficiency disorder</strong>. I developed and maintain <a href="https://github.com/paulshamrat/ColabMDA" target="_blank">ColabMDA</a> and am a contributor to <a href="https://github.com/delphi001/sampdi3dv2" target="_blank">SAMPDI-3Dv2</a>.
    <a href="javascript:void(0)" onclick="toggleBio()" style="color: var(--link-color); font-style: italic; font-weight: 500; text-decoration: none;">Read more</a>
  </p>
</div>

<div id="bio-full" style="display: none;">
  <p>I am a PhD student in Medical Biophysics at Clemson University. I specialize in computational biophysics and the thermodynamics of biomolecules, with a dedicated focus on developing therapeutics for rare diseases, principally <strong>CDKL5 deficiency disorder</strong>. I developed and maintain <a href="https://github.com/paulshamrat/ColabMDA" target="_blank">ColabMDA</a> and am a contributor to <a href="https://github.com/delphi001/sampdi3dv2" target="_blank">SAMPDI-3Dv2</a>.</p>
  
  <p>I also hold an MS in Medical Biophysics from Clemson University and a BSc in Biochemistry from BSMRSTU, Bangladesh. My background spans molecular biology, physical chemistry, and computational modeling, which I combine to study biomolecular systems.</p>
  
  <p>My doctoral research investigates how missense variants alter protein stability and partner binding, curates large variant datasets, and translates structure- and energy-based insights into ideas for variant-guided small-molecule discovery. I also work on machine-learning approaches to predict mutation effects on biomolecular interactions.</p>
  
  <p>I recently presented a CDKL5 variant reclassification framework named <a href="https://github.com/paulshamrat/cdkl5-variants" target="_blank">cdkl5-variants</a> that links variant impacts of folding and binding energetics to pathogenicity and highlights potential avenues for targeted therapy design.</p>
  
  <p>My work has been supported by several fellowships, including the Clemson Graduate Education Program Quasi‑Endowment (College of Science fellowship) and the Pearce Center Grad WAC Fellowship. Earlier, I received a GRIESHMA research fellowship at IIT Madras and was joint second runner‑up at the BAUET Tech Fair for a project combining quantum chemistry with docking.
  <a href="javascript:void(0)" onclick="toggleBio()" style="color: var(--link-color); font-style: italic; font-weight: 500; text-decoration: none;">Show less</a></p>
</div>

<script>
function toggleBio() {
  var shortBio = document.getElementById("bio-short");
  var fullBio = document.getElementById("bio-full");

  if (shortBio.style.display === "none") {
    shortBio.style.display = "block";
    fullBio.style.display = "none";
  } else {
    shortBio.style.display = "none";
    fullBio.style.display = "block";
  }
}
</script>

## Research Interests

- **Rare-Disease Therapeutics**: Investigating the molecular mechanisms of CDKL5 deficiency to identify novel treatment pathways.
- **Computational Biophysics & Thermodynamics**: Modeling biomolecular interactions to understand stability and binding affinity.
- **Open-Source Tool Development**: Creating accessible, high-performance workflows for the scientific community.
<br>



## Conference Presentations

1. Paul, S.K. et al. [**Shared Molecular Mechanisms of CDKL5 Variants**](https://events.clemson.edu/event/24076-clembio-symposium). [**ClemBIO Symposium**](https://mbio-symposium.netlify.app/), Clemson University. April 17, 2026. (Talk & Poster Presentation)
2. Paul, S.K. et al. [**Thermodynamic perspective on CDKL5 deficiency disorder via exploring altered protein folding and binding**](https://acs.digitellinc.com/p/s/thermodynamic-perspective-on-cdkl5-deficiency-disorder-via-exploring-altered-protein-folding-and-binding-656655). [**ACS Spring 2026**](https://www.acs.org/events/spring.html). [**Certificate**](https://credentials.acs.org/a607e44d-fdc8-46f1-85e4-3ad246ebdf78#acc.TfyMgZvd).
3. Paul, S.K. et al. [**Thermodynamics-guided reclassification of CDKL5 variants**](https://github.com/paulshamrat/cdkl5-variants). **SIRPA 2025** (Symposium for the Introduction of Research in Physics and Astronomy), Clemson University. Aug 2025.
4. Paul, S.K. et al. **11th Cellular Biology of Eukaryotic Pathogens Meeting 2023**, Clemson University Eukaryotic Pathogens Innovation Center. Oct 12–13, 2023.

<p><a href="{{ "/presentations/" | relative_url }}" style="font-weight: 500;">View all presentations &rarr;</a></p>

## Awards and Grants

- **2023-2024**: Grad WAC Fellowship (Pearce Center for Professional Commn., Clemson University)
- **2022-2023**: College of Science Fellowship (Clemson University, USA)
- **2021-2022**: N.S.T. Fellowship 2021 (Ministry of Science and Technology, Bangladesh.)

<p><a href="{{ "/awards/" | relative_url }}" style="font-weight: 500;">View all awards &rarr;</a></p>

## Professional Memberships

- **American Chemical Society (ACS)**, Member since Feb 2026. [**Certificate**](https://credentials.acs.org/34232bdc-3fda-48ca-8958-406e45d5b197#acc.nZ8WCcas)
- **American Society for Microbiology (ASM)**, Member since Jan 2024. [**Certificate**]({{ "/assets/certificates/asm-membership-2024.pdf" | relative_url }})

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

<script src="{{ '/assets/js/citations.js' | relative_url }}"></script>

<p><a href="{{ "/publications/" | relative_url }}" style="font-weight: 500;">View all publications &rarr;</a></p>
