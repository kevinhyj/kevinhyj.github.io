---
title: Academic CV
permalink: /cv/
eyebrow: Curriculum vitae
description: "Academic CV of Yanjie Huang (黄䶮杰), an undergraduate researcher at Shanghai Jiao Tong University working on generative AI and scientific discovery, with a focus on scientific synthetic data, reasoning, alignment, and molecular design."
---

<section class="section page-section cv-page">
  <div class="container">
    <div class="cv-profile">
      <div class="cv-profile-copy">
        <p class="cv-name-line">Yanjie Huang <span>黄䶮杰</span></p>
        <p class="cv-lead">I am an undergraduate researcher at Shanghai Jiao Tong University. My research lies at the intersection of generative AI and scientific discovery, with a focus on scientific synthetic data, reasoning, alignment, and molecular design.</p>
        <div class="resource-links cv-actions">
          <a href="mailto:huangyanjie@sjtu.edu.cn">Email me</a>
          <a class="cv-action-secondary" href="{{ '/assets/cv/Yanjie-Huang-CV.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
          <a class="cv-action-secondary" href="https://github.com/kevinhyj" target="_blank" rel="noopener">GitHub</a>
          <a class="cv-action-secondary" href="{{ '/projects/' | relative_url }}">Selected work</a>
        </div>
      </div>

      <dl class="cv-facts" aria-label="Academic profile at a glance">
        <div>
          <dt>Education</dt>
          <dd>SJTU · Computer Science</dd>
        </div>
        <div>
          <dt>Expected</dt>
          <dd>June 2027</dd>
        </div>
        <div>
          <dt>GPA</dt>
          <dd>3.7</dd>
        </div>
        <div>
          <dt>Focus</dt>
          <dd>AI &amp; AI for Bio</dd>
        </div>
      </dl>
    </div>

    <section class="cv-section" aria-labelledby="cv-education">
      <div class="cv-section-title">
        <p class="eyebrow">01</p>
        <h2 id="cv-education">Education</h2>
      </div>
      <div class="cv-section-body">
        <article class="cv-entry">
          <div class="cv-entry-head">
            <div class="cv-institution">
              <img class="cv-institution-logo cv-institution-logo-sjtu" src="{{ '/assets/shared/logos/sjtu.png' | relative_url }}" alt="Shanghai Jiao Tong University logo">
              <div>
                <h3>Shanghai Jiao Tong University</h3>
                <p class="cv-role">Computer Science</p>
              </div>
            </div>
            <p class="cv-date">Sep 2023 – Jun 2027</p>
          </div>
          <p>GPA: <strong>3.7</strong> · Comprehensive evaluation: <strong>92.4 / 100, ranked 2nd of 22</strong> · Shanghai, China</p>
          <p>Selected as the sole student from SJTU's Global Institute of Future Technology and one of 30 students from 18,584 undergraduates for the Bolè Plan (Elite Scientific Talent Program), recognizing exceptional research potential.</p>
        </article>
      </div>
    </section>

    <section class="cv-section" aria-labelledby="cv-experience">
      <div class="cv-section-title">
        <p class="eyebrow">02</p>
        <h2 id="cv-experience">Research Experience</h2>
      </div>
      <div class="cv-section-body">
        <article class="cv-entry cv-entry-featured">
          <div class="cv-entry-head">
            <div class="cv-institution">
              <img class="cv-institution-logo cv-institution-logo-stanford" src="{{ '/assets/shared/logos/stanford.webp' | relative_url }}" alt="Stanford University logo">
              <div>
                <h3>Stanford University · Yejin Choi Group</h3>
                <p class="cv-role">Research Assistant</p>
              </div>
            </div>
            <p class="cv-date">Mar 2026 – Present</p>
          </div>
          <p>Mentored by <a href="https://hai.stanford.edu/people/fang-wu" target="_blank" rel="noopener"><strong>Fang Wu</strong></a> &amp; <a href="https://profiles.stanford.edu/yejin-choi?tab=bio" target="_blank" rel="noopener"><strong>Yejin Choi</strong></a>.</p>
          <p>Researching biological reasoning, unified multimodal models, and post-training, with an emphasis on scientific synthetic data and molecular design. Completed UniEvo-VL (May – Sep 2026), building a distributed on-policy self-distillation pipeline and conducting training ablations.</p>
          <div class="cv-tag-row" aria-label="Current research areas">
            <span>Bio reasoning</span>
            <span>Unified multimodal models</span>
            <span>Scientific synthetic data</span>
            <span>Post-training</span>
            <span>AI for Science</span>
          </div>
        </article>

        <article class="cv-entry">
          <div class="cv-entry-head">
            <div class="cv-institution">
              <img class="cv-institution-logo cv-institution-logo-lin-gang" src="{{ '/assets/shared/logos/lin-gang-laboratory.png' | relative_url }}" alt="Lin Gang Laboratory logo">
              <div>
                <h3>Lin Gang Laboratory · AI Research Division</h3>
                <p class="cv-role">Research Intern · Shanghai</p>
              </div>
            </div>
            <p class="cv-date">Aug 2025 – Nov 2025</p>
          </div>
          <ul class="cv-list">
            <li>Optimized Model Context Protocol design for the Origene scientific agent.</li>
            <li>Worked on CAR-T stability and expression potency in mRNA and circRNA vaccine platforms.</li>
          </ul>
        </article>
      </div>
    </section>

    <section class="cv-section" aria-labelledby="cv-research">
      <div class="cv-section-title">
        <p class="eyebrow">03</p>
        <h2 id="cv-research">Selected Research</h2>
      </div>
      <div class="cv-section-body">
        <div class="cv-project-grid">
          <a class="cv-project" href="{{ '/work/eva/' | relative_url }}">
            <p class="eyebrow">RNA foundation model</p>
            <h3>EVA</h3>
            <p>Team leader and first author. Designed a 1.4B-parameter long-context MoE model for universal RNA modeling and controllable design.</p>
            <span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/phaseflow/' | relative_url }}">
            <p class="eyebrow">Multimodal protein model</p>
            <h3>PhaseFlow</h3>
            <p>Team leader and co-first author. Built a unified sequence-and-flow model for phase-separating protein understanding and design.</p>
            <span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/proteo-r1-r2/' | relative_url }}">
            <p class="eyebrow">Biological reasoning</p>
            <h3>Proteo-R1 / Proteo-R2</h3>
            <p>Developing chain-of-thought data and reasoning-centered methods for antibody, enzyme, and synthetic protein design.</p>
            <span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/self-evolving-diffusion/' | relative_url }}">
            <p class="eyebrow">Multimodal self-improvement · May – Sep 2026</p>
            <h3>UniEvo-VL ★</h3>
            <p>Co-first author. Built distributed on-policy self-distillation for unified multimodal models and implemented ablations over sampling and teacher dynamics. Submitted to ICLR 2027.</p>
            <span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/rl-diffusion/' | relative_url }}">
            <p class="eyebrow">Diffusion post-training</p>
            <h3>What Matters in RL for Diffusion Models?</h3>
            <p>Studying noise-driven optimization signals and efficient trajectory selection for RL post-training of diffusion models.</p>
            <span>View project →</span>
          </a>
        </div>
      </div>
    </section>

    <section class="cv-section" aria-labelledby="cv-publications">
      <div class="cv-section-title">
        <p class="eyebrow">04</p>
        <h2 id="cv-publications">Selected Publications</h2>
      </div>
      <div class="cv-section-body cv-publications">
        <article class="cv-publication">
          <span class="cv-publication-index">01</span>
          <div>
            <h3>EVA: A Long-Context Generative Foundation Model Deciphers RNA Design Principles</h3>
            <p><strong>Y. Huang*</strong>, G. Lv*, et al. · <em>Nature Machine Intelligence</em>, Accepted, Spotlight (Top 10%) · 2026</p>
            <a href="https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2" target="_blank" rel="noopener">Preprint</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">02</span>
          <div>
            <h3>PhaseFlow: A Unified Model for Multi-scale Biomolecular Condensates Understanding and Design</h3>
            <p>Y. Zhu*, <strong>Y. Huang*</strong>, et al. · <em>Nature</em>, Under Review · 2026</p>
            <a href="{{ '/work/phaseflow/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">03</span>
          <div>
            <h3>Energy-Adaptive Elastic Equivariant Transformer-SSM for Noise-Robust Protein Structure Representation</h3>
            <p>Zhongyue Zhang, Runze Ma, <strong>Yanjie Huang</strong>, Shuangjia Zheng† · NeurIPS 2026 (Accepted)</p>
            <a href="https://arxiv.org/abs/2503.16996" target="_blank" rel="noopener">Preprint</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">04</span>
          <div>
            <h3>ProteoCraft: Proposal-Verification Search for Protein Design with Diffusion Structure Predictors</h3>
            <p>F. Wu*, H. Lin*, B. Duan*, <strong>Y. Huang*</strong>, Y. Li*, et al. · ICLR 2027 (Submitted)</p>
            <a href="{{ '/work/proteocraft/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">05</span>
          <div>
            <h3>UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement</h3>
            <p>Fang Wu*, Da Xing*, <strong>Yanjie Huang*</strong>, Junxi Wang*, …, Jure Leskovec†, Yejin Choi† · ICLR 2027 (Submitted)</p>
            <a href="https://arxiv.org/abs/2609.38721" target="_blank" rel="noopener">Preprint</a>
            <a href="{{ '/work/self-evolving-diffusion/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">06</span>
          <div>
            <h3>What Matters in RL for Diffusion Models? The Dominant Role of Noise</h3>
            <p>Da Xing, Haokai Zhao, Yanchao Li, Hanqun Cao, <strong>Yanjie Huang</strong>, et al. · ICLR 2027 (Submitted)</p>
            <a href="{{ '/work/rl-diffusion/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">07</span>
          <div>
            <h3>Capturing Natural Evolution in RNA Design for in Vivo Functionality via Genomic Foundational Models</h3>
            <p><strong>Y. Huang*</strong>, B. Zhang*, et al. · <em>Communications Biology</em>, Under Review · 2025</p>
            <a href="https://doi.org/10.1101/2025.04.08.647793" target="_blank" rel="noopener">Preprint</a>
          </div>
        </article>
      </div>
    </section>

    <section class="cv-section" aria-labelledby="cv-awards">
      <div class="cv-section-title">
        <p class="eyebrow">05</p>
        <h2 id="cv-awards">Honors</h2>
      </div>
      <div class="cv-section-body">
        <ul class="cv-honors">
          <li><span>2026</span><strong>National Scholarship for Undergraduate Students</strong><p>Sep 2026.</p></li>
          <li><span>SJTU</span><strong>Bolè Plan</strong><p>Elite Scientific Talent Program, Shanghai Jiao Tong University.</p></li>
          <li><span>2022</span><strong>Bronze Medal</strong><p>Chinese Mathematical Olympiad.</p></li>
          <li><span>IMMC</span><strong>First Prize · International Round</strong><p>The 7th International Mathematical Modeling Challenge.</p></li>
        </ul>
      </div>
    </section>

    <section class="cv-section" aria-labelledby="cv-skills">
      <div class="cv-section-title">
        <p class="eyebrow">06</p>
        <h2 id="cv-skills">Technical Focus</h2>
      </div>
      <div class="cv-section-body cv-skill-groups">
        <div class="cv-skill-group">
          <h3>Models</h3>
          <p>MoE Transformers (MegaBlocks), unified multimodal models (Qwen-Image, Bagel), flow matching, mechanistic interpretability, scientific agents.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Training</h3>
          <p>Pretraining, SFT, LoRA, full-parameter tuning, DPO, OPSD, GRPO, inference-time optimization, vLLM.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Scientific Computing</h3>
          <p>Scientific synthetic data, large-scale data processing, SELEX/NGS pipelines, metagenomic mining, structure-based data mining.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Molecular Design</h3>
          <p>RNA design, CRISPR-Cas, phase-separating proteins, protein binders, CAR-T, and biological sequence-structure modeling.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Programming</h3>
          <p>Python, C++, Shell scripting, and LaTeX.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Languages</h3>
          <p>Chinese (native), English (TOEFL 99), Japanese (JLPT N3).</p>
        </div>
      </div>
    </section>

    <section class="cv-contact" aria-labelledby="cv-contact-title">
      <p class="eyebrow">PhD & research opportunities</p>
      <h2 id="cv-contact-title">Let's talk about ambitious models for living systems.</h2>
      <p>I am happy to discuss research collaborations, PhD opportunities, and research engineering roles in AI for science.</p>
      <a class="button" href="mailto:huangyanjie@sjtu.edu.cn">huangyanjie@sjtu.edu.cn</a>
    </section>
  </div>
</section>
