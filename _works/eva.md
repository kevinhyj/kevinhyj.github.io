---
title: "EVA"
subtitle: "A long-context generative RNA foundation model for universal modeling and controllable design."
kind: "Genomic Foundation Model"
year: "2026"
role: "Team leader / first author"
status: "Nature Machine Intelligence, under revision"
order: 1
image: "/assets/works/eva/cover.png"
tags:
  - RNA
  - MoE Transformer
  - OpenRNA
  - CLM / GLM
links:
  - label: "GitHub"
    url: "https://github.com/GENTEL-lab/EVA"
  - label: "Hugging Face"
    url: "https://huggingface.co/GENTEL-Lab/EVA"
  - label: "Try EVA"
    url: "https://evabio.net"
  - label: "BioRxiv"
    url: "https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2"
---

<section class="project-visuals">
  <figure class="project-figure project-figure-wide">
    <img src="/assets/works/eva/model-architecture.svg" alt="EVA model architecture diagram">
    <figcaption>Model architecture: long-context MoE Transformer with CLM and GLM generation paradigms.</figcaption>
  </figure>

  <figure class="project-figure project-figure-tall">
    <img src="/assets/works/eva/application-concept.svg" alt="EVA application concept for RNA modeling and design">
    <figcaption>Application concept: EVA as a model for RNA understanding, generation, optimization, and design.</figcaption>
  </figure>
</section>

<div class="resource-links">
  <a href="https://github.com/GENTEL-lab/EVA" target="_blank" rel="noopener">GitHub</a>
  <a href="https://huggingface.co/GENTEL-Lab/EVA" target="_blank" rel="noopener">Hugging Face</a>
  <a href="https://evabio.net" target="_blank" rel="noopener">Online Demo</a>
</div>

EVA, short for Evolutionary Versatile Architect, is a generative RNA foundation model built for full-length RNA modeling and controllable RNA design. It learns from OpenRNA v1, a curated atlas of 114 million full-length RNA sequences across domains of life, and uses a 1.4B-parameter decoder-only Transformer with a Mixture-of-Experts backbone and an 8,192-token context window.

The model unifies RNA sequence scoring and generation in one framework. Causal language modeling supports de novo design and continuation, while general language modeling supports span infilling and domain redesign. EVA can condition generation on RNA type and taxonomic lineage, making it useful for designing mRNA, tRNA, rRNA, lncRNA, miRNA, circRNA, viral RNA, and other RNA classes.

## What It Enables

- Full-length RNA sequence modeling without aggressive truncation.
- Zero-shot RNA fitness prediction and log-likelihood scoring.
- Controllable generation by RNA type, species, or lineage.
- De novo RNA design, domain redesign, and in-silico directed evolution.
- Sequence-to-structure-aware optimization for practical RNA engineering tasks.

## My Role

As Y.H., I designed the EVA architecture and wrote the first training, inference, and fine-tuning code. I led model training and evaluation, co-curated the pretraining data, drove RNA design studies across tRNA, aptamer, CRISPR omegaRNA, vaccine, and circRNA IRES tasks, and co-created the conceptual figures, usage website, and first manuscript draft.

## Release

The public EVA repository releases training, finetuning, inference, generation, scoring, and directed-evolution code, with model and data access documented for reproducible use.
