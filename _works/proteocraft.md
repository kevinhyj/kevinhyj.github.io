---
title: "ProteoCraft"
subtitle: "AF3-based hallucination with inference-time scaling for binder and TCR design"
kind: "Protein Foundation Model"
year: "2026"
role: "Co-first author"
status: "ICLR 2027 (Under Review)"
order: 6
image: "/assets/works/proteocraft/method-overview-cover.png"
tags:
  - Protein foundation models
  - AlphaFold3-like predictors
  - Diffusion structure prediction
  - MCTS
  - Protein design
  - Binder design
---

<section class="project-visuals">
  <figure class="project-figure project-figure-wide">
    <img src="/assets/works/proteocraft/method-overview-cover.png" alt="ProteoCraft method overview">
    <figcaption>Method overview: gradient proposals suggest local sequence edits, while full forward AF3-like verification ranks discrete protein designs.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteocraft/applications.png" alt="ProteoCraft application targets">
    <figcaption>Applications: cellular receptors, common allergens, multi-domain nucleases, TCR binders, and TCR CDR redesign.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteocraft/benchmark-summary.png" alt="ProteoCraft benchmark summary table">
    <figcaption>Benchmark summary: Rosetta filter pass rates across Type I de novo binder and TCR binder design tasks.</figcaption>
  </figure>

  <figure class="project-figure project-figure-wide project-figure-compact">
    <img src="/assets/works/proteocraft/benchmark-detail.png" alt="ProteoCraft detailed benchmark table">
    <figcaption>Detailed benchmark: target-level results for standard non-TCR binder targets and TCR-facing binder targets.</figcaption>
  </figure>
</section>

ProteoCraft is a protein foundation-model project for design under frozen diffusion-based structure predictors. It treats protein design as a proposal-verification search problem: truncated diffusion gradients are useful for proposing candidate mutations, but reliable values should come from complete forward prediction on discrete sequences.

The framework is built around a hard-forward / soft-backward sequence bridge, gradient-prior Monte Carlo Tree Search, and region-localized masked losses. This lets the system search over mutable protein regions while keeping the broader molecular context fixed, which is important for binder design, TCR-facing interfaces, and localized CDR or TCR redesign.

## What It Enables

- Protein sequence design with AF3-like diffusion structure predictors without training a new model.
- Local mutation proposals from truncated diffusion gradients while preserving legal all-atom topology.
- Full-forward verification of candidate sequences before ranking.
- Search over de novo binders, immune-relevant TCR targets, and localized protein redesign tasks.
- Region-aware losses that optimize designated mutable regions while respecting fixed structural context.

## My Role

I am a co-first author and worked on inference-time search and efficient model evaluation. I built reproducible benchmarks across search strategies and diffusion- and hallucination-based baselines for binder and TCR design, outperforming BindCraft, PXDesign-d, and RFDiffusion3 on success rate. I contributed to architecture, template and domain redesign, and Monte Carlo Tree Search, reducing memory usage by 40%.

## Release

The manuscript is under review at ICLR 2027.
