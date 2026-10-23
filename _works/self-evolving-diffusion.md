---
title: "UniEvo-VL"
subtitle: "An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement."
kind: "Multimodal Models / Post-training"
year: "2026"
role: "Co-first author"
status: "ICLR 2027 (Under Review)"
order: 1
image: "/assets/works/unievo-vl/overview.png"
detail_image: "/assets/works/unievo-vl/method.png"
tags:
  - Qwen-Image
  - Unified multimodal models
  - On-policy self-distillation
  - Self-improvement
links:
  - label: "Paper (arXiv)"
    url: "https://arxiv.org/abs/2609.38721"
  - label: "GitHub"
    url: "https://github.com/dxing20/self-evolving-vlm"
---

UniEvo-VL is a completed research project on self-improvement in unified multimodal models. It turns feedback on generated images into training signals through on-policy self-distillation, so the model can improve generation from the original prompt alone.

<section class="project-visuals">
  <figure class="project-figure project-figure-wide">
    <img src="/assets/works/unievo-vl/overview.png" alt="UniEvo-VL overview: image generation, visual critique, and model self-improvement">
    <figcaption>Generation and understanding form a self-improvement loop. Figure 1 from <a href="https://arxiv.org/abs/2609.38721" target="_blank" rel="noopener">Wu et al., UniEvo-VL</a>, <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a>.</figcaption>
  </figure>
</section>

## How It Works

A visual critic identifies errors in a generated image. Its feedback is used to revise the prompt, giving the teacher additional context while the student keeps the original prompt. Distillation matches their denoising predictions along the student's own trajectories. The critic stays fixed, and generator LoRA updates retain the benefit of corrective feedback.

## Results

The paper reports direct-generation improvements on Qwen-Image-2512: GenEval increases from **0.747 to 0.808**, and GenEval2 Soft-TIFA from **32.97 to 35.53**. An additional reflection pass can still help after training; text-rendering improvements vary across tasks.

## My Role

I am a co-first author and worked on this project from **May to September 2026**. I built the initial distributed OPSD pipeline for unified multimodal models, integrating on-policy sampling, critique-conditioned teacher feedback, LoRA updates, and evaluation. I implemented ablations over noise, prompts, seeds, denoising steps, and teacher dynamics to study self-improvement quality and training stability.

## Paper

Fang Wu*, Da Xing*, **Yanjie Huang***, Junxi Wang*, …, Jure Leskovec†, Yejin Choi† (2026).

The manuscript is available on arXiv and is **under review at ICLR 2027**.
