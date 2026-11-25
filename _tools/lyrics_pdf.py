import re, html, os, glob
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
COV={'devitsa-krasavitsa':'cover_devica','gorod-na-levom-beregu':'cover_gorod','gory-sinie':'cover_gory','starye-igrushki-u-kamina':'cover_igrushki','takoe-kino':'cover_kino','lyubimaya-mama':'cover_mama','novogodniy-perezvon':'cover_novogodniy'}
RED=(0.78,0.06,0.18)
out=[]
for d in sorted(glob.glob('music/*/index.html')):
    slug=d.split('/')[1]; t=open(d,encoding='utf-8').read()
    title=html.unescape(re.search(r'<h1[^>]*>(.*?)</h1>',t,re.S).group(1)); title=re.sub('<[^>]+>','',title).strip()
    cr=dict(zip([html.unescape(x) for x in re.findall(r'<dt>(.*?)</dt>',t)],[html.unescape(re.sub('<[^>]+>','',x)) for x in re.findall(r'<dd>(.*?)</dd>',t)]))
    m=re.search(r'<div class="lyrics-text">(.*?)</div>\s*</details>',t,re.S)
    if not m: print('no lyrics',slug); continue
    blocks=[]
    for b in re.findall(r'<div><div class=lab>(.*?)</div>(.*?)</div>',m.group(1),re.S):
        lab=html.unescape(b[0]); paras=[(('ch' in p[0]), html.unescape(re.sub('<[^>]+>','',p[1])).strip()) for p in re.findall(r'<p([^>]*)>(.*?)</p>',b[1],re.S)]
        blocks.append((lab,paras))
    fn=f'files/fans/tekst-{slug}.pdf'; c=canvas.Canvas(fn,pagesize=A4); W,H=A4
    def header(first):
        c.setFillColorRGB(*RED); c.rect(0,H-14*mm,W,14*mm,fill=1,stroke=0)
        c.setFillColorRGB(1,1,1); c.setFont('DVB',10); c.drawString(15*mm,H-9*mm,'АСЯ NOVA'); c.setFont('DV',9); c.drawRightString(W-15*mm,H-9*mm,'asyanova.ru')
    header(True)
    y=H-24*mm; cov=f'assets/img/{COV.get(slug,"")}.jpg'
    if os.path.exists(cov): c.drawImage(ImageReader(cov),W-15*mm-40*mm,y-40*mm,40*mm,40*mm)
    c.setFillColorRGB(0.1,0.1,0.1); c.setFont('DVB',22); c.drawString(15*mm,y-10*mm,title)
    c.setFont('DV',10); yy=y-18*mm
    for k,v in cr.items(): c.drawString(15*mm,yy,f'{k}: {v}'); yy-=5*mm
    y=y-48*mm; colx=[15*mm,W/2+3*mm]; col=0; lh=5.2*mm
    def need(n):
        nonlocal_y=None
    for lab,paras in blocks:
        lines=sum(len(p.split('\n'))+1 for _,p in paras)+1
        if y-lines*lh<15*mm:
            if col==0: col=1; y=H-24*mm-48*mm if c.getPageNumber()==1 else H-24*mm
            else: c.showPage(); header(False); col=0; y=H-24*mm
        x=colx[col]; c.setFillColorRGB(*RED); c.setFont('DVB',10); c.drawString(x,y,lab.upper()); y-=lh
        for ch,p in paras:
            c.setFillColorRGB(0.1,0.1,0.1); c.setFont('DVB' if ch else 'DV',11)
            for line in p.split('\n'): c.drawString(x,y,line.strip()); y-=lh
            y-=lh*0.5
        y-=lh*0.5
    c.setFont('DV',8); c.setFillColorRGB(0.5,0.5,0.5); c.drawCentredString(W/2,8*mm,f'Текст песни «{title}» — для репетиций и личного пользования. Минусовка и песня: asyanova.ru')
    c.save(); out.append((slug,title,fn))
for o in out: print(o, os.path.getsize(o[2])//1024,'KB')
