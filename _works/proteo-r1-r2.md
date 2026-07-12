---
title: "Proteo-R1 / Proteo-R2"
subtitle: "Multi-modal Reasoning for Multi-scale Biomolecule Understanding and Design"
kind: "Protein Reasoning Model"
year: "2026"
status: "R1: ICML 2026 accepted / R2: in progress"
order: 5
image: "/assets/works/proteo-r1-r2/cover-card.png"
tags:
  - Protein reasoning
  - CoT data
  - Synthetic protein design
  - Antibody design
  - Enzyme design
  - Multimodal reasoning
---

<section class="project-visuals">
  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteo-r1-r2/cover.png" alt="Proteo-R1 training and reasoning framework">
    <figcaption>Framework: multimodal understanding experts reason over protein sequence, structure, and text before guiding task-specific protein generators.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteo-r1-r2/multi-cdr-redesign.png" alt="Proteo-R1 multi-CDR redesign result table">
    <figcaption>Result: geometry-centric evaluation of simultaneous multi-CDR redesign.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteo-r1-r2/cdr-h3-rabd.png" alt="Proteo-R1 CDR-H3 design results on RAbD">
    <figcaption>Result: CDR-H3 design on RAbD, comparing sequence recovery, structural quality, RMSD, and docking quality.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteo-r1-r2/rabd-comparison.png" alt="Proteo-R1 antigen-binding CDR-H3 design comparison">
    <figcaption>Result: antigen-binding CDR-H3 sequence and structure design comparisons on the RAbD dataset.</figcaption>
  </figure>
</section>

Proteo-R1 and Proteo-R2 explore a reasoning-first direction for protein design. Instead of asking a generative model to directly sample molecules, the system separates molecular understanding from geometric generation: a multimodal reasoning expert identifies important residues, interaction anchors, and design constraints, then a generation expert performs conditional sequence-structure co-design.

Proteo-R1 focuses on de novo antibody CDR design, where residue-level reasoning can make generation more interpretable and controllable. Proteo-R2 extends this line toward enzyme design, with a stronger emphasis on chain-of-thought reasoning data for synthetic protein design and controllable protein engineering.

## What It Enables

- Reasoning-guided antibody CDR redesign conditioned on antigen context.
- CoT-style reasoning data for synthetic protein design.
- Enzyme-design reasoning for Proteo-R2.
- Multimodal alignment across protein sequence, structure, and text.
- Explicit residue-level design commitments before geometric generation.
- Conditional sequence-structure co-design through task-specific protein generators.

## My Role

My main work is building chain-of-thought reasoning data for synthetic protein design, especially for the Proteo-R2 enzyme-design direction. I also contributed to the broader Proteo-R line of work, with focus on turning multimodal molecular reasoning into controllable design behavior.

## Release

Proteo-R1 has been accepted to ICML 2026. Proteo-R2 is currently in progress for enzyme design, and public materials will be added here after release.
