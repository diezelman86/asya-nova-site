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
      if (viewer && viewer.isOpen()) return;
      var r = reader.getBoundingClientRect();
      if (r.top > window.innerHeight || r.bottom < 0) return;
      if (e.key === 'ArrowRight') go(i + 1);
      if (e.key === 'ArrowLeft') go(i - 1);
    });
    var x0 = null, y0 = null, swiped = false;
    img.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; swiped = false; }, { passive: true });
    img.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) { swiped = true; go(dx < 0 ? i + 1 : i - 1); }
    });

    // полноэкранный просмотр: свайп, двойное касание, щипок, колёсико
    var viewer = comicViewer(pages, function (k) { go(k); });
    img.addEventListener('click', function () { if (!swiped) viewer.open(i); swiped = false; });
    var fsBtn = reader.querySelector('[data-fullscreen]');
    if (fsBtn) fsBtn.addEventListener('click', function () { viewer.open(i); });
  }

  function comicViewer(pages, onPage) {
    var n = pages.length, MAX = 4;
    var ico = function (d, sw) { return '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="' + (sw || 2.4) + '" stroke-linecap="round" stroke-linejoin="round"><path d="' + d + '"></path></svg>'; };
    var el = document.createElement('div');
    el.className = 'cv'; el.hidden = true;
    el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'true'); el.setAttribute('aria-label', 'Комикс на весь экран');
    el.innerHTML =
      '<div class="cv-track"></div>' +
      '<div class="cv-bar"><span class="cv-count" aria-live="polite"></span>' +
      '<button class="cv-btn" type="button" data-z="-1" aria-label="Уменьшить">' + ico('M5 12h14') + '</button>' +
      '<button class="cv-btn" type="button" data-z="1" aria-label="Увеличить">' + ico('M12 5v14M5 12h14') + '</button>' +
      '<button class="cv-btn cv-close" type="button" data-close aria-label="Закрыть">' + ico('M6 6l12 12M18 6L6 18') + '</button></div>' +
      '<button class="cv-btn cv-nav cv-prev" type="button" data-go="-1" aria-label="Предыдущая страница">' + ico('M15 18l-6-6 6-6', 2.6) + '</button>' +
      '<button class="cv-btn cv-nav cv-next" type="button" data-go="1" aria-label="Следующая страница">' + ico('M9 18l6-6-6-6', 2.6) + '</button>' +
      '<div class="cv-tip off"></div>';
    document.body.appendChild(el);
    var track = el.querySelector('.cv-track'), count = el.querySelector('.cv-count'), tip = el.querySelector('.cv-tip');
    var zOut = el.querySelector('[data-z="-1"]'), zIn = el.querySelector('[data-z="1"]');
    var bPrev = el.querySelector('[data-go="-1"]'), bNext = el.querySelector('[data-go="1"]');
    var imgs = pages.map(function (src, k) {
      var s = document.createElement('div'); s.className = 'cv-slide';
      var im = document.createElement('img'); im.alt = k === 0 ? 'Обложка комикса' : 'Страница ' + (k + 1); im.draggable = false;
      s.appendChild(im); track.appendChild(s); return im;
    });

    var cur = 0, opened = false, usedFs = false, pushed = false, lastFocus = null;
    var z = { s: 1, x: 0, y: 0 };
    var W = function () { return el.clientWidth; };

    function load(k) { if (k >= 0 && k < n && !imgs[k].getAttribute('src')) imgs[k].src = pages[k]; }
    function place(dx, anim) {
      track.classList.toggle('anim', !!anim);
      track.style.transform = 'translate3d(' + (-cur * W() + (dx || 0)) + 'px,0,0)';
    }
    function bounds() {
      var im = imgs[cur], sl = im.parentNode;
      return { mx: Math.max(0, (im.offsetWidth * z.s - sl.clientWidth) / 2), my: Math.max(0, (im.offsetHeight * z.s - sl.clientHeight) / 2) };
    }
    function clamp() { var b = bounds(); z.x = Math.min(b.mx, Math.max(-b.mx, z.x)); z.y = Math.min(b.my, Math.max(-b.my, z.y)); }
    function applyZoom(anim) {
      var im = imgs[cur];
      im.classList.toggle('anim', !!anim);
      im.style.transform = z.s === 1 ? '' : 'translate3d(' + z.x + 'px,' + z.y + 'px,0) scale(' + z.s + ')';
      el.classList.toggle('zoomed', z.s > 1.01);
      zOut.disabled = z.s <= 1.01; zIn.disabled = z.s >= MAX - 0.01;
    }
    function resetZoom(anim) { z.s = 1; z.x = 0; z.y = 0; applyZoom(anim); }
    // увеличить до s, оставив точку экрана (px,py) на месте
    function zoomAt(s, px, py, anim) {
      s = Math.min(MAX, Math.max(1, s));
      var sl = imgs[cur].parentNode.getBoundingClientRect();
      var cx = px - (sl.left + sl.width / 2), cy = py - (sl.top + sl.height / 2);
      var lx = (cx - z.x) / z.s, ly = (cy - z.y) / z.s;
      z.s = s; z.x = cx - s * lx; z.y = cy - s * ly;
      if (s <= 1.01) { z.s = 1; z.x = 0; z.y = 0; }
      clamp(); applyZoom(anim);
    }
    function zoomCenter(f) { var r = el.getBoundingClientRect(); zoomAt(z.s * f, r.left + r.width / 2, r.top + r.height / 2, true); }

    function show(k, anim) {
      k = Math.max(0, Math.min(n - 1, k));
      if (k !== cur) resetZoom(false);
      cur = k; load(k); load(k + 1); load(k - 1);
      place(0, anim);
      count.textContent = (k + 1) + ' / ' + n;
      bPrev.disabled = k === 0; bNext.disabled = k === n - 1;
      onPage(k);
    }

    var tipTimer;
    function hint(text, ms) {
      tip.textContent = text; tip.classList.remove('off');
      clearTimeout(tipTimer); tipTimer = setTimeout(function () { tip.classList.add('off'); }, ms || 2600);
    }

    function open(k) {
      if (opened) return;
      opened = true; lastFocus = document.activeElement;
      el.hidden = false; el.classList.remove('ui-off');
      document.documentElement.style.overflow = 'hidden';
      show(k, false); resetZoom(false);
      requestAnimationFrame(function () { el.classList.add('is-open'); });
      try { history.pushState({ comicViewer: true }, ''); pushed = true; } catch (e) { pushed = false; }
      var rq = el.requestFullscreen || el.webkitRequestFullscreen;
      usedFs = false;
      if (rq) { try { var p = rq.call(el); usedFs = true; if (p && p.catch) p.catch(function () { usedFs = false; }); } catch (e) { usedFs = false; } }
      var touch = window.matchMedia && matchMedia('(hover: none)').matches;
      hint(touch ? 'Листайте свайпом · двойное касание или два пальца — увеличить' : 'Стрелки — листать · колёсико или двойной клик — увеличить', 3200);
      el.querySelector('[data-close]').focus({ preventScroll: true });
    }
    function hide() {
      if (!opened) return;
      opened = false;
      el.classList.remove('is-open'); el.hidden = true;
      document.documentElement.style.overflow = '';
      resetZoom(false);
      var fe = document.fullscreenElement || document.webkitFullscreenElement;
      if (fe === el) { var ex = document.exitFullscreen || document.webkitExitFullscreen; try { var p = ex.call(document); if (p && p.catch) p.catch(function () {}); } catch (e) {} }
      if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
    }
    function close() {
      if (!opened) return;
      if (pushed) { pushed = false; hide(); try { history.back(); } catch (e) {} }
      else hide();
    }
    // кнопка «Назад» на телефоне закрывает просмотр, а не уходит со страницы
    window.addEventListener('popstate', function () { if (opened) { pushed = false; hide(); } });
    var onFs = function () { if (opened && usedFs && !(document.fullscreenElement || document.webkitFullscreenElement)) close(); };
    document.addEventListener('fullscreenchange', onFs);
    document.addEventListener('webkitfullscreenchange', onFs);
    window.addEventListener('resize', function () { if (opened) { place(0, false); clamp(); applyZoom(false); } });

    el.addEventListener('click', function (e) {
      if (e.target.closest('[data-close]')) return close();
      var g = e.target.closest('[data-go]'); if (g) return show(cur + (+g.getAttribute('data-go')), true);
      var zb = e.target.closest('[data-z]'); if (zb) return zoomCenter(+zb.getAttribute('data-z') > 0 ? 1.6 : 1 / 1.6);
    });
    document.addEventListener('keydown', function (e) {
      if (!opened) return;
      if (e.key === 'Escape') { e.preventDefault(); close(); }
      else if (e.key === 'ArrowRight' || e.key === 'PageDown' || (e.key === ' ' && z.s === 1)) { e.preventDefault(); show(cur + 1, true); }
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(cur - 1, true); }
      else if (e.key === '+' || e.key === '=') zoomCenter(1.6);
      else if (e.key === '-' || e.key === '_') zoomCenter(1 / 1.6);
      else if (e.key === '0') resetZoom(true);
    });
    el.addEventListener('wheel', function (e) {
      e.preventDefault();
      var f = Math.exp(-e.deltaY * (e.ctrlKey ? 0.01 : 0.0025));
      zoomAt(z.s * f, e.clientX, e.clientY, false);
    }, { passive: false });

    // жесты: свайп, перетаскивание, щипок, двойное касание
    var pts = {}, mode = null, st = null, lastTap = 0, tapTimer = null;
    var ptList = function () { return Object.keys(pts).map(function (k) { return pts[k]; }); };
    var dist = function (a, b) { return Math.hypot(a.x - b.x, a.y - b.y); };
    function startPinch() {
      var p = ptList(); mode = 'pinch';
      st = { d: dist(p[0], p[1]) || 1, s: z.s, mx: (p[0].x + p[1].x) / 2, my: (p[0].y + p[1].y) / 2, zx: z.x, zy: z.y };
      place(0, true);
    }
    el.addEventListener('pointerdown', function (e) {
      if (e.target.closest('button')) return;
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      try { el.setPointerCapture(e.pointerId); } catch (er) {}
      var c = ptList().length;
      if (c === 2) startPinch();
      else if (c === 1) { mode = 'down'; st = { x: e.clientX, y: e.clientY, t: Date.now(), zx: z.x, zy: z.y }; }
    });
    el.addEventListener('pointermove', function (e) {
      if (!pts[e.pointerId]) return;
      pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      if (mode === 'pinch') {
        var p = ptList(); if (p.length < 2) return;
        var s = Math.min(MAX, Math.max(1, st.s * dist(p[0], p[1]) / st.d));
        var mx = (p[0].x + p[1].x) / 2, my = (p[0].y + p[1].y) / 2;
        var sl = imgs[cur].parentNode.getBoundingClientRect(), ox = sl.left + sl.width / 2, oy = sl.top + sl.height / 2;
        var lx = (st.mx - ox - st.zx) / st.s, ly = (st.my - oy - st.zy) / st.s;
        z.s = s; z.x = mx - ox - s * lx; z.y = my - oy - s * ly;
        clamp(); applyZoom(false);
        return;
      }
      if (!st) return;
      var dx = e.clientX - st.x, dy = e.clientY - st.y;
      if (mode === 'down' && Math.hypot(dx, dy) > 8) mode = z.s > 1.01 ? 'pan' : (Math.abs(dx) >= Math.abs(dy) ? 'swipe' : 'pull');
      if (mode === 'pan') { z.x = st.zx + dx; z.y = st.zy + dy; clamp(); applyZoom(false); }
      else if (mode === 'swipe') {
        var edge = (cur === 0 && dx > 0) || (cur === n - 1 && dx < 0);
        place(edge ? dx * 0.3 : dx, false);
      } else if (mode === 'pull') {
        var off = Math.max(0, dy);
        imgs[cur].style.transform = 'translate3d(0,' + off + 'px,0) scale(' + (1 - Math.min(off, 400) / 2000) + ')';
        el.style.backgroundColor = 'rgba(14,9,7,' + (1 - Math.min(off, 300) / 450) + ')';
      }
    });
    function endPointer(e) {
      if (!pts[e.pointerId]) return;
      delete pts[e.pointerId];
      var left = ptList().length;
      if (mode === 'pinch') {
        if (left === 1) { var p = ptList()[0]; mode = 'pan'; st = { x: p.x, y: p.y, t: 0, zx: z.x, zy: z.y }; if (z.s <= 1.01) mode = 'done'; }
        else if (!left) { mode = null; st = null; if (z.s < 1.05) resetZoom(true); }
        return;
      }
      if (left) return;
      var dx = e.clientX - (st ? st.x : 0), dy = e.clientY - (st ? st.y : 0), dt = st ? Date.now() - st.t : 999;
      if (mode === 'swipe') {
        var fast = Math.abs(dx) / Math.max(dt, 1) > 0.5 && Math.abs(dx) > 30;
        if (dx < 0 && (dx < -W() * 0.18 || fast) && cur < n - 1) show(cur + 1, true);
        else if (dx > 0 && (dx > W() * 0.18 || fast) && cur > 0) show(cur - 1, true);
        else place(0, true);
      } else if (mode === 'pull') {
        el.style.backgroundColor = '';
        if (dy > 110) close(); else { imgs[cur].classList.add('anim'); imgs[cur].style.transform = ''; }
      } else if (mode === 'down' && e.type === 'pointerup') {
        var now = Date.now(), x = e.clientX, y = e.clientY;
        if (now - lastTap < 300) {
          clearTimeout(tapTimer); lastTap = 0;
          if (z.s > 1.01) resetZoom(true); else zoomAt(2.5, x, y, true);
        } else {
          lastTap = now;
          tapTimer = setTimeout(function () { el.classList.toggle('ui-off'); }, 300);
        }
      }
      mode = null; st = null;
    }
    el.addEventListener('pointerup', endPointer);
    el.addEventListener('pointercancel', endPointer);
    el.addEventListener('dblclick', function (e) { e.preventDefault(); });
    // Safari: не даём странице масштабироваться системным жестом
    el.addEventListener('gesturestart', function (e) { e.preventDefault(); });

    return { open: open, close: close, isOpen: function () { return opened; } };
  }
})();
