---
title: "What Matters in RL for Diffusion Models?"
subtitle: "The dominant role of noise in RL post-training for diffusion models."
kind: "RL for Diffusion"
year: "2026"
role: "Research collaborator"
status: "Submitted to NeurIPS 2026"
order: 6
image: "/assets/works/rl-diffusion/ningshan/rl-diffusion-000.png"
tags:
  - Reinforcement learning
  - Diffusion models
  - Post-training
  - FlowGRPO
---

This page describes **What Matters in RL for Diffusion Models? The Dominant Role of Noise**, submitted to NeurIPS 2026.

Reinforcement learning has become a powerful paradigm for post-training generative models: improving reasoning in language models and improving alignment in diffusion models. But a basic question has gone unanswered: what actually drives learning in RL-based diffusion training?

For language models, the signal is clear: it comes from the response. Diffusion models introduce a second axis of stochasticity: **noise initialization**. Each generated image is shaped both by the text prompt and by the noise sample that seeds the denoising trajectory. These two axes both produce variation in reward, but their relative contributions have not been disentangled carefully.

<section class="project-visuals">
  <div class="project-figure-pair">
    <figure class="project-figure project-figure-wide">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-000.png" alt="PickScore training curve comparing 2x Noise Margin with FlowGRPO">
      <figcaption>2x Noise Margin reaches the FlowGRPO baseline score in fewer training steps.</figcaption>
    </figure>

    <figure class="project-figure project-figure-wide">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-002.png" alt="Advantage variance versus improvement scatter plot">
      <figcaption>Noise-margin strategies align with larger improvement over baseline.</figcaption>
    </figure>
  </div>
</section>

We present the first systematic study separating prompt-level and noise-level sources of optimization signal in RL training for diffusion models. The key finding: **noise dominates**. Reward variance and policy-gradient informativeness are driven overwhelmingly by differences among trajectories generated from the same prompt, not by differences across prompts. Prompt-level variation contributes substantially less after group-wise normalization.

This has a direct practical implication: if noise is what matters, training should be structured to maximize informative noise-induced variation. Two strategies follow naturally:

- **Structured noise oversampling**: generate more candidate trajectories per prompt, exploiting the noise axis more efficiently under the same compute budget.
- **Margin-based trajectory selection**: select training pairs with the largest reward margin, prioritizing trajectories that carry the most learning signal.

<section class="project-visuals">
  <div class="project-figure-pair">
    <figure class="project-figure project-figure-wide">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-004.png" alt="Qualitative image generation examples across training methods">
      <figcaption>Qualitative examples show how noise-margin training changes image quality under the same prompts.</figcaption>
    </figure>

    <figure class="project-figure project-figure-wide">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-005.png" alt="OCR accuracy curve for noise-margin training">
      <figcaption>Noise-margin selection also improves OCR-based text rendering performance.</figcaption>
    </figure>
  </div>

  <div class="project-figure-pair">
    <figure class="project-figure project-figure-wide project-figure-scroll">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-011.png" alt="Text rendering examples">
      <figcaption>Text-rendering cases from the same project asset set.</figcaption>
    </figure>

    <figure class="project-figure project-figure-wide project-figure-scroll">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-013.png" alt="Compositional image generation examples">
      <figcaption>Compositional generation cases compare prompt, baseline, and trained samples.</figcaption>
    </figure>
  </div>
</section>

Both strategies plug directly into FlowGRPO, the standard RL framework for flow-based diffusion models. Across three tasks -- compositional image generation, OCR-based text rendering, and human preference alignment -- noise margin selection consistently improves over the baseline. The 2x Noise Margin variant reaches FlowGRPO's final PickScore in **2.2x fewer training steps**, and ends with a higher final score. Prompt-level filtering yields substantially weaker gains, confirming the asymmetry.

<section class="project-visuals">
  <div class="project-figure-pair">
    <figure class="project-figure project-figure-wide">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-007.png" alt="Additional RL diffusion training comparison">
      <figcaption>Additional training comparison from the same project assets.</figcaption>
    </figure>

    <figure class="project-figure project-figure-wide">
      <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-009.png" alt="Additional RL diffusion evaluation curve">
      <figcaption>Evaluation curve for another RL post-training setting.</figcaption>
    </figure>
  </div>

  <figure class="project-figure project-figure-panorama">
    <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-015.png" alt="Panoramic qualitative examples for RL diffusion">
    <figcaption>Qualitative generation examples from the RL diffusion project.</figcaption>
  </figure>

  <figure class="project-figure project-figure-panorama">
    <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-016.png" alt="Panoramic qualitative examples for OCR generation">
    <figcaption>More visual cases showing task-specific behavior after post-training.</figcaption>
  </figure>

  <figure class="project-figure project-figure-panorama">
    <img src="/assets/works/rl-diffusion/ningshan/rl-diffusion-017.png" alt="Panoramic human preference alignment examples">
    <figcaption>Human-preference alignment examples from the shared project figure set.</figcaption>
  </figure>
</section>

The broader takeaway is that RL for diffusion models is governed by **trajectory-level exploration and selection over the noise-induced space**. This is structurally different from RL alignment in autoregressive language models, where the prompt is the primary axis of variation. Understanding this distinction matters for how we design data collection, sampling strategies, and reward-weighting schemes for the next generation of RL-trained generative models.
