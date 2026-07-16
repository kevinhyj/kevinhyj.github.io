---
title: Academic CV
permalink: /cv/
eyebrow: Curriculum vitae
subtitle: "Undergraduate researcher working on biological reasoning models, molecular foundation models, diffusion, and post-training."
description: "Academic background, research experience, publications, and technical focus of Yanjie Huang."
---

<section class="section page-section cv-page">
  <div class="container">
    <div class="cv-profile">
      <div class="cv-profile-copy">
        <p class="cv-name-line">Yanjie Huang <span>黄䶮杰</span></p>
        <p class="cv-lead">I am an undergraduate researcher at Shanghai Jiao Tong University. My research lies at the intersection of generative AI and scientific discovery, with a focus on reasoning, alignment and molecular design.</p>
        <div class="resource-links cv-actions">
          <a href="mailto:huangyanjie@sjtu.edu.cn">Email me</a>
          <a class="cv-action-secondary" href="https://github.com/kevinhyj" target="_blank" rel="noopener">GitHub</a>
          <a class="cv-action-secondary" href="{{ '/projects/' | relative_url }}">Selected work</a>
        </div>
      </div>

      <dl class="cv-facts" aria-label="Academic profile at a glance">
        <div>
          <dt>Education</dt>
          <dd>SJTU · CS</dd>
        </div>
        <div>
          <dt>Expected</dt>
          <dd>June 2027</dd>
        </div>
        <div>
          <dt>GPA</dt>
          <dd>3.98 / 4.30</dd>
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
                <p class="cv-role">Bachelor of Computer Science and Technology</p>
              </div>
            </div>
            <p class="cv-date">Sep 2023 – Jun 2027</p>
          </div>
          <p>GPA: <strong>3.98 / 4.30</strong> · Shanghai, China</p>
          <p>Selected for the Bolè Plan (Elite Scientific Talent Program) as one of 30 students from 18,584 undergraduates, recognizing exceptional scientific potential and dedication.</p>
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
                <p class="cv-role">Research Intern</p>
              </div>
            </div>
            <p class="cv-date">Apr 2026 – Present</p>
          </div>
          <p>Mentored by <a href="https://hai.stanford.edu/people/fang-wu" target="_blank" rel="noopener"><strong>Fang Wu</strong></a> &amp; <a href="https://profiles.stanford.edu/yejin-choi?tab=bio" target="_blank" rel="noopener"><strong>Yejin Choi</strong></a>.</p>
          <p>Researching biological reasoning models, diffusion models, and post-training, with an emphasis on reasoning-centered molecular intelligence and training methods for scientific generative models.</p>
          <div class="cv-tag-row" aria-label="Current research areas">
            <span>Bio reasoning</span>
            <span>Diffusion</span>
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
            <p class="cv-date">Sep 2025 – Present</p>
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
            <p><strong>Y. Huang*</strong>, G. Lv*, et al. · <em>Nature Machine Intelligence</em>, under revision · 2026</p>
            <a href="https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2" target="_blank" rel="noopener">Preprint</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">02</span>
          <div>
            <h3>PhaseFlow: A Unified Model for Multi-modal and Multi-scale Phase-separating Protein Understanding and Design</h3>
            <p>Y. Zhu*, <strong>Y. Huang*</strong>, et al. · <em>Nature</em>, submitted · 2026</p>
            <a href="{{ '/work/phaseflow/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">03</span>
          <div>
            <h3>ProteoCraft: Proposal-Verification Search for Protein Design with Diffusion Structure Predictors</h3>
            <p>F. Wu*, H. Lin*, B. Duan*, <strong>Y. Huang*</strong>, Y. Li*, et al. · Submitted to NeurIPS 2026</p>
            <a href="{{ '/work/proteocraft/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">04</span>
          <div>
            <h3>What Matters in RL for Diffusion Models? The Dominant Role of Noise</h3>
            <p>Research collaborator · Submitted to NeurIPS 2026</p>
            <a href="{{ '/work/rl-diffusion/' | relative_url }}">Project page</a>
          </div>
        </article>
        <article class="cv-publication">
          <span class="cv-publication-index">05</span>
          <div>
            <h3>Capturing Natural Evolution in RNA Design via Genomic Foundation Models</h3>
            <p><strong>Y. Huang</strong>, B. Zhang, et al. · Preprint · 2025</p>
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
          <p>MoE Transformers, multimodal Transformers, flow matching, mechanistic interpretability, scientific agents.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Training</h3>
          <p>Pretraining, SFT, LoRA, full-parameter tuning, DPO, GRPO, inference-time optimization, vLLM.</p>
        </div>
        <div class="cv-skill-group">
          <h3>Scientific Computing</h3>
          <p>Large-scale data processing, SELEX/NGS pipelines, metagenomic mining, structure-based data mining.</p>
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
