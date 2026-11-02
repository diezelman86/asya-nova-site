// АСЯ NOVA — переключатель темы, карусели, читалка комикса
(function () {
  var root = document.documentElement;
  function saved() { try { return localStorage.getItem('theme'); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem('theme', v); } catch (e) {} }

  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-theme-toggle]');
    if (t) {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      save(next);
      return;
    }
    var c = e.target.closest('[data-car]');
    if (c) {
      var sec = c.closest('section');
      var track = sec && sec.querySelector('.car-track');
      if (track) track.scrollBy({ left: (c.getAttribute('data-car') === 'next' ? 1 : -1) * Math.max(280, track.clientWidth * 0.8), behavior: 'smooth' });
    }
  });

  // если пользователь не выбирал тему сам — следуем системной
  if (!saved() && window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function () { if (!saved()) root.setAttribute('data-theme', mq.matches ? 'dark' : 'light'); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
  }

  // читалка комикса
  var reader = document.querySelector('[data-reader]');
  if (reader) {
    var pages = JSON.parse(reader.getAttribute('data-pages'));
    var img = reader.querySelector('[data-page-img]');
    var num = reader.querySelector('[data-page-num]');
    var thumbs = reader.querySelectorAll('.thumbs button');
    var i = 0;
    var go = function (n) {
      i = (n + pages.length) % pages.length;
      img.src = pages[i];
      img.alt = i === 0 ? 'Обложка комикса' : 'Страница ' + (i + 1);
      num.textContent = i + 1;
      thumbs.forEach(function (b, k) { b.classList.toggle('on', k === i); });
      var on = thumbs[i]; if (on && on.scrollIntoView) on.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
      var nx = new Image(); nx.src = pages[(i + 1) % pages.length];
    };
    reader.querySelector('[data-prev]').addEventListener('click', function () { go(i - 1); });
    reader.querySelector('[data-next]').addEventListener('click', function () { go(i + 1); });
    thumbs.forEach(function (b, k) { b.addEventListener('click', function () { go(k); }); });
    document.addEventListener('keydown', function (e) {
      var r = reader.getBoundingClientRect();
      if (r.top > window.innerHeight || r.bottom < 0) return;
      if (e.key === 'ArrowRight') go(i + 1);
      if (e.key === 'ArrowLeft') go(i - 1);
    });
    var x0 = null;
    img.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    img.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 40) go(dx < 0 ? i + 1 : i - 1);
    });
  }
})();
