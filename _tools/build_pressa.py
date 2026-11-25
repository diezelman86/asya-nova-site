# Builds /pressa/ from smi/index.html shell (header/footer), adds CSS and song-page blocks.
import re, html, os
R='/home/claude/asya-nova-site'
def rd(p): return open(os.path.join(R,p),encoding='utf-8').read()
def wr(p,t):
    os.makedirs(os.path.dirname(os.path.join(R,p)),exist_ok=True); open(os.path.join(R,p),'w',encoding='utf-8').write(t)
E=html.escape

RADIO=[('detskoe-radio','Детское радио','https://detifm.ru/','«Старые игрушки у камина»',('Страница АСИ NOVA на сайте радио','https://detifm.ru/artist/242682')),
 ('rebyachya-respublika','Ребячья Республика','https://vk.com/club73516844','«Любимая мама»',None),
 ('limeteens','LimeTeens','https://limeteens.ru/','«Горы синие», «Любимая мама», «Новогодний перезвон»',[('Слушать эфир «На STARTE»','https://vkvideo.ru/video-31319842_456239099'),('Слушать выпуск MUZ.TRAVEL о Боре','https://vk.ru/audio148051_456239422_1c7840a3344f5dcd9f')]),
 ('baby-fm','Baby FM','https://babyfm.ru/','«Любимая мама»',None),
 ('radio-detki','Радио Детки','https://radiodetki.ru/','«Любимая мама»',None),
 ('radio-ptitsa','Радио Птица','http://xn----7sbboub4bjd0a9b.xn--p1ai/','«Любимая мама», «Старые игрушки у камина»',None)]

# kind: pub | int | rep ; song key for song pages
ITEMS=[
 dict(k='pub',d='2026-11-15',src='Платформа «ЗВУЧИ» · Движение Первых',t='#ЗВУЧИАВТОР: авторский трек «Девица-красавица»',x='Платформа представила песню двух юных исполнительниц, где русские мотивы встречаются с современной поп-музыкой.',u='https://vk.com/wall-213706821_15051',song='devitsa-krasavitsa',go='Читать',top=1,grp='Платформа «ЗВУЧИ»'),
 dict(k='press',d='2026-10-04',src='Сайт «Детского радио»',t='Страница АСИ NOVA на сайте «Детского радио»',x='Песню «Старые игрушки у камина» можно слушать не только в эфире, но и на сайте радиостанции.',u='https://detifm.ru/artist/242682',song='starye-igrushki-u-kamina',go='Слушать на сайте радио',img='/assets/img/cover_igrushki.jpg'),
 dict(k='pub',d='2026-10-30',src='Ура! Музыка',t='#урапремьера: «Девица-красавица»',x='Лейбл «Детского радио» представил релиз дуэта АСЯ NOVA и Евгении Русевой.',u='https://vk.com/wall-226006844_2678',song='devitsa-krasavitsa',go='Читать'),
 dict(k='pub',d='2026-10-11',src='Афиша Нашего Города · Нижний Новгород',t='АСЯ NOVA и Евгения Русева. Впервые в Нижнем Новгороде!',x='Анонс премьеры «Девицы-красавицы» на главной сцене ТРК «Небо».',u='https://vk.com/wall-111650482_292814',song='devitsa-krasavitsa',go='Читать',top=1,grp='Афиша Нашего Города'),
 dict(k='pub',d='2026-08-28',src='Твой Бор',t='Борская певица АСЯ NOVA выпустила новый сингл «Такое кино»',x='О премьере песни о школьных годах, дружбе и взрослении.',u='https://vk.com/wall-8470759_766644',song='takoe-kino',go='Читать'),
 dict(k='pub',d='2026-08-28',src='Весь Бор',t='Новый релиз борской певицы: АСЯ NOVA представила песню «Такое кино»',x='Рассказ о новой песне и команде, которая над ней работала.',u='https://vk.com/wall-160837255_127485',song='takoe-kino',go='Читать',top=1),
 dict(k='press',d='2026-02-25',src='Сайт радио LimeTeens',t='Новинка эфира: премьера песни «Горы синие»',x='Радио LimeTeens о премьере песни «от талантливой исполнительницы из г. Бор».',u='https://limeteens.ru/news/tpost/5pc4u0x881-novinka-efira',song='gory-sinie',go='Читать',img='/assets/img/cover_gory.jpg'),
 dict(k='int',d='2025-12-31',src='Весь Бор',t='АСЯ NOVA о новогоднем релизе «Новогодний перезвон»',x='Интервью о песне, которая собрала сотни тысяч прослушиваний и просмотров в соцсетях.',u='https://vkvideo.ru/video-160837255_456242380',song='novogodniy-perezvon',go='Смотреть',v=(-160837255,456242380)),
 dict(k='pub',d='2025-12-24',src='Твой Бор',t='Вирусный хит от 11-летней певицы из Нижегородской области покоряет соцсети',x='О том, как «Новогодний перезвон» стал феноменом в соцсетях.',u='https://vk.com/wall-8470759_718202',song='novogodniy-perezvon',go='Читать',top=1),
 dict(k='pub',d='2025-05-13',src='Твой Бор',t='АСЯ NOVA на кастинге проекта «Голос. Дети»',x='Борчане поддерживают юную землячку.',u='https://vk.com/wall-8470759_670812',song=None,go='Читать'),
 dict(k='int',d='2025-05-02',dl='Радиоэфир',src='LimeTeens · MUZ.TRAVEL',t='MUZ.TRAVEL: выпуск о Боре с АСЕЙ NOVA',x='Выпуск рубрики MUZ.TRAVEL радио LimeTeens, посвящённый Бору — родному городу певицы, с участием АСИ NOVA.',u='https://vk.ru/audio148051_456239422_1c7840a3344f5dcd9f',song=None,go='Слушать выпуск'),
 dict(k='int',d='2025-05-03',src='LimeTeens · «На STARTE»',t='Эфир об АСЕ NOVA в передаче «На STARTE»',x='Ведущие рассказывают о биографии певицы и её планах.',u='https://vkvideo.ru/video-31319842_456239099',song=None,go='Слушать',v=(-31319842,456239099)),
 dict(k='press',d='2025-04-03',src='Журнал «Redlily. Цветы в жизни», №27',t='АСЯ NOVA на обложке и в интервью «Новая звезда»',x='Обложка весеннего номера и интервью на двух разворотах в рубрике «Мисс Redlily».',u='/pressa/redlily/',song=None,go='Смотреть журнал',img='/assets/img/cases/zhurnal-redlily/m0.jpg'),
 dict(k='int',d='2024-12-01',dl='2024',src='Конкурс «Современный вокалист»',t='Интервью после выступления с высшими баллами жюри',x='Все трое судей поставили по 10 баллов.',u='https://vkvideo.ru/video-31319842_456239031',song=None,go='Смотреть',v=(-31319842,456239031)),
]
KN={'pub':'Соцсети','press':'Пресса','int':'Интервью','rep':'Репортаж'}
MON=['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря']
def dstr(it):
    if it.get('dl'): return it['dl']
    y,m,d=it['d'].split('-'); return f'{int(d)} {MON[int(m)-1]} {y}'
def card(it,small=False):
    ext=not it['u'].startswith('/')
    tgt=' target="_blank" rel="noopener"' if ext else ''
    img=f'<div class="pr-img"><img src="{it["img"]}" alt="" loading="lazy"></div>' if it.get('img') else ''
    return (f'<a class="pr-card card" data-k="{it["k"]}" href="{E(it["u"])}"{tgt}>{img}<div class="pr-b">'
            f'<div class="pr-meta"><span class="pr-k pr-k-{it["k"]}">{KN[it["k"]]}</span><span>{E(dstr(it))}</span></div>'
            f'<div class="pr-src">{E(it["src"])}</div><h3>{E(it["t"])}</h3><p>{E(it["x"])}</p>'
            f'<span class="pr-go">{E(it["go"])} →</span></div></a>')

def vcard(it):
    o,i=it['v']
    return (f'<figure class="pr-vid card"><div class="pr-frame"><iframe src="https://vkvideo.ru/video_ext.php?oid={o}&id={i}&hd=2" title="{E(it["t"])}" loading="lazy" allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock" frameborder="0" allowfullscreen></iframe></div>'
            f'<figcaption class="pr-b"><div class="pr-meta"><span>{E(dstr(it))}</span></div><div class="pr-src">{E(it["src"])}</div><h3>{E(it["t"])}</h3><p>{E(it["x"])}</p></figcaption></figure>')

SONGSLUG={'Старые игрушки у камина':'starye-igrushki-u-kamina','Любимая мама':'lyubimaya-mama','Горы синие':'gory-sinie','Новогодний перезвон':'novogodniy-perezvon','Девица-красавица':'devitsa-krasavitsa','Такое кино':'takoe-kino','Город на левом берегу':'gorod-na-levom-beregu'}
def songlinks(s):
    return re.sub(r'«([^»]+)»',lambda m:f'<a href="/music/{SONGSLUG[m.group(1)]}/">«{m.group(1)}»</a>' if m.group(1) in SONGSLUG else m.group(0),s)

def radio_tile(r):
    slug,name,url,songs,extra=r
    ex=''.join(f'<a class="pr-ex" href="{e[1]}" target="_blank" rel="noopener">{E(e[0])} →</a>' for e in (extra if isinstance(extra,list) else [extra] if extra else []))
    return (f'<div class="pr-radio card"><a class="radio-logo" href="{url}" target="_blank" rel="noopener" title="Сайт: {E(name)}">'
            f'<img src="/assets/radio/{slug}.png" alt="{E(name)}" loading="lazy"></a><b>{E(name)}</b>'
            f'<span class="pr-songs">{songlinks(songs)} в эфире</span>{ex}</div>')

smi=rd('smi/index.html')
head_end=smi.index('</header>')+len('</header>')
foot_start=smi.index('<footer class="site-footer">')
shell_head=smi[:head_end]; shell_foot=smi[foot_start:]
TITLE='Пресса об АСЕ NOVA: публикации, интервью, радио'
DESC='Публикации СМИ, интервью и радиоэфиры юной певицы АСЯ NOVA: «Детское радио», LimeTeens, Baby FM, журнал Redlily, «Твой Бор», «Весь Бор» и другие.'
h=shell_head
h=re.sub(r'<title>.*?</title>',f'<title>{TITLE}</title>',h)
h=re.sub(r'(<meta name="description" content=")[^"]*',lambda m:m.group(1)+DESC,h)
h=re.sub(r'(<meta property="og:description" content=")[^"]*',lambda m:m.group(1)+DESC,h)
h=re.sub(r'(<meta property="og:title" content=")[^"]*',lambda m:m.group(1)+TITLE,h)
h=h.replace('https://asyanova.ru/smi/','https://asyanova.ru/pressa/')
h=h.replace(' class=active','').replace('<a href="/pressa/">Пресса</a>','<a href="/pressa/" class=active>Пресса</a>',1)
pubs=[i for i in ITEMS]
pubs.sort(key=lambda i:i['d'],reverse=True)
body=f'''
<section class="band-red" style="background:#C8102E;color:#fff"><div class="wrap split" style="padding-bottom:0;align-items:stretch">
  <div style="flex:1 1 520px;display:flex;flex-direction:column;justify-content:center;gap:22px;padding-bottom:72px">
    <div class="eyebrow" style="color:#FFD7DC">Пресса</div>
    <h1 style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(28px,3.8vw,54px);line-height:1.02;text-transform:uppercase">О певице пишут<br>и говорят</h1>
    <p style="margin:0;font-size:19px;line-height:1.55;color:#FFE3E6;max-width:560px">Радиоэфиры, интервью, публикации и обложки — всё, что СМИ рассказывают о юной певице АСЯ NOVA.</p>
  </div>
  <div style="flex:1 1 340px;min-height:420px;position:relative;border-radius:24px 24px 0 0;overflow:hidden"><img src="/assets/img/cases/zhurnal-redlily/s0.jpg" alt="Журналы с АСЯ NOVA на обложке" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 55%"></div>
</div></section>
<main class="wrap">
  <section id="radio" class="sec" aria-labelledby="pr-r">
    <h2 id="pr-r" class="h-display h2">Радио</h2>
    <p class="pr-lead">Песни АСИ NOVA звучат в эфире детских и семейных радиостанций. «Старые игрушки у камина» — в ротации «Детского радио», крупнейшей детской радиостанции страны с многомиллионной аудиторией.</p>
    <div class="pr-radios">{''.join(radio_tile(r) for r in RADIO)}</div>
    <p class="pr-note">Список радиостанций будет пополняться.</p>
  </section>
  <section id="interview" class="sec" aria-labelledby="pr-i">
    <h2 id="pr-i" class="h-display h2">Интервью</h2>
    <div class="pr-vids">{''.join(vcard(i) if i.get('v') else card(i) for i in pubs if i['k']=='int')}</div>
  </section>
  <section id="press" class="sec" aria-labelledby="pr-p">
    <h2 id="pr-p" class="h-display h2">Журналы и статьи</h2>
    <div class="pr-grid">{''.join(card(i) for i in pubs if i['k']=='press')}</div>
  </section>
  <section id="posts" class="sec" aria-labelledby="pr-a">
    <div class="sec-head"><h2 id="pr-a" class="h-display h2">Соцсети и паблики</h2><a href="/pressa/socseti/" style="font-weight:800">Все публикации в соцсетях →</a></div>
    <p class="pr-lead">Новости об АСЕ NOVA в городских сообществах, у лейбла, платформ и организаторов.</p>
    <div class="pr-grid pr-grid4">{''.join(card(i) for i in pubs if i['k']=='pub' and i.get('top'))}</div>
    <p class="pr-more"><a class="btn btn-accent" href="/pressa/socseti/">Читать остальные →</a></p>
  </section>
  <section class="sec pr-journ card" aria-labelledby="pr-j">
    <div><h2 id="pr-j" class="h-display" style="font-size:clamp(22px,2.6vw,32px);margin:0 0 8px">Вы журналист?</h2><p style="margin:0">Интервью, эфир или фотосессия с АСЕЙ NOVA — расскажем, как подготовить материал.</p></div>
    <a class="btn btn-accent" href="/smi/">Для СМИ →</a>
  </section>
</main>
'''
wr('pressa/index.html',h+body+shell_foot)

# /pressa/socseti/
posts=[i for i in pubs if i['k']=='pub']
def grp(i): return i.get('grp') or i['src']
groups=[]
for i in posts:
    if grp(i) not in groups: groups.append(grp(i))
T2='Соцсети и паблики об АСЕ NOVA — Пресса'
D2='Посты и анонсы об АСЕ NOVA в городских сообществах, у лейбла «Ура! Музыка», платформы «ЗВУЧИ» и организаторов.'
h2=h.replace(f'<title>{TITLE}</title>',f'<title>{T2}</title>').replace(DESC,D2).replace(TITLE,T2).replace('https://asyanova.ru/pressa/','https://asyanova.ru/pressa/socseti/')
def scard(i): return card(i).replace('<a class="pr-card card"',f'<a class="pr-card card" data-g="{E(grp(i))}"',1)
chips='<button type="button" class="on" data-f="all">Все</button>'+''.join(f'<button type="button" data-f="{E(g)}">{E(g)} <span>{sum(1 for i in posts if grp(i)==g)}</span></button>' for g in groups)
b2=f'''
<main class="wrap">
  <nav class="crumbs" style="margin-top:28px;font-size:14px"><a href="/">Главная</a> / <a href="/pressa/">Пресса</a> / Соцсети и паблики</nav>
  <section class="sec" style="margin-top:28px" aria-labelledby="ss-h">
    <h1 id="ss-h" class="h-display h2">Соцсети и паблики</h1>
    <p class="pr-lead">Посты и анонсы об АСЕ NOVA в городских сообществах, у лейбла, платформ и организаторов. Выберите источник:</p>
    <div class="pr-filter" role="group" aria-label="Источник">{chips}</div>
    <div class="pr-grid">{''.join(scard(i) for i in posts)}</div>
    <p class="pr-note"><a href="/pressa/">← Вся пресса об АСЕ NOVA</a></p>
  </section>
</main>
<script>document.addEventListener('click',function(e){{var b=e.target.closest('.pr-filter button');if(!b)return;var f=b.getAttribute('data-f');document.querySelectorAll('.pr-filter button').forEach(function(x){{x.classList.toggle('on',x===b)}});document.querySelectorAll('.pr-grid .pr-card').forEach(function(c){{c.hidden=!(f==='all'||c.getAttribute('data-g')===f)}});}});</script>
'''
wr('pressa/socseti/index.html',h2+b2+shell_foot)

# song-page blocks
for slug in sorted({i['song'] for i in ITEMS if i['song']}):
    p=f'music/{slug}/index.html'; t=rd(p)
    t=re.sub(r'[ \t]*<section class="sec pr-song".*?</section>\n','',t,flags=re.S)
    its=[i for i in ITEMS if i['song']==slug]
    blk=(f'<section class="sec pr-song" aria-labelledby="ps-h"><h2 id="ps-h" class="h-display h2">О песне пишут</h2>'
         f'<div class="pr-grid">{"".join(vcard(i) if i.get("v") else card(i) for i in its)}</div><p class="pr-note"><a href="/pressa/">Вся пресса об АСЕ NOVA →</a></p></section>\n')
    m=re.search(r'  <section class="sec" aria-labelledby="(mo-h|ot-h)"',t)
    i=m.start() if m else t.rindex('</main>')
    t=t[:i]+'  '+blk+t[i:]
    wr(p,t)
print('ok')


# /pressa/redlily/
T3='АСЯ NOVA в журнале «Redlily. Цветы в жизни» №27, апрель 2025 — обложка и интервью'
D3='Обложка весеннего номера журнала «Redlily. Цветы в жизни» и интервью «АСЯ NOVA — новая звезда» в рубрике «Мисс Redlily»: страницы журнала и фото со съёмки.'
h3=h.replace(f'<title>{TITLE}</title>',f'<title>{T3}</title>').replace(DESC,D3).replace(TITLE,T3).replace('https://asyanova.ru/pressa/','https://asyanova.ru/pressa/redlily/')
J='/assets/img/cases/zhurnal-redlily/'
def ph(f,alt,cls=''): return f'<a class="rl-ph {cls}" href="{J}{f}" target="_blank" rel="noopener"><img src="{J}{f}" alt="{E(alt)}" loading="lazy"></a>'
b3=f'''
<main class="wrap">
  <nav class="crumbs" style="margin-top:28px;font-size:14px"><a href="/">Главная</a> / <a href="/pressa/">Пресса</a> / Журнал «Redlily»</nav>
  <section class="sec rl-top" style="margin-top:28px" aria-labelledby="rl-h">
    <div class="rl-cover">{ph('m0.jpg','Обложка журнала «Redlily. Цветы в жизни» №27, апрель 2025, с АСЯ NOVA')}</div>
    <div class="rl-txt">
      <div class="eyebrow">Журнал · апрель 2025</div>
      <h1 id="rl-h" class="h-display h2">АСЯ NOVA на обложке журнала «Redlily. Цветы в жизни»</h1>
      <p class="pr-lead">Весенний номер №27 вышел с АСЕЙ NOVA на обложке. Внутри — интервью «АСЯ NOVA — новая звезда» в рубрике «Мисс Redlily» на двух разворотах: о музыке, сцене, конкурсах и семье.</p>
      <p><a href="https://vk.com/wall-54587732_4533" target="_blank" rel="noopener" style="font-weight:800">Пост журнала о выходе номера →</a><br><a href="https://vk.com/wall-110834174_2132" target="_blank" rel="noopener" style="font-weight:800">REDLILY KIDS: интервью после кастинга «Голос. Дети» →</a></p>
    </div>
  </section>
  <section class="sec" aria-labelledby="rl-p">
    <h2 id="rl-p" class="h-display h2">Страницы журнала</h2>
    <div class="rl-grid">{ph('m1.jpg','Разворот журнала с интервью АСЯ NOVA')}{ph('m2.jpg','Разворот журнала «АСЯ NOVA — новая звезда»')}</div>
  </section>
  <section class="sec" aria-labelledby="rl-f">
    <h2 id="rl-f" class="h-display h2">Фото со съёмки</h2>
    <div class="rl-grid">{ph('m3.jpg','АСЯ NOVA с мамой на фотосессии для журнала')}{ph('m4.jpg','АСЯ NOVA в голубом платье с букетом')}{ph('s0.jpg','Журналы с АСЯ NOVA на обложке')}{ph('s1.jpg','Стопка журналов с АСЯ NOVA')}</div>
    <p class="pr-note"><a href="/pressa/">← Вся пресса об АСЕ NOVA</a></p>
  </section>
</main>
'''
wr('pressa/redlily/index.html',h3+b3+shell_foot)
