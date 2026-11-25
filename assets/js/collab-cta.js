/* Плавающая кнопка «Обсудить проект» на страницах сотрудничества и кейсов.
   Появляется после первого экрана, прячется, когда видны контакты продюсера.
   Клик по кнопке → цель collab_cta; клик по контактам в кейсах → collab_contact. */
(function () {
  var target = document.getElementById('contacts');
  if (!target) return;

  function goal(n, p) {
    try { if (window.ym) ym(114138090, 'reachGoal', n, p || {}); } catch (e) {}
    try { (window._tmr = window._tmr || []).push({ type: 'reachGoal', id: 3815746, goal: n }); } catch (e) {}
  }

  var label = document.body.getAttribute('data-cta') || 'Обсудить проект';
  var css = document.createElement('style');
  css.textContent =
    '.cc-fab{position:fixed;right:20px;bottom:20px;z-index:60;display:inline-flex;align-items:center;gap:10px;' +
    'padding:14px 22px 14px 18px;border-radius:999px;background:#ffd23f;color:#1d1b1a!important;text-decoration:none!important;' +
    'font:800 15px/1 Manrope,system-ui,sans-serif;box-shadow:0 12px 30px -10px rgba(0,0,0,.45),0 0 0 3px rgba(255,255,255,.7);' +
    'opacity:0;transform:translateY(16px);pointer-events:none;transition:opacity .25s,transform .25s}' +
    '.cc-fab.on{opacity:1;transform:none;pointer-events:auto}' +
    '.cc-fab:hover{transform:translateY(-2px)}' +
    '.cc-fab:focus-visible{outline:3px solid #d7262e;outline-offset:3px}' +
    '.cc-fab svg{flex:none}' +
    '@media (max-width:600px){.cc-fab{left:16px;right:16px;bottom:14px;justify-content:center;padding:15px 18px}}' +
    '@media (prefers-reduced-motion:reduce){.cc-fab{transition:none}}';
  document.head.appendChild(css);

  var a = document.createElement('a');
  a.className = 'cc-fab';
  a.href = '#contacts';
  a.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span></span>';
  a.querySelector('span').textContent = label;
  document.body.appendChild(a);

  a.addEventListener('click', function (e) {
    e.preventDefault();
    goal('collab_cta', { page: location.pathname, from: 'fab' });
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (history.replaceState) history.replaceState(null, '', '#contacts');
  });

  var contactsVisible = false;
  function update() {
    var past = (window.scrollY || window.pageYOffset) > window.innerHeight * 0.6;
    a.classList.toggle('on', past && !contactsVisible);
  }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      contactsVisible = es[0].isIntersecting; update();
    }, { rootMargin: '0px 0px -10% 0px' }).observe(target.closest('section') || target);
  }
  window.addEventListener('scroll', update, { passive: true });
  update();

  /* Остальные кнопки, ведущие к контактам (в шапке, на первом экране) */
  document.addEventListener('click', function (e) {
    var l = e.target.closest && e.target.closest('a[href="#contacts"]');
    if (l && l !== a) goal('collab_cta', { page: location.pathname, from: 'button' });
  });

  /* В кейсах контакты лежат в .contact-card — на них site.js не подключён */
  if (!document.querySelector('.prod-contacts')) {
    document.addEventListener('click', function (e) {
      var c = e.target.closest && e.target.closest('.contact-card a');
      if (c) goal('collab_contact', { page: location.pathname });
    });
  }
})();
