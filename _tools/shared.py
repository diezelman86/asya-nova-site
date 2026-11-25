# Shared pieces for АСЯ NOVA site artboards
A = {}
for line in open('/home/claude/scripts/assets_new.txt', encoding='utf-8'):
    n, i, _ = line.split()
    A[n] = '/_blob/' + i
A.update({
    'logo_white': '/_blob/bc4c3a79193e142249e51ed6b232e09d',
    'logo_black': '/_blob/014f49fd2c43313e5590141409c8defd',
    'main_1988': '/_blob/cec732bcf465feb217b27bf8a3aed22c',
    'main_8375': '/_blob/2b97ffdc42c5ca7f0dcc7e5f1ff90bf8',
    'main_8378': '/_blob/596ae266c5f4fbdd184748cbfa06de50',
    'dev_1833': '/_blob/bd9357d7a4e7d67c2e71ce755422cef3',
    'dev_1779': '/_blob/5c34e22871f7cf325e3722f50ecc39f3',
    'dev_1826': '/_blob/b1098cd978396d13de6dd275e23d0bc5',
    'cover_devica': '/_blob/178e50bc77c4f9cc68a8bd219d1dbcfd',
    'cover_gorod': '/_blob/1e65ac5303c32f13ca1b875fdeaadd2d',
    'cover_gory': '/_blob/bb90542533ba008199efb92f1a07f789',
    'cover_igrushki': '/_blob/b7c4be6778d738c308bf4599be01acd8',
    'cover_kino': '/_blob/4d71169086490f0bac50579d8f5d78b5',
    'cover_mama': '/_blob/36ea295dd61b274c089b89603d7d34a7',
    'cover_novogodniy': '/_blob/948d1efd39ce854f67c7357352ca78f1',
})

SONGS = [  # file, title, cover, sub
    ('Song-Devica.dc.html', 'Девица-красавица', 'cover_devica'),
    ('Song-Gory.dc.html', 'Горы синие', 'cover_gory'),
    ('Song-Kino.dc.html', 'Такое кино', 'cover_kino'),
    ('Song-Igrushki.dc.html', 'Старые игрушки у камина', 'cover_igrushki'),
    ('Song-Mama.dc.html', 'Любимая мама', 'cover_mama'),
    ('Song-Gorod.dc.html', 'Город на левом берегу', 'cover_gorod'),
    ('Song-Novogodniy.dc.html', 'Новогодний перезвон', 'cover_novogodniy'),
]

NAV = [('Музыка', 'Main.dc.html#music', 'music'), ('Афиша', 'Main.dc.html#afisha', 'afisha'),
       ('Видео', 'Main.dc.html#video', 'video'), ('Комиксы', 'Comic.dc.html', 'comics'),
       ('Мерч', 'Merch.dc.html', 'merch'), ('Об Асе', 'Main.dc.html#about', 'about'),
       ('Сотрудничество', 'Main.dc.html#collab', 'collab')]

PLAT = [("Яндекс Музыка", "https://music.yandex.ru/artist/23980872", "Я", "#FFCC00", "#121212"),
        ("VK Музыка", "https://band.link/asya_nova", "VK", "#0077FF", "#FFFFFF"),
        ("Звук", "https://band.link/asya_nova", "Зв", "#FFFFFF", "#121212")]
SOC = [("ВКонтакте", "https://vk.com/asya_nova_sing", "VK", "#0077FF", "#FFFFFF"),
       ("Telegram", "https://t.me/asya_nova_sing", "TG", "#2AABEE", "#121212"),
       ("TikTok", "https://www.tiktok.com/@asya_nova_song", "TT", "#FFFFFF", "#121212"),
       ("MAX — «АСЯ NOVA на MAXимум!»", "https://max.ru/channel_asya_nova", "MAX", "#7A3CFF", "#FFFFFF")]


ICONS = {"Яндекс Музыка": "/_blob/31d7cf8989bdf2a2869fb47c401aea99", "VK Музыка": "/_blob/56db9c4e1b52e5bff2b698289937b6db",
         "Звук": "/_blob/2cd3894d9555ca56652489bdd2a0e9be", "ВКонтакте": "/_blob/aacd11cba769afdf931b8904361a0e06",
         "Telegram": "/_blob/7c61cfb041e1d7835847b2811b6c79f5", "TikTok": "/_blob/9ab3be9c94fed73fdef4ed8bfcb58bb5",
         "MAX — «АСЯ NOVA на MAXимум!»": "/_blob/195d635b937da2ed838d5fc101e59213"}


def icon(n, u, t, bg, fg):
    return (f'<a href="{u}" aria-label="{n}" title="{n}" style="flex: none; width: 34px; height: 34px; border-radius: 50%; '
            f'display: inline-flex; overflow: hidden; text-decoration: none">'
            f'<img src="{ICONS[n]}" alt="Значок: {n}" style="width: 34px; height: 34px; display: block"></a>')


def link_bar(bg, muted):
    lab = f'style="font-size: 12px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: {muted}; white-space: nowrap"'
    return f'''    <div class="link-bar" style="background: {bg}; color: #FFFFFF">
      <div class="link-row" style="max-width: 1320px; margin: 0 auto; padding: 8px 32px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px 24px">
        <div class="link-group" style="display: flex; align-items: center; gap: 8px">
          <span class="link-label" {lab}>Слушать на</span>
          {"".join(icon(*p) for p in PLAT)}
        </div>
        <div class="link-group" style="display: flex; align-items: center; gap: 8px">
          <span class="link-label" {lab}>Соцсети</span>
          {"".join(icon(*s) for s in SOC)}
        </div>
      </div>
    </div>
'''


def header(t, active, cta_href, cta_label='Слушать'):
    links = []
    for label, href, key in NAV:
        if key == active:
            links.append(f'<a href="{href}" style="text-decoration: none; padding: 10px 0; color: {t["accent_text"]}; border-bottom: 2px solid {t["accent_text"]}">{label}</a>')
        else:
            links.append(f'<a href="{href}" style="text-decoration: none; padding: 10px 0; color: {t["ink"]}">{label}</a>')
    logo = '/_blob/8c65532d014893f274ff7f7b4e0f0f5c' if t.get('dark') else '/_blob/7288b9423a060db877052d49c0212ff3'
    return f'''  <header style="position: sticky; top: 0; z-index: 20; background: {t["header_bg"]}; border-bottom: 1px solid {t["border"]}">
{link_bar(t["bar"], t["bar_muted"])}    <div class="hdr-row" style="max-width: 1320px; margin: 0 auto; padding: 14px 32px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 16px">
      <a href="Main.dc.html" aria-label="АСЯ NOVA — на главную" style="display: flex; align-items: center"><img src="{logo}" alt="АСЯ NOVA" style="height: 52px; width: auto; display: block"></a>
      <nav class="site-nav" aria-label="Главное меню" style="display: flex; flex-wrap: wrap; gap: 4px 24px; font-weight: 700; font-size: 15px; letter-spacing: 0.02em">
        {chr(10).join("        " + l for l in links).strip()}
      </nav>
      <a href="{cta_href}" style="text-decoration: none; background: {t["accent"]}; color: {t["on_accent"]}; font-weight: 800; font-size: 14px; padding: 13px 22px; border-radius: 999px">{cta_label}</a>
    </div>
  </header>
'''


BASE_CSS = '''body{margin:0;background:BGCOLOR}
a{color:INK}a:hover{color:ACCENTTEXT}
*{box-sizing:border-box}
summary{list-style:none;cursor:pointer}
summary::-webkit-details-marker{display:none}
.link-row::-webkit-scrollbar,.site-nav::-webkit-scrollbar,.car-track::-webkit-scrollbar,.thumbs::-webkit-scrollbar{display:none}
.car-track{scrollbar-width:none}
@media (min-width: 1000px){.song-left{position:sticky;top:156px}}
@media (max-width: 760px){
.link-row{flex-wrap:nowrap !important;overflow-x:auto;padding:8px 18px !important;gap:16px !important;justify-content:flex-start !important;scrollbar-width:none}
.link-label{display:none}
.hdr-row{padding:10px 18px !important}
.hdr-row img{height:40px !important}
.site-nav{order:3;width:100%;flex-wrap:nowrap !important;overflow-x:auto;gap:22px !important;padding-bottom:2px;scrollbar-width:none}
.site-nav a{white-space:nowrap}
.page-main{padding:18px 18px 0 !important}
.song-cols{gap:32px !important;margin-top:18px !important}
.lyrics{padding:22px 20px 28px !important}
.lyrics-text{font-size:18px !important}
.car-track img{height:340px !important}
.car-arrows{display:none !important}
.more-sec,.photo-sec,.other-sec,.sec{margin-top:64px !important}
.other-grid{grid-template-columns:repeat(2,minmax(0,1fr)) !important}
.mini-player{padding:10px 18px !important;gap:10px 14px !important}
}
'''


def css(t):
    return BASE_CSS.replace('BGCOLOR', t['bg']).replace('INK', t['ink']).replace('ACCENTTEXT', t['accent_text'])


def page(title, fonts_q, t, body, preview_h, script_extra='', props_extra=''):
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts_q}&amp;family=Manrope:wght@400;500;600;700;800&amp;display=swap">
<style>
{css(t)}</style>
</helmet>
<div style="font-family: Manrope, system-ui, sans-serif; color: {t["ink"]}; background: {t["bg"]}; width: 100%; min-height: 100vh; position: relative">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{preview_h}}}{props_extra}}}'>
class Component extends DCLogic {{
{script_extra}
}}
</script>
</body>
</html>
'''


CAROUSEL_JS = '''  scrollCar(e, d) {
    const sec = e && e.currentTarget ? e.currentTarget.closest('section') : null;
    const track = sec ? sec.querySelector('.car-track') : null;
    if (!track) return;
    track.scrollBy({ left: d * Math.max(280, track.clientWidth * 0.8), behavior: 'smooth' });
  }'''


def carousel(t, photos, heading='Фото со съёмки'):
    imgs = '\n'.join(
        f'        <img src="{A[p]}" alt="{alt}" style="height: 480px; width: auto; flex: none; border-radius: 16px; scroll-snap-align: start; display: block">'
        for p, alt in photos)
    arrow = lambda lbl, h, path: (f'<button type="button" aria-label="{lbl}" onClick="{{{{ {h} }}}}" style="width: 48px; height: 48px; border-radius: 50%; '
                                  f'border: 1.5px solid {t["ink"]}; background: transparent; color: {t["ink"]}; display: flex; align-items: center; justify-content: center; cursor: pointer">'
                                  f'<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"></path></svg></button>')
    return f'''    <section class="photo-sec" aria-labelledby="ph-h" style="margin-top: 104px">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 16px; margin-bottom: 24px">
        <div>
          <h2 id="ph-h" style="margin: 0; {t["h2_style"]}">{heading}</h2>
          <p style="margin: 8px 0 0; font-size: 15px; color: {t["muted"]}; font-weight: 600">Листайте вбок · {len(photos)} фото</p>
        </div>
        <div class="car-arrows" style="display: flex; gap: 10px">
          {arrow("Предыдущие фото", "prev", "M15 18l-6-6 6-6")}
          {arrow("Следующие фото", "next", "M9 18l6-6-6-6")}
        </div>
      </div>
      <div class="car-track" style="display: flex; gap: 14px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 6px">
{imgs}
      </div>
    </section>
'''


def mini_player(t, cover, title, artist):
    return f'''  <div style="position: sticky; bottom: 0; z-index: 30; background: {t["bar"]}; color: #FFFFFF; border-top: 3px solid {t["accent"]}">
    <div class="mini-player" style="max-width: 1320px; margin: 0 auto; padding: 12px 32px; display: flex; flex-wrap: wrap; align-items: center; gap: 16px 20px">
      <img src="{A[cover]}" alt="" style="width: 52px; height: 52px; border-radius: 8px; object-fit: cover">
      <div style="display: flex; flex-direction: column; gap: 2px; min-width: 180px">
        <span style="font-weight: 800; font-size: 15px">{title}</span>
        <span style="font-size: 13px; color: {t["bar_muted"]}">{artist}</span>
      </div>
      <button type="button" aria-label="Слушать" style="width: 48px; height: 48px; border-radius: 50%; border: 0; background: {t["accent"]}; color: {t["on_accent"]}; display: flex; align-items: center; justify-content: center; cursor: pointer"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M7 4.5v15l13-7.5z"></path></svg></button>
      <div style="flex: 1 1 240px; display: flex; align-items: center; gap: 12px; font-size: 13px; color: {t["bar_muted"]}">
        <span>[0:00]</span>
        <div style="flex: 1; height: 4px; border-radius: 2px; background: rgba(255,255,255,0.18)"><div style="width: 28%; height: 4px; border-radius: 2px; background: #FFFFFF"></div></div>
        <span>[0:00]</span>
      </div>
    </div>
  </div>
'''


def footer_min(t):
    return f'''  <footer style="background: {t["bar"]}; color: #FFFFFF">
    <div style="max-width: 1320px; margin: 0 auto; padding: 40px 32px; display: flex; flex-wrap: wrap; gap: 24px; justify-content: space-between; align-items: center">
      <img src="{A["logo_white"]}" alt="АСЯ NOVA" style="height: 60px; width: auto">
      <div style="display: flex; gap: 10px">{"".join(icon(*s) for s in SOC)}</div>
      <span style="font-size: 14px; color: {t["bar_muted"]}">© 2026 АСЯ NOVA</span>
    </div>
  </footer>
'''
