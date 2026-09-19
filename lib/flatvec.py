#!/usr/bin/env python3
# Shared flat-vector SVG core for every Xmind image set in this repo.
# Palette + primitives live here once; each <set>/gen.py imports them and adds its own content.
import os, html, textwrap

BG="#F7F5F2"; INK="#2A2722"; ACCENT="#E8683F"; BUBBLE="#E7E2DA"
STROKE="#D9D3C9"; MUTE="#8A8378"; PANEL="#FFFFFF"; SOFT="#F2EEE8"; SUB="#5B554D"
W,H=480,300
FONT='font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif"'
MONO='font-family="ui-monospace,Menlo,Consolas,monospace"'

def esc(s): return html.escape(str(s), quote=True)
SCALE = 2  # explicit px size = viewBox * SCALE, so Xmind reads an intrinsic size and renders crisp
def svg(frag):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W*SCALE}" height="{H*SCALE}" '
            f'viewBox="0 0 {W} {H}" {FONT}>'
            f'<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>'
            f'<rect x="0" y="0" width="{W}" height="8" fill="{ACCENT}"/>{frag}</svg>\n')
def wrap(t,x,y,size,fill,mc,lh=None,weight=None,anchor="start",family=None):
    lh=lh or size+5
    w=f' font-weight="{weight}"' if weight else ""
    a=f' text-anchor="{anchor}"' if anchor!="start" else ""
    fam=f' {family}' if family else ""
    lines=textwrap.wrap(str(t),mc) or [""]
    o=f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}"{w}{a}{fam}>'
    for i,ln in enumerate(lines):
        o+=f'<tspan x="{x}" dy="{0 if i==0 else lh}">{esc(ln)}</tspan>'
    return o+'</text>', len(lines)
def eyebrow(t): return f'<text x="38" y="40" fill="{MUTE}" font-size="12" letter-spacing="2">{esc(t.upper())}</text>'
def tagtxt(t): return f'<text x="{W-38}" y="40" fill="{MUTE}" font-size="10" text-anchor="end" letter-spacing="1">{esc(t.upper())}</text>'

G={
 "dot":f'<circle cx="14" cy="14" r="6" fill="{ACCENT}"/>',
 "book":f'<path d="M4 5h9a3 3 0 0 1 3 3v15a3 3 0 0 0-3-3H4z M24 5h-9a3 3 0 0 0-3 3v15a3 3 0 0 1 3-3h9z" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "sync":f'<path d="M6 12a8 8 0 0 1 14-4 M22 16a8 8 0 0 1-14 4" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/><path d="M20 4v5h-5 M8 24v-5h5" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "spark":f'<path d="M14 3l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="{ACCENT}" opacity="0.85"/>',
 "warn":f'<path d="M14 4 26 24H2z" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/><path d="M14 11v6 M14 20v.5" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "target":f'<circle cx="14" cy="14" r="10" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="14" cy="14" r="4" fill="{ACCENT}"/>',
 "shield":f'<path d="M14 3l10 4v7c0 7-5 10-10 12-5-2-10-5-10-12V7z" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M9 14l4 4 7-8" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 "chat":f'<path d="M4 6h20a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H12l-6 5v-5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "memory":f'<rect x="5" y="7" width="18" height="14" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M9 3v4 M14 3v4 M19 3v4 M9 21v4 M14 21v4 M19 21v4" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "plug":f'<path d="M10 3v7 M18 3v7 M6 10h16v4a8 8 0 0 1-16 0z M14 22v4" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "doc":f'<path d="M7 3h10l6 6v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M10 14h8 M10 19h8" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "tokens":f'<circle cx="10" cy="14" r="6" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="18" cy="14" r="6" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "rocket":f'<path d="M14 3c5 4 7 9 7 14l-4 4h-6l-4-4c0-5 2-10 7-14z" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="14" cy="12" r="2.5" fill="{ACCENT}"/><path d="M10 22l-3 5 M18 22l3 5" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "gear":f'<circle cx="14" cy="14" r="5" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M14 2v4 M14 22v4 M2 14h4 M22 14h4 M5 5l3 3 M20 20l3 3 M23 5l-3 3 M5 23l3-3" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "download":f'<path d="M14 3v14 M8 12l6 6 6-6 M4 23h20" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 "eye":f'<path d="M2 14c4-7 20-7 24 0-4 7-20 7-24 0z" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="14" cy="14" r="3.5" fill="{ACCENT}"/>',
 "globe":f'<circle cx="14" cy="14" r="11" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M3 14h22 M14 3c6 6 6 16 0 22-6-6-6-16 0-22" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "folder":f'<path d="M4 8h7l3 3h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V10a2 2 0 0 1 2-2z" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "table":f'<rect x="4" y="6" width="20" height="16" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M4 12h20 M11 6v16 M18 6v16" stroke="{ACCENT}" stroke-width="2"/>',
 "hand":f'<path d="M9 14V8a2 2 0 0 1 4 0v5 M13 13V6a2 2 0 0 1 4 0v7 M17 13V8a2 2 0 0 1 4 0v10a7 7 0 0 1-7 7h-2a7 7 0 0 1-6-4l-3-6a2 2 0 0 1 4-2l1 2" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 "flag":f'<path d="M6 3v22 M6 4h14l-3 5 3 5H6" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>',
 "search":f'<circle cx="12" cy="12" r="8" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M18 18l7 7" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "term":f'<rect x="3" y="5" width="22" height="18" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M8 11l4 3-4 3 M14 17h5" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 "layers":f'<path d="M14 3l11 6-11 6-11-6z M3 15l11 6 11-6 M3 21l11 6 11-6" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>',
 "euro":f'<circle cx="14" cy="14" r="11" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M19 9a6 6 0 0 0-9 3 6 6 0 0 0 9 5 M6 12h9 M6 16h8" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" fill="none"/>',
 "list":f'<path d="M9 7h15 M9 14h15 M9 21h15 M4 7v.1 M4 14v.1 M4 21v.1" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "brain":f'<path d="M11 5a5 5 0 0 0-5 5 4 4 0 0 0-1 7 4 4 0 0 0 4 5 4 4 0 0 0 7 1V6a4 4 0 0 0-6-1z M17 5a5 5 0 0 1 5 5 4 4 0 0 1 1 7 4 4 0 0 1-4 5 4 4 0 0 1-7 1" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "grid":f'<rect x="4" y="4" width="9" height="9" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><rect x="15" y="4" width="9" height="9" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><rect x="4" y="15" width="9" height="9" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><rect x="15" y="15" width="9" height="9" rx="2" fill="{ACCENT}"/>',
 "device":f'<rect x="3" y="5" width="15" height="12" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><rect x="19" y="9" width="7" height="13" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "mail":f'<rect x="3" y="6" width="22" height="16" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M4 8l10 7 10-7" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "steer":f'<circle cx="14" cy="14" r="11" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="14" cy="14" r="3" fill="{ACCENT}"/><path d="M14 3v8 M4 19l7-4 M24 19l-7-4" stroke="{ACCENT}" stroke-width="2"/>',
 "image":f'<rect x="3" y="5" width="22" height="18" rx="2" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="10" cy="11" r="2" fill="{ACCENT}"/><path d="M5 21l6-6 4 3 4-5 4 5" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>',
 "camera":f'<rect x="3" y="7" width="22" height="15" rx="3" fill="none" stroke="{ACCENT}" stroke-width="2"/><circle cx="14" cy="14" r="4" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M9 7l2-3h6l2 3" fill="none" stroke="{ACCENT}" stroke-width="2"/>',
 "check":f'<circle cx="14" cy="14" r="11" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M8 14l4 4 8-9" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 "split":f'<path d="M14 4v20 M6 9a12 12 0 0 0 8 6 M22 9a12 12 0 0 1-8 6" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
 "clock":f'<circle cx="14" cy="14" r="11" fill="none" stroke="{ACCENT}" stroke-width="2"/><path d="M14 7v7l5 3" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linecap="round"/>',
}
def gl(name,tx,ty,s=1.0): return f'<g transform="translate({tx},{ty}) scale({s})">{G.get(name,G["dot"])}</g>'


def motif_tiles(items,y=176):
    n=len(items); tw=(W-80-(n-1)*12)/n; o=""
    for i,(lab,g) in enumerate(items):
        x=40+i*(tw+12)
        o+=f'<rect x="{x:.0f}" y="{y}" width="{tw:.0f}" height="96" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
        o+=gl(g,x+tw/2-14,y+16)
        o+=wrap(lab,x+tw/2,y+76,10,INK,16,lh=12,weight=600,anchor="middle")[0]
    return o

def f_section(eb,title,blurb,motif=""):
    t,_=wrap(title,38,92,30,INK,24,weight=700)
    b,_=wrap(blurb,40,132,14,SUB,58,lh=18)
    return eyebrow(eb)+t+b+motif

def f_card(title,sub="",g="dot",tg=""):
    o=f'<rect x="24" y="26" width="{W-48}" height="{H-52}" rx="14" fill="{PANEL}" stroke="{STROKE}"/>'
    o+=f'<rect x="24" y="26" width="{W-48}" height="7" rx="7" fill="{ACCENT}" opacity="0.85"/>'
    o+=gl(g,52,58,1.15)
    t,nn=wrap(title,56,150,20,INK,34,lh=26,weight=600); o+=t
    if sub: o+=wrap(sub,56,150+nn*26+16,12.5,MUTE,52,lh=16)[0]
    if tg: o+=tagtxt(tg)
    return o

def f_browser(title,url,umsg,blines,ph,model="Claude Sonnet"):
    o=f'<rect x="20" y="22" width="440" height="258" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
    o+=f'<path d="M20 34a12 12 0 0 1 12-12h416a12 12 0 0 1 12 12v12H20z" fill="#EFECE6"/>'
    o+=f'<circle cx="38" cy="34" r="4" fill="{ACCENT}"/><circle cx="52" cy="34" r="4" fill="{STROKE}"/><circle cx="66" cy="34" r="4" fill="{STROKE}"/>'
    o+=f'<rect x="86" y="25" width="356" height="18" rx="9" fill="{PANEL}" stroke="{STROKE}"/><text x="98" y="38" fill="{MUTE}" font-size="11">{esc(url)}</text>'
    o+=f'<rect x="20" y="46" width="120" height="234" fill="#FAF8F5"/>'
    o+=f'<rect x="34" y="62" width="92" height="20" rx="10" fill="{ACCENT}" opacity="0.14"/><text x="44" y="76" fill="{ACCENT}" font-size="10" font-weight="600">+ Nouveau chat</text>'
    for i,yy in enumerate((96,112,128,144)): o+=f'<rect x="34" y="{yy}" width="{86-i*6}" height="9" rx="4.5" fill="{BUBBLE}"/>'
    o+=wrap(title,154,60,12,INK,44,weight=600)[0]
    if umsg:
        um,nn=wrap(umsg,300,88,10,INK,30,lh=13,anchor="end")
        o+=f'<rect x="196" y="76" width="250" height="{12+nn*13}" rx="8" fill="{BUBBLE}"/>'+um; yb=76+12+nn*13+12
    else: yb=88
    for ln in blines:
        bl,nn=wrap(ln,158,yb+13,10,SUB,44,lh=13)
        o+=f'<rect x="154" y="{yb}" width="286" height="{12+nn*13}" rx="7" fill="{SOFT}"/>'+bl; yb+=12+nn*13+8
    o+=f'<rect x="154" y="212" width="118" height="18" rx="9" fill="{PANEL}" stroke="{STROKE}"/><circle cx="166" cy="221" r="3" fill="{ACCENT}"/><text x="176" y="225" fill="{MUTE}" font-size="10">{esc(model)}</text>'
    o+=f'<rect x="154" y="240" width="292" height="30" rx="15" fill="{PANEL}" stroke="{STROKE}"/><text x="168" y="259" fill="{MUTE}" font-size="11">{esc(ph)}</text>'
    o+=f'<circle cx="430" cy="255" r="9" fill="{ACCENT}"/><path d="M430 251v8 M426 255l4-4 4 4" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    return o

def f_desktop(title,badge,blines,foot=""):
    o=f'<rect x="28" y="30" width="424" height="240" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
    o+=f'<path d="M28 42a12 12 0 0 1 12-12h400a12 12 0 0 1 12 12v10H28z" fill="#EFECE6"/>'
    o+=f'<circle cx="44" cy="41" r="4" fill="{ACCENT}"/><circle cx="58" cy="41" r="4" fill="{STROKE}"/><circle cx="72" cy="41" r="4" fill="{STROKE}"/>'
    o+=f'<text x="240" y="45" fill="{MUTE}" font-size="10" text-anchor="middle">Claude — Desktop</text>'
    o+=wrap(title,48,76,13,INK,54,weight=600)[0]; yb=92
    if badge:
        bw=12+len(badge)*6.4
        o+=f'<rect x="48" y="{yb}" width="{bw:.0f}" height="18" rx="9" fill="{ACCENT}" opacity="0.14"/><text x="{48+bw/2:.0f}" y="{yb+13}" fill="{ACCENT}" font-size="10" font-weight="600" text-anchor="middle">{esc(badge)}</text>'
        yb+=28
    for ln in blines:
        bl,nn=wrap(ln,52,yb+14,11,SUB,58,lh=14)
        o+=f'<rect x="44" y="{yb}" width="392" height="{12+nn*14}" rx="8" fill="{SOFT}"/>'+bl; yb+=12+nn*14+8
    if foot: o+=f'<text x="48" y="260" fill="{MUTE}" font-size="10">{esc(foot)}</text>'
    return o

def f_terminal(title,cwd,cmd,olines):
    o=f'<rect x="26" y="30" width="428" height="240" rx="12" fill="{INK}"/>'
    o+=f'<path d="M26 42a12 12 0 0 1 12-12h404a12 12 0 0 1 12 12v10H26z" fill="#3A3630"/>'
    o+=f'<circle cx="42" cy="41" r="4" fill="{ACCENT}"/><circle cx="56" cy="41" r="4" fill="#5B554D"/><circle cx="70" cy="41" r="4" fill="#5B554D"/>'
    o+=f'<text x="240" y="45" fill="{MUTE}" font-size="10" text-anchor="middle" {MONO}>{esc(cwd)}</text>'
    o+=wrap(title,44,74,12,"#E7E2DA",58,weight=600)[0]
    o+=f'<text x="44" y="100" fill="{ACCENT}" font-size="11" {MONO}>$ <tspan fill="#E7E2DA">{esc(cmd)}</tspan></text>'
    yy=120
    for ln in olines:
        ol,nn=wrap(ln,44,yy,10,"#B7B0A6",64,lh=13,family=MONO); o+=ol; yy+=nn*13+5
    o+=f'<text x="44" y="252" fill="{ACCENT}" font-size="11" {MONO}>$ <tspan fill="#E7E2DA">▍</tspan></text>'
    return o

def f_panel(title,rows,tg="",note=""):
    o=f'<rect x="24" y="26" width="{W-48}" height="{H-52}" rx="14" fill="{PANEL}" stroke="{STROKE}"/>'
    o+=f'<rect x="24" y="26" width="{W-48}" height="30" rx="14" fill="{SOFT}"/><rect x="24" y="42" width="{W-48}" height="14" fill="{SOFT}"/>'
    o+=wrap(title,40,46,13,INK,52,weight=600)[0]
    if tg: o+=f'<text x="{W-40}" y="46" fill="{MUTE}" font-size="10" text-anchor="end">{esc(tg.upper())}</text>'
    yy=80
    for label,val in rows:
        o+=f'<circle cx="44" cy="{yy-4}" r="3" fill="{ACCENT}"/><text x="56" y="{yy}" fill="{INK}" font-size="12" font-weight="600">{esc(label)}</text>'
        if val:
            vl,nn=wrap(val,56,yy+15,11,MUTE,62,lh=13); o+=vl; yy+=15+nn*13+10
        else: yy+=24
    if note: o+=f'<text x="40" y="{H-34}" fill="{MUTE}" font-size="10">{esc(note)}</text>'
    return o

def f_toggle(title,a,b,active,da,db):
    o=f'<rect x="24" y="26" width="{W-48}" height="{H-52}" rx="14" fill="{PANEL}" stroke="{STROKE}"/>'
    o+=wrap(title,40,54,15,INK,44,weight=700)[0]
    o+=f'<rect x="40" y="68" width="236" height="30" rx="15" fill="{SOFT}" stroke="{STROKE}"/>'
    ax=44 if active==0 else 160
    o+=f'<rect x="{ax}" y="72" width="112" height="22" rx="11" fill="{ACCENT}"/>'
    o+=f'<text x="100" y="87" fill="{"#fff" if active==0 else MUTE}" font-size="11" font-weight="600" text-anchor="middle">{esc(a)}</text>'
    o+=f'<text x="216" y="87" fill="{"#fff" if active==1 else MUTE}" font-size="11" font-weight="600" text-anchor="middle">{esc(b)}</text>'
    o+=f'<text x="40" y="128" fill="{ACCENT}" font-size="11" font-weight="700">{esc(a)}</text>'
    o+=wrap(da,40,146,12,INK,58,lh=15)[0]
    o+=f'<text x="40" y="202" fill="{ACCENT}" font-size="11" font-weight="700">{esc(b)}</text>'
    o+=wrap(db,40,220,12,INK,58,lh=15)[0]
    return o

def f_steps(eb,title,items):
    o=eyebrow(eb)+wrap(title,38,60,22,INK,28,weight=700)[0]; yy=98
    for i,s in enumerate(items,1):
        o+=f'<circle cx="52" cy="{yy}" r="13" fill="{ACCENT}"/><text x="52" y="{yy+4}" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">{i}</text>'
        sl,nn=wrap(s,76,yy+4,12,INK,54,lh=14); o+=sl; yy+=max(36,nn*14+20)
    return o

# ---- writer ----
def write_all(OUT, SPEC, index_preamble):
    """Write every (anchor, filename, fragment) in SPEC as an SVG in OUT, plus INDEX.md."""
    os.makedirs(OUT, exist_ok=True)
    seen=set(); rows=[]
    for anchor,fname,frag in SPEC:
        assert anchor not in seen, f"dup anchor {anchor}"
        seen.add(anchor)
        with open(os.path.join(OUT,fname),"w",encoding="utf-8") as fh:
            fh.write(svg(frag))
        rows.append((anchor,fname))
    print(f"wrote {len(rows)} svg -> {OUT}")
    idx=list(index_preamble)
    for a,f in rows: idx.append(f"| `{a}` | {f} |")
    with open(os.path.join(OUT,"INDEX.md"),"w",encoding="utf-8") as fh:
        fh.write("\n".join(idx)+"\n")
    print(f"wrote INDEX.md ({len(rows)} rows)")
