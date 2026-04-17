/**
 * gallery.js — Modern lightbox for paulshamrat.github.io
 * Features: prev/next nav, keyboard, swipe-to-dismiss, full image (contain),
 *           smooth animations, caption display.
 */

(function () {
  'use strict';

  // ─── State ───────────────────────────────────────────────────────────────
  let items = [];     // All gallery-link elements in DOM order
  let currentIndex = 0;

  // ─── DOM ─────────────────────────────────────────────────────────────────
  function buildLightbox() {
    if (document.getElementById('gl-lightbox')) return;

    const html = `
      <div id="gl-lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
        <div id="gl-backdrop"></div>
        <button id="gl-close" aria-label="Close">&times;</button>
        <button id="gl-prev" aria-label="Previous image">&#8249;</button>
        <button id="gl-next" aria-label="Next image">&#8250;</button>
        <div id="gl-stage">
          <img id="gl-img" alt="" draggable="false">
        </div>
        <div id="gl-caption">
          <div id="gl-caption-title"></div>
          <div id="gl-caption-context"></div>
        </div>
        <div id="gl-counter"></div>
      </div>`;

    document.body.insertAdjacentHTML('beforeend', html);

    document.getElementById('gl-backdrop').addEventListener('click', closeLightbox);
    document.getElementById('gl-close').addEventListener('click', closeLightbox);
    document.getElementById('gl-prev').addEventListener('click', showPrev);
    document.getElementById('gl-next').addEventListener('click', showNext);

    // Swipe support
    let touchStartX = 0;
    const stage = document.getElementById('gl-stage');
    stage.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', e => {
      const delta = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(delta) > 50) delta < 0 ? showNext() : showPrev();
    });
  }

  // ─── Open / Close ────────────────────────────────────────────────────────
  function openLightbox(index) {
    buildLightbox();
    currentIndex = index;
    renderSlide();
    const lb = document.getElementById('gl-lightbox');
    lb.classList.add('gl-active');
    document.body.style.overflow = 'hidden';
    lb.focus();
  }

  function closeLightbox() {
    const lb = document.getElementById('gl-lightbox');
    if (!lb) return;
    lb.classList.remove('gl-active');
    document.body.style.overflow = '';
    // Let CSS transition finish then clear src to free memory
    setTimeout(() => {
      const img = document.getElementById('gl-img');
      if (img) img.src = '';
    }, 350);
  }

  // ─── Navigation ──────────────────────────────────────────────────────────
  function showPrev() {
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    renderSlide();
  }

  function showNext() {
    currentIndex = (currentIndex + 1) % items.length;
    renderSlide();
  }

  // ─── Render ──────────────────────────────────────────────────────────────
  function renderSlide() {
    const item = items[currentIndex];
    const src = item.dataset.src;
    const title = item.dataset.title || '';
    const context = item.dataset.context || '';

    const img = document.getElementById('gl-img');
    img.classList.remove('gl-loaded');
    img.src = src;
    img.alt = title;
    img.onload = () => img.classList.add('gl-loaded');
    img.onerror = () => img.classList.add('gl-loaded'); // still reveal on error

    document.getElementById('gl-caption-title').textContent = title;
    document.getElementById('gl-caption-context').textContent = context;
    document.getElementById('gl-counter').textContent = `${currentIndex + 1} / ${items.length}`;

    // Show/hide nav arrows
    document.getElementById('gl-prev').style.display = items.length > 1 ? '' : 'none';
    document.getElementById('gl-next').style.display = items.length > 1 ? '' : 'none';
  }

  // ─── Keyboard ────────────────────────────────────────────────────────────
  document.addEventListener('keydown', e => {
    const lb = document.getElementById('gl-lightbox');
    if (!lb || !lb.classList.contains('gl-active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showPrev();
    if (e.key === 'ArrowRight') showNext();
  });

  // ─── Init ────────────────────────────────────────────────────────────────
  function init() {
    const links = document.querySelectorAll('a.gallery-link');
    if (!links.length) return;

    items = Array.from(links);

    items.forEach((link, idx) => {
      link.addEventListener('click', e => {
        e.preventDefault();
        openLightbox(idx);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
