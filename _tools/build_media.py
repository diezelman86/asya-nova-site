import re, html, os, glob
R='/home/claude/asya-nova-site'; os.chdir(R); E=html.escape
def rd(p): return open(p,encoding='utf-8').read()
def wr(p,t): os.path.dirname(p) and os.makedirs(os.path.dirname(p),exist_ok=True); open(p,'w',encoding='utf-8').write(t)
ALT={}
for f in glob.glob('**/*.html',recursive=True):
    for src,alt in re.findall(r'<img src="/assets/img/([a-z]+_\d+\.jpg)" alt="([^"]+)"',rd(f)): ALT.setdefault(src,html.unescape(alt))
smi=rd('smi/index.html'); HEAD=smi[:smi.index('</header>')+9]; FOOT=smi[smi.index('<footer class="site-footer">'):]
def head(title,desc,url):
    h=re.sub(r'<title>.*?</title>',f'<title>{E(title)}</title>',HEAD)
    for a in ('name="description"','property="og:description"'): h=re.sub(r'(<meta '+a+r' content=")[^"]*',lambda m:m.group(1)+E(desc),h)
    h=re.sub(r'(<meta property="og:title" content=")[^"]*',lambda m:m.group(1)+E(title),h)
    h=h.replace('https://asyanova.ru/smi/',url).replace(' class=active','')
    return h.replace('<a href="/media/">Медиа</a>','<a href="/media/" class=active>Медиа</a>')
ALB=[('devitsa-krasavitsa','dev','Девица-красавица','Фотосессия к релизу дуэта АСЯ NOVA и Евгении Русевой','/music/devitsa-krasavitsa/','1826'),
 ('gory-sinie','gory','Горы синие','Фотосессия к песне «Горы синие»','/music/gory-sinie/','8604'),
 ('starye-igrushki','igr','Старые игрушки у камина','Фотосессия к песне «Старые игрушки у камина»','/music/starye-igrushki-u-kamina/','7041'),
 ('takoe-kino','kino','Такое кино','Фотосессия к песне «Такое кино»','/music/takoe-kino/','1984'),
 ('gorod','gorod','Город на левом берегу','Фотосессия к песне «Город на левом берегу»','/music/gorod-na-levom-beregu/','8440'),
 ('lyubimaya-mama','mama','Любимая мама','Фотосессия к песне «Любимая мама»','/music/lyubimaya-mama/','1107'),
 ('promo','main','Промо-фотосессия','Портреты АСИ NOVA для афиш, СМИ и соцсетей',None,'1993')]
VID=[('-31319842','456239296','Девица-красавица','LIVE · Сергиевская ярмарка'),('-31319842','456239235','Старые игрушки у камина','LIVE-клип'),
 ('-31319842','456239122','Горы синие','LIVE'),('-31319842','456239120','Город на левом берегу','LIVE'),('-31319842','456239124','Любимая мама','LIVE')]

def kb(p):
    s=os.path.getsize(p); return f'{s/1048576:.1f} МБ'.replace('.',',') if s>1048576 else f'{s//1024} КБ'
WALL=[('novogodniy-perezvon','Новогодний перезвон'),('asya-1','АСЯ NOVA'),('asya-2','АСЯ NOVA'),('asya-3','АСЯ NOVA'),('devitsa-krasavitsa','Девица-красавица'),('gory-sinie','Горы синие'),('starye-igrushki','Старые игрушки у камина')]
SONGS=[('novogodniy-perezvon','Новогодний перезвон'),('devitsa-krasavitsa','Девица-красавица'),('lyubimaya-mama','Любимая мама'),('starye-igrushki-u-kamina','Старые игрушки у камина'),('gory-sinie','Горы синие'),('takoe-kino','Такое кино'),('gorod-na-levom-beregu','Город на левом берегу')]
COV={'devitsa-krasavitsa':'cover_devica','gorod-na-levom-beregu':'cover_gorod','gory-sinie':'cover_gory','starye-igrushki-u-kamina':'cover_igrushki','takoe-kino':'cover_kino','lyubimaya-mama':'cover_mama','novogodniy-perezvon':'cover_novogodniy'}
walls=''.join(f'<a class="fn-wall" href="/files/fans/oboi-{s}.jpg" download="asya-nova-oboi-{s}.jpg" data-fan="oboi-{s}"><img src="/assets/fans/oboi-{s}.jpg" alt="Обои на телефон: {E(n)}" loading="lazy" width="270" height="480"><span>Скачать</span></a>' for s,n in WALL)
texts=''.join(f'<a class="fn-file card" href="/files/fans/tekst-{s}.pdf" download data-fan="tekst-{s}"><img src="/assets/img/{COV[s]}.jpg" alt="" loading="lazy"><span><b>{E(n)}</b><small>PDF · {kb(f"files/fans/tekst-{s}.pdf")}</small></span><i>↓</i></a>' for s,n in SONGS)
KP='files/fans/komiks-devitsa-krasavitsa.pdf'

def photos(pre): return sorted(os.path.basename(f) for f in glob.glob(f'assets/img/{pre}_*.jpg'))
vids=''.join(f'<figure class="pr-vid card"><div class="pr-frame"><iframe src="https://vkvideo.ru/video_ext.php?oid={o}&id={i}&hd=2" title="{E(t)}" loading="lazy" allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock" frameborder="0" allowfullscreen></iframe></div><figcaption class="pr-b"><div class="pr-meta"><span>{E(k)}</span></div><h3>{E(t)}</h3></figcaption></figure>' for o,i,t,k in VID)
tiles=''.join(f'<a class="md-alb card" href="/media/foto/{s}/"><img src="/assets/img/{p}_{c}.jpg" alt="{E(n)}" loading="lazy"><span><b>{E(n)}</b><small>{len(photos(p))} фото</small></span></a>' for s,p,n,d,u,c in ALB)
T='Медиа АСИ NOVA: видео, фото, комиксы, обои и тексты песен'; D='Концертные видео, фотоальбомы, комикс и бесплатные файлы для фанатов юной певицы АСЯ NOVA: обои на телефон, комикс в PDF, тексты песен.'
body=f'''
<section class="band-red" style="background:#121212;color:#fff"><div class="wrap" style="padding-top:64px;padding-bottom:64px">
  <div class="eyebrow" style="color:#FFD7DC">Медиа</div>
  <h1 style="margin:12px 0 18px;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(28px,3.8vw,54px);line-height:1.02;text-transform:uppercase">Видео и фото</h1>
  <p style="margin:0;font-size:19px;line-height:1.55;color:#ddd;max-width:640px">Концертные видео, фотоальбомы, комиксы и бесплатные файлы для фанатов.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px"><a class="btn" style="background:#fff;color:#121212" href="#video">Видео</a><a class="btn" style="border-color:#fff;color:#fff" href="#foto">Фото</a><a class="btn" style="border-color:#fff;color:#fff" href="#komiks">Комиксы и игра</a><a class="btn" style="border-color:#fff;color:#fff" href="#skachat">Скачать</a></div>
</div></section>
<main class="wrap">
  <section id="video" class="sec" aria-labelledby="md-v">
    <div class="sec-head"><h2 id="md-v" class="h-display h2" style="margin:0">Видео</h2><a href="https://vkvideo.ru/@asya_nova_sing/all" target="_blank" rel="noopener" style="font-weight:800">Все видео во ВКонтакте →</a></div>
    <h3 class="fn-h3" style="margin-top:0">Концертные видео</h3>
    <div class="pr-vids">{vids}</div>
    <p class="pr-note">Интервью и радиоэфиры — в разделе <a href="/pressa/#interview">«Пресса»</a>.</p>
  </section>
  <section id="foto" class="sec" aria-labelledby="md-f">
    <h2 id="md-f" class="h-display h2">Фото</h2>
    <h3 class="fn-h3" style="margin-top:0">Фотосессии</h3>
    <div class="md-albs">{tiles}</div>
  </section>
  <section id="komiks" class="sec" aria-labelledby="md-k">
    <h2 id="md-k" class="h-display h2">Комиксы и игра</h2>
    <div class="fn-tiles">
      <a class="fn-tile card" href="/komiks/"><img src="/assets/img/c_01.jpg" alt="Комикс «Девица-красавица»" loading="lazy"><span><b>Комикс «Девица-красавица»</b><small>Читать онлайн</small></span></a>
      <a class="fn-tile card" href="https://vk.ru/app54835318_-31319842" target="_blank" rel="noopener"><img src="/assets/img/h_game-poster.jpg" alt="Игра «Весёлая ярмарка»" loading="lazy"><span><b>Игра «Весёлая ярмарка»</b><small>Мини-игра по мотивам песни и комикса во ВКонтакте</small></span></a>
    </div>
  </section>
  <section id="skachat" class="sec" aria-labelledby="md-d">
    <h2 id="md-d" class="h-display h2">Фанатам: скачать бесплатно</h2>
    <h3 class="fn-h3" style="margin-top:0">Обои на телефон</h3>
    <p class="pr-lead" style="margin-top:0">Нажмите на картинку, чтобы скачать в полном размере (1080×1920).</p>
    <div class="fn-walls">{walls}</div>
    <h3 class="fn-h3">Комикс в PDF</h3>
    <a class="fn-file fn-big card" href="/{KP}" download data-fan="komiks-pdf"><img src="/assets/img/c_01.jpg" alt="" loading="lazy"><span><b>Комикс «Девица-красавица»</b><small>Все 19 страниц в одном файле — читать и распечатывать · PDF · {kb(KP)}</small></span><i>↓</i></a>
    <h3 class="fn-h3">Тексты песен для печати</h3>
    <p class="pr-lead" style="margin-top:0">Для репетиций, караоке и вокальных занятий. Минусовки — на страницах песен.</p>
    <div class="fn-files">{texts}</div>
    <h3 class="fn-h3">Скоро</h3>
    <p class="pr-lead" style="margin-top:0">Стикеры для печати, раскраски и открытки — следите за обновлениями.</p>
  </section>
</main>
'''
wr('media/index.html',head(T,D,'https://asyanova.ru/media/')+body+FOOT)
for s,p,n,d,u,c in ALB:
    ph=photos(p)
    gal=''.join(f'<a href="/assets/img/{f}" data-gal><img src="/assets/img/{f}" alt="{E(ALT.get(f,n))}" loading="lazy"></a>' for f in ph)
    link=f'<a href="{u}" style="font-weight:800">Песня «{E(n)}»: слушать, текст, минус →</a>' if u else ''
    b=f'''
<main class="wrap">
  <nav class="crumbs" style="margin-top:28px;font-size:14px"><a href="/">Главная</a> / <a href="/media/">Медиа</a> / <a href="/media/#foto">Фото</a> / {E(n)}</nav>
  <section class="sec" style="margin-top:28px" aria-labelledby="al-h">
    <div class="eyebrow" style="margin-bottom:10px">Фотосессия · {len(ph)} фото</div>
    <h1 id="al-h" class="h-display h2" style="margin-bottom:14px">{E(n)}</h1>
    <p class="pr-lead">{E(d)}. Нажмите на фото, чтобы открыть его крупно.</p>
    <p>{link}</p>
    <div class="md-gal">{gal}</div>
    <p class="pr-note"><a href="/media/#foto">← Все альбомы</a></p>
  </section>
</main>
'''
    wr(f'media/foto/{s}/index.html',head(f'{n} — фотосессия АСИ NOVA | Медиа',f'{d}: {len(ph)} фото.',f'https://asyanova.ru/media/foto/{s}/')+b+FOOT)
print('ok', [ (s,len(photos(p))) for s,p,*_ in ALB])

# redirect /fanatam/ -> /media/#skachat
wr('fanatam/index.html','<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Фанатам — АСЯ NOVA</title><meta name="robots" content="noindex"><link rel="canonical" href="https://asyanova.ru/media/"><meta http-equiv="refresh" content="0; url=/media/#skachat"><script>location.replace("/media/#skachat")</script></head><body><a href="/media/#skachat">Перейти в раздел «Медиа»</a></body></html>')
s=rd('sitemap.xml')
s=re.sub(r'\s*<url><loc>https://asyanova.ru/fanatam/</loc>.*?</url>','',s)
for u in ['/media/']+[f'/media/foto/{a[0]}/' for a in ALB]:
    if u not in s: s=s.replace('</urlset>',f'  <url><loc>https://asyanova.ru{u}</loc><priority>0.5</priority></url>\n</urlset>')
wr('sitemap.xml',s)
