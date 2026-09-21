#!/usr/bin/env python3
# Flat-vector SVG set for the Xmind sheet "Originality: free options" (file mKRiB2a3, sheet 3997fca9-...).
# One image per top-level branch. Palette and primitives: ../../lib/flatvec.py (shared).
# Public repo: no personal names and no project data, only generic wording.
import os, sys
OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT, os.pardir, os.pardir, "lib"))
from flatvec import *  # noqa: F401,F403
PFX = "Originality_Options"
RAWBASE = "https://raw.githubusercontent.com/bulle-it/public-assets/main/maps/Originality_Options"

def head(eb, title): return eyebrow(eb) + wrap(title, 38, 76, 22, INK, 32, weight=700)[0]

def steps2(eb, title, items):
    o = eyebrow(eb) + wrap(title, 38, 76, 22, INK, 28, weight=700)[0]; yy = 116
    for i, t in enumerate(items, 1):
        o += f'<circle cx="52" cy="{yy}" r="13" fill="{ACCENT}"/><text x="52" y="{yy+4}" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">{i}</text>'
        tl, nn = wrap(t, 76, yy+4, 12, INK, 54, lh=14); o += tl; yy += max(34, nn*14+20)
    return o

def chips(x, y, w, items, hot=None):
    o = ""
    for i, t in enumerate(items):
        yy = y + i*34; fill = ACCENT if i == hot else PANEL; col = "#fff" if i == hot else INK
        o += f'<rect x="{x}" y="{yy}" width="{w}" height="26" rx="8" fill="{fill}" stroke="{STROKE}"/>'
        o += f'<text x="{x+w/2}" y="{yy+17}" fill="{col}" font-size="11" font-weight="600" text-anchor="middle">{esc(t)}</text>'
    return o

def f_turnitin():
    o = head("Turnitin and us", "What they see, what we can see")
    for x, lab in ((30, "TURNITIN"), (260, "OUR FREE LAYERS")):
        o += f'<rect x="{x}" y="98" width="190" height="146" rx="12" fill="{SOFT}" stroke="{STROKE}"/>'
        o += f'<text x="{x+14}" y="118" fill="{MUTE}" font-size="10" letter-spacing="1.5">{lab}</text>'
    o += chips(42, 128, 166, ["Web pages", "Journals under licence", "Earlier student papers"], hot=2)
    o += chips(272, 128, 166, ["Her sources and chapters", "Open research papers", "The open web"])
    o += f'<text x="240" y="178" fill="{ACCENT}" font-size="26" font-weight="700" text-anchor="middle">≠</text>'
    o += f'<text x="240" y="270" fill="{SUB}" font-size="11.5" text-anchor="middle">A clean result on our side never means a clean result on theirs</text>'
    return o

def f_layers():
    o = head("Three free layers", "Only short phrases ever leave")
    tiles = [("Her sources", "and chapters, all on this computer", "folder"),
             ("Open papers", "through CORE, short phrases only", "book"),
             ("Open web", "through SearXNG, short phrases only", "globe")]
    for (lab, sub, g), x in zip(tiles, (30, 181, 332)):
        o += f'<rect x="{x}" y="104" width="118" height="128" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
        o += gl(g, x + 45, 120, 1.0)
        o += wrap(lab, x + 59, 176, 12, INK, 14, lh=14, weight=700, anchor="middle")[0]
        o += wrap(sub, x + 59, 194, 10, SUB, 18, lh=12, anchor="middle")[0]
    o += f'<text x="240" y="264" fill="{SUB}" font-size="12" text-anchor="middle">Nothing is uploaded, ever</text>'
    return o

def f_out():
    return f_panel("Ruled out", [
        ("Paid checkers", "the full text would leave, and there is no budget"),
        ("Brave Search API", "its free tier is gone in 2026"),
        ("Google search API", "closed to new users, ends in 2027"),
        ("Claude's search tool", "not an exact-phrase engine"),
    ], tg="and why", note="Zero budget, and nothing is uploaded.")

def f_rules():
    return f_panel("Rules we keep", [
        ("Short phrases only", "about 8 to 12 words, never a file"),
        ("Quotes and Works Cited are left out", ""),
        ("A hit is a lead", "a person reviews it, never a verdict"),
        ("Drive links in the email", "shared with her account only"),
    ], tg="rules")

def f_next():
    return steps2("Next steps", "Five small steps", [
        "SearXNG with Brave Search: built and tested",
        "Test rare passages, not only famous ones",
        "Read Brave's terms on automated use",
        "Check the two canaries in autumn",
        "Register for the free CORE key"])

SPEC = []
def add(a, name, frag): SPEC.append((a, f"{PFX}_{name}.svg", frag))
add("0e28a2fa-0756-42e2-a787-e3205e82abb6", "01_what-turnitin-compares-against", f_turnitin())
add("87ac6576-6354-4741-b1a0-b0fde27340a9", "02_our-three-free-layers", f_layers())
add("3b5dd4f3-8f83-4039-9304-7c80ba20aea5", "03_ruled-out", f_out())
add("6294ba18-baf2-42df-a876-8eceb9dc5bfe", "04_rules-we-keep", f_rules())
add("a87a3c97-3a3a-404b-a4a8-77615a2be904", "05_next-steps", f_next())
write_all(OUT, SPEC, [
 "# Originality without Turnitin — visual assets", "",
 "Flat-vector SVGs for the Xmind sheet \"Originality: free options\" (file `mKRiB2a3`), one per top-level branch.", "",
 "Naming: `Originality_Options_<NN>_<branch-slug>.svg`.", "",
 f"Raw base: `{RAWBASE}/`", "",
 "| Xmind node id | file |", "|---|---|"])
