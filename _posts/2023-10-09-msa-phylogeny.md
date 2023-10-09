---
layout: post
title:  "MSA & Phylogeny"
image: assets/images/wsl2.png
---
## Multiple Sequence Alignment (MSA)

1. Open the MSA tool.
2. Set the reference sequence to "AFUA_5G01230."
3. Click on "Align > Edit or build alignment."
4. Choose "Create a new alignment."
5. Select "Protein" as the sequence type.
6. Paste the first sequence (already copied from a fasta/text file) into "Sequence 1."
7. Delete the placeholder "Sequence 1" entry.

Now you have your data ready for alignment.

8. Go to "Alignment > Align by Clustalw/ MUSCLE."
9. If nothing is selected, choose "Select all" and click "Ok."
10. Keep the alignment options as default and click "Ok."

Wait for the alignment process to complete.

11. Once alignment is complete, go to "Data > Export alignment > MEGA format."

## MUSCLE: Default Parameters

12. In the MUSCLE parameters window, you'll see the following default settings:

   - **GAP penalties:**
     - Gap open: -2.90
     - Gap extend: 0.00
     - Hydrophobicity multiplier: 1.20

   - **Memory Iterations:**
     - Max memory in MB: 2048
     - Max iterations: 16

   - **Advanced options:**
     - Cluster method (iter 1,2): UPGMA
     - Cluster method (iter): UPGMA
     - Min diagonal length (lambda): 24

13. Give a name for your alignment and save it, then close the window.

## Phylogeny Reconstruction

14. Navigate to "Phylogeny > Construct/Test-neighbor-joining Tree."
15. When asked about the current data, select "No."
16. When asked if you want to preserve data, select "No."
17. It will ask if you want to save the alignment again, do so.

It will open the last sequence alignment for phylogeny reconstruction.

## Phylogeny Reconstruction Parameters

18. In the "Phylogeny reconstruction parameters" window, configure the following settings:

   - **ANALYSIS:**
     - Scope: All selected taxa
     - Statistical method: Neighbor-joining

   - **PHYLOGENY TEST:**
     - Test of phylogeny: Bootstrap method (You can choose the number of bootstrap replicates, e.g., 100 or 1000)

   - **SUBSTITUTIONAL MODEL:**
     - Substitution type: Amino acids
     - Model/method: Jones-Taylor-Thornton (jTT) model

   - **RATES AND PATTERNS:**
     - Rates among sites: Uniform rates
     - Pattern among lineages: Same (homogeneous)

   - **DATA SUBSET TO USE:**
     - Gaps/missing data treatment: Pairwise deletion
     - Site coverage cutoff (%): Not applicable

   - **SYSTEM RESOURCES USAGE:**
     - NUMBER OF THREADS: 4

19. After configuring these settings, proceed with the phylogeny reconstruction.
