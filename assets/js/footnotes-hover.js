// Footnote hover tooltips
// Shows footnote content when hovering over footnote references (e.g., [^1])
(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  function stripBackRef(html) {
    // Remove back-reference links typically rendered by kramdown
    return html.replace(/<a[^>]*class="footnote-backref"[^>]*>.*?<\/a>/gi, '');
  }

  function createTooltip() {
    const el = document.createElement('div');
    el.className = 'footnote-tooltip';
    el.style.position = 'absolute';
    el.style.display = 'none';
    el.setAttribute('role', 'tooltip');
    document.body.appendChild(el);
    return el;
  }

  function positionTooltip(tt, ref) {
    const rect = ref.getBoundingClientRect();
    const top = window.scrollY + rect.bottom + 8; // 8px below
    let left = window.scrollX + rect.left;
    // Prevent overflow off the right edge
    const maxWidth = tt.offsetWidth || 360;
    const viewportRight = window.scrollX + document.documentElement.clientWidth;
    if (left + maxWidth > viewportRight - 12) {
      left = Math.max(12, viewportRight - maxWidth - 12);
    }
    tt.style.top = top + 'px';
    tt.style.left = left + 'px';
  }

  ready(function () {
    const refs = document.querySelectorAll('sup a[href^="#fn"]');
    if (!refs.length) return;

    refs.forEach(function (ref) {
      const href = ref.getAttribute('href');
      if (!href) return;
      const id = href.replace('#', '');
      const li = document.getElementById(id);
      if (!li) return;

      const tt = createTooltip();
      // Use innerHTML to preserve links/emphasis; strip the backref link
      tt.innerHTML = stripBackRef(li.innerHTML);

      function show() {
        tt.style.display = 'block';
        positionTooltip(tt, ref);
      }
      function hide() {
        tt.style.display = 'none';
      }

      ref.addEventListener('mouseenter', show);
      ref.addEventListener('mouseleave', hide);
      ref.addEventListener('focus', show);
      ref.addEventListener('blur', hide);
      window.addEventListener('scroll', function () {
        if (tt.style.display === 'block') positionTooltip(tt, ref);
      }, { passive: true });
    });
  });
})();
