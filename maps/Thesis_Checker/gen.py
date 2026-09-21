#!/usr/bin/env python3
# Flat-vector SVG set for the Xmind sheet "Your thesis checker" (file mKRiB2a3, sheet 34ea33d4-...).
# One image on the centre topic and one per top-level branch.
# Palette and primitives: ../../lib/flatvec.py — shared with every image set in this repo.
# Public repo: no personal names or project data in the images, only generic wording.
import os, sys

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT, os.pardir, os.pardir, "lib"))
from flatvec import *  # noqa: F401,F403

PFX = "Thesis_Checker"
RAWBASE = "https://raw.githubusercontent.com/bulle-it/public-assets/main/maps/Thesis_Checker"

def head(eb, title):
    return eyebrow(eb) + wrap(title, 38, 76, 22, INK, 32, weight=700)[0]

FOUR = [("Layout", "table"), ("Language", "chat"), ("Originality", "search"), ("Machine text", "brain")]

# ---- builders ----
def steps2(eb, title, items):
    o = eyebrow(eb) + wrap(title, 38, 76, 22, INK, 28, weight=700)[0]; yy = 116
    for i, t in enumerate(items, 1):
        o += f'<circle cx="52" cy="{yy}" r="13" fill="{ACCENT}"/><text x="52" y="{yy+4}" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">{i}</text>'
        tl, nn = wrap(t, 76, yy+4, 12, INK, 54, lh=14); o += tl; yy += max(34, nn*14+20)
    return o

def f_root():
    return f_section("Thesis checker", "Your thesis checker",
                     "A careful second reader: layout, language, originality and a machine-text signal. It suggests and never rewrites.",
                     motif_tiles(FOUR))

def f_what():
    return f_card("A careful second reader",
                  "It checks four things and gives you suggestions. It never rewrites your text and never touches your original.",
                  "eye", "suggestions only")

def f_run():
    return steps2("How a run goes", "From your file to your inbox", [
        "You drop a Word file on Drive",
        "Christophe starts the checker",
        "The checks run on a copy of your file",
        "A commented copy and a report land on Drive",
        "You receive two links by email, no attachments"])

def f_checks():
    return f_section("Four checks", "Four checks, one report",
                     "Each check reports what it finds as comments and in a short report. Nothing in your text is changed.",
                     motif_tiles(FOUR))

def f_examples():
    return f_panel("Examples of comments", [
        ("Layout", "Page 3: the left margin is 1.25 inch, MLA asks for 1 inch"),
        ("Language", "it's should be its, from a real test"),
        ("Originality", "Chapter 2 paragraph 4 is close to a source you supplied"),
        ("Machine text", "Paragraph 4 reads closer to machine text than your usual style: please check"),
    ], tg="examples", note="Only the language line is from a real test; the others use invented numbers.")

def f_privacy():
    o = head("Privacy", "Where your text goes")
    tiles = [("Your files", "stay on Drive and on one computer", "folder"),
             ("His computer", "does the checks on a copy", "device"),
             ("Claude", "sees short flagged passages only", "chat")]
    xs = [30, 181, 332]
    for (lab, sub, g), x in zip(tiles, xs):
        o += f'<rect x="{x}" y="104" width="118" height="128" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
        o += gl(g, x + 45, 120, 1.0)
        o += wrap(lab, x + 59, 176, 12, INK, 14, lh=14, weight=700, anchor="middle")[0]
        o += wrap(sub, x + 59, 194, 10, SUB, 20, lh=12, anchor="middle")[0]
    for x in (150, 301):
        o += f'<path d="M{x} 168h26" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>'
        o += f'<path d="M{x+19} 160l8 8-8 8" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    o += f'<text x="240" y="264" fill="{SUB}" font-size="12" text-anchor="middle">Nothing is published</text>'
    return o

def f_limits():
    return f_card("Suggests, never decides",
                  "It will not rewrite your text, prove that a passage is machine-written, search the whole internet or replace the official check at submission.",
                  "shield", "limits")

def f_part():
    return steps2("Your part", "Four small things", [
        "Keep using Zotero: nothing changes",
        "Ask which MLA edition applies",
        "Name the sources to compare",
        "Share texts you wrote yourself"])

# ---- node table: (xmind topic id, filename-suffix, fragment) ----
SPEC = []
def add(a, name, frag): SPEC.append((a, f"{PFX}_{name}.svg", frag))

add("e95dc20a-cb7a-480b-b2cc-9bcde2b6073e", "00_root", f_root())
add("cf484c1e-713b-459b-a51f-2b78d00b2289", "01_what-it-does", f_what())
add("3f2e3ba3-c9b1-4314-98e9-6e1bd09174d6", "02_how-a-run-goes", f_run())
add("fe559697-31e6-4280-b991-5e777226468c", "03_four-checks", f_checks())
add("7dc683a0-28c3-470b-a5c0-1e2ce5efc442", "04_examples", f_examples())
add("eb544a1d-92a2-4cad-89b2-2310d6ffe50d", "05_where-your-text-goes", f_privacy())
add("39fb73ff-97d1-4def-b254-255a023f9dcb", "06_what-it-will-not-do", f_limits())
add("d78359bc-ee54-4d7c-8970-a0c794039af0", "07_what-we-need-from-you", f_part())

write_all(OUT, SPEC, [
 "# Thesis checker — visual assets", "",
 "Flat-vector SVGs for the Xmind sheet \"Your thesis checker\" (file `mKRiB2a3`): one on the centre topic, one per top-level branch.", "",
 "Naming: `Thesis_Checker_<NN>_<branch-slug>.svg` — 00 = centre, then branch order.", "",
 f"Raw base: `{RAWBASE}/`", "",
 "| Xmind node id | file |", "|---|---|"])
