import sys
sys.path.insert(0, '/home/claude/scripts')
from shared import *

OUT = '/home/claude/work/canvas/project/'

THEMES = {
 'devica': dict(bg='#F7EFE2', surface='#FFFFFF', border='#E6D9C3', ink='#2A1A12', muted='#6E5A48', accent='#A80D0B', accent_text='#A80D0B',
                on_accent='#FFFFFF', label='#8A5F10', bar='#2A1A12', bar_muted='#D9CBB6', chip='#F7EFE2', header_bg='rgba(247,239,226,0.95)',
                font='Kurale, Georgia, serif', font_q='family=Kurale', title_weight='400', title_size='clamp(42px, 4.6vw, 64px)', title_transform='none',
                chorus='#A80D0B', track='#EFE3CF', dashed='#D9C4A0'),
 'gory': dict(bg='#EAF0F8', surface='#FFFFFF', border='#CFDCEC', ink='#14233B', muted='#4A5D78', accent='#2E5E9E', accent_text='#2E5E9E',
              on_accent='#FFFFFF', label='#5A4FA0', bar='#14233B', bar_muted='#C3D0E4', chip='#EAF0F8', header_bg='rgba(234,240,248,0.95)',
              font="Philosopher, Georgia, serif", font_q='family=Philosopher:ital,wght@0,700;1,700', title_weight='700', title_size='clamp(44px, 4.8vw, 66px)', title_transform='none',
              chorus='#2E5E9E', track='#DCE6F3', dashed='#B9CBE3'),
 'kino': dict(bg='#F1EFEC', surface='#FFFFFF', border='#DDD9D3', ink='#111111', muted='#55524D', accent='#C8102E', accent_text='#C8102E',
              on_accent='#FFFFFF', label='#C8102E', bar='#111111', bar_muted='#BDBAB4', chip='#F1EFEC', header_bg='rgba(241,239,236,0.95)',
              font="'Russo One', Impact, sans-serif", font_q='family=Russo+One', title_weight='400', title_size='clamp(44px, 4.8vw, 68px)', title_transform='uppercase',
              chorus='#C8102E', track='#E6E2DC', dashed='#CFC9C0'),
 'igr': dict(bg='#1C2622', surface='#26322D', border='#3A4A43', ink='#F3E7D3', muted='#C9B99E', accent='#E39B2D', accent_text='#F0B24F',
             on_accent='#1C2622', label='#F0B24F', bar='#111814', bar_muted='#C9B99E', chip='#1C2622', header_bg='rgba(28,38,34,0.95)',
             font="'Playfair Display', Georgia, serif", font_q='family=Playfair+Display:wght@600;700', title_weight='700', title_size='clamp(40px, 4.4vw, 60px)', title_transform='none',
             chorus='#F0B24F', track='#3A4A43', dashed='#4D5F57', dark=True),
 'mama': dict(bg='#F3F0FA', surface='#FFFFFF', border='#DFD8EE', ink='#241D38', muted='#5D5478', accent='#6A4FB6', accent_text='#6A4FB6',
              on_accent='#FFFFFF', label='#6A4FB6', bar='#241D38', bar_muted='#CFC6E6', chip='#F3F0FA', header_bg='rgba(243,240,250,0.95)',
              font="'Marck Script', cursive", font_q='family=Marck+Script', title_weight='400', title_size='clamp(52px, 5.6vw, 80px)', title_transform='none',
              chorus='#6A4FB6', track='#E6E0F3', dashed='#CFC4E8'),
 'gorod': dict(bg='#F4EFE3', surface='#FFFFFF', border='#E2D8BF', ink='#1E1B16', muted='#5E574A', accent='#E0A800', accent_text='#8A6A00',
               on_accent='#1E1B16', label='#8A6A00', bar='#1E1B16', bar_muted='#D5CCB6', chip='#F4EFE3', header_bg='rgba(244,239,227,0.95)',
               font="Comfortaa, sans-serif", font_q='family=Comfortaa:wght@700', title_weight='700', title_size='clamp(40px, 4.4vw, 60px)', title_transform='none',
               chorus='#8A6A00', track='#EDE4CC', dashed='#D8CCA8'),
 'novogod': dict(bg='#0E1A33', surface='#16264A', border='#2A3D66', ink='#F2F5FB', muted='#B9C4DB', accent='#E8C66A', accent_text='#E8C66A',
                 on_accent='#0E1A33', label='#E8C66A', bar='#08101F', bar_muted='#B9C4DB', chip='#0E1A33', header_bg='rgba(14,26,51,0.95)',
                 font="'Cormorant Garamond', Georgia, serif", font_q='family=Cormorant+Garamond:ital,wght@1,700', title_weight='700', title_size='clamp(48px, 5.2vw, 72px)', title_transform='none',
                 chorus='#E8C66A', track='#2A3D66', dashed='#34497A', dark=True, italic=True),
}
for k, t in THEMES.items():
    st = 'italic' if t.get('italic') or k == 'gory' else 'normal'
    t['h2_style'] = f'font-family: {t["font"]}; font-weight: {t["title_weight"]}; font-style: {st}; font-size: clamp(32px, 3.4vw, 46px); line-height: 1.1; color: {t["ink"]}; text-transform: {t["title_transform"]}'
    t['title_style'] = f'font-family: {t["font"]}; font-weight: {t["title_weight"]}; font-style: {st}; font-size: {t["title_size"]}; line-height: 1.05; color: {t["accent_text"]}; text-transform: {t["title_transform"]}'

C, V = 'Припев', 'Куплет'
L = {}
L['devica'] = [
 (C, True, ["Девица-красавица\nЯмочки на щёчках\nСолнцу улыбается\nКаблучками – цок-цок!", "Во что ни нарядится\nВсё идёт к лицу!\nПусть простое платьице\nХоть сейчас к венцу"]),
 (V + ' 1', False, ["Что бы ни примерила\nВсё ей, милой впору.\nНету злата-серебра?\nНу, так что за горе?", "Молодость дороже\nВсех богатств на свете!\nВедь купить не сможешь\nЕё ты за монеты!"]),
 (V + ' 2', False, ["А ещё не купишь ты\nДоброе сердечко!\nНе заменит доброты\nНа руке колечко!", "Улыбайся, девица\nПока молодая!\nКак судьба завертится\nОй, никто не знает"]),
 (C, True, ["Девица-красавица\nЯмочки на щёчках\nСолнцу улыбается\nКаблучками – цок-цок!", "Во что ни нарядится\nВсё идёт к лицу\nПусть простое платьице\nХоть сейчас к венцу"]),
]
L['gory'] = [
 (None, True, ["Горы синие,\nГоры дальние,\nАх, увижу ли\nВас когда-нибудь?!\nПолететь бы к вам,\nПтицей быстрою.\nНа вершине я\nДом свой выстрою"]),
 (None, False, ["Я совью гнездо\nНа семи ветрах.\nЯ вплету в него\nЗапах пряных трав.\nБуду жить легко\nИ свободно там.\nБуду верить я\nЛишь семи ветрам."]),
 (None, True, ["Горы дальние,\nГоры снежные,\nВы мечта моя\nСладко-нежная.\nГоры синие,\nГоры дальние,\nАх, увижу ли\nВас когда-нибудь?"]),
]
KC = ["Я знаю одно\nЧто мне всё равно\nДавно не смотрю\nЯ это кино\nТы главную роль\nСвою не сыграл\nА только актрису\nСвою потерял"]
L['kino'] = [
 (V + ' 1', False, ["С тобою, не скрою\nНам было весело вдвоём\nИз школы, весною\nДо дома шли мы под дождём\nНо время прошло\nИ вдаль унесло\nВсе наши с тобой тик-токи\nЗнаю, теперь нелегко, тебе одному\nУчить без меня уроки\nУслышь этой песни строки"]),
 (C, True, KC),
 (V + ' 2', False, ["При встрече, замечу\nКак улыбаешься ты мне\nНо я не отвечу\nОбида всё ещё в душе\nПусть время идёт\nОбида пройдёт\nИ может быть осознаешь\nПорою тех слов\nЧто ты говоришь\nЗначенья не понимаешь\nДрузей снова ты теряешь"]),
 (C, True, KC),
 (V + ' 3', False, ["Летели, недели\nУже каникулы прошли\nМы стали взрослее\nНо дружбу нашу сберегли\nПусть в нашем кино\nБыл долгий антракт\nСледы на песке размыло\nНо мы подтвердили следующий факт\nРазлука наш путь продлила\nНе зря это с нами было"]),
 ('Финальный припев', True, ["Я знаю одно\nТакое кино\nУ каждого быть\nДолжно всё равно\nМы роли свои\nДолжны отыграть\nНо верную дружбу\nНе потерять"]),
]
IC = ["Старые игрушки у камина\nВ доме у прабабушки моей\nВ памяти навеки сохранили\nРадость и тепло минувших дней\nСтарые игрушки у камина\nСказки у лампады до зари\nВспоминая, мама говорила\nВзгляд их — словно зеркало души"]
L['igr'] = [
 (C, True, IC),
 (V + ' 1', False, ["Ночь, ты снова у окна — одна\nДочь твоя уже давно — жена\nУ неё теперь есть внуки\nЗавтра утром смеха звуки\nИх наполнят дом твой добротой"]),
 (C, True, IC),
 (V + ' 2', False, ["Сны вернут тебя опять — туда\nГде войны ребёнком ты была\nПулей свист, мороз и холод\nБоль потерь и дикий голод —\nТы преодолела, ты смогла"]),
 (C, True, IC),
 (V + ' 3', False, ["Я верёвкой заведу волчок\nИ мотанку-куклу на бочок\nПоложу, ты спи, родная\nТолько ты на свете знаешь\nКак трёх матерей прошли года"]),
 (C, True, IC),
]
L['mama'] = [
 (V + ' 1', False, ["Когда в моменты тревожной суеты\nТвоя улыбка согревает нас,\nСтою за сценой и знаю: рядом ты\nПереживаешь словно в первый раз"]),
 (C, True, ["Скажу тебе а ия ия\nЛюблю я тебя ия ия\nЛюбимая мамочка моя\nЛюбимая мама", "Ты самый родной иой иой\nЧеловек дорогой иой иой\nБудь рядом со мной иой всегда\nЛюбимая мама"]),
 (V + ' 2', False, ["Года проходят, я старше становлюсь,\nНо, как и прежде, я твоя звезда\nТы говоришь мне: «Я так тобой горжусь»\nНе подведу тебя я никогда"]),
 (V + ' 3', False, ["С утра до ночи и с ночи до утра\nТы сон мой охраняла от беды\nВсегда ты будешь мудра и молода\nТы помнишь мои первые шаги"]),
]
GC = ["Город на левом берегу\nВ моем сердце навсегда ты\nВновь расставаясь не могу\nЯ забыть твои закаты", "Город на левом берегу\nДетства нашего начало\nВ памяти бережно храню\nНаш кораблик у причала"]
L['gorod'] = [
 (V + ' 1', False, ["Помнишь сидели во дворах\nПели песни под гитару\nВместе гуляли до утра\nВдоль дождливого бульвара", "Это место, где сбывались все мечты\nГород детства, любим я и ты"]),
 (C, True, GC),
 (V + ' 2', False, ["Помнишь когда на высоте\nМы туда-сюда катались\nПосле на Борской стороне\nУ «канатки» целовались", "Может, кто-то встретит здесь свою любовь,\nЭта песня заиграет вновь"]),
 (C, True, GC),
 (V + ' 3', False, ["Помнишь в кругу большой семьи\nЗа столом все собирались\nКак встрече радовались мы\nКак над шутками смеялись", "Это место, где ты точно не один\nГород сердца, с нами ты един"]),
 (C, True, GC),
]
NC12 = ["Бом, бом, бом\nСлышишь этот перезвон\nДед Мороз на белой колеснице\nБом, бом, бом\nС Новым годом, Рождеством\nВсю Россию он поздравить мчится", "Бом, бом, бом\nВ ритме с новым волшебством\nНа часах двенадцать бьют куранты\nБом, бом, бом\nМы танцуем и поём\nПусть раскроет праздник все таланты"]
L['novogod'] = [
 (V + ' 1', False, ["Я и все мои друзья\nНадежды не тая\nПорою в облаках витаем\nТам предела нет мечтам\nИ, веря чудесам,\nЖелания мы загадаем", "Вот снежинок хоровод\nОтправился в полёт\nУкрыть деревья белым пледом\nЗов волшебных бубенцов\nТам тройка скакунов\nПроносится за вьюгой следом"]),
 (C, True, NC12),
 (V + ' 2', False, ["Мы ждём каждый год зимы\nКогда леса, холмы\nНаденут ледяную маску\nВ ней волшебник-чародей\nДля взрослых и детей\nГотовит про Мороза сказку", "Ждёт, когда среди хлопот\nВсех снова соберёт\nЛюбимый и семейный праздник\nОн набрал уже разгон\nВзлетает в небосклон\nИ машет бородой проказник"]),
 (C, True, [NC12[0]]),
 (C, True, NC12),
]

ALT = {
 'dev': 'Ася и Женя в народных костюмах', 'gory': 'Ася в голубом костюме с перьями', 'igr': 'Ася в жёлтом платье со старинными игрушками',
 'mama': 'Ася в сиреневом платье с перьями', 'gorod': 'Ася и Евгений Игнатов с гитарой', 'kino': 'Ася в красном бомбере и клетчатой юбке'}


def photos(prefix, extra_first=()):
    keys = list(extra_first) + sorted(k for k in A if k.startswith(prefix + '_') and k.split('_')[1].isdigit())
    return [(k, ALT[prefix]) for k in keys]


PAGES = [
 dict(key='devica', file='Song-Devica.dc.html', title='Девица-красавица', cover='cover_devica', artist='АСЯ NOVA, Евгения Русева',
      eyebrow='Сингл · 30 октября 2026', credits=[('Музыка и слова', 'Татьяна Шабрацкая'), ('Исполняют', 'АСЯ NOVA и Евгения Русева'), ('Лейбл', '«Ура! Музыка»')],
      photos=photos('dev', ('dev_1833', 'dev_1779', 'dev_1826')), extra='devica'),
 dict(key='gory', file='Song-Gory.dc.html', title='Горы синие', cover='cover_gory', artist='АСЯ NOVA',
      eyebrow='Сингл · 20 февраля 2026', credits=[('Музыка и слова', 'Татьяна Шабрацкая'), ('Исполняет', 'АСЯ NOVA')], photos=photos('gory')),
 dict(key='kino', file='Song-Kino.dc.html', title='Такое кино', cover='cover_kino', artist='АСЯ NOVA',
      eyebrow='Сингл · 28 августа 2026', credits=[('Музыка и слова', 'Евгений Игнатов'), ('Исполняет', 'АСЯ NOVA')], photos=photos('kino')),
 dict(key='igr', file='Song-Igrushki.dc.html', title='Старые игрушки у камина', cover='cover_igrushki', artist='АСЯ NOVA',
      eyebrow='В эфире Детского радио', credits=[('Музыка и слова', 'Евгений Игнатов'), ('Исполняет', 'АСЯ NOVA')], photos=photos('igr')),
 dict(key='mama', file='Song-Mama.dc.html', title='Любимая мама', cover='cover_mama', artist='АСЯ NOVA',
      eyebrow='Сингл · 21 марта 2025', credits=[('Музыка и слова', 'Евгений Игнатов'), ('Исполняет', 'АСЯ NOVA')], photos=photos('mama')),
 dict(key='gorod', file='Song-Gorod.dc.html', title='Город на левом берегу', cover='cover_gorod', artist='АСЯ NOVA, Евгений Игнатов',
      eyebrow='Сингл · 27 ноября 2025', credits=[('Музыка и слова', 'Евгений Игнатов'), ('Исполняют', 'АСЯ NOVA и Евгений Игнатов')], photos=photos('gorod')),
 dict(key='novogod', file='Song-Novogodniy.dc.html', title='Новогодний перезвон', cover='cover_novogodniy', artist='АСЯ NOVA',
      eyebrow='Новогодняя песня · 12 декабря 2025', credits=[('Музыка и слова', 'Евгений Игнатов'), ('Исполняет', 'АСЯ NOVA')], photos=[]),
]


def lyrics_html(t, blocks):
    out = []
    for label, chorus, stanzas in blocks:
        ps = []
        for i, s in enumerate(stanzas):
            m = '0' if i == 0 else '16px 0 0'
            style = f'margin: {m}; white-space: pre-line' + (f'; color: {t["chorus"]}; font-weight: 700' if chorus else '')
            ps.append(f'            <p style="{style}">{s}</p>')
        lab = (f'            <div style="font-weight: 800; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: {t["label"]}; margin-bottom: 8px">{label}</div>\n' if label else '')
        out.append('          <div>\n' + lab + '\n'.join(ps) + '\n          </div>')
    return '\n'.join(out)


def chip(t, name):
    return (f'<a href="#" style="text-decoration: none; color: {t["ink"]}; background: {t["chip"]}; padding: 6px 16px 6px 6px; border-radius: 999px; font-weight: 700; font-size: 14px; display: inline-flex; align-items: center; gap: 8px">'
            f'<img src="{ICONS[name]}" alt="Значок: {name}" style="width: 28px; height: 28px; display: block; border-radius: 50%">{name}</a>')


def more_section(t, p):
    h2 = f'<h2 id="mo-h" style="margin: 0 0 28px; {t["h2_style"]}">Ещё про эту песню</h2>'
    if p.get('extra') == 'devica':
        tiles = f'''        <a href="#" style="text-decoration: none; color: #FFFFFF; position: relative; border-radius: 18px; overflow: hidden; min-height: 300px; display: block; background: #A80D0B">
          <img src="{A["dev_1833"]}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
          <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.72) 100%)"></div>
          <div style="position: absolute; left: 50%; top: 42%; transform: translate(-50%, -50%); width: 72px; height: 72px; border-radius: 50%; background: #FFFFFF; color: #A80D0B; display: flex; align-items: center; justify-content: center"><svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M7 4.5v15l13-7.5z"></path></svg></div>
          <span style="position: absolute; left: 22px; bottom: 18px; font-weight: 800; font-size: 19px">Смотреть тизер</span>
        </a>
        <a href="Comic.dc.html" style="text-decoration: none; color: #2A1A12; border-radius: 18px; min-height: 300px; display: flex; gap: 20px; align-items: center; padding: 22px; background: #FFFFFF; border: 3px solid #2A1A12">
          <img src="{A["c_01"]}" alt="Обложка комикса" style="width: 42%; flex: none; border-radius: 6px; transform: rotate(-3deg); box-shadow: 0 10px 24px rgba(42,26,18,0.25)">
          <div>
            <div style="font-family: Kurale, Georgia, serif; font-size: 24px">Читать комикс</div>
            <div style="font-size: 15px; color: #6E5A48; margin-top: 6px">«Девицы-красавицы. Лавка, где продают всё» · 19 страниц</div>
          </div>
        </a>
        <a href="https://vk.ru/app54835318_-31319842" style="text-decoration: none; color: #FFFFFF; border-radius: 18px; min-height: 300px; display: block; position: relative; overflow: hidden; background: #2A1A12">
          <img src="{A["h_game-poster"]}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
          <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 45%, rgba(42,26,18,0.85) 100%)"></div>
          <div style="position: absolute; left: 22px; bottom: 18px">
            <div style="font-weight: 800; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: #E9C77A">Мини-игра во ВКонтакте</div>
            <div style="font-family: Kurale, Georgia, serif; font-size: 30px; margin-top: 6px">Весёлая Ярмарка</div>
          </div>
        </a>'''
    else:
        ph = p['photos'][0][0] if p['photos'] else p['cover']
        tiles = f'''        <a href="#" style="text-decoration: none; color: #FFFFFF; position: relative; border-radius: 18px; overflow: hidden; min-height: 300px; display: block; background: {t["bar"]}">
          <img src="{A[ph]}" alt="" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.85">
          <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.75) 100%)"></div>
          <div style="position: absolute; left: 50%; top: 42%; transform: translate(-50%, -50%); width: 72px; height: 72px; border-radius: 50%; background: #FFFFFF; color: #111111; display: flex; align-items: center; justify-content: center"><svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M7 4.5v15l13-7.5z"></path></svg></div>
          <span style="position: absolute; left: 22px; bottom: 18px; font-weight: 800; font-size: 19px">Смотреть [клип / live]</span>
        </a>
        <a href="Main.dc.html#collab" style="text-decoration: none; color: {t["ink"]}; border-radius: 18px; min-height: 300px; display: flex; flex-direction: column; justify-content: flex-end; gap: 10px; padding: 28px; background: {t["surface"]}; border: 1px solid {t["border"]}">
          <div style="font-weight: 800; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: {t["label"]}">Для организаторов</div>
          <div style="{t["h2_style"]}; font-size: 30px">Пригласить Асю спеть эту песню</div>
          <div style="font-size: 15px; color: {t["muted"]}">Концерт, праздник, конкурс или эфир</div>
        </a>'''
    return f'''    <section class="more-sec" aria-labelledby="mo-h" style="margin-top: 96px">
      {h2}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px">
{tiles}
      </div>
    </section>
'''


def others(t, p):
    cards = []
    for f, title, cover in SONGS:
        if f == p['file']:
            continue
        cards.append(f'        <a href="{f}" style="text-decoration: none; display: flex; flex-direction: column; gap: 10px; color: {t["ink"]}"><img src="{A[cover]}" alt="Обложка «{title}»" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 14px"><span style="font-weight: 800; font-size: 16px">{title}</span></a>')
    return f'''    <section class="other-sec" aria-labelledby="ot-h" style="margin-top: 96px; padding-bottom: 96px">
      <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 16px; margin-bottom: 28px">
        <h2 id="ot-h" style="margin: 0; {t["h2_style"]}">Другие песни</h2>
        <a href="Main.dc.html#music" style="font-weight: 800; font-size: 16px; color: {t["ink"]}">Вся музыка →</a>
      </div>
      <div class="other-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 24px 18px">
{chr(10).join(cards)}
      </div>
    </section>
'''


def build(p):
    t = THEMES[p['key']]
    creds = '\n'.join(f'          <dt style="color: {t["muted"]}; font-weight: 600">{a}</dt><dd style="margin: 0; font-weight: 700">{b}</dd>' for a, b in p['credits'])
    body = header(t, 'music', '#player') + f'''
  <main class="page-main" style="max-width: 1320px; margin: 0 auto; padding: 28px 32px 0">
    <nav aria-label="Хлебные крошки" style="font-size: 14px; font-weight: 600; color: {t["muted"]}; display: flex; gap: 8px; flex-wrap: wrap">
      <a href="Main.dc.html" style="color: {t["muted"]}">Главная</a><span aria-hidden="true">/</span><a href="Main.dc.html#music" style="color: {t["muted"]}">Музыка</a><span aria-hidden="true">/</span><span style="color: {t["ink"]}">{p["title"]}</span>
    </nav>

    <div class="song-cols" style="display: flex; flex-wrap: wrap; gap: 56px; align-items: flex-start; margin-top: 28px">
      <div id="player" class="song-left" style="flex: 1 1 500px; max-width: 580px; display: flex; flex-direction: column; gap: 22px">
        <img src="{A[p["cover"]]}" alt="Обложка «{p["title"]}»" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 20px; box-shadow: 0 24px 50px rgba(0,0,0,0.22)">
        <div>
          <div style="font-weight: 800; font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: {t["label"]}">{p["eyebrow"]}</div>
          <h1 style="margin: 10px 0 6px; {t["title_style"]}">{p["title"]}</h1>
          <div style="font-size: 18px; font-weight: 700">{p["artist"]}</div>
        </div>
        <div style="background: {t["surface"]}; border: 1px solid {t["border"]}; border-radius: 18px; padding: 18px 20px; display: flex; flex-direction: column; gap: 14px">
          <div style="display: flex; align-items: center; gap: 14px">
            <button type="button" aria-label="Слушать «{p["title"]}»" style="flex: none; width: 60px; height: 60px; border-radius: 50%; border: 0; background: {t["accent"]}; color: {t["on_accent"]}; display: flex; align-items: center; justify-content: center; cursor: pointer">
              <svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M7 4.5v15l13-7.5z"></path></svg>
            </button>
            <div style="flex: 1; display: flex; flex-direction: column; gap: 8px">
              <div style="height: 6px; border-radius: 3px; background: {t["track"]}"><div style="width: 28%; height: 6px; border-radius: 3px; background: {t["accent"]}"></div></div>
              <div style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 700; color: {t["muted"]}"><span>[0:00]</span><span>[0:00]</span></div>
            </div>
          </div>
          <div style="display: flex; flex-wrap: wrap; gap: 8px">
            {chip(t, "Яндекс Музыка")}
            {chip(t, "VK Музыка")}
            {chip(t, "Звук")}
          </div>
        </div>
        <dl style="margin: 0; display: grid; grid-template-columns: max-content 1fr; gap: 8px 20px; font-size: 15px">
{creds}
        </dl>
      </div>

      <details open class="lyrics" style="flex: 1 1 440px; min-width: 0; background: {t["surface"]}; border: 1px solid {t["border"]}; border-radius: 22px; padding: 34px 40px 44px">
        <summary style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding-bottom: 22px; border-bottom: 1px dashed {t["dashed"]}; margin-bottom: 28px">
          <span style="{t["h2_style"]}; font-size: 30px; color: {t["accent_text"]}">Текст песни</span>
          <span style="font-weight: 700; font-size: 14px; color: {t["label"]}; display: inline-flex; align-items: center; gap: 6px">Свернуть
            <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 15l6-6 6 6"></path></svg>
          </span>
        </summary>
        <div class="lyrics-text" style="display: flex; flex-direction: column; gap: 30px; font-size: 20px; line-height: 1.6">
{lyrics_html(t, L[p["key"]])}
        </div>
      </details>
    </div>

{carousel(t, p["photos"]) if p["photos"] else ""}{more_section(t, p)}{others(t, p)}  </main>

{footer_min(t)}{mini_player(t, p["cover"], p["title"], p["artist"])}'''
    script = ''
    if p['photos']:
        script = CAROUSEL_JS + '''
  renderVals() {
    return { prev: (e) => this.scrollCar(e, -1), next: (e) => this.scrollCar(e, 1) };
  }'''
    else:
        script = '  renderVals() {\n    return {};\n  }'
    font_q = t['font_q'] + '&amp;family=Unbounded:wght@700;900' if False else t['font_q']
    html = page(f'{p["title"]} — песня и текст', font_q, t, body, p.get('h', 4000), script)
    open(OUT + p['file'], 'w', encoding='utf-8').write(html)


if __name__ == '__main__':
    import json
    hs = json.load(open('/home/claude/scripts/heights.json')) if len(sys.argv) > 1 else {}
    for p in PAGES:
        if p['file'] in hs:
            p['h'] = hs[p['file']]
        build(p)
    print('built', len(PAGES))
