#!/usr/bin/env python3
# Flat-vector SVG set for the Xmind sheet "TM_Claude  Atelier#01 Decouverte" (owA1I1tG / bd65bfcf).
# One image per node, shared palette + primitives so the whole deck reads as one system.
import os, html, textwrap

# Output = the folder this script lives in (so it runs from a fresh clone anywhere).
OUT = os.path.dirname(os.path.abspath(__file__))
PFX = "TM_Claude_Atelier01_Decouverte"
RAWBASE = "https://raw.githubusercontent.com/bulle-it/public-assets/main/trainings/TM_Claude_Atelier01_Decouverte"

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

# ---- primitives ----
def f_cover():
    return f'''
    <text x="40" y="82" fill="{MUTE}" font-size="14" letter-spacing="3">ATELIER #01</text>
    <text x="38" y="134" fill="{INK}" font-size="46" font-weight="700">Découverte</text>
    <text x="40" y="166" fill="{SUB}" font-size="17">Claude — prise en main en 1 heure</text>
    <g transform="translate(40,200)">
      <rect x="0" y="0" width="96" height="64" rx="10" fill="{PANEL}" stroke="{STROKE}"/><rect x="0" y="0" width="96" height="16" rx="10" fill="{BUBBLE}"/><circle cx="10" cy="8" r="2.5" fill="{ACCENT}"/>
      <rect x="14" y="28" width="56" height="6" rx="3" fill="{BUBBLE}"/><rect x="14" y="40" width="42" height="6" rx="3" fill="{BUBBLE}"/><text x="48" y="82" fill="{MUTE}" font-size="11" text-anchor="middle">web</text>
      <rect x="116" y="0" width="96" height="64" rx="10" fill="{PANEL}" stroke="{STROKE}"/><rect x="130" y="12" width="68" height="40" rx="6" fill="{BUBBLE}"/><text x="164" y="82" fill="{MUTE}" font-size="11" text-anchor="middle">Desktop</text>
      <rect x="232" y="0" width="96" height="64" rx="10" fill="{PANEL}" stroke="{STROKE}"/><circle cx="264" cy="32" r="12" fill="{ACCENT}" opacity="0.18"/><circle cx="292" cy="32" r="12" fill="{ACCENT}" opacity="0.18"/><path d="M270 32h16" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/><text x="280" y="82" fill="{MUTE}" font-size="11" text-anchor="middle">Cowork</text>
      <rect x="348" y="0" width="96" height="64" rx="10" fill="{INK}"/><text x="362" y="28" fill="{ACCENT}" font-size="13" {MONO}>&gt;_</text><rect x="362" y="36" width="48" height="5" rx="2.5" fill="#5B554D"/><rect x="362" y="46" width="30" height="5" rx="2.5" fill="#5B554D"/><text x="396" y="82" fill="{MUTE}" font-size="11" text-anchor="middle">Code</text>
    </g>'''

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

def f_pricing():
    o=eyebrow("Section 2")+wrap("Les offres",38,60,22,INK,20,weight=700)[0]
    tw=(W-80-3*12)/4
    for i,(n,d,p) in enumerate([("Free","découverte","0 $"),("Pro","+ Claude Code","~20 $/m"),("Team / Max","volume, partage","plus"),("API","à l'usage","jetons")]):
        x=40+i*(tw+12)
        o+=f'<rect x="{x:.0f}" y="92" width="{tw:.0f}" height="152" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
        if i==1: o+=f'<rect x="{x:.0f}" y="92" width="{tw:.0f}" height="6" rx="6" fill="{ACCENT}"/>'
        o+=wrap(n,x+tw/2,120,12,INK,13,weight=700,anchor="middle")[0]
        o+=wrap(p,x+tw/2,142,10,ACCENT,14,weight=600,anchor="middle")[0]
        o+=wrap(d,x+tw/2,170,9.5,MUTE,16,lh=12,anchor="middle")[0]
    return o

# ---- node table: (anchor, filename-suffix, fragment) ----
SPEC=[]
def add(a,name,frag): SPEC.append((a,f"{PFX}_{name}.svg",frag))

add("2515227d-6c38-4e68-9270-6493d412f1eb","00_cover",f_cover())

# 01
add("e1ad8f46-f812-4c21-9d32-06094d09a422","01_quest-ce-que-cest",
    f_section("Section 1","Qu'est-ce que c'est ?","Un assistant IA qui comprend, rédige, résume, analyse, code et raisonne.",
              motif_tiles([("comprendre","brain"),("rédiger","doc"),("analyser","search"),("coder","term")])))
add("701f2453-4e5b-4383-be5b-2b51a8505c11","01_def-histoire",f_card("Définition & histoire","D'où vient Claude, et ce que « IA » veut dire ici.","book","Section 1"))
add("797e564e-714d-48c7-89c8-4fd27ee678e8","01_claude-le-cerveau",f_card("Claude = l'IA, le « cerveau »","Créé par Anthropic. Un grand modèle de langage (LLM), comme GPT (OpenAI) ou Gemini (Google).","brain","Section 1"))
add("ffee0dd6-9aae-4969-a1b4-3e50a954998a","01_versions-du-modele",
    f_panel("Choisir le modèle",[("Haiku","le plus rapide, tâches simples"),("Sonnet","par défaut, efficace au quotidien"),("Opus","tâches complexes, raisonnement long")],"Section 1","Menu déroulant, en haut de la conversation"))
add("b2ef3988-d652-4a5e-9c6c-335fb48811f8","01_claude-ai-cest-quoi",
    f_section("Section 1","« Claude AI » = claude.ai","Le site web où l'on parle à Claude dans un navigateur. C'est « Claude web ».",
              motif_tiles([("le cerveau","brain"),("claude.ai","globe"),("= 1 porte","chat")])))
add("9add6861-853a-4f78-a0bd-1e7f36134ed8","01_portes-dentree",
    f_section("Section 1","Un cerveau, plusieurs portes","Le même Claude : navigateur, app Desktop, app mobile, terminal (Code), API.",
              motif_tiles([("web","globe"),("Desktop","device"),("mobile","device"),("Code","term"),("API","plug")])))
add("81c99d03-a94c-40ed-9bdc-45afdabfac68","01_un-seul-compte",f_card("Un seul compte","Conversations et Projects synchronisés entre claude.ai, Desktop et mobile.","sync","Section 1"))
add("fbbe731c-abab-48b2-8488-ab41173d0696","01_ce-que-ca-fait",f_card("Ce que ça fait","Comprend, rédige, résume, analyse, code, raisonne.","spark","Section 1"))
add("6aeeedbc-08ad-4e8d-b1f9-ab744b3d33cf","01_multimodal",
    f_section("Section 1","Multimodal","En entrée : texte, image, PDF, tableur, capture d'écran.",
              motif_tiles([("texte","doc"),("image","image"),("PDF","doc"),("tableur","table"),("capture","camera")])))
add("1d0a17ef-9bc3-413a-82a0-946a069ed77f","01_ce-que-ce-nest-pas",f_card("Ce que ce n'est pas","Ni un moteur de recherche, ni infaillible. On vérifie les faits et les chiffres.","warn","Section 1"))

# 02
add("051da947-22fd-41a6-bb26-d606791f8cdd","02_combien-ca-coute",f_pricing())
add("0b50d611-1e2a-41c4-997f-c39c2aabcbf7","02_free",f_card("Free","Usage limité. Pour découvrir.","euro","Section 2"))
add("cc61fd37-c5d7-40fa-a920-abdb2dc6c36d","02_pro",f_card("Pro — ~20 $/mois","Usage confortable. Claude Code inclus.","euro","Section 2"))
add("a329655f-e4b8-4be7-8809-8d7835339201","02_max-team-enterprise",f_card("Max / Team / Enterprise","Plus de volume, partage d'équipe, administration.","layers","Section 2"))
add("71b72363-b2c8-4217-9c80-41cae95a733e","02_api",f_card("API","Paiement à l'usage (jetons). Pour intégrer Claude dans des outils.","tokens","Section 2"))

# 03
add("7d120daa-7d45-4121-8e8e-a63f5c5557bc","03_composants",
    f_section("Section 3","Les composants","Quatre portes d'entrée vers le même Claude — de la plus simple à la plus outillée.",
              motif_tiles([("Claude web","globe"),("Desktop","device"),("Cowork","steer"),("Code","term")])))
add("796c52fb-8eb5-4d8b-9596-d999a64d38a2","03_claude-web",
    f_browser("Claude web — navigateur, rien à installer","claude.ai","",["Bonjour ! Comment puis-je aider ?"],"Envoyer un message à Claude…"))
add("ac4b6bf5-8b8c-445e-971b-b0693fe1fd3a","03_claude-web-navigateur",f_card("Navigateur, rien à installer","Le point d'entrée par défaut. Une adresse : claude.ai.","globe","Section 3"))
add("2b3afea8-20ea-4323-9586-29dbe48379ad","03_claude-desktop",
    f_desktop("Claude Desktop","App Mac / Windows",["Tout le web, plus l'accès à ton poste","Connecteurs (Gmail, Drive…) + serveurs MCP","Extensions installables en un clic"]))
add("b3aab6ab-2553-4cbb-807b-b0333d0bd2a0","03_desktop-connecteurs-mcp",f_card("Connecteurs + serveurs MCP","Des outils « branchés » sur Claude : tes services et des capacités locales.","plug","Section 3"))
add("a4271798-738b-462a-af2c-d30ee01542dc","03_cowork",
    f_toggle("Cowork — un mode, pas une app","Chat","Cowork",1,"Tu discutes, tu valides chaque étape.","Tu délègues : Claude planifie et enchaîne seul, sur ton poste (Desktop) ou dans le cloud (web / mobile). Offres payantes."))
add("c437c594-b2ec-4213-87c9-e3bf3d8b9d71","03_cowork-mode-delegation",f_card("Mode délégation","Claude enchaîne seul une tâche en plusieurs étapes. Offres payantes.","steer","Section 3"))
add("fcfa7c44-ba6e-4e31-bf5f-e4d71da3d3e6","03_claude-code",
    f_terminal("Claude Code — agent sur un dossier / projet","~/projets/mon-app","claude",["Lecture du dossier…","J'ai trouvé 3 scripts. Que veux-tu faire ?"]))
add("adcff8c7-f361-4565-9450-311f5099cbde","03_code-terminal-agent",f_card("Terminal — agent sur un projet","Sur un dossier : code, scripts, skills. Il lit, écrit et lance des commandes.","term","Section 3"))
add("3ae6be98-0b35-4345-a0d3-036cf48030fc","03_claude-web-pwa",f_card("PWA installable","Chrome : ⋮ → « Installer la page en tant qu'appli ». 100 % identique au web — aucune capacité locale en plus.","download","Section 3"))

# 03b — Niveaux d'acquisition (added 2026-09-11, correlated to the 4 Composants)
add("46f93ca1-cb00-4099-b821-1a7560a9f7a5","03b_niveaux-acquisition",
    f_section("Niveaux","Niveaux d'acquisition","Quatre niveaux, corrélés aux composants : je discute → je m'équipe → je délègue → je fais construire.",
              motif_tiles([("Niveau 1","chat"),("Niveau 2","plug"),("Niveau 3","steer"),("Niveau 4","term")])))
add("b8695c20-8cfa-4ab4-8ff4-9ce4f1d056a7","03b_niveau1-je-discute",f_card("Niveau 1 — Je discute","Une question, une réponse. Le point d'entrée le plus simple.","chat","Claude web"))
add("72ee2073-786c-416e-bc87-949cea25b59c","03b_niveau1-cas-usage",f_card("Cas d'usage","« Quelle est la RAM 16 Go la moins chère en France ? »","search","Niveau 1"))
add("df0a694b-abea-4e32-80f2-08b67c3bd262","03b_niveau2-je-mequipe",f_card("Niveau 2 — Je m'équipe","Je branche mes fichiers et mes outils.","plug","Claude Desktop"))
add("8cc579fc-a908-47c1-93a6-b4fea93416d4","03b_niveau2-cas-usage",f_card("Cas d'usage","Résumer un PDF local et préparer un mail via le connecteur Gmail","mail","Niveau 2"))
add("c4ee4e99-601e-4aa8-b2c0-872dc3d5cee0","03b_niveau3-je-delegue",f_card("Niveau 3 — Je délègue","Je décris un résultat, Claude enchaîne seul.","steer","Cowork"))
add("4806318d-a5cf-47ec-a433-7fbda1f775ca","03b_niveau3-cas-usage",f_card("Cas d'usage","« Prends ces 10 factures PDF et fais-moi un tableau Excel récapitulatif »","table","Niveau 3"))
add("73441ae0-9d29-41f5-9176-5765eeddf3b9","03b_niveau4-je-fais-construire",f_card("Niveau 4 — Je fais construire","Sur un projet complet, en autonomie.","term","Claude Code"))
add("a057ed4f-99ff-45c1-b16b-9260b169b221","03b_niveau4-cas-usage",f_card("Cas d'usage","« Écris-moi un script qui renomme mes photos par date de prise de vue »","gear","Niveau 4"))

# 04
add("6a18ddbb-807f-4639-a318-516973256dfe","04_bonnes-pratiques",
    f_section("Section 4","Bonnes pratiques & limites","Donner le contexte, itérer par petits pas, vérifier, choisir ce qu'on partage.",
              motif_tiles([("contexte","target"),("itérer","sync"),("vérifier","shield"),("web ?","globe")])))
add("f3b82972-3004-4c23-91c1-7f094491069a","04_donner-le-contexte",f_card("Donner le contexte","Rôle, objectif, format, audience. Puis itérer par petits pas.","target","Section 4"))
add("63888b66-6b72-4a13-a517-d12fe23cb142","04_verifier-et-partager",f_card("Vérifier & choisir ce qu'on partage","Contrôler les faits et chiffres importants. Décider des données sensibles.","shield","Section 4"))
add("dc09c5cc-3ead-4ded-a219-60be1b644a82","04_acces-web",
    f_panel("Accès web",[("Par défaut","Claude répond de mémoire (date de coupure)"),("Recherche web","seulement si l'outil est disponible"),("claude.ai","à activer"),("Claude Code","déjà actif")],"Section 4"))

# 05
add("d4e20782-b84c-41cf-8229-e16b82d3b856","05_comment-cest-organise",
    f_section("Section 5","Comment c'est organisé","Conversation, mémoire, Project, Artifacts, connecteurs, compte unique.",
              motif_tiles([("conversation","chat"),("mémoire","memory"),("Project","folder"),("Artifacts","grid")])))
add("20301de5-e896-4bf9-85e3-eb68ed78a8c1","05_conversation",f_card("Conversation","L'unité de base. Nouveau sujet = nouvelle conversation.","chat","Section 5"))
add("4539766f-2cc1-46c6-bbcd-b68d0cc8a8d1","05_la-memoire",f_card("La mémoire","Claude peut se souvenir d'infos utiles d'une conversation à l'autre.","memory","Section 5"))
add("e23862f1-fbf4-442f-a24d-1b2c2a7c5c6d","05_memoire-beta",f_card("En béta (09/26)","Fonction récente, encore en évolution.","clock","Section 5"))
add("9952e9c7-5e15-4678-a227-93deb35458bc","05_project",
    f_panel("Project",[("Instructions permanentes","valables pour toutes ses conversations"),("Fichiers de référence","joints une fois, réutilisés"),("Conversations regroupées","au même endroit")],"Section 5"))
add("6f3b1e3f-6540-4716-b880-a1ac43261f6e","05_artifacts",
    f_desktop("Artifacts","à côté du chat",["Documents, tableaux, mini-apps générés par Claude","Éditables et réutilisables","S'ouvrent dans un panneau à côté de la conversation"]))
add("af4495f6-37b2-4ccc-ae53-2fdcfa683d60","05_connecteurs",
    f_section("Section 5","Connecteurs","Gmail, Drive, Calendar… Claude lit tes vraies données, avec ton accord.",
              motif_tiles([("Gmail","mail"),("Drive","folder"),("Calendar","clock"),("ton accord","shield")])))
add("692c89ad-7d71-4a6d-9602-eb101a7c7ade","05_compte-unique",f_card("Compte unique","Historique synchronisé entre web, desktop et mobile.","device","Section 5"))

# 06
add("b26fc04c-5f00-4c94-97e6-c883f1a0605d","06_exemples",
    f_section("Section 6","Exemples — démo live","Une démo par composant, puis la règle simple : Chat ou Cowork ?",
              motif_tiles([("web","globe"),("Desktop","device"),("Cowork","steer"),("Code","term")])))
# 06 · Claude web
add("a70392cc-37c9-433a-a525-c2c65deecbab","06_web",
    f_browser("Démo — Claude web","claude.ai","Quelle est la barrette de RAM 16 Go la moins chère en France ?",
              ["Je lance une recherche web…","3 offres trouvées — sources citées"],"Envoyer un message à Claude…"))
add("a6ad80b5-1fa2-42e7-9cbd-221531096146","06_web_demo",f_card("Démo","« Quelle est la barrette de RAM 16 Go la moins chère en France ? »","search","Claude web"))
add("57c9aa7c-04dd-4dbe-9829-0448a833f241","06_web_complement",f_card("Complément d'infos","Ce qu'il faut retenir sur Claude web.","list","Claude web"))
add("8dc1a785-c3cc-494f-ab23-a16426792d2d","06_web_c1",f_card("Dans le navigateur (claude.ai)","Rien à installer.","globe","Claude web"))
add("2e943f42-4001-42b7-a3d0-31afe4507bdf","06_web_c2",f_card("Claude ne voit que ce que tu écris ou joins","Pas les fichiers de ton PC.","eye","Claude web"))
add("5f18be98-6b21-43f6-93da-db841b1d0c15","06_web_c3",f_card("Info récente","Il lance une recherche web et cite ses sources.","search","Claude web"))
# 06 · Claude Desktop
add("71074e90-2572-4a34-89b1-a5e48626f9b6","06_desktop",
    f_desktop("Démo — Claude Desktop","PDF local + connecteur Gmail",["« Résume ce PDF et prépare un mail pour l'envoyer à mon ami »","Claude lit le fichier sur ton poste","Il prépare le brouillon dans Gmail"]))
add("37d9e46a-cb8d-4b94-9871-a695d4b4cc41","06_desktop_demo",f_card("Démo","« Résume ce PDF et prépare un mail pour l'envoyer à mon ami » (PDF local + connecteur Gmail)","mail","Claude Desktop"))
add("86cf6960-1a6c-429b-b2e8-37063118e40e","06_desktop_complement",f_card("Complément d'infos","Ce qu'il faut retenir sur Claude Desktop.","list","Claude Desktop"))
add("e6fb8428-6b4a-4d11-bfea-5ffea52dc41b","06_desktop_c1",f_card("L'app installée sur ton ordinateur","Tout le web + l'accès à ton poste.","device","Claude Desktop"))
add("7f68c2fd-a1ae-48a0-9d14-6d3a1248463c","06_desktop_c2",f_card("Mode Chat","Tu discutes : une demande, une réponse, tu valides chaque étape.","chat","Claude Desktop"))
add("f19bee01-0f1f-4d31-93fa-c3a4c1325379","06_desktop_c3",f_card("Fichiers et outils branchés","Connecteurs, extensions — quand tu le lui demandes.","plug","Claude Desktop"))
# 06 · Cowork
add("bca59db6-5680-4e10-acf8-9135e36197ca","06_cowork",
    f_desktop("Démo — Cowork","mode Cowork",["« Prends les 10 factures PDF de ce dossier…","…et fais-moi un tableau Excel récapitulatif »","Claude planifie, enchaîne, te rend le fichier"]))
add("ff2b114e-270b-440a-a93a-8fd5ee98547e","06_cowork_demo",f_card("Démo","« Prends les 10 factures PDF de ce dossier et fais-moi un tableau Excel récapitulatif »","table","Cowork"))
add("832ac009-22e4-44ac-babb-97c63b71eb7a","06_cowork_complement",f_card("Complément d'infos","Ce qu'il faut retenir sur Cowork.","list","Cowork"))
add("e6c4a15d-6d79-4e6b-b164-f80d86287104","06_cowork_c1",f_card("Mode Cowork","Tu délègues : tu décris le résultat, Claude planifie et enchaîne les étapes seul.","steer","Cowork"))
add("10c9169e-1f1f-48b4-afdf-1866d791ca80","06_cowork_c2",f_card("Il travaille dans les dossiers que tu ouvres","Et te rend un travail fini : fichiers, documents, tableaux.","folder","Cowork"))
add("5183df5c-9549-425c-b830-969d1226ad75","06_cowork_c3",f_card("Tu gardes la main","Tu suis l'avancement, tu peux reprendre. Il demande avant de supprimer un fichier.","shield","Cowork"))
add("1dff4854-b7f5-4cad-85b8-9c1ac330bfe0","06_cowork_c4",f_card("Même app que Desktop","On bascule entre « Chat » et « Cowork » dans la zone de message. Offres payantes.","split","Cowork"))
# 06 · Claude Code
add("122f5849-55e4-413c-8501-a7c25fcf744f","06_code",
    f_terminal("Démo — Claude Code","~/photos","claude \"renomme mes photos par date de prise de vue\"",["Lecture des métadonnées EXIF…","42 fichiers renommés : 2026-08-14_0001.jpg …"]))
add("feca23d8-af57-4502-a195-bbbf2fe14293","06_code_demo",f_card("Démo","« Écris-moi un petit script qui renomme mes photos par date de prise de vue »","term","Claude Code"))
add("98f204ff-122c-4ca0-8066-a9608bcef6a2","06_code_complement",f_card("Complément d'infos","Ce qu'il faut retenir sur Claude Code.","list","Claude Code"))
add("754b2796-32fd-4d0e-a0f7-474143a061ac","06_code_c1",f_card("Dans un terminal ou VS Code","Sur un dossier de projet.","term","Claude Code"))
add("43b2596f-bf85-4ec1-a701-a709c810e457","06_code_c2",f_card("Il lit, écrit et lance des commandes","Pour construire ou corriger du code.","gear","Claude Code"))
add("181ae8fd-33bb-4568-aeb7-a41ee1710545","06_code_c3",f_card("Même moteur que Cowork","Mais pour le code et l'automatisation.","term","Claude Code"))
# 06 · règle
add("46a9d4d6-d41a-4307-996d-cdc8b900b6b6","06_chat-ou-cowork",
    f_toggle("Chat ou Cowork ? La règle simple","Chat","Cowork",0,"Je discute — une question, une réponse, je garde la main.","Je délègue — je décris le résultat, Claude fait le travail et me le rend."))
add("5eb50560-7af5-4d47-9b90-ca301fef9285","06_regle-chat",f_card("Chat : je discute","Une question, une réponse. Je garde la main.","chat","Règle"))
add("f0d01b19-8a99-4eb4-8e63-2ea43d549740","06_regle-cowork",f_card("Cowork : je délègue","Je décris le résultat, Claude fait le travail et me le rend.","steer","Règle"))

# 07
add("8befcad7-b338-49c6-8cc1-86ddddd3377f","07_on-se-lance",
    f_steps("Section 7","On se lance",["Ouvrir claude.ai et se connecter","Poser une vraie question de son travail","Joindre un fichier, itérer","Ranger la conversation dans un Project"]))

# 08
add("20bb6ede-fb83-4455-8f62-90ee98046498","08_deploiement",
    f_section("Section 8","Déploiement","Installer l'app, puis la configurer : les menus, un par un.",
              motif_tiles([("installer","download"),("configurer","gear")])))
add("6f42de58-8611-401d-a423-bdd93cd63fe3","08_installation",
    f_desktop("Installation","télécharger l'app",["claude.ai/download — Mac ou Windows","Installer, se connecter à son compte","Accepter les autorisations demandées"]))
add("1b0bc325-7475-4166-9088-635d02ba88a9","08_installation_menus",
    f_panel("Installation — les menus",[("Téléchargement","Mac (Apple Silicon / Intel) · Windows"),("Première ouverture","connexion au compte"),("Autorisations","accès dossiers, notifications")],"Section 8"))
add("8c94d810-2cea-48b7-b591-d7502bbc4f18","08_configuration",
    f_panel("Configuration",[("Compte","modèle par défaut, langue"),("Connecteurs","Gmail, Drive, Calendar…"),("Extensions / MCP","outils locaux"),("Confidentialité","données, historique")],"Section 8"))
add("e26a0d54-6faf-45bc-b601-1092b4e1aa34","08_configuration_menus",
    f_panel("Configuration — les menus",[("Général","modèle, langue, thème"),("Connecteurs","ajouter / retirer un service"),("Extensions","serveurs MCP, un clic"),("Confidentialité","historique, mémoire, partage")],"Section 8"))

# ---- write ----
os.makedirs(OUT, exist_ok=True)
seen=set(); rows=[]
for anchor,fname,frag in SPEC:
    assert anchor not in seen, f"dup anchor {anchor}"
    seen.add(anchor)
    with open(os.path.join(OUT,fname),"w",encoding="utf-8") as fh:
        fh.write(svg(frag))
    rows.append((anchor,fname))
print(f"wrote {len(rows)} svg -> {OUT}")

idx=["# TM_Claude Atelier#01 Découverte — visual assets","",
 "Flat-vector SVGs for Xmind sheet `bd65bfcf-ba51-4d40-843f-77e418699458` (file `owA1I1tG`).","",
 "Naming: `TM_Claude_Atelier01_Decouverte_<NN>_<branche>[_<sous>].svg` — NN = top-level order",
 "(00 cover, 01–08 sections). Slugs: ASCII, lowercase, hyphens, no accents/`#`/spaces.","",
 f"Raw base: `{RAWBASE}/`","",
 "| Xmind node id | file |","|---|---|"]
for a,f in rows: idx.append(f"| `{a}` | {f} |")
with open(os.path.join(OUT,"INDEX.md"),"w",encoding="utf-8") as fh:
    fh.write("\n".join(idx)+"\n")
print(f"wrote INDEX.md ({len(rows)} rows)")
