---
title: "PhaseFlow"
subtitle: "A unified model for multi-modal and multi-scale phase-separating protein understanding and design."
kind: "Protein Foundation Model"
year: "2026"
role: "Team leader / co-first author"
status: "Nature, submitted"
order: 2
image: "/assets/works/phaseflow/cover.png"
tags:
  - LLPS
  - Protein design
  - Flow matching
  - Multimodal learning
links:
  - label: "GitHub"
    url: "https://github.com/kevinhyj/PhaseFlow"
---

<section class="project-visuals">
  <figure class="project-figure project-figure-wide">
    <img src="/assets/works/phaseflow/model-architecture.svg" alt="PhaseFlow model architecture diagram">
    <figcaption>Model architecture: peptide sequence-phase learning, Flow Matching, and full-length protein context for LLPS prediction and design.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-scroll">
    <img src="/assets/works/phaseflow/application-map.svg" alt="PhaseFlow application map">
    <figcaption>Application map: protein-level LLPS prediction, DPR scanning, peptide phase-diagram generation, and mutation-scale optimization.</figcaption>
  </figure>
</section>

<div class="resource-links">
  <a href="https://github.com/kevinhyj/PhaseFlow" target="_blank" rel="noopener">GitHub</a>
</div>

PhaseFlow is a multimodal generative model for liquid-liquid phase separation (LLPS). It connects full-length protein understanding, peptide-scale phase diagrams, and mutation-level optimization in one workflow.

The core peptide module jointly models amino acid sequences and 4x4 PSSI phase diagrams. A Transfusion-style Transformer combines autoregressive sequence modeling with Conditional Optimal Transport Flow Matching over continuous phase values, enabling both sequence-to-phase prediction and phase-to-sequence design. A full-length GNN-Transformer branch then brings in long-range sequence, structural, disorder, and peptide-derived local phase evidence for protein-scale LLPS prediction and droplet-promoting region scanning.

## What It Enables

- Predicting full 4x4 LLPS phase diagrams from peptide sequences.
- Generating novel peptide sequences conditioned on target phase behavior.
- Predicting full-length protein LLPS propensity.
- Scanning proteins for droplet-promoting regions.
- Scoring mutation effects and steering in-silico directed evolution toward desired phase profiles.

## My Role

I worked across dataset processing, model design, training and evaluation, inference-time optimization, design workflows, and scientific visualization. I also helped shape PhaseFlow into a multi-scale system that links protein-level prediction, peptide-level generation, and mutation-level optimization.

## Release

The public repository provides the PhaseFlow codebase for training, inference, sequence-to-phase prediction, phase-conditioned sequence generation, and directed-evolution style optimization.
