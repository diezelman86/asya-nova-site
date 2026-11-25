"""Собирает статичный сайт АСЯ NOVA в /home/claude/asya-nova-site"""
import sys, json, os, html
sys.path.insert(0, '/home/claude/scripts')
from songs import L, PAGES as SPAGES

ROOT = '/home/claude/asya-nova-site/'
IMG = '/assets/img/'
DOMAIN = 'https://asyanova.ru'


RADIO = [('Детское радио','detskoe-radio'),('Ребячья Республика','rebyachya-respublika'),('LimeTeens','limeteens'),('Baby FM','baby-fm'),('Радио Детки','radio-detki'),('Радио Птица','radio-ptitsa')]
def radio_html():
    out=[]
    for n,f in RADIO:
        logo=None
        for ext in ('.svg','.png','.jpg','.webp'):
            if os.path.exists(ROOT+'assets/radio/'+f+ext): logo='/assets/radio/'+f+ext; break
        inner=(f'<span class="radio-logo"><img src="{logo}" alt="{n}" loading="lazy"></span><span class="radio-name">{n}</span>' if logo else f'<b>{n}</b>')
        out.append(f'      <div class="radio-tile" title="{n}">{inner}</div>')
    return "\n".join(out)

import hashlib
def ver(path):
    data = theme_css().encode() if path == 'themes' else open(ROOT + path, 'rb').read()
    return hashlib.md5(data).hexdigest()[:8]
def img(name):
    for ext in ('.jpg', '.png'):
        if os.path.exists(ROOT + 'assets/img/' + name + ext):
            return IMG + name + ext
    raise SystemExit('no image ' + name)


# ---------- темы: светлая / тёмная ----------
FONTS = {
 'brand': ("Unbounded, sans-serif", '900', 'normal', 'uppercase', 'clamp(44px,4.8vw,68px)'),
 'devica': ("Kurale, Georgia, serif", '400', 'normal', 'none', 'clamp(42px,4.6vw,64px)'),
 'gory': ("Philosopher, Georgia, serif", '700', 'italic', 'none', 'clamp(44px,4.8vw,66px)'),
 'kino': ("'Russo One', Impact, sans-serif", '400', 'normal', 'uppercase', 'clamp(44px,4.8vw,68px)'),
 'igr': ("'Playfair Display', Georgia, serif", '700', 'normal', 'none', 'clamp(40px,4.4vw,60px)'),
 'mama': ("'Marck Script', cursive", '400', 'normal', 'none', 'clamp(52px,5.6vw,80px)'),
 'gorod': ("Comfortaa, sans-serif", '700', 'normal', 'none', 'clamp(40px,4.4vw,60px)'),
 'novogod': ("'Cormorant Garamond', Georgia, serif", '700', 'italic', 'none', 'clamp(48px,5.2vw,72px)'),
}
K = ['bg', 'surface', 'border', 'ink', 'muted', 'accent', 'accent-text', 'on-accent', 'label', 'bar', 'bar-muted', 'chip', 'header-bg', 'chorus', 'dashed', 'hero-bg', 'cream']


def T(bg, surface, border, ink, muted, accent, accent_text, on_accent, label, bar, bar_muted, chip, header_bg, chorus, dashed, hero_bg=None, cream=None):
    return dict(zip(K, [bg, surface, border, ink, muted, accent, accent_text, on_accent, label, bar, bar_muted, chip, header_bg, chorus, dashed, hero_bg or bg, cream or surface]))


THEMES = {
 'brand': (T('#F2F1EE', '#FFFFFF', '#DEDCD7', '#121212', '#5B5852', '#C8102E', '#C8102E', '#FFFFFF', '#C8102E', '#121212', '#BDBAB4', '#F2F1EE', 'rgba(242,241,238,.92)', '#C8102E', '#CFCAC2', '#C4C4C3', '#FFF4E6'),
           T('#0F0F10', '#1A1A1C', '#2C2C2F', '#F2F1EE', '#A9A6A0', '#E0243C', '#FF5A6E', '#FFFFFF', '#FF5A6E', '#000000', '#A9A6A0', '#1A1A1C', 'rgba(15,15,16,.9)', '#FF5A6E', '#3A3A3D', '#19191B', '#1E1612')),
 'devica': (T('#F7EFE2', '#FFFFFF', '#E6D9C3', '#2A1A12', '#6E5A48', '#A80D0B', '#A80D0B', '#FFFFFF', '#8A5F10', '#2A1A12', '#D9CBB6', '#F7EFE2', 'rgba(247,239,226,.94)', '#A80D0B', '#D9C4A0'),
            T('#1C1310', '#281C17', '#3D2C24', '#F3E7D7', '#C9B49C', '#C8261E', '#F0645A', '#FFFFFF', '#E9C77A', '#100A08', '#C9B49C', '#1C1310', 'rgba(28,19,16,.92)', '#F0645A', '#4A372D')),
 'gory': (T('#EAF0F8', '#FFFFFF', '#CFDCEC', '#14233B', '#4A5D78', '#2E5E9E', '#2E5E9E', '#FFFFFF', '#5A4FA0', '#14233B', '#C3D0E4', '#EAF0F8', 'rgba(234,240,248,.94)', '#2E5E9E', '#B9CBE3'),
          T('#0D1626', '#16223A', '#26375A', '#E6EEF8', '#A9BAD3', '#4C7FCB', '#8DB4EE', '#FFFFFF', '#B3A8F2', '#070D18', '#A9BAD3', '#0D1626', 'rgba(13,22,38,.92)', '#8DB4EE', '#2C4068')),
 'kino': (T('#F1EFEC', '#FFFFFF', '#DDD9D3', '#111111', '#55524D', '#C8102E', '#C8102E', '#FFFFFF', '#C8102E', '#111111', '#BDBAB4', '#F1EFEC', 'rgba(241,239,236,.94)', '#C8102E', '#CFC9C0'),
          T('#0F0F10', '#1A1A1C', '#2C2C2F', '#F1EFEC', '#A9A6A0', '#E0243C', '#FF5A6E', '#FFFFFF', '#FF5A6E', '#000000', '#A9A6A0', '#1A1A1C', 'rgba(15,15,16,.9)', '#FF5A6E', '#3A3A3D')),
 'igr': (T('#F6EEDF', '#FFFFFF', '#E5D7BD', '#1C2622', '#5E5A4C', '#B5700E', '#8A5A0B', '#FFFFFF', '#8A5A0B', '#1C2622', '#D6C8AE', '#F6EEDF', 'rgba(246,238,223,.94)', '#8A5A0B', '#D8C6A2'),
         T('#1C2622', '#26322D', '#3A4A43', '#F3E7D3', '#C9B99E', '#E39B2D', '#F0B24F', '#1C2622', '#F0B24F', '#111814', '#C9B99E', '#1C2622', 'rgba(28,38,34,.94)', '#F0B24F', '#4D5F57')),
 'mama': (T('#F3F0FA', '#FFFFFF', '#DFD8EE', '#241D38', '#5D5478', '#6A4FB6', '#6A4FB6', '#FFFFFF', '#6A4FB6', '#241D38', '#CFC6E6', '#F3F0FA', 'rgba(243,240,250,.94)', '#6A4FB6', '#CFC4E8'),
          T('#16121F', '#221C30', '#352C4A', '#EFEAF9', '#B9AED6', '#8A6FDA', '#BBA6F5', '#FFFFFF', '#BBA6F5', '#0C0912', '#B9AED6', '#16121F', 'rgba(22,18,31,.92)', '#BBA6F5', '#3F3558')),
 'gorod': (T('#F4EFE3', '#FFFFFF', '#E2D8BF', '#1E1B16', '#5E574A', '#E0A800', '#8A6A00', '#1E1B16', '#8A6A00', '#1E1B16', '#D5CCB6', '#F4EFE3', 'rgba(244,239,227,.94)', '#8A6A00', '#D8CCA8'),
           T('#18160F', '#24211A', '#3A3528', '#F4EFE3', '#C2B9A3', '#E0A800', '#F2C440', '#1E1B16', '#F2C440', '#0E0D09', '#C2B9A3', '#18160F', 'rgba(24,22,15,.92)', '#F2C440', '#4A4433')),
 'novogod': (T('#EEF2FA', '#FFFFFF', '#D3DCEE', '#0E1A33', '#4A587A', '#1E3A72', '#1E3A72', '#FFFFFF', '#8A6A10', '#0E1A33', '#B9C4DB', '#EEF2FA', 'rgba(238,242,250,.94)', '#1E3A72', '#C5D0E6'),
             T('#0E1A33', '#16264A', '#2A3D66', '#F2F5FB', '#B9C4DB', '#E8C66A', '#E8C66A', '#0E1A33', '#E8C66A', '#08101F', '#B9C4DB', '#0E1A33', 'rgba(14,26,51,.94)', '#E8C66A', '#34497A')),
}


def theme_css():
    out = ['/* Сгенерировано: темы страниц (светлая / тёмная) */']
    for k, (lt, dk) in THEMES.items():
        f = FONTS[k]
        fontv = f'--font-display:{f[0]};--title-weight:{f[1]};--title-style:{f[2]};--title-transform:{f[3]};--title-size:{f[4]};'
        out.append(f'.t-{k}{{{fontv}' + ''.join(f'--{a}:{lt[a]};' for a in K) + '}')
        out.append(f'[data-theme=dark] .t-{k}{{' + ''.join(f'--{a}:{dk[a]};' for a in K) + '}')
    return '\n'.join(out) + '\n'


GFONTS = {'brand': 'family=Unbounded:wght@500;700;900', 'devica': 'family=Kurale', 'gory': 'family=Philosopher:ital,wght@0,700;1,700',
          'kino': 'family=Russo+One', 'igr': 'family=Playfair+Display:wght@600;700', 'mama': 'family=Marck+Script',
          'gorod': 'family=Comfortaa:wght@700', 'novogod': 'family=Cormorant+Garamond:ital,wght@1,700'}

SLUG = {'devica': 'devitsa-krasavitsa', 'gory': 'gory-sinie', 'kino': 'takoe-kino', 'igr': 'starye-igrushki-u-kamina',
        'mama': 'lyubimaya-mama', 'gorod': 'gorod-na-levom-beregu', 'novogod': 'novogodniy-perezvon'}
YANDEX = 'https://music.yandex.ru/artist/23980872'
# Треки на Яндекс Музыке для встроенного плеера: ключ песни -> (id трека, id альбома)
YM_TRACKS = {'devica': ('156888013', '44371174'), 'gory': ('147694763', '40435016'), 'mama': ('137569779', '35969202'),
             'kino': ('154880490', '43577120'), 'igr': ('150891993', '41855452'), 'gorod': ('145330437', '39273237'),
             'novogod': ('146001421', '39644502')}
BANDLINK = 'https://band.link/asya_nova'
GAME = 'https://vk.ru/app54835318_-31319842'
VK = 'https://vk.com/asya_nova_sing'
PLAT = [("Яндекс Музыка", YANDEX, "yandex-music.svg"), ("VK Музыка", "https://vk.com/artist/2154594960509680592", "vk-music.png"),
        ("Звук", "https://zvuk.com/artist/213241525", "zvuk.png"), ("KION Музыка", "https://music.mts.ru/artist/23980872", "kion-music.svg"),
        ("Apple Music", "https://music.apple.com/us/artist/%D0%B0%D1%81%D1%8F-nova/1833734286", "apple-music.svg"), ("Spotify", "https://open.spotify.com/artist/5FQZ8GB9Ooa1BPmH74Ajqj", "spotify.svg")]
SOC = [("ВКонтакте", VK, "vk.svg"), ("Telegram", "https://t.me/asya_nova_sing", "telegram.svg"),
       ("TikTok", "https://www.tiktok.com/@asya_nova_song", "tiktok.png"), ("MAX — «АСЯ NOVA на MAXимум!»", "https://max.ru/channel_asya_nova", "max.svg"),
       ("RUTUBE", "https://rutube.ru/channel/39685316", "rutube.png")]
NAV = [('О певице', '/#about', 'about'), ('Музыка', '/#music', 'music'), ('Афиша', '/#afisha', 'afisha'), ('Видео', '/#video', 'video'), ('Комиксы', '/komiks/', 'comics'),
       ('Мерч', '/merch/', 'merch'), ('Сотрудничество', '/#collab', 'collab')]
PLAY = '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M7 4.5v15l13-7.5z"></path></svg>'
def chev(d): return f'<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="{d}"></path></svg>'
LEFT, RIGHT = 'M15 18l-6-6 6-6', 'M9 18l6-6-6-6'


def pl(n, u, f):
    # Значки лежат в /assets/icons/ — замените файл с тем же именем, и значок обновится на всех страницах
    return f'<a class="pl" href="{u}" target="_blank" rel="noopener" aria-label="{n}" title="{n}"><img src="/assets/icons/{f}" alt="{n}" width="34" height="34"></a>'


def header(active):
    nav = ''.join(f'<a href="{h}"{" class=active" if k == active else ""}>{n}</a>' for n, h, k in NAV)
    return f'''<header class="site-header">
  <div class="link-bar"><div class="wrap link-row">
    <div class="link-group"><span class="link-label">Слушать на</span>{"".join(pl(*p) for p in PLAT)}</div>
    <div class="link-group"><span class="link-label">Соцсети</span>{"".join(pl(*s) for s in SOC)}</div>
  </div></div>
  <div class="wrap hdr-row">
    <a class="logo" href="/" aria-label="АСЯ NOVA — на главную"><img class="logo-b" src="{img("logo_red_dark")}" alt="АСЯ NOVA" width="66" height="52"><img class="logo-w" src="{img("logo_red_light")}" alt="АСЯ NOVA" width="66" height="52"></a>
    <nav class="site-nav no-scrollbar" aria-label="Главное меню">{nav}</nav>
    <div class="hdr-actions">
      <button class="theme-btn" type="button" data-theme-toggle aria-label="Сменить тему: светлая или тёмная" title="Светлая / тёмная тема">
        <svg class="i-moon" width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"></path></svg>
        <svg class="i-sun" width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"></circle><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"></path></svg>
      </button>
      <a class="btn btn-accent hdr-cta" href="{BANDLINK}" target="_blank" rel="noopener">Слушать</a>
    </div>
  </div>
</header>'''


def footer():
    return f'''<footer class="site-footer"><div class="wrap foot-row">
  <img src="{img("logo_white")}" alt="АСЯ NOVA" style="height:60px;width:auto">
  <div style="display:flex;gap:10px;flex-wrap:wrap">{"".join(pl(*s) for s in SOC)}</div>
  <span style="font-size:14px;color:var(--bar-muted)">© 2026 АСЯ NOVA · <a href="/pesni-dlya-konkursov/">Песни для конкурсов и минусовки</a> · <a href="{VK}" target="_blank" rel="noopener">Связаться во ВКонтакте</a></span>
</div></footer>'''


def page(path, theme, title, desc, body, og_img='og', head_extra=''):
    url = DOMAIN + path
    doc = f'''<!doctype html>
<html lang="ru" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{DOMAIN}{img(og_img)}">
<link rel="icon" type="image/png" href="/favicon.png">
{head_extra}
<script>(function(){{var t;try{{t=localStorage.getItem('theme')}}catch(e){{}}if(!t&&window.matchMedia)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';document.documentElement.setAttribute('data-theme',t||'light')}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{GFONTS[theme]}&family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/css/site.css?v={ver("assets/css/site.css")}">
<link rel="stylesheet" href="/assets/css/themes.css?v={ver("themes")}">
<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function(m,e,t,r,i,k,a){{
        m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {{if (document.scripts[j].src === r) {{ return; }}}}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    }})(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=114138090', 'ym');

    ym(114138090, 'init', {{ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce:true, trackLinks:true}});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/114138090" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
</head>
<body class="t-{theme}">
{body}
<script>window.SONGS={songs_json()};</script>
<script src="/assets/js/site.js?v={ver("assets/js/site.js")}" defer></script>
</body>
</html>
'''
    d = ROOT + path.strip('/')
    os.makedirs(d, exist_ok=True) if path != '/' else None
    open((d + '/' if path != '/' else ROOT) + 'index.html', 'w', encoding='utf-8').write(doc)


SONGS = [(p['key'], p['title'], p['cover']) for p in SPAGES]


def song_file(k, minus=False):
    f = f'files/{SLUG[k]}{"-minus" if minus else ""}.mp3'
    return '/' + f if os.path.exists(ROOT + f) else None
def songs_json():
    d = {}
    for k, t, c in SONGS:
        d[k] = {'t': t, 'u': f'{DOMAIN}/music/{SLUG[k]}/', 's': f'{DOMAIN}/s/{SLUG[k]}/', 'c': DOMAIN + img(c), 'ci': img(c), 'f': song_file(k), 'm': song_file(k, True), 'n': SLUG[k]}
    return json.dumps(d, ensure_ascii=False)
def song_actions(k, cls='song-acts'):
    dl = f'<button type="button" class="sa" data-dl="{k}">{ICON_DL}Скачать</button>' if song_file(k) else ''
    return (f'<div class="{cls}">{dl}'
            f'<a class="sa" href="/music/{SLUG[k]}/#text">{ICON_TXT}Текст песни</a>'
            f'<button type="button" class="sa" data-dl="{k}" data-kind="minus">{ICON_MINUS}Получить минус</button></div>')
ICON_DL = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M11 3h2v9.6l3.3-3.3 1.4 1.4L12 16.4 6.3 10.7l1.4-1.4 3.3 3.3V3zM5 19h14v2H5z"/></svg>'
ICON_TXT = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M5 4h14v2H5zm0 4h14v2H5zm0 4h10v2H5zm0 4h14v2H5z"/></svg>'
ICON_MINUS = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M12 3v10.6A4 4 0 1 0 14 17V7h4V3h-6z"/></svg>'

def lyrics_html(blocks):
    out = []
    for label, chorus, stanzas in blocks:
        ps = ''.join(f'<p{" class=ch" if chorus else ""}>{s}</p>' for s in stanzas)
        out.append(f'<div>{f"<div class=lab>{label}</div>" if label else ""}{ps}</div>')
    return '\n'.join(out)


def covers_grid(exclude=None):
    return '<div class="grid-covers">' + ''.join(
        f'<a href="/music/{SLUG[k]}/"><img src="{img(c)}" alt="Обложка «{t}»" loading="lazy"><span>{t}</span></a>'
        for k, t, c in SONGS if k != exclude) + '</div>'


def carousel(photos, alt):
    imgs = ''.join(f'<img src="{img(p)}" alt="{alt}" loading="lazy">' for p in photos)
    return f'''<section class="sec" aria-labelledby="ph-h">
  <div class="sec-head"><div><h2 id="ph-h" class="h-display h2">Фото со съёмки</h2><p class="muted" style="margin:8px 0 0;font-weight:600;font-size:15px">Листайте вбок · {len(photos)} фото</p></div>
  <div class="car-arrows" style="display:flex;gap:10px"><button class="car-btn" type="button" data-car="prev" aria-label="Предыдущие фото">{chev(LEFT)}</button><button class="car-btn" type="button" data-car="next" aria-label="Следующие фото">{chev(RIGHT)}</button></div></div>
  <div class="car-track no-scrollbar">{imgs}</div>
</section>'''


ALT = {'devica': 'Ася и Женя в народных костюмах', 'gory': 'Ася в голубом костюме с перьями', 'igr': 'Ася в жёлтом платье со старинными игрушками',
       'mama': 'Ася в сиреневом платье с перьями', 'gorod': 'Ася и Евгений Игнатов с гитарой', 'kino': 'Ася в красном бомбере и клетчатой юбке', 'novogod': ''}


def player_html(k):
    if k in YM_TRACKS:
        t, a = YM_TRACKS[k]
        return (f'<iframe class="ym-player" src="https://music.yandex.ru/iframe/#track/{t}/{a}" title="Плеер Яндекс Музыки" '
                f'loading="lazy" frameborder="0" allow="clipboard-write; autoplay"></iframe>')
    return (f'<a class="listen-main" href="{YANDEX}" target="_blank" rel="noopener"><span class="play">{PLAY}</span><span>'
            f'<b style="display:block;font-size:17px">Слушать песню</b><span class="muted" style="font-size:14px">на Яндекс Музыке</span></span></a>')


SONG_VIDEO = {'devica': 'https://vkvideo.ru/video-31319842_456239296', 'igr': 'https://vkvideo.ru/video-31319842_456239235',
              'gory': 'https://vkvideo.ru/video-31319842_456239122', 'mama': 'https://vkvideo.ru/video-31319842_456239124', 'gorod': 'https://vkvideo.ru/video-31319842_456239120'}
from song_seo import SEO
def about_html(k, p):
    ab = SEO.get(k, {}).get('about')
    if not ab: return ''
    return '<section class="sec song-about" aria-labelledby="ab-' + k + '"><h2 id="ab-' + k + '" class="h-display h2">О песне «' + p['title'] + '»</h2>' + ''.join(f'<p>{x}</p>' for x in ab) + '</section>'
def song_ld(k, p):
    sd = SEO.get(k, {}); url = f'{DOMAIN}/music/{SLUG[k]}/'
    d = {'@context': 'https://schema.org', '@type': 'MusicRecording', 'name': p['title'], 'url': url,
         'image': DOMAIN + img(p['cover']), 'inLanguage': 'ru',
         'byArtist': [{'@type': 'MusicGroup', 'name': 'АСЯ NOVA', 'url': DOMAIN + '/'}] + ([{'@type': 'Person', 'name': a.strip()} for a in p['artist'].split(',')[1:]]),
         'recordingOf': {'@type': 'MusicComposition', 'name': p['title']}}
    if sd.get('date'): d['datePublished'] = sd['date']
    if sd.get('genre'): d['genre'] = sd['genre']
    if sd.get('writer'):
        d['recordingOf']['composer'] = {'@type': 'Person', 'name': sd['writer']}
        d['recordingOf']['lyricist'] = {'@type': 'Person', 'name': sd['writer']}
    try:
        from mutagen.mp3 import MP3
        f = ROOT + f'files/{SLUG[k]}.mp3'
        if os.path.exists(f):
            sec = int(MP3(f).info.length); d['duration'] = f'PT{sec // 60}M{sec % 60}S'
    except Exception: pass
    lyr = '\n\n'.join('\n'.join(ss) for _, _, ss in L[k])
    d['recordingOf']['lyrics'] = {'@type': 'CreativeWork', 'text': lyr}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False).replace('</', '<\\/') + '</script>'
def build_song(p):
    k = p['key']
    creds = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in p['credits'] if '[' not in b)
    eyebrow = p['eyebrow'] if '[' not in p['eyebrow'] else ('Сингл' if k != 'novogod' else 'Новогодняя песня')
    photos = [x for x, _ in p['photos']]
    if k == 'devica':
        more = f'''<a class="tile" href="{SONG_VIDEO['devica']}" target="_blank" rel="noopener" style="background:#A80D0B"><img src="{img("dev_1833")}" alt="" loading="lazy"><div class="shade"></div><div class="pbtn">{PLAY}</div><span class="cap">Смотреть LIVE-видео</span></a>
<a class="tile card" href="/komiks/" style="color:var(--ink);display:flex;gap:20px;align-items:center;padding:22px;border:3px solid var(--ink)"><img src="{img("c_01")}" alt="Обложка комикса" loading="lazy" style="position:static;width:42%;height:auto;flex:none;border-radius:6px;transform:rotate(-3deg);box-shadow:0 10px 24px rgba(0,0,0,.25)"><div><div class="h-display" style="font-size:24px">Читать комикс</div><div class="muted" style="font-size:15px;margin-top:6px">«Девицы-красавицы. Лавка, где продают всё» · 19 страниц</div></div></a>
<a class="tile" href="{GAME}" target="_blank" rel="noopener" style="background:#2A1A12"><img src="{img("h_game-poster")}" alt="" loading="lazy"><div class="shade"></div><div class="cap"><div class="eyebrow" style="color:#E9C77A">Мини-игра во ВКонтакте</div><div style="font-family:Kurale,serif;font-size:30px;font-weight:400;margin-top:6px">Весёлая Ярмарка</div></div></a>'''
    else:
        from PIL import Image as _I
        land = [x for x in photos if (lambda f: f and _I.open(f).width > _I.open(f).height)(next((ROOT + 'assets/img/' + x + e for e in ('.jpg', '.jpeg', '.png', '.webp') if os.path.exists(ROOT + 'assets/img/' + x + e)), None))]
        ph = {'gory': 'gory_8617', 'igr': 'igr_7064'}.get(k) or (land[0] if land else (photos[0] if photos else p['cover']))
        more = f'''<a class="tile song-vtile" href="{SONG_VIDEO.get(k, 'https://vkvideo.ru/@asya_nova_sing/all')}" target="_blank" rel="noopener" style="background:var(--bar)"><img src="{img(ph)}" alt="" loading="lazy" style="opacity:.85"><div class="shade"></div><div class="pbtn">{PLAY}</div><span class="cap">{'Смотреть LIVE-видео' if k in SONG_VIDEO else 'Видео Аси во ВКонтакте'}</span></a>
<a class="tile card" href="/#collab" style="color:var(--ink);display:flex;flex-direction:column;justify-content:flex-end;gap:10px;padding:28px"><div class="eyebrow">Для организаторов</div><div class="h-display" style="font-size:30px">Пригласить Асю спеть эту песню</div><div class="muted" style="font-size:15px">Концерт, праздник, конкурс или эфир</div></a>'''
    body = header('music') + f'''
<main class="wrap">
  <nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span aria-hidden="true">/</span><a href="/#music">Музыка</a><span aria-hidden="true">/</span><span style="color:var(--ink)">{p["title"]}</span></nav>
  <div class="song-cols">
    <div class="song-left">
      <img class="cover" src="{img(p["cover"])}" alt="Обложка «{p["title"]}»">
      <div><div class="eyebrow">{eyebrow}</div><h1 class="h-display song-title">{p["title"]}</h1><div style="font-size:18px;font-weight:700">{p["artist"]}</div></div>
      {song_actions(k, "song-acts song-acts-big")}
      <div class="card listen">
        {player_html(k)}
        <div class="chips">{"".join(f'<a class="chip chip-ic" href="{u}" target="_blank" rel="noopener"><img src="/assets/icons/{f}" alt="" width="26" height="26">{n}</a>' for n, u, f in PLAT)}<a class="chip" href="{BANDLINK}" target="_blank" rel="noopener">Все площадки</a></div>
      </div>
      {f'<dl class="credits">{creds}</dl>' if creds else ''}
    </div>
    <details open class="card lyrics" id="text">
      <summary><span class="h-display" style="font-size:30px;color:var(--accent-text)">Текст песни</span><span style="font-weight:700;font-size:14px;color:var(--label)"><span class="when-open">Свернуть ▲</span><span class="when-closed">Показать ▼</span></span></summary>
      <div class="lyrics-text">{lyrics_html(L[k])}</div>
    </details>
  </div>
  {about_html(k, p)}
  {carousel(photos, ALT[k]) if photos else ''}
  <section class="sec" aria-labelledby="mo-h"><h2 id="mo-h" class="h-display h2" style="margin-bottom:28px">Ещё про эту песню</h2><div class="tiles">{more}</div></section>
  <section class="sec" aria-labelledby="ot-h"><div class="sec-head"><h2 id="ot-h" class="h-display h2">Другие песни</h2><a href="/#music" style="font-weight:800">Вся музыка →</a></div>{covers_grid(k)}</section>
</main>
''' + footer()
    sd = SEO.get(k, {})
    desc = sd.get('desc') or f'«{p["title"]}» — {p["artist"]}. Текст песни, где послушать, ' + ('скачать MP3, ' if song_file(k) else '') + 'минусовка, фото со съёмки.'
    title = sd.get('title') or f'{p["title"]} — {p["artist"]}: текст песни, слушать, минус'
    page(f'/music/{SLUG[k]}/', k, title, desc, body, og_img=p['cover'], head_extra=song_ld(k, p))


def build_home():
    def card(k, t, c, sub):
        return f'<div class="song-card"><a href="/music/{SLUG[k]}/"><img src="{img(c)}" alt="Обложка «{t}»" loading="lazy"><span>{t}</span><span class="muted" style="font-weight:600;font-size:14px;margin-top:-6px">{sub}</span></a>{song_actions(k)}</div>'
    subs = {'devica': 'feat. Евгения Русева · 2026', 'gory': '2026', 'kino': 'Сингл', 'igr': 'в эфире Детского радио', 'mama': 'Сингл', 'gorod': 'feat. Евгений Игнатов', 'novogod': 'Новогодняя'}
    comic_imgs = ''.join(f'<a href="/komiks/"{" style=transform:rotate(-2deg)" if i == 1 else ""}><img src="{img(f"c_{i:02d}")}" alt="{"Обложка комикса" if i == 1 else f"Страница {i} комикса"}" loading="lazy"></a>' for i in (1, 2, 3, 5, 9, 15))
    body = header('') + f'''
<main>
<section class="hero"><div class="wrap hero-row">
  <div class="hero-txt">
    <div style="display:inline-flex;align-self:flex-start;align-items:center;gap:10px;background:#121212;color:#fff;font-weight:700;font-size:13px;letter-spacing:.12em;text-transform:uppercase;padding:9px 16px;border-radius:999px"><span style="width:8px;height:8px;border-radius:50%;background:#FF3E9A;display:inline-block"></span>Новый релиз — «Девица-красавица»</div>
    <h1 style="margin:0"><img src="{img("logo_red_dark")}" alt="АСЯ NOVA" style="display:block;width:clamp(240px,30vw,440px);height:auto"></h1>
    <p style="margin:0;font-size:21px;line-height:1.5;font-weight:600;max-width:470px">Новая звезда, новые песни, новые истории.</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn btn-accent" href="/music/devitsa-krasavitsa/">{PLAY}Слушать новый трек</a><a class="btn btn-line" href="#video">Смотреть видео</a></div>
  </div>
  <div class="hero-photo"><img src="{img("main_1988")}" alt="АСЯ NOVA в красном бомбере, улыбается"></div>
</div>
<div class="marquee" aria-hidden="true"><span>Девица-красавица ✶ уже на всех площадках ✶ Старые игрушки у камина ✶ в эфире Детского радио ✶ Горы синие ✶ Такое кино ✶ Любимая мама ✶ Город на левом берегу ✶ Новогодний перезвон ✶</span></div>
</section>

<section id="about" class="wrap about" aria-labelledby="ab-h">
  <div class="about-top">
    <div class="about-photo"><img src="{img("main_8378")}" alt="АСЯ NOVA в прыжке" loading="lazy"></div>
    <div class="about-intro">
      <div class="eyebrow">О певице</div>
      <h2 id="ab-h" class="h-display h2">Знакомьтесь — АСЯ NOVA</h2>
      <p class="about-lead">АСЯ NOVA (Анастасия Игнатова) — юная певица из Нижегородской области. Её творчество объединяет современную поп-музыку, эмоциональную вокальную подачу и песни-истории о семье, дружбе, взрослении и важных жизненных ценностях.</p>
      <p class="muted" style="margin:0;font-size:17px;line-height:1.6">Занимается в вокальном коллективе «Арт-Студио». Обладательница Гран-при и многочисленных наград всероссийских и международных вокальных конкурсов.</p>
    </div>
  </div>

  <div class="about-stats">
    <div class="stat"><div class="stat-mid">7 песен</div><div class="stat-txt">в формате синглов доступны на крупнейших музыкальных площадках</div></div>
    <div class="stat"><div class="stat-mid">Детское радио</div><div class="stat-txt">песня «Старые игрушки у камина» в ротации крупнейшей детской радиостанции с многомиллионной аудиторией</div></div>
    <div class="stat"><div class="stat-mid">«Ура! Музыка»</div><div class="stat-txt">действующий артист лейбла «Детского радио», совместный релиз «Девица-красавица» уже в сети</div></div>
    <div class="stat"><div class="stat-mid">Гран-при</div><div class="stat-txt">и награды всероссийских и международных вокальных конкурсов</div></div>
    <div class="stat"><div class="stat-mid">Амбассадор</div><div class="stat-txt">брендов: продукция «ОГО!», печатные издания для юных вокалистов «Эксперт Блокнот», амбассадор культуры «Движения Первых»</div></div>
  </div>

  <div class="about-world card">
    <div class="about-world-txt">
      <h3 class="h-display" style="font-size:clamp(24px,2.6vw,34px)">Целый музыкальный мир</h3>
      <p class="muted" style="margin:10px 0 0;font-size:16px;line-height:1.6">Вокруг АСИ NOVA растёт творческая экосистема — это не просто исполнительский проект, а мир, который меняется вместе с артисткой и её аудиторией.</p>
    </div>
    <div class="world-grid">
      <a href="#music"><b>Музыка</b><span>релизы на всех площадках</span></a>
      <a href="#video"><b>Образы</b><span>клипы и фотосессии</span></a>
      <a href="#afisha"><b>Сцена</b><span>концерты и проекты</span></a>
      <a href="/komiks/"><b>Комиксы</b><span>у каждой песни своя история</span></a>
      <a href="/merch/"><b>Мерч</b><span>шопперы, значки и не только</span></a>
      <a href="{GAME}" target="_blank" rel="noopener"><b>Мини-игры</b><span>«Весёлая Ярмарка»</span></a>
    </div>
  </div>

  <div class="about-world about-radio card">
    <div class="about-world-txt">
      <h3 class="h-display" style="font-size:clamp(24px,2.6vw,34px)">АСЯ NOVA: в эфире</h3>
      <p class="muted" style="margin:10px 0 0;font-size:16px;line-height:1.6">Песни АСИ NOVA звучат на детских и семейных радиостанциях — включайте и подпевайте!</p>
    </div>
    <div class="world-grid radio-grid">
{radio_html()}
    </div>
  </div>

</section>

<section class="band-red" aria-labelledby="rel-h"><div class="wrap split">
  <img src="{img("cover_devica")}" alt="Обложка «Девица-красавица»" style="flex:0 1 440px;width:100%;max-width:440px;aspect-ratio:1;object-fit:cover;border-radius:18px;box-shadow:0 30px 60px rgba(0,0,0,.35)">
  <div style="flex:1 1 480px;display:flex;flex-direction:column;gap:22px">
    <div class="eyebrow" style="color:#FFD7D0">Премьера · 30 октября 2026</div>
    <h2 id="rel-h" style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(34px,4.6vw,64px);line-height:1;text-transform:uppercase">Девица-<br>красавица</h2>
    <p style="margin:0;font-size:18px;line-height:1.55;color:#FFE9E5;max-width:560px">АСЯ NOVA и Евгения Русева. Музыка и слова Татьяны Шабрацкой. Лейбл «Ура! Музыка».</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn" style="background:#fff;color:#A80D0B" href="/music/devitsa-krasavitsa/">{PLAY}Слушать и читать текст</a><a class="btn" style="border-color:#fff;color:#fff" href="{BANDLINK}" target="_blank" rel="noopener">Все площадки</a></div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;max-width:560px">
      <a href="/komiks/" style="text-decoration:none;background:#FFF4E6;color:#121212;border-radius:14px;padding:18px 20px"><b style="font-family:Unbounded,sans-serif;font-size:16px;display:block">Читать комикс</b><span style="font-size:14px;color:#5B534B">«Лавка, где продают всё»</span></a>
      <a href="{GAME}" target="_blank" rel="noopener" style="text-decoration:none;background:#FFF4E6;color:#121212;border-radius:14px;padding:18px 20px"><b style="font-family:Unbounded,sans-serif;font-size:16px;display:block">Играть</b><span style="font-size:14px;color:#5B534B">«Весёлая Ярмарка»</span></a>
    </div>
  </div>
</div></section>

<section id="afisha" class="wrap" style="padding-top:96px" aria-labelledby="af-h">
  <div class="sec-head"><h2 id="af-h" class="h-display h2">Афиша</h2></div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px">
    <article class="card event"><div class="date-badge">Скоро</div><div><h3 style="margin:0 0 8px;font-size:19px">Живой концерт на Детском радио</h3><p class="muted" style="margin:0 0 8px">Дату объявим во ВКонтакте и Telegram</p><a href="{VK}" target="_blank" rel="noopener" style="font-weight:800;color:var(--accent-text)">Следить за новостями</a></div></article>
    <article class="card event"><div class="date-badge" style="background:var(--ink);color:var(--bg)">Зовите</div><div><h3 style="margin:0 0 8px;font-size:19px">Концерты, праздники, конкурсы</h3><p class="muted" style="margin:0 0 8px">Ася выступает с сольной программой и в дуэте</p><a href="#collab" style="font-weight:800;color:var(--accent-text)">Пригласить Асю</a></div></article>
  </div>
</section>

<section id="music" class="wrap" style="padding-top:96px" aria-labelledby="mu-h">
  <div class="sec-head"><h2 id="mu-h" class="h-display h2">Музыка</h2><div style="display:flex;gap:22px;flex-wrap:wrap"><a href="/pesni-dlya-konkursov/" style="font-weight:800">Песни для конкурсов и минусовки →</a><a href="{BANDLINK}" target="_blank" rel="noopener" style="font-weight:800">Слушать на всех площадках →</a></div></div>
  <div class="grid-covers">{"".join(card(k, t, c, subs[k]) for k, t, c in SONGS)}</div>
</section>

<section id="video" style="background:#121212;color:#fff;margin-top:96px" aria-labelledby="vi-h"><div class="wrap" style="padding-top:96px;padding-bottom:96px">
  <div class="sec-head"><div><h2 id="vi-h" style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(30px,4vw,52px);text-transform:uppercase">Концертные видео</h2></div><a href="https://vkvideo.ru/@asya_nova_sing/all" target="_blank" rel="noopener" style="font-weight:800;color:#fff">Все видео во ВКонтакте →</a></div>
  <div class="tiles vtiles">
    <a class="tile" href="https://vkvideo.ru/video-31319842_456239296" target="_blank" rel="noopener"><img src="{img("dev_1833")}" alt="" loading="lazy"><div class="shade"></div><div class="pbtn">{PLAY}</div><span class="cap"><span class="eyebrow" style="color:#FFD7D0;display:block">LIVE · Сергиевская ярмарка</span><span style="font-family:Unbounded,sans-serif;font-size:22px">Девица-красавица</span></span></a>
    <a class="tile" href="https://vkvideo.ru/video-31319842_456239235" target="_blank" rel="noopener"><img src="{img("igr_7064")}" alt="" loading="lazy"><div class="shade"></div><div class="pbtn">{PLAY}</div><span class="cap"><span class="eyebrow" style="color:#FFD7D0;display:block">LIVE-клип</span><span style="font-family:Unbounded,sans-serif;font-size:22px">Старые игрушки у камина</span></span></a>
    <a class="tile" href="https://vkvideo.ru/video-31319842_456239122" target="_blank" rel="noopener"><img src="{img("gory_8617")}" alt="" loading="lazy"><div class="shade"></div><div class="pbtn">{PLAY}</div><span class="cap"><span class="eyebrow" style="color:#FFD7D0;display:block">LIVE</span><span style="font-family:Unbounded,sans-serif;font-size:22px">Горы синие</span></span></a>
  </div>
</div></section>

<section id="comics" class="band-cream" aria-labelledby="co-h"><div class="wrap split">
  <div style="flex:1 1 440px;display:flex;flex-direction:column;gap:20px">
    <div class="eyebrow">Комиксы АСИ NOVA</div>
    <h2 id="co-h" style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(30px,4vw,52px);line-height:1.05;text-transform:uppercase">У каждой песни — своя история</h2>
    <p class="muted" style="margin:0;font-size:18px;line-height:1.55;max-width:520px">Первый выпуск: «Девицы-красавицы. Лавка, где продают всё». Ася и Женя против Сороки и купца Златобрюха — а после чтения можно сыграть в «Весёлую Ярмарку».</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn btn-accent" href="/komiks/">Читать комикс</a><a class="btn btn-line" href="{GAME}" target="_blank" rel="noopener">Играть в «Весёлую Ярмарку»</a></div>
  </div>
  <div class="comic-grid" style="flex:1 1 440px">{comic_imgs}</div>
</div></section>


<section id="merch" class="wrap" style="padding-bottom:96px" aria-labelledby="me-h">
  <div class="sec-head"><div><h2 id="me-h" class="h-display h2">Фан-магазин</h2><p class="muted" style="margin:10px 0 0;font-size:18px;font-weight:600">Шопперы и значки с логотипом и образами АСИ NOVA</p></div><a href="/merch/" style="font-weight:800">Весь мерч →</a></div>
  <div class="shop-grid">{"".join(shop_card(MERCH[i], True, "2/3") for i in (0, 1, 2))}{shop_card(MERCH[6], True, "2/3", 1, "/assets/merch/badge-mult-asya.jpg")}</div>
</section>

<section id="collab" style="background:#C8102E;color:#fff" aria-labelledby="cl-h"><div class="wrap split" style="padding-bottom:0;align-items:stretch">
  <div style="flex:1 1 520px;display:flex;flex-direction:column;gap:24px;padding-bottom:88px">
    <h2 id="cl-h" style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(30px,4vw,52px);line-height:1.05;text-transform:uppercase">Пригласить АСЮ NOVA</h2>
    <p style="margin:0;font-size:18px;line-height:1.55;color:#FFE3E6;max-width:540px">Концерты, фестивали, конкурсы, детские и семейные праздники, эфиры, съёмки и коллаборации с брендами.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;max-width:640px">
      <div style="background:rgba(0,0,0,.18);border-radius:14px;padding:18px;font-weight:800">Организаторам</div><div style="background:rgba(0,0,0,.18);border-radius:14px;padding:18px;font-weight:800">СМИ и радио</div><div style="background:rgba(0,0,0,.18);border-radius:14px;padding:18px;font-weight:800">Брендам</div>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn" style="background:#fff;color:#C8102E" href="/brendam/">Брендам: форматы и кейсы</a><a class="btn" style="border-color:#fff;color:#fff" href="{VK}" target="_blank" rel="noopener">Написать во ВКонтакте</a></div>
  </div>
  <div style="flex:1 1 340px;min-height:420px;position:relative;border-radius:24px 24px 0 0;overflow:hidden"><img src="{img("main_8375")}" alt="АСЯ NOVA с микрофоном машет рукой" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 25%"></div>
</div></section>
</main>
''' + footer().replace('class="site-footer"', 'class="site-footer" style="margin-top:0"')
    home_ld = {'@context': 'https://schema.org', '@type': 'MusicGroup', 'name': 'АСЯ NOVA', 'alternateName': ['Ася Нова', 'Asya Nova'], 'url': DOMAIN + '/',
               'image': DOMAIN + img('main_8378'), 'genre': ['Поп', 'Детская музыка'], 'foundingLocation': {'@type': 'Place', 'name': 'Нижегородская область'},
               'description': 'Юная певица из Нижегородской области: песни, тексты, минусовки, концертные видео.',
               'sameAs': [u for _, u, _ in PLAT] + [u for _, u, _ in SOC],
               'track': [{'@type': 'MusicRecording', 'name': t, 'url': f'{DOMAIN}/music/{SLUG[k]}/'} for k, t, c in SONGS]}
    page('/', 'brand', 'АСЯ NOVA — юная певица: песни для детей, тексты, минусовки | Официальный сайт', 'Официальный сайт юной певицы АСИ NOVA (Нижегородская область): песни и тексты, скачать MP3, минусовки для вокальных конкурсов, песни в эфире «Детского радио», концертные видео, мерч и сотрудничество.', body, head_extra='<script type="application/ld+json">' + json.dumps(home_ld, ensure_ascii=False) + '</script>')


def build_comic():
    pages = [img(f'c_{i:02d}') for i in range(1, 20)]
    heroes = [('h_asya', 'Ася', 'В чём ни выйдешь — всё к лицу, если настроение хорошее!', 'Светленькая и всегда на позитиве. Никуда не опаздывает: «Заранее — это прямо сейчас!»', '#0B0B0B'),
              ('h_zhenya', 'Женя', 'Какая странность. Вчера здесь ничего не было.', 'Тёмненькая и рассудительная. Первой замечает, что в лавке что-то нечисто.', '#0B0B0B'),
              ('h_soroka', 'Сорока', 'Блестит — значит, моё! Кар-р!', 'Носит монокль и золотую манишку. Тащит всё, что сверкает, прямиком хозяину.', '#0B0B0B'),
              ('h_zlatobryuh', 'Купец Златобрюх', 'Продай мне свою улыбку, девица!', 'Хозяин лавки «Куплю всё дорого». Скупает смех, песни и улыбки за золото.', '#FFF4E6')]
    hcards = ''.join(f'<article class="card" style="overflow:hidden;display:flex;flex-direction:column"><div style="background:{bg};aspect-ratio:1"><img src="{img(k)}" alt="{n}" loading="lazy" style="width:100%;height:100%;object-fit:contain"></div><div style="padding:20px 22px 24px;display:flex;flex-direction:column;gap:10px"><h3 class="h-display" style="font-size:26px;color:var(--accent-text)">{n}</h3><q style="font-weight:700;line-height:1.45">{q}</q><p class="muted" style="margin:0;font-size:15px;line-height:1.55">{d}</p></div></article>' for k, n, q, d, bg in heroes)
    thumbs = ''.join(f'<button type="button" class="{"on" if i == 0 else ""}" aria-label="Открыть страницу {i + 1}"><img src="{p}" alt="" loading="lazy"></button>' for i, p in enumerate(pages))
    body = header('comics') + f'''
<main class="wrap">
  <nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span aria-hidden="true">/</span><span style="color:var(--ink)">Комиксы</span></nav>
  <section class="split" style="padding-top:32px;padding-bottom:0">
    <a href="#reader" style="flex:0 1 400px;display:block;transform:rotate(-2deg)"><img src="{pages[0]}" alt="Обложка комикса «Девицы-красавицы. Лавка, где продают всё»" style="width:100%;display:block;border-radius:8px;box-shadow:0 3px 0 #B8862B,0 28px 56px -18px rgba(0,0,0,.55)"></a>
    <div style="flex:1 1 460px;display:flex;flex-direction:column;gap:20px">
      <div class="eyebrow">Выпуск 1 · комикс по мотивам песни «Девица-красавица»</div>
      <h1 class="h-display" style="font-size:clamp(38px,4.6vw,64px);color:var(--accent-text)">Девицы-красавицы. Лавка, где продают всё</h1>
      <p style="margin:0;font-size:18px;line-height:1.6;max-width:620px">В день праздника Ася и Женя спешат на поляну, где им выступать. По дороге через лес сорока в монокле срывает бусину с Асиных рябиновых бус. Девочки бегут за воровкой и находят золочёную лавку «Куплю всё дорого», которой вчера здесь не было. Хозяин лавки, купец Златобрюх, готов купить что угодно. Даже улыбку.</p>
      <div class="muted" style="display:flex;flex-wrap:wrap;gap:32px;font-size:15px"><div><b style="display:block;font-size:28px;color:var(--accent-text)">19</b>страниц</div><div><b style="display:block;font-size:28px;color:var(--accent-text)">5 мин</b>на чтение</div><div><b style="display:block;font-size:28px;color:var(--accent-text)">QR</b>на песню в финале</div></div>
      <div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn btn-accent" href="#reader">Читать с первой страницы</a><a class="btn btn-line" href="/music/devitsa-krasavitsa/">Слушать песню</a></div>
    </div>
  </section>
  <section id="reader" class="sec reader" data-reader data-pages='{json.dumps(pages)}' aria-labelledby="rd-h">
    <div class="sec-head" style="align-items:center"><h2 id="rd-h" style="margin:0;font-family:Kurale,serif;font-weight:400;font-size:clamp(28px,3vw,40px)">Читать комикс</h2><div style="font-weight:700;color:#E9C77A">Страница <span data-page-num>1</span> из 19</div></div>
    <div class="reader-stage"><button class="rd-btn" type="button" data-prev aria-label="Предыдущая страница">{chev(LEFT)}</button><img data-page-img src="{pages[0]}" alt="Обложка комикса" width="1000" height="1500"><button class="rd-btn" type="button" data-next aria-label="Следующая страница">{chev(RIGHT)}</button></div>
    <div class="thumbs no-scrollbar">{thumbs}</div>
  </section>
  <section class="sec" aria-labelledby="he-h"><h2 id="he-h" class="h-display h2">Герои</h2><p class="muted" style="margin:8px 0 28px;font-size:17px">Они же — персонажи мини-игры «Весёлая Ярмарка».</p><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:20px">{hcards}</div></section>
  <section class="sec" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px" aria-label="Игра и новые выпуски">
    <a href="{GAME}" target="_blank" rel="noopener" style="text-decoration:none;color:#fff;border-radius:24px;overflow:hidden;display:flex;flex-wrap:wrap;background:#2A1A12"><img src="{img("h_game-poster")}" alt="Постер игры «Весёлая Ярмарка»" loading="lazy" style="flex:1 1 220px;width:100%;aspect-ratio:1;object-fit:cover"><div style="flex:1 1 220px;padding:28px;display:flex;flex-direction:column;justify-content:center;gap:12px"><div class="eyebrow" style="color:#E9C77A">Мини-игра во ВКонтакте</div><div style="font-family:Kurale,serif;font-size:34px;line-height:1.05">Весёлая Ярмарка</div><p style="margin:0;font-size:15px;line-height:1.55;color:#E8DCCB">Играйте за Асю, Женю или Златобрюха. Поделитесь результатом и получите комикс в личные сообщения.</p><span style="align-self:flex-start;background:#E9C77A;color:#2A1A12;font-weight:800;padding:14px 24px;border-radius:999px">Играть</span></div></a>
    <div style="border:3px dashed var(--dashed);border-radius:24px;padding:32px;display:flex;flex-direction:column;justify-content:center;gap:12px;min-height:280px"><div class="eyebrow">Скоро</div><div class="h-display" style="font-size:34px;color:var(--accent-text)">Новый выпуск готовится</div><p class="muted" style="margin:0;font-size:16px;line-height:1.55">У каждой песни будет своя история. Следите за новостями, чтобы прочитать первыми.</p><a href="{VK}" target="_blank" rel="noopener" style="font-weight:800">Узнать первыми во ВКонтакте →</a></div>
  </section>
</main>
''' + footer()
    page('/komiks/', 'devica', 'Комикс «Девицы-красавицы. Лавка, где продают всё» — АСЯ NOVA', 'Читайте онлайн комикс по песне «Девица-красавица»: 19 страниц, герои и мини-игра «Весёлая Ярмарка».', body, og_img='c_01')


from merch_data import ITEMS as MERCH
def vkimg(u, w=640):
    return html.escape(u + f'&cs={w}x0', quote=True)
def shop_card(it, short=False, ratio=None, main=0, photo=None):
    ratio = ratio or ('4/3' if it['cat'] == 'Значки' else '2/3')
    fit = 'contain' if (ratio == '2/3' and it['cat'] == 'Значки' and not photo) else 'cover'
    i1 = photo or vkimg(it['imgs'][main]); i2 = vkimg(it['imgs'][main]) if photo else ('' if main else (vkimg(it['imgs'][1]) if len(it['imgs']) > 1 else ''))
    alt = html.escape(it['title'])
    second = f'<img class="alt" src="{i2}" alt="" loading="lazy" referrerpolicy="no-referrer">' if i2 else ''
    txt = '' if short else f'<p class="muted" style="margin:0;font-size:14px;line-height:1.5">{it["text"]}</p>'
    old = f' <s class="muted" style="font-weight:600;font-size:14px">{it["old"]}</s>' if it.get('old') else ''
    return (f'<article class="product shop-item"><a class="pic" href="{it["href"]}" target="_blank" rel="noopener" style="background:#fff;aspect-ratio:{ratio};--fit:{fit}">'
            f'<img src="{i1}" alt="{alt}" loading="lazy" referrerpolicy="no-referrer">{second}<span class="tag">{it["cat"]}</span></a>'
            f'<div style="padding:16px 18px 18px;display:flex;flex-direction:column;gap:10px;flex:1"><h3 style="margin:0;font-size:17px;line-height:1.3">{alt}</h3>{txt}'
            f'<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:10px"><span style="font-weight:900;font-size:18px">{it["price"]}{old}</span>'
            f'<a class="chip" href="{it["href"]}" target="_blank" rel="noopener" style="background:var(--accent);color:var(--on-accent);border:0">Купить</a></div></div></article>')
WEAR = ['sun9-83.userapi.com/s/v1/ig2/VDGwJglRtwS08DVbzOCqvjryeWqJkq1CFF2nPhLDQQUBfE9Pz41fQIxyjh3O5F3GIY-OHqpO10SaKM2bqQf6fpbp.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,1080x1620,1280x1920,1440x2160,1707x2560&from=bu&u=pbv1L8YqjWW-k22dIy-BTh7ZPct16e9Zlwn_dJtQwms',
 'sun9-39.userapi.com/s/v1/ig2/4sHdIsZpI6i0oqRNM130jt7H4Gm3YgJdbn2zJAxgR1vlrvyPLpNW2YbUKqdywGdW43nMRKRZQRzSbmBsMWzvHpFh.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,1080x1620,1280x1920,1440x2160,1707x2560&from=bu&u=6WXsBzk_jMFY6Xb5ddOtZALoYAVXx6pTl2MvIhAXhf4',
 'sun9-6.userapi.com/s/v1/ig2/D507oqfshyU2Xd4urL_i2Wql0_MtDY531gA5X1W3ABmCk8PN8CJSdnrdZkS0RK_WEqDfKH58EjFOyuuwSKUXuSDl.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,1080x1620,1280x1920,1440x2160,1707x2560&from=bu&u=MkvhaovD5wK2HoUEW_fcv4HKjWGFOcogCkPA2WMBn3I',
 'sun9-45.userapi.com/s/v1/ig2/qxUuAMbCEfJ9rFaZp56B4AAGM21OB40W16oiFcQ1M7oAbRPh7iOLywZ0zLjot_ZKzA1HFj8ID0f9dMgIRHzqAtuR.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,1080x1620,1280x1920,1440x2160,1707x2560&from=bu&u=DLfquxaHiEJceIp7PXgfgfUiaNj08uW4ONSgRVBFGOc',
 'sun9-45.userapi.com/s/v1/ig2/7xQInZwjL9g5hvRZ81GieP4yKyZSRbvL0u5NiQVrTuQ7thzzV9SyKdlX2QXyMfwJJVG-uwqFCmDKICs5kjx8_Rey.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,1080x1620,1280x1920,1440x2160,1707x2560&from=bu&u=x_Yzgupk6chShBgXkfui8QSo0KNf9s0ghGJncSNrZEc',
 'sun9-64.userapi.com/s/v1/ig2/0AuJ7mVclWAKGpUM2uIVzd7fUCUFq44RTC6x3rge6Zt0qH85Lzp3fzRbj0k4HfON4sd7qpj5vJTtRTxN6LvZOSMD.jpg?quality=95&as=32x22,48x32,72x49,108x73,160x108,240x162,360x243,480x324,540x364,640x431,720x485,1080x728,1280x863,1440x971,2560x1726&from=bu&u=vFxhS8sFw_kY3e2KbefnjhDtHq_sqo79cm0mVV91f1g']
def merch_gallery():
    imgs = ''.join(f'<img src="{vkimg("https://" + u, 1080)}" alt="АСЯ NOVA с фирменными значками" loading="lazy" referrerpolicy="no-referrer">' for u in WEAR)
    return f'''<section class="sec" style="margin-top:80px" aria-labelledby="wear-h">
  <div class="sec-head"><div><h2 id="wear-h" class="h-display" style="font-size:clamp(22px,2.6vw,34px)">Носи как АСЯ NOVA</h2><p class="muted" style="margin:8px 0 0;font-weight:600">Фирменные значки — на худи, рюкзаке и даже на плюшевом друге</p></div></div>
  <div class="wear-grid">{imgs}</div>
</section>'''
def build_merch():
    from merch_data import ITEMS, SHOP
    soon = [('Футболка «Девица-красавица»', 'Одежда', 'h_asya'), ('Худи с героями комикса', 'Одежда', 'h_zhenya'), ('Стикерпак «Ярмарка»', 'Мелочи', 'h_soroka'), ('Блокноты Эксперт Блокнот × АСЯ NOVA', 'Блокноты', None)]
    def soonp(n, c, i):
        bg = '#0B0B0B' if i in ('h_asya', 'h_zhenya', 'h_soroka') else 'var(--cream)'
        pic = f'<img src="{img(i)}" alt="" loading="lazy">' if i else '<span class="muted" style="font-weight:700">Фото скоро</span>'
        return f'<article class="product"><div class="pic" style="background:{bg}">{pic}<span class="tag">{c}</span></div><div style="padding:16px 18px 18px;display:flex;flex-direction:column;gap:12px;flex:1"><h3 style="margin:0;font-size:17px;line-height:1.3">{n}</h3><div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="muted" style="font-weight:700;font-size:14px">Скоро в продаже</span><a class="chip" href="{VK}" target="_blank" rel="noopener">Узнать первым</a></div></div></article>'
    cats = []
    for it in ITEMS:
        if it['cat'] not in cats: cats.append(it['cat'])
    sec = lambda t, s, cards: f'<section class="sec" style="margin-top:80px" aria-label="{t}"><div class="sec-head"><div><h2 class="h-display" style="font-size:clamp(22px,2.6vw,34px)">{t}</h2><p class="muted" style="margin:8px 0 0;font-weight:600">{s}</p></div></div><div class="shop-grid">{cards}</div></section>'
    subs = {'Шопперы': 'Фирменный логотип АСИ NOVA на каждый день', 'Значки': 'Металлические значки 44 мм — на рюкзак, сумку или куртку'}
    sections = ''.join(sec(c, subs.get(c, ''), ''.join(shop_card(it) for it in ITEMS if it['cat'] == c)) for c in cats)
    body = header('merch') + f'''
<section style="background:#C8102E;color:#fff"><div class="wrap split" style="padding-bottom:0;align-items:stretch">
  <div style="flex:1 1 520px;display:flex;flex-direction:column;justify-content:center;gap:22px;padding-bottom:72px">
    <div class="eyebrow" style="color:#FFD7DC">Официальный мерч</div>
    <h1 style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(38px,5.4vw,76px);line-height:.98;text-transform:uppercase">Фан-магазин<br>АСИ NOVA</h1>
    <p style="margin:0;font-size:19px;line-height:1.55;color:#FFE3E6;max-width:520px">Шопперы и значки с логотипом и образами АСИ NOVA. Заказ, оплата и доставка — в магазине сообщества ВКонтакте.</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn" style="background:#fff;color:#C8102E" href="#shop">Смотреть товары</a><a class="btn" style="border-color:#fff;color:#fff" href="{SHOP}" target="_blank" rel="noopener">Магазин ВКонтакте</a></div>
  </div>
  <div style="flex:1 1 340px;min-height:440px;position:relative;border-radius:24px 24px 0 0;overflow:hidden"><img src="{img("kino_1991")}" alt="АСЯ NOVA в красном бомбере" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 20%"></div>
</div></section>
<main id="shop" class="wrap" style="padding-top:8px">
{sections}
{merch_gallery()}
  <section class="sec" aria-labelledby="how-h"><h2 id="how-h" class="h-display h2" style="margin-bottom:26px">Как купить</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px">
      <div class="stat"><div style="font-family:Unbounded,sans-serif;font-weight:900;font-size:34px;color:var(--accent-text)">1</div><h3 style="margin:10px 0 6px">Выберите товар</h3><p class="muted" style="margin:0;line-height:1.55">Нажмите «Купить» — откроется карточка товара во ВКонтакте.</p></div>
      <div class="stat"><div style="font-family:Unbounded,sans-serif;font-weight:900;font-size:34px;color:var(--accent-text)">2</div><h3 style="margin:10px 0 6px">Оформите заказ</h3><p class="muted" style="margin:0;line-height:1.55">Добавьте в корзину и выберите доставку — условия указаны в магазине сообщества.</p></div>
      <div class="stat"><div style="font-family:Unbounded,sans-serif;font-weight:900;font-size:34px;color:var(--accent-text)">3</div><h3 style="margin:10px 0 6px">На концертах</h3><p class="muted" style="margin:0;line-height:1.55">Часть мерча можно купить на выступлениях АСИ NOVA.</p></div>
    </div>
  </section>
</main>
''' + footer()
    page('/merch/', 'brand', 'Фан-магазин АСИ NOVA — мерч', 'Официальный мерч АСИ NOVA: одежда, блокноты и сувениры с героями песен и комиксов.', body)


def build_contest():
    from contest_page import META, ORDER, FAQ
    from mutagen.mp3 import MP3
    titles = {k: (t, c) for k, t, c in SONGS}
    def dur(k):
        for f in (ROOT + f'files/{SLUG[k]}.mp3', f'/home/claude/work/tracks/{SLUG[k]}.mp3'):
            if os.path.exists(f):
                sec = int(MP3(f).info.length); return f'{sec // 60}:{sec % 60:02d}'
        return ''
    cards = []
    for k in ORDER:
        t, c = titles[k]; theme, occ, mood, perf = META[k]; d = dur(k)
        dl = f'<button type="button" class="btn btn-accent cbtn" data-dl="{k}">{ICON_DL}Скачать MP3</button>' if song_file(k) else ''
        cards.append(f'''<article class="cs-card">
  <a href="/music/{SLUG[k]}/" class="cs-cover"><img src="{img(c)}" alt="Обложка песни «{t}»" loading="lazy"></a>
  <div class="cs-body">
    <h3 class="cs-title"><a href="/music/{SLUG[k]}/">{t}</a></h3>
    <dl class="cs-meta"><dt>Тема</dt><dd>{theme}</dd><dt>Когда петь</dt><dd>{occ}</dd><dt>Характер</dt><dd>{mood}</dd><dt>Исполнение</dt><dd>{perf}</dd>{f"<dt>Длительность</dt><dd>{d}</dd>" if d else ""}</dl>
    <div class="cs-acts"><a class="btn btn-line cbtn" href="/music/{SLUG[k]}/#text">{ICON_TXT}Текст песни</a><button type="button" class="btn btn-line cbtn" data-dl="{k}" data-kind="minus">{ICON_MINUS}Получить минус</button>{dl}</div>
  </div>
</article>''')
    faq = ''.join(f'<details class="card cs-faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    body = header('music') + f'''
<main class="wrap">
  <nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span aria-hidden="true">/</span><a href="/#music">Музыка</a><span aria-hidden="true">/</span><span style="color:var(--ink)">Песни для конкурсов</span></nav>
  <header class="cs-head">
    <div class="eyebrow">Репертуар · тексты · минусовки</div>
    <h1 class="h-display" style="font-size:clamp(30px,4vw,54px);margin:10px 0 16px">Песни для детских вокальных конкурсов: тексты и минусовки</h1>
    <p class="cs-lead">Авторские эстрадные песни в исполнении юной певицы АСИ NOVA — для детских вокальных конкурсов, утренников и концертов. У каждой песни есть полный текст, оригинал для разучивания (можно скачать MP3) и минусовка по запросу. Песни про маму, Новый год, мечту и родной город, а также патриотическая песня «Старые игрушки у камина» — она основана на судьбе прабабушки певицы, ребёнка войны, и рассказывает о памяти и преодолении. Сейчас песня звучит в эфире «Детского радио».</p>
  </header>
  <section class="cs-list" aria-label="Песни">{"".join(cards)}</section>
  <section class="sec" aria-labelledby="faq-h"><h2 id="faq-h" class="h-display h2" style="margin-bottom:20px">Вопросы о песнях и минусовках</h2>{faq}</section>
</main>
''' + footer()
    ld = [{'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Песни для детских вокальных конкурсов — АСЯ NOVA',
           'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': f'{DOMAIN}/music/{SLUG[k]}/', 'name': titles[k][0]} for i, k in enumerate(ORDER)]},
          {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]}]
    head = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in ld)
    page('/pesni-dlya-konkursov/', 'brand', 'Песни для детских вокальных конкурсов: тексты и минусовки | АСЯ NOVA',
         'Песни для детского вокального конкурса: тексты, минусовки, скачать MP3. Про маму ко Дню матери, новогодние, лирические и эстрадные песни в исполнении АСИ NOVA.', body, head_extra=head)

def build_brands():
    tg_msg = 'Здравствуйте! Хотим обсудить сотрудничество с АСЯ NOVA.'
    import urllib.parse as up
    formats = [('VK-клипы, посты и сторис', 'Интеграции продукта в контент артистки'),
               ('Тематические фотосессии', 'Съёмки с вашей продукцией для постов и рекламы'),
               ('Рубрики и контент-серии', 'Собственная рубрика под бренд, которая живёт дольше одной кампании'),
               ('Амбассадорство', 'Ася — лицо бренда на длительный срок'),
               ('Выступления и мероприятия', 'Концерты, праздники, презентации и фестивали'),
               ('Творческий мир артистки', 'Комиксы, мини-игра «Весёлая Ярмарка» во ВКонтакте, тематический мерч')]
    fcards = ''.join(f'<div class="br-f"><div class="br-n">{i + 1:02d}</div><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(formats))
    body = header('collab') + f'''
<section style="background:#C8102E;color:#fff"><div class="wrap split" style="padding-bottom:0;align-items:stretch">
  <div style="flex:1 1 520px;display:flex;flex-direction:column;justify-content:center;gap:22px;padding-bottom:72px">
    <div class="eyebrow" style="color:#FFD7DC">Брендам и партнёрам</div>
    <h1 style="margin:0;font-family:Unbounded,sans-serif;font-weight:900;font-size:clamp(28px,3.8vw,54px);line-height:1.02;text-transform:uppercase;overflow-wrap:anywhere">Сотрудничество<br>с АСЕЙ NOVA</h1>
    <p style="margin:0;font-size:19px;line-height:1.55;color:#FFE3E6;max-width:540px">Интеграции, амбассадорство, контент-серии и выступления. Для каждого бренда — своя идея, а не шаблонный пакет.</p>
    <div><a class="btn" style="background:#fff;color:#C8102E" href="#contacts">Обсудить проект</a></div>
  </div>
  <div style="flex:1 1 340px;min-height:440px;position:relative;border-radius:24px 24px 0 0;overflow:hidden"><img src="{img("main_8375")}" alt="АСЯ NOVA" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 25%"></div>
</div></section>
<main class="wrap">
  <section class="sec br-about" aria-labelledby="br-a">
    <h2 id="br-a" class="h-display h2">Об артистке</h2>
    <p>АСЯ NOVA (Анастасия Игнатова) — юная певица из Нижегородской области, артистка лейбла «Ура! Музыка». Она исполняет современную поп-музыку, а её песни — это истории о семье, дружбе, взрослении и важных жизненных ценностях. Песни АСИ NOVA звучат в эфире крупнейших радиостанций России.</p>
    <p>Аудитория артистки — дети, подростки и их родители. Это семейная аудитория, которая доверяет тому, что рекомендует любимая артистка.</p>
  </section>
  <section class="sec" aria-labelledby="br-o">
    <h2 id="br-o" class="h-display h2">Что мы предлагаем</h2>
    <p class="br-lead">Менеджмент АСИ NOVA разрабатывает индивидуальные предложения для брендов. Мы делаем как разовые рекламные интеграции, так и полноценные проекты, которые живут дольше одной кампании: становятся отдельным инфоповодом и постоянно дают новый контент.</p>
    <div class="br-grid">{fcards}</div>
  </section>
  <section class="sec" aria-labelledby="br-c">
    <div class="br-case card">
      <div class="eyebrow">Кейс</div>
      <h2 id="br-c" class="h-display" style="font-size:clamp(24px,3vw,38px);margin:8px 0 14px">Рубрика #ОГО!Советы от&nbsp;АСИ&nbsp;NOVA</h2>
      <p>Для продвижения продукции бренда «ОГО!» мы придумали отдельную рубрику #ОГО!Советы от АСИ NOVA. Ася делится в ней полезными советами, а продукция бренда естественно встроена в каждый выпуск.</p>
      <p>В рамках рубрики записана серия VK-клипов и проведена фотосессия с продукцией для серии постов. Так продукция бренда получила не разовое упоминание, а постоянное присутствие в контенте артистки. Рубрику можно продолжать и развивать.</p>
    </div>
  </section>
  <section class="sec" aria-labelledby="br-h">
    <h2 id="br-h" class="h-display h2">Как мы работаем</h2>
    <ol class="br-steps"><li><b>Знакомимся с задачей</b><span>Продукт, аудитория, цели кампании.</span></li><li><b>Предлагаем идею</b><span>Разрабатываем формат под ваш бренд — без шаблонных пакетов.</span></li><li><b>Согласовываем и делаем</b><span>Формат, сроки и объём контента — и запускаем.</span></li></ol>
  </section>
  <section id="contacts" class="sec br-contacts card" aria-labelledby="br-k">
    <h2 id="br-k" class="h-display" style="font-size:clamp(24px,3vw,38px);margin:0 0 10px">Будем рады обсудить, что можем сделать вместе с вашим брендом</h2>
    <p class="muted" style="margin:0 0 20px">Напишите менеджменту АСИ NOVA удобным способом.</p>
    <div class="br-btns">
      <a class="m-btn" href="https://max.ru/u/f9LHodD0cOJ5S2-14DDen5gNBaiiB9LqZckwguthnryLwvFU8zgnq4HaRXQ" target="_blank" rel="noopener"><img src="/assets/icons/max.svg" alt="">Написать в MAX</a>
      <a class="m-btn" href="https://t.me/diezelman?text={up.quote(tg_msg)}" target="_blank" rel="noopener"><img src="/assets/icons/telegram.svg" alt="">Написать в Telegram</a>
      <a class="m-btn" href="https://vk.me/club31319842" target="_blank" rel="noopener"><img src="/assets/icons/vk.svg" alt="">Написать ВКонтакте</a>
    </div>
    <p class="br-all">Телефон: <a href="tel:+79534151286">+7 953 415-12-86</a> · Все площадки артистки: <a href="{BANDLINK}" target="_blank" rel="noopener">band.link/asya_nova</a> · <a href="/">asyanova.ru</a></p>
  </section>
</main>
''' + footer()
    page('/brendam/', 'brand', 'Сотрудничество с АСЕЙ NOVA — брендам: интеграции, амбассадорство, реклама с юной певицей',
         'Сотрудничество с юной певицей АСЯ NOVA, артисткой лейбла «Ура! Музыка»: интеграции в VK-клипы, фотосессии с продукцией, контент-серии, амбассадорство бренда, выступления. Семейная аудитория.', body)

def build_share():
    for k, t, c in SONGS:
        slug = SLUG[k]; dest = f'/music/{slug}/'
        title = f'Мне нравится песня АСЯ NOVA «{t}» — слушай и ты!'
        desc = f'«{t}» — АСЯ NOVA. Слушай, читай текст и скачивай песню на официальном сайте.'
        doc = f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{DOMAIN}{dest}">
<meta property="og:type" content="music.song"><meta property="og:site_name" content="АСЯ NOVA">
<meta property="og:url" content="{DOMAIN}/s/{slug}/">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{DOMAIN}{img(c)}"><meta property="og:image:width" content="800"><meta property="og:image:height" content="800">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{DOMAIN}{img(c)}">
<link rel="image_src" href="{DOMAIN}{img(c)}">
<meta http-equiv="refresh" content="0;url={dest}">
<script>location.replace("{dest}")</script>
</head><body><a href="{dest}">{html.escape(t)} — АСЯ NOVA</a></body></html>'''
        os.makedirs(ROOT + f's/{slug}', exist_ok=True)
        open(ROOT + f's/{slug}/index.html', 'w', encoding='utf-8').write(doc)

def build_misc():
    open(ROOT + 'assets/css/themes.css', 'w').write(theme_css())
    body = header('') + f'<main class="wrap" style="padding:120px 32px;text-align:center"><h1 class="h-display" style="font-size:clamp(40px,6vw,80px)">Страница не найдена</h1><p class="muted" style="font-size:18px">Возможно, ссылка устарела.</p><a class="btn btn-accent" href="/">На главную</a></main>' + footer()
    page('/404/', 'brand', 'Страница не найдена — АСЯ NOVA', 'Страница не найдена', body)
    os.replace(ROOT + '404/index.html', ROOT + '404.html'); os.rmdir(ROOT + '404')
    urls = ['/', '/brendam/', '/pesni-dlya-konkursov/', '/komiks/', '/merch/'] + [f'/music/{s}/' for s in SLUG.values()]
    open(ROOT + 'sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{DOMAIN}{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    open(ROOT + 'robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n')
    open(ROOT + 'README.md', 'w').write('''# АСЯ NOVA — официальный сайт

Статичный сайт (HTML/CSS/JS без сборки). Точка входа — `index.html`.
Домены: https://asyanova.ru (основной), https://асянова.рф.

## Timeweb Cloud → Приложения → Frontend → HTML
- Команда сборки: не нужна (оставить пустой)
- Директория сайта: корень репозитория (`/`)
- Автодеплой: включить

## Устройство
- `index.html` — главная; `music/<песня>/` — страницы песен; `komiks/` — читалка комикса; `merch/` — фан-магазин.
- `assets/css/site.css` — общий стиль; `assets/css/themes.css` — цвета страниц в светлой и тёмной теме.
- `assets/js/site.js` — переключатель темы, карусели фото, читалка комикса.
- Тема по умолчанию следует настройке устройства; выбор посетителя запоминается.
''')


if __name__ == '__main__':
    build_misc(); build_home(); build_comic(); build_merch(); build_share(); build_contest(); build_brands()
    for p in SPAGES:
        build_song(p)
    print('ok')
