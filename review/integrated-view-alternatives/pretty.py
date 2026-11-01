"""Draw the Integrated View in the style of the RA's Figure 3.2, from an Archi model.
Usage: pretty.py model.xml "view name" out.svg [--marks]
Everything drawn comes from the model: the view's groupings (layers, in order),
the elements in them, and their properties figureNote, reddhi, formerName, candidateMatch."""
import sys,html,xml.etree.ElementTree as ET
X='{http://www.w3.org/2001/XMLSchema-instance}type'
src,vname,out=sys.argv[1:4]; MARKS='--marks' in sys.argv
r=ET.parse(src).getroot(); E={e.get('id'):e for e in r.iter('element')}
def props(e): return {p.get('key'):p.get('value') for p in e.findall('property')}
view=[e for e in E.values() if e.get('name')==vname][0]
def node(c):
  e=E[c.get('archimateElement')]; b=c.find('bounds')
  return {'name':e.get('name'),'type':e.get(X).split(':')[1],'p':props(e),'x':int(b.get('x',0)),'y':int(b.get('y',0)),
          'kids':sorted([node(k) for k in c.findall('child') if k.get('archimateElement')],key=lambda n:(n['y'],n['x']))}
top=[node(c) for c in view.findall('child') if c.get('archimateElement')]
layers=sorted([n for n in top if n['kids'] and n['type']=='Grouping'],key=lambda n:(n['x']>1500,n['y']))
side=[l for l in layers if l['x']>1500]; layers=[l for l in layers if l['x']<=1500]
esc=lambda s:html.escape(s or '',quote=True)
def wrap(s,n):
  out,cur=[], ''
  for w in s.split():
    if cur and len(cur)+1+len(w)>n: out.append(cur); cur=w
    else: cur=(cur+' '+w).strip()
  return out+([cur] if cur else [])
def bullets(n,merge=True):
  raw=[x.strip() for x in (n['p'].get('figureNote') or '').split(' · ') if x.strip()]
  out=[]
  for t in raw:  # short items share a line, as in the figure
    if merge and out and len(t)<14 and len(out[-1])+len(t)<30 and not out[-1].endswith(':'): out[-1]+=' · '+t
    else: out.append(t)
  return out
S=[]
def T(x,y,s,size=11,w=400,fill='#14213d',anchor='start',italic=False,ls=0):
  S.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}"'+(' font-style="italic"' if italic else '')+(f' letter-spacing="{ls}"' if ls else '')+f'>{esc(s)}</text>')
def R(x,y,w,h,fill,stroke='none',rx=6,sw=1,dash=''):
  S.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def mark(x,y,n):
  if not MARKS: return
  p=n['p']
  if 'formerName' in p: S.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#2b6cb0"><title>renamed from {esc(p["formerName"])}</title></circle>')
  elif 'candidateMatch' in p: S.append(f'<circle cx="{x}" cy="{y}" r="5" fill="none" stroke="#c05621" stroke-width="2"><title>new; may match {esc(p["candidateMatch"])}</title></circle>')
STAR='#c9922e'
STYLE={  # by the start of the grouping's name
 'Strategic':dict(bg='#0f2a4a',head='#9fb3c8',card='#1d3d63',cs='#2e5584',title='#e8eef6',text='#c9d6e6'),
 'Cross-cutting':dict(bg='#f7ecd6',stroke='#c9a24a',head='#6b4e12',card='#ffffff',cs='#c9a24a',title='#5a4210',text='#7a6230'),
 'Stakeholders':dict(bg='#e9edf3',stroke='#c4ccd8',head='#1f3a5f',card='#ffffff',cs='#c4ccd8',title='#1f3a5f',text='#6b778a'),
 'Capabilities':dict(bg='#e9edf3',stroke='#c4ccd8',head='#1f3a5f',card='#ffffff',cs='#1f3a5f',title='#14213d',text='#3c4659',center=True),
 'Point-of-service':dict(bg='#f4e8f4',stroke='#7b4a8f',head='#5a2e6e',card='#ffffff',cs='#a77bb9',title='#5a2e6e',text='#4a3f55',center=True),
 'DPI-H reusable':dict(bg='#e6f2ef',stroke='#2a8c7c',head='#145a50',card='#ffffff',cs='#2a8c7c',title='#0f4c44',text='#3d5a56'),
 'DPI-H shared':dict(bg='#fcf4e4',stroke='#c9a24a',head='#6b4e12',card='#ffffff',cs='#2a8c7c',title='#0f3b36',text='#3d5a56'),
 'Foundational':dict(bg='#dfe5ee',stroke='#1f3a5f',head='#14213d',card='#ffffff',cs='#1f3a5f',title='#14213d',text='#3c4659'),
 'Technology':dict(bg='#e9edf2',stroke='#8a94a6',head='#14213d',card='#ffffff',cs='#8a94a6',title='#14213d',text='#4a5568'),
}
def style(name): return next(v for k,v in STYLE.items() if name.startswith(k))
W=1800; PAD=36; COLW=270; LW=W-2*PAD-COLW-16
def card(x,y,w,n,st,center=False,dark=False):
  """Return height needed; draw if y is not None."""
  chars=max(12,int(w/6.3)); lines=[]
  b=bullets(n)
  head=None
  if n['p'].get('reddhi') or (b and n['type']=='ApplicationComponent' and b[0] in ('Person Identity','Health Record','Workforce','Location','Health Products','Semantics – Meaning','Syntax – Structure')):
    head=b[0]; b=b[1:]
  tl=wrap(n['name'],int(w/7.4))
  sub=[]
  if st is STYLE['Strategic'] or st is STYLE['Cross-cutting'] or st is STYLE['Stakeholders'] or dark:
    sub=wrap(' · '.join(b),chars)
  else:
    for x_ in b: sub+=['· '+l if i==0 else '  '+l for i,l in enumerate(wrap(x_,chars-2))]
  h=12+(14 if head else 0)+15*len(tl)+12*len(sub)+(16 if n['p'].get('reddhi') else 0)+8
  if y is None: return h
  return h,(tl,sub,head)
def draw_card(x,y,w,h,n,st,center=False,dark=False):
  _,(tl,sub,head)=card(x,0,w,n,st,center,dark)
  fill=st['card'] if not dark else ('#0d4a42' if 'AI' in n['name'] else '#0f2a4a')
  R(x,y,w,h,fill,st['cs'] if not dark else fill,6,1.4)
  ty=y+16; cx=x+w/2 if center else x+9; anc='middle' if center else 'start'
  if head:
    T(x+9,ty,head+(' ★' if n['p'].get('reddhi') else ''),10.5,700,'#2a8c7c'); ty+=14
  if n['p'].get('reddhi'): T(x+w-10,y+20,'★',18,400,STAR,'end')
  tc='#ffffff' if dark else st['title']
  for l in tl: T(cx,ty,l,11.5,700,tc,anc); ty+=15
  ty+=1
  for l in sub: T(x+9 if not center else x+9,ty,l,9.5,400,'#c9e3de' if dark else st['text']); ty+=12
  if n['p'].get('reddhi'): T(x+9,y+h-8,'REDDHI component',9,400,'#a07a2a',italic=True)
  mark(x+w-8 if not n['p'].get('reddhi') else x+w-26,y+h-9,n)
def row(x,y,w,nodes,st,center=False,gap=10):
  k=len(nodes); bw=(w-gap*(k-1))/k
  h=max(card(0,None,bw,n,st)  for n in nodes)
  for i,n in enumerate(nodes): draw_card(x+i*(bw+gap),y,bw,h,n,st,center, n.get('dark',False))
  return h
y=78
for L in layers:
  st=style(L['name']); kids=L['kids']
  if L['name'].startswith('DPI-H reusable'):
    # domain groupings: white panels with their components inside; the cross-cutting one as dark cards
    doms=[k for k in kids if k['type']=='Grouping']
    inner=[]
    for d in doms:
      for c in d['kids']: c['dark']=d['name']=='Cross-cutting'
    panels=[d for d in doms if d['name']!='Cross-cutting']; darks=[c for d in doms if d['name']=='Cross-cutting' for c in d['kids']]
    units=sum(len(d['kids']) for d in panels)+len(darks); uw=(LW-24-10*(len(panels)+len(darks)-1))/units
    hh=max([card(0,None,uw*len(d['kids'])-16,c,st) for d in panels for c in d['kids']]+[0])
    dh=max([card(0,None,uw-0,c,st,dark=True) for c in darks]+[0])
    ph=max(hh+66,dh)
    if y and True:
      dpi_top=y
      R(PAD,y,LW,ph+46+0,st['bg'],st['stroke'],8,1.6)
      T(PAD+14,y+22,'REUSABLE COMPONENTS · organised by business service',11,700,st['head'],ls=0.4)
      x=PAD+12; yy=y+34
      for d in panels:
        pw=uw*len(d['kids'])+10*(len(d['kids'])-1)
        R(x,yy,pw,ph,'#ffffff',st['stroke'],6,1.4)
        T(x+10,yy+18,d['name'],13,700,st['title'])
        for i_,l_ in enumerate(wrap(d['p'].get('figureNote',''),int(pw/5.2))[:2]): T(x+10,yy+31+i_*11,l_,9,400,'#6b8a86',italic=True)
        ix=x+8; iw=(pw-16-8*(len(d['kids'])-1))/len(d['kids'])
        for c in d['kids']:
          S.append(f'<rect x="{ix:.1f}" y="{yy+50:.1f}" width="{iw:.1f}" height="{ph-58:.1f}" rx="4" fill="#d6ece7" stroke="#2a8c7c"/>')
          tl=wrap(c['name'],int(iw/7.2)); ty=yy+66
          for l in tl: T(ix+8,ty,l,11,700,'#0f3b36'); ty+=14
          for bl in bullets(c):
            for l in wrap(bl,int(iw/5.8)): T(ix+8,ty,l,9.5,400,'#2f5a54'); ty+=12
          mark(ix+iw-8,yy+ph-14,c)
          ix+=iw+8
        x+=pw+10
      for c in darks:
        draw_card(x,yy,uw,ph,c,st,dark=True); x+=uw+10
      y+=ph+46+10
    continue
  if L['name'].startswith('DPI-H shared'):
    pass
  label=L['name'].upper()
  if L['name'].startswith('DPI-H shared'):
    label='SHARED DATA LAYER · core registries, lifelong health record, terminology service & logical information models'
  hdr=26
  hb=row(0,0,0.0001,[],st) if False else None
  k=len(kids); bw=(LW-24-10*(k-1))/k
  h=max(card(0,None,bw,n,st) for n in kids)
  R(PAD,y,LW,h+hdr+20,st['bg'],st.get('stroke','none'),8,1.6)
  T(PAD+14,y+20,label,11,700,st['head'],ls=0.5)
  if L['name'].startswith('DPI-H shared'): T(PAD+LW-14,y+20,'★ = REDDHI component · Resilient Essential Data and Digital Health Infrastructure',10,400,'#6b4e12','end')
  row(PAD+12,y+hdr+4,LW-24,kids,st,st.get('center',False))
  if L['name'].startswith('DPI-H shared'):
    # frame the two DPI-H groupings together, as the figure does
    S.append(f'<rect x="{PAD-6}" y="{dpi_top-30}" width="{LW+12}" height="{y+h+hdr+20+6-dpi_top+30}" rx="10" fill="none" stroke="#14213d" stroke-width="2.2"/>')
    T(PAD+8,dpi_top-12,'DPI-H LAYER · GOVERNMENT-STEWARDED REUSABLE DIGITAL PUBLIC INFRASTRUCTURE FOR HEALTH',12,700,'#14213d',ls=0.4)
  y+=h+hdr+20+12
  if L['name'].startswith('Point-of-service'):
    y+=50
    T(PAD+LW/2,y-34,'↓ Point-of-service applications consume the DPI-H (and DPI-F where available) layer via standards-based APIs ↓',11.5,700,'#14213d','middle')
  if L['name'].startswith('DPI-H shared'): y+=8
bottom=y-12
# interoperability column
x=W-PAD-COLW
R(x,78,COLW,bottom-78,'#f5ead4','#b07d12',10,2,'8 5'); R(x,78,COLW,52,'#b07d12','none',10)
T(x+COLW/2,102,'INTEROPERABILITY',14,700,'#ffffff','middle',ls=1); T(x+COLW/2,120,'cross-cutting · pervades every layer',10,400,'#fbeecd','middle',italic=True)
yy=144
for S_ in side:
  for n in S_['kids']:
    if n['name'].endswith('Information Mediator'):
      b=bullets(n,False); h=26+16+12*sum(len(wrap(z,40)) for z in b[2:])+18
      R(x+10,yy,COLW-20,h,'#0f2a4a','none',6)
      T(x+20,yy+20,n['name'].upper(),12,700,'#7ee0d0'); T(x+20,yy+36,' · '.join(b[:2]),9.5,400,'#9fb3c8')
      ty=yy+54
      for z in b[2:]:
        for l in wrap(z,40): T(x+20,ty,l,10,400,'#e8eef6'); ty+=12
      mark(x+COLW-18,yy+h-10,n); yy+=h+16
    else:
      T(x+12,yy+4,n['name'].upper(),11,700,'#5a4210'); yy+=14
      px=x+12
      for pill in bullets(n,False):
        pw=len(pill)*5.6+18
        if px+pw>x+COLW-10: px=x+12; yy+=24
        S.append(f'<rect x="{px:.1f}" y="{yy:.1f}" width="{pw:.1f}" height="19" rx="9.5" fill="#ffffff" stroke="#14213d" stroke-width="1.2"/>')
        T(px+pw/2,yy+13,pill,9,700,'#14213d','middle'); px+=pw+6
      mark(x+COLW-18,yy-10,n); yy+=34
H=bottom+(64 if MARKS else 40)
head=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Inter, Helvetica, Arial, sans-serif">',
 f'<rect width="{W}" height="{H}" fill="#f8f9fb"/>']
T(PAD,46,'DPI-H Reference Architecture — Integrated View',26,800,'#14213d')
T(PAD,66,f'Drawn from the ArchiMate model, view “{vname}”',11,400,'#6b778a',italic=True)
if MARKS:
  ly=bottom+30
  S.append(f'<circle cx="{PAD+6}" cy="{ly-4}" r="5" fill="#2b6cb0"/>'); T(PAD+18,ly,'existing element renamed to the handbook name (old name kept as formerName)',11,400,'#14213d')
  S.append(f'<circle cx="{PAD+526}" cy="{ly-4}" r="5" fill="none" stroke="#c05621" stroke-width="2"/>'); T(PAD+538,ly,'new element; a similar older element is kept (candidateMatch)',11,400,'#14213d')
open(out,'w').write('\n'.join(head+S+['</svg>']))
print('wrote',out,W,H)
