(() => {
  const content = document.querySelector('.writing-content');
  if (!content) return;
  if (window.matchMedia('(max-width: 900px)').matches) {
    content.querySelector('.writing-toc')?.removeAttribute('open');
  }
  if (typeof window.renderMathInElement === 'function') {
    window.renderMathInElement(content, {
      delimiters: [
        {left: '\\[', right: '\\]', display: true},
        {left: '\\(', right: '\\)', display: false}
      ],
      throwOnError: false,
      trust: false
    });
  }
  const explorer = document.getElementById('ep-estimator');
  if (explorer) {
    const epSelect = explorer.querySelector('[data-ep]');
    const tokensSelect = explorer.querySelector('[data-tokens]');
    const draw = () => {
      const ep = Number(epSelect.value);
      const tokens = Number(tokensSelect.value);
      const experts = 384 / ep;
      const rows = ep * tokens * 6 / 384;
      const times = {
        compute: tokens * 7 * 70778880 / 4.5e15 * 1e6,
        weights: (experts * 18.8e6 + 35.4e6) / 8e12 * 1e6,
        communication: tokens * 6 * (1 - 1 / ep) * 15616 / 900e9 * 1e6
      };
      const format = value => value >= 1000
        ? `${(value / 1000).toFixed(2)} ms`
        : `${value.toFixed(value < 10 ? 1 : 0)} µs`;
      for (const [name, value] of Object.entries(times)) {
        explorer.querySelector(`[data-${name}]`).textContent = format(value);
      }
      explorer.querySelector('.ep-dot').style.left = `${Math.min(100, Math.log10(Math.max(1, rows)) / 5 * 100)}%`;
      const bottleneck = Object.entries(times).sort((a, b) => b[1] - a[1])[0][0];
      const labels = {compute: 'compute', weights: 'weight read', communication: 'communication'};
      explorer.querySelector('.ep-summary').textContent = `${experts} experts per GPU, ${Math.round(rows).toLocaleString()} rows per expert, ${(rows / 150).toFixed(2)}× the threshold; the longest is ${labels[bottleneck]}.`;
    };
    epSelect.addEventListener('change', draw);
    tokensSelect.addEventListener('change', draw);
    draw();
  }
})();
