---
layout: post
title:  "MSA & Phylogeny"
image: assets/images/wsl2.png
---
Multiple Sequence Alignment (MSA) and phylogenetic tree reconstruction are core tasks in bioinformatics. This guide outlines the workflow using tools like MEGA.

## Multiple Sequence Alignment (MSA)

1. **Open MSA Tool:** Launch your preferred MSA software (e.g., MEGA).
2. **Reference Sequence:** Set the reference sequence (e.g., "AFUA_5G01230").
3. **Initiate Alignment:** Go to **Align > Edit or Build Alignment**.
4. **Create New:** Select **Create a new alignment** and choose **Protein** as the sequence type.
5. **Add Sequences:** Paste your sequences from a FASTA or text file into the alignment window.
6. **Clean Up:** Ensure all sequences are correctly labeled and delete any empty placeholder entries.
7. **Perform Alignment:** Navigate to **Alignment > Align by ClustalW** or **Align by MUSCLE**.
   - If prompted, select **Select All** and click OK.
   - Use the default alignment options for a standard analysis.
8. **Export:** Once complete, go to **Data > Export Alignment** and save it in the **MEGA format** (.meg).

## MUSCLE Default Parameters

When using MUSCLE, the following parameters are typically used for protein alignments:

- **Gap Penalties:**
  - Gap Open: -2.90
  - Gap Extend: 0.00
  - Hydrophobicity Multiplier: 1.20
- **Memory & Iterations:**
  - Max Memory: 2048 MB
  - Max Iterations: 16
- **Advanced Options:**
  - Cluster Method (Iter 1, 2): UPGMA
  - Min Diagonal Length (Lambda): 24

## Phylogenetic Tree Reconstruction

1. **Start Analysis:** Navigate to **Phylogeny > Construct/Test Neighbor-Joining Tree**.
2. **Load Data:** When prompted to use current data or preserve existing sessions, select **No** to ensure you are starting fresh with the newly aligned data.
3. **Configure Parameters:** In the reconstruction window, use the following settings for reliable results:

### Reconstruction Parameters

- **Analysis:**
  - **Scope:** All selected taxa
  - **Statistical Method:** Neighbor-Joining
- **Phylogeny Test:**
  - **Test Method:** Bootstrap method (Recommended: 100 or 1000 replicates)
- **Substitution Model:**
  - **Substitution Type:** Amino Acid
  - **Model/Method:** Jones-Taylor-Thornton (JTT) model
- **Rates and Patterns:**
  - **Rates Among Sites:** Uniform Rates
  - **Pattern Among Lineages:** Homogeneous
- **Data Subset Treatment:**
  - **Gaps/Missing Data:** Pairwise Deletion
- **System Resources:**
  - **Number of Threads:** 4 (or adjust based on your CPU)

4. **Compute:** Click OK to begin the reconstruction. The resulting tree will provide insights into the evolutionary relationships between your sequences.
