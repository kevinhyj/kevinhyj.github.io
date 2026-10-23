---
title: Academic CV
permalink: /cv/
eyebrow: Curriculum vitae
description: "Academic CV of Yanjie Huang (黄䶮杰), a Shanghai Jiao Tong University undergraduate building self-improving AI systems for automated research through algorithm design, synthetic data, post-training, and test-time search."
---

<section class="section page-section cv-page">
  <div class="container">
    <div class="cv-profile">
      <div class="cv-profile-copy">
        <p class="cv-name-line">Yanjie Huang <span>黄䶮杰</span></p>
        <p class="cv-lead">I am an undergraduate researcher at Shanghai Jiao Tong University. I build self-improving AI systems for automated research through algorithm design, with a focus on scientific synthetic data, post-training, test-time search, and learning from computational and experimental feedback.</p>
        <div class="resource-links cv-actions">
          <a href="mailto:huangyanjie@sjtu.edu.cn">Email me</a>
          <a class="cv-action-secondary" href="{{ '/assets/cv/Yanjie-Huang-CV.pdf' | relative_url }}" target="_blank" rel="noopener">Download CV (PDF)</a>
          <a class="cv-action-secondary" href="https://github.com/kevinhyj" target="_blank" rel="noopener">GitHub</a>
          <a class="cv-action-secondary" href="{{ '/projects/' | relative_url }}">Selected work</a>
        </div>
      </div>
      <dl class="cv-facts" aria-label="Academic profile at a glance">
        <div><dt>Education</dt><dd>SJTU · Artificial Intelligence</dd></div>
        <div><dt>Expected</dt><dd>June 2027</dd></div>
        <div><dt>GPA</dt><dd>4.0</dd></div>
        <div><dt>Focus</dt><dd>Self-improving AI</dd></div>
      </dl>
    </div>
    <section class="cv-section" aria-labelledby="cv-education">
      <div class="cv-section-title"><p class="eyebrow">01</p><h2 id="cv-education">Education</h2></div>
      <div class="cv-section-body">
        <article class="cv-entry">
          <div class="cv-entry-head"><div class="cv-institution"><img class="cv-institution-logo" src="{{ '/assets/shared/logos/sjtu.png' | relative_url }}" alt="Shanghai Jiao Tong University logo"><div><h3>Shanghai Jiao Tong University</h3><p class="cv-role">Department of Artificial Intelligence</p></div></div></div>
          <p class="cv-date">Sep 2023 – Jun 2027</p>
          <p>GPA: <strong>4.0</strong> · Cohort rank: <strong>2/22</strong> · Shanghai, China</p>
          <p>Selected for the Bolè Plan (Elite Scientific Talent Program), one of 30 students among 18,584 SJTU undergraduates.</p>
        </article>
      </div>
    </section>
    <section class="cv-section" aria-labelledby="cv-experience">
      <div class="cv-section-title"><p class="eyebrow">02</p><h2 id="cv-experience">Research Experience</h2></div>
      <div class="cv-section-body">
        <article class="cv-entry cv-entry-featured">
          <div class="cv-entry-head"><div class="cv-institution"><img class="cv-institution-logo" src="{{ '/assets/shared/logos/stanford.webp' | relative_url }}" alt="Stanford University logo"><div><h3>Stanford University</h3><p class="cv-role">Research Assistant</p></div></div></div>
          <p>Advisors: <strong>Prof. Yejin Choi</strong>, <strong>Prof. Jure Leskovec</strong>, and <strong>Dr. Fang Wu</strong>.</p>
          <ul class="cv-list">
            <li><strong>Recursive Self-Improvement for ML Research and Engineering · Ongoing.</strong> Implementing and empirically evaluating recursive self-improvement approaches for kernel optimization and ML algorithm development.</li>
            <li><strong>UniEvo-VL · May – Sep 2026 · Co-first author.</strong> Built the initial distributed OPSD pipeline, integrating on-policy sampling, critique-conditioned teacher feedback, LoRA updates, and evaluation; implemented ablations over noise, prompts, seeds, denoising steps, and teacher dynamics. The framework improved Qwen-Image-2512 from 0.747 to 0.808 on GenEval and from 32.97 to 35.53 on GenEval2 Soft-TIFA.</li>
            <li><strong>Proteo-R2 · May 2026 – Present.</strong> Built pipelines to generate, filter, and standardize reasoning traces for text-molecule alignment, mid-training, and joint training; trained residue- and atom-level reasoning models for controllable molecular design.</li>
            <li><strong>ProteoCraft · Mar – May 2026 · Co-first author.</strong> Built reproducible benchmarks across search strategies and diffusion- and hallucination-based baselines for binder and TCR design. Contributed architecture, template and domain redesign, and Monte Carlo Tree Search; reduced memory usage by 40%.</li>
          </ul>
        </article>
        <article class="cv-entry">
          <div class="cv-entry-head"><div class="cv-institution"><div><h3>Columbia University</h3><p class="cv-role">Research Team Leader</p></div></div></div>
          <p>Advisors: Prof. Erran Li and Dr. Fang Wu.</p>
          <ul class="cv-list">
            <li><strong>Proteo-R1 · Mar – Apr 2026.</strong> Synthesized reasoning data for alignment, mid-training, and joint training, improving indexing ability by 40% and translating model understanding into controllable antibody design. ICML (Accepted).</li>
          </ul>
        </article>
        <article class="cv-entry">
          <div class="cv-entry-head"><div class="cv-institution"><div><h3>Tsinghua University</h3><p class="cv-role">Research Team Leader</p></div></div></div>
          <p>Advisor: Prof. Yi Lin.</p>
          <ul class="cv-list">
            <li><strong>PhaseFlow · May 2025 – Jul 2026.</strong> Built data and quality-control pipelines for a high-throughput phase-separation dataset and a unified model combining sequence generation with flow matching for phase-diagram prediction. Outperformed DDPM and Transformer-only baselines; implemented inference-time scaling, improving self-consistency by 30%.</li>
          </ul>
        </article>
        <article class="cv-entry">
          <div class="cv-entry-head"><div class="cv-institution"><img class="cv-institution-logo" src="{{ '/assets/shared/logos/sjtu.png' | relative_url }}" alt="Shanghai Jiao Tong University logo"><div><h3>Shanghai Jiao Tong University</h3><p class="cv-role">Research Team Leader</p></div></div></div>
          <p>Advisor: Prof. Shuangjia Zheng.</p>
          <ul class="cv-list">
            <li><strong>EVA · Jul 2025 – Mar 2026.</strong> Developed MoE architectures with MegaBlocks and the first pretraining and mid-training code, achieving 30% lower perplexity than the dense baseline; co-curated and released OpenRNA v1 across more than 15 RNA types. Used sparse autoencoders to identify structure/function features (Spearman &gt; 0.9) and steer generation. The best designed aptamers improved fluorescence and binding affinity by 2x over the positive control.</li>
            <li><strong>Non-canonical amino acid design · May 2025 – Jul 2026.</strong> Used experimental data for DPO-based few-shot learning, improving enrichment of high-fitness proteins by 30%; built BoltzGen, Boltz2, and AlphaFold generator-predictor pipelines, yielding 2 successful designs and 14x activity improvement.</li>
            <li><strong>RNA evolution · Jul 2024 – Mar 2025.</strong> Combined inverse-folding and language-model approaches for RNA design and fitness benchmarking, achieving 2.6x in vivo fluorescence improvement for multiple variants.</li>
          </ul>
        </article>
        <article class="cv-entry">
          <div class="cv-entry-head"><div class="cv-institution"><div><h3>Massachusetts Institute of Technology</h3><p class="cv-role">Research Assistant</p></div></div></div>
          <p>Advisor: Dr. Jack Xiaoyu Chen.</p>
          <ul class="cv-list">
            <li><strong>SynthArchitect · Mar – May 2025.</strong> Built an agent integrating 20+ tools, including Golden Gate and DNA Cauldron, for automated plasmid engineering and laboratory workflows.</li>
          </ul>
        </article>
      </div>
    </section>
    <section class="cv-section" aria-labelledby="cv-research">
      <div class="cv-section-title"><p class="eyebrow">03</p><h2 id="cv-research">Selected Research</h2></div>
      <div class="cv-section-body">
        <div class="cv-project-grid">
          <a class="cv-project" href="{{ '/work/self-evolving-diffusion/' | relative_url }}">
            <p class="eyebrow">Multimodal self-improvement · May – Sep 2026</p><h3>UniEvo-VL</h3><p>Co-first author. Built distributed critique-conditioned on-policy self-distillation for unified multimodal models. ICLR 2027 (Under Review).</p><span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/recursive-self-improvement/' | relative_url }}">
            <p class="eyebrow">Automated ML research · Ongoing</p><h3>Recursive Self-Improvement</h3><p>Implementing and empirically evaluating self-improvement approaches for kernel optimization and ML algorithm development.</p><span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/eva/' | relative_url }}">
            <p class="eyebrow">Lab-in-the-loop learning</p><h3>EVA</h3><p>Team leader and first author. Connected MoE model development, mechanistic interpretability, and experimentally validated RNA design.</p><span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/phaseflow/' | relative_url }}">
            <p class="eyebrow">Multimodal modeling · Inference-time scaling</p><h3>PhaseFlow</h3><p>Team leader and co-first author. Built sequence-and-flow modeling and inference-time scaling for controllable phase-separating protein design.</p><span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/proteo-r1-r2/' | relative_url }}">
            <p class="eyebrow">Scientific reasoning synthetic data</p><h3>Proteo-R1 / Proteo-R2</h3><p>Built synthetic reasoning data and trained multimodal models for controllable molecular design at residue and atom resolution.</p><span>View project →</span>
          </a>
          <a class="cv-project" href="{{ '/work/proteocraft/' | relative_url }}">
            <p class="eyebrow">Inference-time search · Efficient evaluation</p><h3>ProteoCraft</h3><p>Co-first author. Built search benchmarks and contributed architecture and Monte Carlo Tree Search, reducing memory usage by 40%.</p><span>View project →</span>
          </a>
        </div>
      </div>
    </section>
    <section class="cv-section" aria-labelledby="cv-publications">
      <div class="cv-section-title"><p class="eyebrow">04</p><h2 id="cv-publications">Selected Publications</h2></div>
      <div class="cv-section-body cv-publications">
        <article class="cv-publication"><span class="cv-publication-index">01</span>
          <div><h3>UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement</h3><p>Fang Wu*, Da Xing*, <strong>Yanjie Huang*</strong>, Junxi Wang*, …, Jure Leskovec†, Yejin Choi† · ICLR 2027 (Under Review)</p><div class="resource-links"><a href="https://arxiv.org/abs/2609.38721" target="_blank" rel="noopener">Preprint</a> <a href="{{ '/work/self-evolving-diffusion/' | relative_url }}">Project page</a></div></div>
        </article>
        <article class="cv-publication"><span class="cv-publication-index">02</span>
          <div><h3>EVA: A Long-Context Generative Foundation Model Deciphers RNA Design Principles</h3><p><strong>Yanjie Huang*</strong>, Guang Lv*, …, Yi Yang†, Shuangjia Zheng† · <em>Nature Machine Intelligence</em> (Accepted, Spotlight, Top 10%) · 2026</p><div class="resource-links"><a href="https://www.biorxiv.org/content/10.64898/2026.03.17.712398v2" target="_blank" rel="noopener">Preprint</a> <a href="{{ '/work/eva/' | relative_url }}">Project page</a></div></div>
        </article>
        <article class="cv-publication"><span class="cv-publication-index">03</span>
          <div><h3>PhaseFlow: A Unified Model for Multi-scale Biomolecular Condensates Understanding and Design</h3><p>Yi Zhu*, <strong>Yanjie Huang*</strong>, …, Shuangjia Zheng†, Yi Lin† · <em>Nature</em> (Under Review) · 2026</p><div class="resource-links"><a href="{{ '/work/phaseflow/' | relative_url }}">Project page</a></div></div>
        </article>
        <article class="cv-publication"><span class="cv-publication-index">04</span>
          <div><h3>Energy-Adaptive Elastic Equivariant Transformer-SSM for Noise-Robust Protein Structure Representation</h3><p>Zhongyue Zhang, Runze Ma, <strong>Yanjie Huang</strong>, Shuangjia Zheng† · NeurIPS 2026 (Accepted)</p><div class="resource-links"><a href="https://arxiv.org/abs/2503.16996" target="_blank" rel="noopener">Preprint</a></div></div>
        </article>
        <article class="cv-publication"><span class="cv-publication-index">05</span>
          <div><h3>ProteoCraft: Proposal-Verification Search for Protein Design with Diffusion Structure Predictors</h3><p>F. Wu*, H. Lin*, B. Duan*, <strong>Yanjie Huang*</strong>, Y. Li*, …, Jure Leskovec†, Yejin Choi† · ICLR 2027 (Under Review)</p><div class="resource-links"><a href="{{ '/work/proteocraft/' | relative_url }}">Project page</a></div></div>
        </article>
        <article class="cv-publication"><span class="cv-publication-index">06</span>
          <div><h3>Capturing Natural Evolution in RNA Design for in Vivo Functionality via Genomic Foundational Models</h3><p><strong>Yanjie Huang*</strong>, B. Zhang*, …, Yi Yang†, Shuangjia Zheng† · <em>Communications Biology</em> (Under Review) · 2025</p><div class="resource-links"><a href="https://doi.org/10.1101/2025.04.08.647793" target="_blank" rel="noopener">Preprint</a> <a href="{{ '/work/rillie/' | relative_url }}">Project page</a></div></div>
        </article>
        <article class="cv-publication"><span class="cv-publication-index">07</span>
          <div><h3>What Matters in RL for Diffusion Models? The Dominant Role of Noise</h3><p>Da Xing, Haokai Zhao, Yanchao Li, Hanqun Cao, <strong>Yanjie Huang</strong>, …, Yejin Choi†, Fang Wu† · ICLR 2027 (Under Review)</p><div class="resource-links"><a href="{{ '/work/rl-diffusion/' | relative_url }}">Project page</a></div></div>
        </article>

      </div>
    </section>
    <section class="cv-section" aria-labelledby="cv-awards">
      <div class="cv-section-title"><p class="eyebrow">05</p><h2 id="cv-awards">Honors</h2></div>
      <div class="cv-section-body">
        <ul class="cv-honors">
          <li><span>2026</span><strong>National Scholarship for Undergraduate Students</strong><p>Sep 2026.</p></li>
          <li><span>SJTU</span><strong>Bolè Plan</strong><p>Elite Scientific Talent Program, Shanghai Jiao Tong University.</p></li>
          <li><span>2022</span><strong>Bronze Medal</strong><p>Chinese Mathematical Olympiad · Dec 2022.</p></li>
          <li><span>2021</span><strong>First Prize · International Round</strong><p>International Mathematical Modeling Challenge · Jul 2021.</p></li>
        </ul>
      </div>
    </section>
    <section class="cv-section" aria-labelledby="cv-skills">
      <div class="cv-section-title"><p class="eyebrow">06</p><h2 id="cv-skills">Technical Focus</h2></div>
      <div class="cv-section-body cv-skill-groups">
        <div class="cv-skill-group"><h3>Models &amp; Training</h3><p>MoE Transformers; unified multimodal and diffusion models (Qwen-Image, BAGEL); multimodal alignment; pretraining, SFT, DPO, on-policy self-distillation (OPSD), and LoRA.</p></div>
        <div class="cv-skill-group"><h3>Data &amp; Evaluation</h3><p>Scientific reasoning synthetic data; large-scale data processing (&gt;150 TB); streaming quality control; benchmarking and ablation studies.</p></div>
        <div class="cv-skill-group"><h3>Systems</h3><p>Distributed training; Megatron-LM; MegaBlocks; vLLM; agentic systems (LangChain, Qwen-Agent).</p></div>
        <div class="cv-skill-group"><h3>Programming</h3><p>Python, C++, Shell.</p></div>
      </div>
    </section>
    <section class="cv-contact" aria-labelledby="cv-contact-title">
      <p class="eyebrow">PhD &amp; research opportunities</p>
      <h2 id="cv-contact-title">Let's build AI that improves how research is done.</h2>
      <p>I am happy to discuss research collaborations, PhD opportunities, and research engineering roles in self-improving AI and automated research.</p>
      <a class="button" href="mailto:huangyanjie@sjtu.edu.cn">huangyanjie@sjtu.edu.cn</a>
    </section>
  </div>
</section>
