import sys, json
sys.path.insert(0, '/home/claude/scripts')
from shared import *
from songs import THEMES

OUT = '/home/claude/work/canvas/project/'
H = json.load(open('/home/claude/scripts/heights2.json')) if len(sys.argv) > 1 else {}

# ---------------- COMIC ----------------
t = THEMES['devica']
pages = [A[f'c_{i:02d}'] for i in range(1, 20)]
heroes = [
    ('h_asya', 'Ася', 'В чём ни выйдешь — всё к лицу, если настроение хорошее!', 'Светленькая и всегда на позитиве. Никуда не опаздывает: «Заранее — это прямо сейчас!»', '#0B0B0B'),
    ('h_zhenya', 'Женя', 'Какая странность. Вчера здесь ничего не было.', 'Тёмненькая и рассудительная. Первой замечает, что в лавке что-то нечисто.', '#0B0B0B'),
    ('h_soroka', 'Сорока', 'Блестит — значит, моё! Кар-р!', 'Носит монокль и золотую манишку. Тащит всё, что сверкает, прямиком хозяину.', '#0B0B0B'),
    ('h_zlatobryuh', 'Купец Златобрюх', 'Продай мне свою улыбку, девица!', 'Хозяин лавки «Куплю всё дорого». Скупает смех, песни и улыбки за золото.', '#FFFFFF'),
]
hero_cards = '\n'.join(f'''        <article style="background: {t["surface"]}; border: 1px solid {t["border"]}; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column">
          <div style="background: {bg}; aspect-ratio: 1; display: flex; align-items: center; justify-content: center; overflow: hidden"><img src="{A[k]}" alt="{n}" style="width: 100%; height: 100%; object-fit: contain"></div>
          <div style="padding: 20px 22px 24px; display: flex; flex-direction: column; gap: 10px">
            <h3 style="margin: 0; font-family: Kurale, Georgia, serif; font-weight: 400; font-size: 26px; color: {t["accent"]}">{n}</h3>
            <q style="font-weight: 700; font-size: 16px; line-height: 1.45">{q}</q>
            <p style="margin: 0; font-size: 15px; line-height: 1.55; color: {t["muted"]}">{d}</p>
          </div>
        </article>''' for k, n, q, d, bg in heroes)

arrow_btn = lambda lbl, h, path: (f'<button type="button" aria-label="{lbl}" onClick="{{{{ {h} }}}}" style="flex: none; width: 56px; height: 56px; border-radius: 50%; border: 0; '
                                  f'background: {t["accent"]}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; cursor: pointer">'
                                  f'<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="{path}"></path></svg></button>')

comic_body = header(t, 'comics', '#reader', 'Читать') + f'''
  <main class="page-main" style="max-width: 1320px; margin: 0 auto; padding: 28px 32px 0">
    <nav aria-label="Хлебные крошки" style="font-size: 14px; font-weight: 600; color: {t["muted"]}; display: flex; gap: 8px; flex-wrap: wrap">
      <a href="Main.dc.html" style="color: {t["muted"]}">Главная</a><span aria-hidden="true">/</span><span style="color: {t["ink"]}">Комиксы</span>
    </nav>

    <section class="song-cols" style="display: flex; flex-wrap: wrap; gap: 64px; align-items: center; margin-top: 32px">
      <a href="#reader" style="flex: 0 1 400px; display: block; transform: rotate(-2deg)"><img src="{pages[0]}" alt="Обложка комикса «Девицы-красавицы. Лавка, где продают всё»" style="width: 100%; display: block; border-radius: 8px; box-shadow: 0 3px 0 #B8862B, 0 28px 56px -18px rgba(42,23,20,0.55)"></a>
      <div style="flex: 1 1 480px; display: flex; flex-direction: column; gap: 20px">
        <div style="font-weight: 800; font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: {t["label"]}">Выпуск 1 · комикс по мотивам песни «Девица-красавица»</div>
        <h1 style="margin: 0; font-family: Kurale, Georgia, serif; font-weight: 400; font-size: clamp(40px, 4.6vw, 64px); line-height: 1.05; color: {t["accent"]}">Девицы-красавицы. Лавка, где продают всё</h1>
        <p style="margin: 0; font-size: 18px; line-height: 1.6; max-width: 620px">В день праздника Ася и Женя спешат на поляну, где им выступать. По дороге через лес сорока в монокле срывает бусину с Асиных рябиновых бус. Девочки бегут за воровкой и находят золочёную лавку «Куплю всё дорого», которой вчера здесь не было. Хозяин лавки, купец Златобрюх, готов купить что угодно. Даже улыбку.</p>
        <div style="display: flex; flex-wrap: wrap; gap: 32px; font-size: 15px; color: {t["muted"]}">
          <div><b style="display: block; font-size: 28px; color: {t["accent"]}">19</b>страниц</div>
          <div><b style="display: block; font-size: 28px; color: {t["accent"]}">5 мин</b>на чтение</div>
          <div><b style="display: block; font-size: 28px; color: {t["accent"]}">QR</b>на песню в финале</div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 12px">
          <a href="#reader" style="text-decoration: none; background: {t["accent"]}; color: #FFFFFF; font-weight: 800; font-size: 16px; padding: 18px 30px; border-radius: 999px">Читать с первой страницы</a>
          <a href="Song-Devica.dc.html" style="text-decoration: none; color: {t["ink"]}; font-weight: 800; font-size: 16px; padding: 16px 28px; border-radius: 999px; border: 2px solid {t["ink"]}">Слушать песню</a>
        </div>
      </div>
    </section>

    <!-- ЧИТАЛКА -->
    <section id="reader" class="sec" aria-labelledby="rd-h" style="margin-top: 104px; background: {t["bar"]}; color: #FFFFFF; border-radius: 28px; padding: 36px 32px 32px">
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 24px">
        <h2 id="rd-h" style="margin: 0; font-family: Kurale, Georgia, serif; font-weight: 400; font-size: clamp(28px, 3vw, 40px)">Читать комикс</h2>
        <div style="font-weight: 700; font-size: 16px; color: #E9C77A">Страница {{{{ pageNum }}}} из 19</div>
      </div>
      <div style="display: flex; align-items: center; justify-content: center; gap: 20px">
        {arrow_btn("Предыдущая страница", "prev", "M15 18l-6-6 6-6")}
        <img src="{{{{ pageSrc }}}}" alt="{{{{ pageAlt }}}}" style="flex: 0 1 auto; width: min(100%, 640px); height: auto; aspect-ratio: 2 / 3; object-fit: contain; border-radius: 8px; background: #F7EFE2; box-shadow: 0 20px 50px rgba(0,0,0,0.45); display: block">
        {arrow_btn("Следующая страница", "next", "M9 18l6-6-6-6")}
      </div>
      <div class="thumbs" style="display: flex; gap: 10px; overflow-x: auto; margin-top: 28px; padding: 4px 2px 8px; scrollbar-width: none">
        <sc-for list="{{{{ thumbs }}}}" as="th" hint-placeholder-count="19">
          <button type="button" aria-label="{{{{ th.label }}}}" onClick="{{{{ th.pick }}}}" style="{{{{ th.style }}}}"><img src="{{{{ th.src }}}}" alt="" style="width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 4px"></button>
        </sc-for>
      </div>
    </section>

    <!-- ГЕРОИ -->
    <section class="sec" aria-labelledby="he-h" style="margin-top: 104px">
      <h2 id="he-h" style="margin: 0 0 8px; {t["h2_style"]}">Герои</h2>
      <p style="margin: 0 0 28px; font-size: 17px; color: {t["muted"]}">Они же — персонажи мини-игры «Весёлая Ярмарка».</p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px">
{hero_cards}
      </div>
    </section>

    <!-- ИГРА + СЛЕДУЮЩИЙ ВЫПУСК -->
    <section class="sec" aria-label="Игра и новые выпуски" style="margin-top: 104px; padding-bottom: 104px; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px">
      <a href="https://vk.ru/app54835318_-31319842" style="text-decoration: none; color: #FFFFFF; border-radius: 24px; overflow: hidden; display: flex; flex-wrap: wrap; background: {t["bar"]}">
        <img src="{A["h_game-poster"]}" alt="Постер игры «Весёлая Ярмарка»" style="flex: 1 1 240px; width: 100%; max-width: 100%; aspect-ratio: 1; object-fit: cover">
        <div style="flex: 1 1 240px; padding: 28px; display: flex; flex-direction: column; justify-content: center; gap: 12px">
          <div style="font-weight: 800; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: #E9C77A">Мини-игра во ВКонтакте</div>
          <div style="font-family: Kurale, Georgia, serif; font-size: 34px; line-height: 1.05">Весёлая Ярмарка</div>
          <p style="margin: 0; font-size: 15px; line-height: 1.55; color: #E8DCCB">Играйте за Асю, Женю или Златобрюха. Поделитесь результатом и получите комикс в личные сообщения.</p>
          <span style="align-self: flex-start; margin-top: 6px; background: #E9C77A; color: #2A1A12; font-weight: 800; font-size: 15px; padding: 14px 24px; border-radius: 999px">Играть</span>
        </div>
      </a>
      <div style="border: 3px dashed {t["dashed"]}; border-radius: 24px; padding: 32px; display: flex; flex-direction: column; justify-content: center; gap: 12px; min-height: 300px">
        <div style="font-weight: 800; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: {t["label"]}">Скоро</div>
        <div style="font-family: Kurale, Georgia, serif; font-size: 34px; color: {t["accent"]}">Выпуск 2: [название]</div>
        <p style="margin: 0; font-size: 16px; line-height: 1.55; color: {t["muted"]}">[О чём следующая история и к какой песне]</p>
        <a href="https://vk.com/asya_nova_sing" style="align-self: flex-start; margin-top: 6px; color: {t["ink"]}; font-weight: 800; font-size: 15px">Узнать первыми во ВКонтакте →</a>
      </div>
    </section>
  </main>

{footer_min(t)}'''

comic_js = '''  constructor(props) {
    super(props);
    this.state = { page: 0 };
  }
  go(i) {
    const n = 19;
    this.setState({ page: (i + n) % n });
  }
  renderVals() {
    const P = PAGES_JSON;
    const p = this.state.page;
    return {
      pageNum: p + 1,
      pageSrc: P[p],
      pageAlt: p === 0 ? 'Обложка комикса' : 'Страница ' + (p + 1),
      prev: () => this.go(p - 1),
      next: () => this.go(p + 1),
      thumbs: P.map((src, i) => ({
        src: src,
        label: 'Открыть страницу ' + (i + 1),
        pick: () => this.go(i),
        style: 'flex: none; width: 64px; height: 96px; padding: 0; border-radius: 6px; cursor: pointer; background: transparent; opacity: ' + (i === p ? '1' : '0.55') + '; border: 3px solid ' + (i === p ? '#E9C77A' : 'transparent')
      }))
    };
  }'''.replace('PAGES_JSON', json.dumps(pages))
open(OUT + 'Comic.dc.html', 'w', encoding='utf-8').write(page('Комикс «Девицы-красавицы» — АСЯ NOVA', t['font_q'], t, comic_body, H.get('Comic', 4200), comic_js))

# ---------------- MERCH ----------------
m = dict(bg='#F2F1EE', surface='#FFFFFF', border='#DEDCD7', ink='#121212', muted='#5B5852', accent='#C8102E', accent_text='#C8102E',
         on_accent='#FFFFFF', label='#C8102E', bar='#121212', bar_muted='#BDBAB4', header_bg='rgba(242,241,238,0.94)')
m['h2_style'] = 'font-family: Unbounded, sans-serif; font-weight: 900; font-size: clamp(30px, 3.6vw, 48px); line-height: 1.05; text-transform: uppercase; color: #121212'

collections = [
    ('Коллекция «Девица-красавица»', 'По комиксу и фотосессии релиза', '#FFF4E6', [
        ('Футболка «Девица-красавица»', 'Одежда', 'h_asya'), ('Худи с героями комикса', 'Одежда', 'h_zhenya'),
        ('Стикерпак «Ярмарка»', 'Мелочи', 'h_soroka'), ('Шопер «Купец Златобрюх»', 'Аксессуары', 'h_zlatobryuh')]),
    ('Блокноты Эксперт Блокнот × АСЯ NOVA', 'Дневники с комиксом внутри', '#FFFFFF', [
        ('«Дневник вокалиста»', 'Блокноты', None), ('«Дневник танцора»', 'Блокноты', None),
        ('«Дневник юного блогера»', 'Блокноты', None), ('Брошь-звезда АСИ NOVA', 'Мелочи', None)]),
]


def product(name, cat, img, bg):
    if img in ('h_asya', 'h_zhenya', 'h_soroka'):
        bg = '#0B0B0B'
    pic = (f'<img src="{A[img]}" alt="" style="width: 100%; height: 100%; object-fit: contain">' if img else
           f'<span style="font-weight: 700; color: #6B6760; font-size: 15px">[фото товара]</span>')
    return f'''          <article style="background: #FFFFFF; border: 1px solid #DEDCD7; border-radius: 18px; overflow: hidden; display: flex; flex-direction: column">
            <div style="position: relative; aspect-ratio: 1; background: {bg}; display: flex; align-items: center; justify-content: center">
              {pic}
              <span style="position: absolute; left: 12px; top: 12px; background: #121212; color: #FFFFFF; font-weight: 700; font-size: 12px; padding: 6px 10px; border-radius: 999px">{cat}</span>
            </div>
            <div style="padding: 16px 18px 18px; display: flex; flex-direction: column; gap: 10px; flex: 1">
              <h3 style="margin: 0; font-size: 17px; font-weight: 800; line-height: 1.3">{name}</h3>
              <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-top: auto">
                <span style="font-family: Unbounded, sans-serif; font-weight: 700; font-size: 18px">[цена]</span>
                <a href="#" style="text-decoration: none; background: #C8102E; color: #FFFFFF; font-weight: 800; font-size: 14px; padding: 11px 16px; border-radius: 999px">В корзину</a>
              </div>
            </div>
          </article>'''


coll_html = ''
for title, sub, bg, items in collections:
    coll_html += f'''    <section class="sec" aria-label="{title}" style="margin-top: 88px">
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 12px; margin-bottom: 26px">
        <div>
          <h2 style="margin: 0; {m["h2_style"]}; font-size: clamp(24px, 2.6vw, 34px)">{title}</h2>
          <p style="margin: 8px 0 0; font-size: 16px; color: #5B5852; font-weight: 600">{sub}</p>
        </div>
        <a href="#" style="font-weight: 800; font-size: 15px">Смотреть всё →</a>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 20px">
{chr(10).join(product(n, c, i, bg) for n, c, i in items)}
      </div>
    </section>
'''

cats = ['Все', 'Одежда', 'Блокноты', 'Аксессуары', 'Мелочи']
cat_chips = ''.join(
    f'<a href="#" style="text-decoration: none; padding: 11px 18px; border-radius: 999px; font-weight: 700; font-size: 15px; '
    + ('background: #121212; color: #FFFFFF' if i == 0 else 'background: #FFFFFF; color: #121212; border: 1px solid #DEDCD7') + f'">{c}</a>'
    for i, c in enumerate(cats))

merch_body = header(m, 'merch', '#shop', 'В магазин') + f'''
  <section style="background: #C8102E; color: #FFFFFF; overflow: hidden">
    <div style="max-width: 1320px; margin: 0 auto; padding: 0 32px; display: flex; flex-wrap: wrap; align-items: stretch">
      <div style="flex: 1 1 520px; padding: 80px 0; display: flex; flex-direction: column; justify-content: center; gap: 22px">
        <div style="font-weight: 800; font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: #FFD7DC">Официальный мерч</div>
        <h1 style="margin: 0; font-family: Unbounded, sans-serif; font-weight: 900; font-size: clamp(40px, 5.4vw, 76px); line-height: 0.98; text-transform: uppercase">Фан-магазин<br>АСИ NOVA</h1>
        <p style="margin: 0; font-size: 19px; line-height: 1.55; color: #FFE3E6; max-width: 520px">Одежда, блокноты и сувениры с героями песен и комиксов. Покупайте здесь или в магазине группы ВКонтакте.</p>
        <div style="display: flex; flex-wrap: wrap; gap: 12px">
          <a href="#shop" style="text-decoration: none; background: #FFFFFF; color: #C8102E; font-weight: 800; font-size: 16px; padding: 18px 30px; border-radius: 999px">Смотреть товары</a>
          <a href="https://vk.com/asya_nova_sing" style="text-decoration: none; color: #FFFFFF; font-weight: 800; font-size: 16px; padding: 16px 28px; border-radius: 999px; border: 2px solid #FFFFFF">Магазин ВКонтакте</a>
        </div>
      </div>
      <div style="flex: 1 1 380px; min-height: 460px; position: relative">
        <img src="{A["kino_1991"]}" alt="Ася NOVA в красном бомбере" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 20%">
      </div>
    </div>
  </section>

  <main id="shop" class="page-main" style="max-width: 1320px; margin: 0 auto; padding: 56px 32px 0">
    <nav aria-label="Категории" style="display: flex; flex-wrap: wrap; gap: 10px">{cat_chips}</nav>
{coll_html}
    <section class="sec" aria-labelledby="how-h" style="margin-top: 96px; padding-bottom: 104px">
      <h2 id="how-h" style="margin: 0 0 26px; {m["h2_style"]}">Как купить</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px">
        <div style="background: #FFFFFF; border-radius: 18px; padding: 26px"><div style="font-family: Unbounded, sans-serif; font-weight: 900; font-size: 34px; color: #C8102E">1</div><h3 style="margin: 10px 0 6px; font-size: 19px">На сайте</h3><p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5B5852">Добавьте товары в корзину и оформите заказ. Оплата [способы оплаты].</p></div>
        <div style="background: #FFFFFF; border-radius: 18px; padding: 26px"><div style="font-family: Unbounded, sans-serif; font-weight: 900; font-size: 34px; color: #C8102E">2</div><h3 style="margin: 10px 0 6px; font-size: 19px">Во ВКонтакте</h3><p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5B5852">Те же товары есть в магазине сообщества АСЯ NOVA.</p></div>
        <div style="background: #FFFFFF; border-radius: 18px; padding: 26px"><div style="font-family: Unbounded, sans-serif; font-weight: 900; font-size: 34px; color: #C8102E">3</div><h3 style="margin: 10px 0 6px; font-size: 19px">Доставка</h3><p style="margin: 0; font-size: 15px; line-height: 1.55; color: #5B5852">[Службы доставки, сроки и стоимость]</p></div>
      </div>
    </section>
  </main>

{footer_min(m)}'''
open(OUT + 'Merch.dc.html', 'w', encoding='utf-8').write(
    page('Фан-магазин АСИ NOVA', 'family=Unbounded:wght@700;900', m, merch_body, H.get('Merch', 3000), '  renderVals() {\n    return {};\n  }'))
print('ok')
