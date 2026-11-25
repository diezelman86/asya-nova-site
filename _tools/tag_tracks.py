import shutil, re, sys
sys.path.insert(0, '/home/claude/scripts')
from songs import L
from mutagen.id3 import ID3, TIT2, TPE1, TPE2, TALB, TRCK, TPOS, TDRC, TCON, TPUB, TCOP, TCOM, TEXT, USLT, APIC, WOAR, COMM, TLAN
U = '/mnt/user-data/uploads/'
OUT = '/home/claude/asya-nova-site/files/'
IMG = '/home/claude/asya-nova-site/assets/img/'
R = {  # key: (file, slug, title, artists, date, genre, label, writer, cover)
 # 'devica' — скачивание отложено до согласования с лейблом
 # 'devica': ('f364ccfd-Asya_Jenya_devitsa_Master_1.mp3', 'devitsa-krasavitsa', 'Девица-красавица', 'АСЯ NOVA, Евгения Русева', '2026-10-30', 'Поп', 'Ура! Музыка', 'Татьяна Шабрацкая', 'cover_devica'),
 'gory': ('311946ac-Gory_Synie_PreMaster_new_vox.mp3', 'gory-sinie', 'Горы синие', 'АСЯ NOVA', '2026-02-20', 'Поп', 'Евгений Игнатов', 'Татьяна Шабрацкая', 'cover_gory'),
 'kino': ('c8076dd6-Asya_Nova_Kino__Master_vers_3.mp3', 'takoe-kino', 'Такое кино', 'АСЯ NOVA', '2026-08-28', 'Поп', 'Евгений Игнатов', 'Евгений Игнатов', 'cover_kino'),
 'igr': ('d8fb9f08-Asya_Nova_Igrushki_Master_.mp3', 'starye-igrushki-u-kamina', 'Старые игрушки у камина', 'АСЯ NOVA', '2026-05-05', 'Поп', 'Евгений Игнатов', 'Евгений Игнатов', 'cover_igrushki'),
 'mama': ('3db6e924-Lubimaya_Mama.mp3', 'lyubimaya-mama', 'Любимая мама', 'АСЯ NOVA', '2025-03-21', 'Детская', 'Евгений Игнатов', 'Евгений Игнатов', 'cover_mama'),
 'gorod': ('f07a8366-Gorod_Correct_Master_3_Vers.mp3', 'gorod-na-levom-beregu', 'Город на левом берегу', 'АСЯ NOVA, Евгений Игнатов', '2025-11-27', 'Рок', 'Евгений Игнатов', 'Евгений Игнатов', 'cover_gorod'),
 'novogod': ('818f87dc-Asya_Nova_Nov_god__Master__.mp3', 'novogodniy-perezvon', 'Новогодний перезвон', 'АСЯ NOVA', '2025-12-12', 'Поп', 'Евгений Игнатов', 'Евгений Игнатов', 'cover_novogodniy'),
}
def lyr(k):
    out = []
    for label, chorus, stanzas in L[k]:
        txt = '\n\n'.join(re.sub(r'<[^>]+>', '', s) for s in stanzas)
        if label: txt = label + '\n' + txt
        elif chorus: txt = 'Припев:\n' + txt
        out.append(txt)
    return '\n\n'.join(out)
for k, (f, slug, t, art, date, genre, label, writer, cover) in R.items():
    dst = OUT + slug + '.mp3'
    shutil.copyfile(U + f, dst)
    tags = ID3(); y = date[:4]
    tags.add(TIT2(encoding=1, text=t)); tags.add(TPE1(encoding=1, text=art)); tags.add(TPE2(encoding=1, text='АСЯ NOVA'))
    tags.add(TALB(encoding=1, text=t)); tags.add(TRCK(encoding=1, text='1/1')); tags.add(TPOS(encoding=1, text='1/1'))
    tags.add(TDRC(encoding=1, text=date)); tags.add(TCON(encoding=1, text=genre)); tags.add(TLAN(encoding=1, text='rus'))
    tags.add(TPUB(encoding=1, text=label)); tags.add(TCOP(encoding=1, text=f'℗ {y} {label}'))
    if writer: tags.add(TCOM(encoding=1, text=writer)); tags.add(TEXT(encoding=1, text=writer))
    tags.add(USLT(encoding=1, lang='rus', desc='', text=lyr(k)))
    tags.add(APIC(encoding=0, mime='image/jpeg', type=3, desc='Cover', data=open(IMG + cover + '.jpg', 'rb').read()))
    tags.add(WOAR(url='https://asyanova.ru'))
    tags.add(COMM(encoding=1, lang='rus', desc='', text=f'Официальный сайт АСИ NOVA: asyanova.ru/music/{slug}/'))
    tags.save(dst, v2_version=3)  # replaces all old tags
    print(k, dst)
