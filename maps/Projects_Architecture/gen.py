#!/usr/bin/env python3
# Flat-vector SVG set for the Xmind map "Design of 00 and the projects" (AP0rhLDy).
# One image per top-level branch.
# Palette and primitives: ../../lib/flatvec.py — shared with every image set in this repo.
import os, sys

# Output = the folder this script lives in (so it runs from a fresh clone anywhere).
OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT, os.pardir, os.pardir, "lib"))
from flatvec import *  # noqa: F401,F403

PFX = "Projects_Architecture"
RAWBASE = "https://raw.githubusercontent.com/bulle-it/public-assets/main/maps/Projects_Architecture"

def head(eb, title):
    return eyebrow(eb) + wrap(title, 38, 76, 22, INK, 32, weight=700)[0]

# ---- builders ----
def f_copy():
    o = head("Founding principle", "One folder, everything inside")
    def machine(x, label):
        s  = f'<rect x="{x}" y="104" width="150" height="126" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
        s += f'<rect x="{x}" y="104" width="150" height="24" rx="12" fill="{SOFT}"/><rect x="{x}" y="116" width="150" height="12" fill="{SOFT}"/>'
        s += f'<text x="{x+12}" y="121" fill="{MUTE}" font-size="10">{esc(label)}</text>'
        for i, t in enumerate(["CLAUDE.md", "memory/", "commands/", "scripts/"]):
            s += f'<rect x="{x+12}" y="{138+i*22}" width="126" height="17" rx="5" fill="{BUBBLE}"/>'
            s += f'<text x="{x+20}" y="{150+i*22}" fill="{INK}" font-size="9.5" {MONO}>{esc(t)}</text>'
        return s
    o += machine(40, "this machine") + machine(290, "any other machine")
    o += f'<path d="M206 167h62" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>'
    o += f'<path d="M260 159l10 8-10 8" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    o += f'<text x="238" y="152" fill="{ACCENT}" font-size="10" font-weight="700" text-anchor="middle">copy</text>'
    o += f'<text x="240" y="254" fill="{SUB}" font-size="11.5" text-anchor="middle">No skill and no experience stays behind</text>'
    o += f'<text x="240" y="274" fill="{MUTE}" font-size="10" text-anchor="middle">the harness cache is regenerable, the repo is the truth</text>'
    return o

def f_hub():
    o = head("The shared root", "00 serves every project")
    cx, cy = 240, 180
    sats = [(42, 116, "Office_git"), (338, 116, "Accounting_git"),
            (42, 216, "JobSeeking_git"), (338, 216, "Solar, Hosting…")]
    for x, y, _ in sats:
        o += f'<path d="M{cx} {cy} L{x+50} {y+16}" stroke="{STROKE}" stroke-width="2"/>'
    for x, y, lab in sats:
        o += f'<rect x="{x}" y="{y}" width="100" height="32" rx="8" fill="{PANEL}" stroke="{STROKE}"/>'
        o += wrap(lab, x+50, y+20, 10, SUB, 20, anchor="middle")[0]
    o += f'<rect x="{cx-74}" y="{cy-36}" width="148" height="72" rx="12" fill="{ACCENT}"/>'
    o += f'<text x="{cx}" y="{cy-12}" fill="#fff" font-size="13" font-weight="700" text-anchor="middle">00 transverse</text>'
    o += f'<text x="{cx}" y="{cy+6}" fill="#fff" font-size="9.5" text-anchor="middle" opacity="0.92">rules · memory</text>'
    o += f'<text x="{cx}" y="{cy+22}" fill="#fff" font-size="9.5" text-anchor="middle" opacity="0.92">scripts · skills</text>'
    o += f'<text x="240" y="276" fill="{MUTE}" font-size="10" text-anchor="middle">No dashboard of its own — it exists only for the others</text>'
    return o

def f_skeleton():
    rows = [("CLAUDE.md", "read automatically"), ("memory/", "read automatically"),
            ("Context/", "read on demand"), (".claude/commands/", "the skills"),
            ("scripts/", "the automation"), ("Outputs/", "every generated file"),
            ("_Local/", "never pushed")]
    o = head("Every project", "Always the same skeleton")
    o += f'<rect x="36" y="92" width="408" height="186" rx="12" fill="{PANEL}" stroke="{STROKE}"/>'
    o += gl("folder", 52, 104, 0.8)
    o += f'<text x="84" y="120" fill="{INK}" font-size="12" font-weight="700" {MONO}>&lt;projet&gt;_git/</text>'
    y = 144
    for i, (name, note) in enumerate(rows):
        br = "└─" if i == len(rows)-1 else "├─"
        o += f'<text x="60" y="{y}" fill="{STROKE}" font-size="11" {MONO}>{br}</text>'
        o += f'<text x="84" y="{y}" fill="{INK}" font-size="11" {MONO}>{esc(name)}</text>'
        o += f'<text x="424" y="{y}" fill="{MUTE}" font-size="9.5" text-anchor="end">{esc(note)}</text>'
        y += 19
    return o

def f_folders():
    o = head("Today", "The folders that exist")
    items = [("Office", "productivity", "spark"), ("Accounting", "invoices", "euro"),
             ("JobSeeking", "missions", "search"), ("Solar", "home steering", "steer"),
             ("Hosting", "rentals", "globe"), ("Training", "videos", "camera")]
    tw, gap = 128, 14
    x0 = (W - (3*tw + 2*gap)) / 2
    for i, (name, sub, g) in enumerate(items):
        x = x0 + (i % 3) * (tw + gap)
        y = 100 + (i // 3) * 84
        o += f'<rect x="{x:.0f}" y="{y}" width="{tw}" height="72" rx="10" fill="{PANEL}" stroke="{STROKE}"/>'
        o += gl(g, x+14, y+16, 0.8)
        o += f'<text x="{x+48:.0f}" y="{y+30}" fill="{INK}" font-size="12" font-weight="700">{esc(name)}</text>'
        o += f'<text x="{x+14:.0f}" y="{y+58}" fill="{MUTE}" font-size="10">{esc(sub)}</text>'
    o += f'<text x="240" y="280" fill="{MUTE}" font-size="10" text-anchor="middle">Quiz-ClaudeAI sits there too — inactive, no rules of its own</text>'
    return o

def f_inherit():
    o = head("The mechanism", "What is inherited, and how")
    cols = [("CLAUDE.md", "automatic", "The harness reads every one on its way up the tree", "check", False),
            ("memory/", "by symlink", "The harness path points straight into the repo", "sync", False),
            ("skills", "nothing at all", "One symlink per project — a copy drifts silently", "hand", True)]
    tw = (W - 80 - 2*12) / 3
    for i, (name, mode, note, g, warn) in enumerate(cols):
        x = 40 + i * (tw + 12)
        br = ACCENT if warn else STROKE
        o += f'<rect x="{x:.1f}" y="100" width="{tw:.1f}" height="140" rx="10" fill="{PANEL}" stroke="{br}" stroke-width="{2 if warn else 1}"/>'
        o += gl(g, x + tw/2 - 14, 114, 0.9)
        o += wrap(name, x + tw/2, 168, 12.5, INK, 18, weight=700, anchor="middle")[0]
        o += wrap(mode, x + tw/2, 186, 10, ACCENT, 20, weight=600, anchor="middle")[0]
        o += wrap(note, x + tw/2, 208, 9.5, MUTE, 24, lh=12, anchor="middle")[0]
    o += f'<text x="240" y="266" fill="{SUB}" font-size="11" text-anchor="middle">Only the first one travels by itself</text>'
    return o

def f_routing():
    o = head("Routing", "Where does a new rule go")
    o += f'<rect x="150" y="96" width="180" height="30" rx="15" fill="{ACCENT}"/>'
    o += f'<text x="240" y="116" fill="#fff" font-size="11.5" font-weight="700" text-anchor="middle">a new rule or correction</text>'
    boxes = [("00", "how I work, anywhere"), ("the project", "its accounts and data"), ("one owner", "mechanics of one tool")]
    tw = (W - 80 - 2*12) / 3
    for i, (name, note) in enumerate(boxes):
        x = 40 + i * (tw + 12)
        o += f'<path d="M240 126 L{x+tw/2:.1f} 168" stroke="{STROKE}" stroke-width="2"/>'
    for i, (name, note) in enumerate(boxes):
        x = 40 + i * (tw + 12)
        o += f'<rect x="{x:.1f}" y="172" width="{tw:.1f}" height="64" rx="10" fill="{PANEL}" stroke="{STROKE}"/>'
        o += wrap(name, x + tw/2, 198, 12.5, INK, 18, weight=700, anchor="middle")[0]
        o += wrap(note, x + tw/2, 218, 9.5, MUTE, 22, lh=12, anchor="middle")[0]
    o += f'<text x="240" y="266" fill="{SUB}" font-size="11" text-anchor="middle">Genuinely ambiguous, ask — never decide alone</text>'
    return o

def f_rails():
    rows = [("shield", "Every repo private, and gitignore still does the work"),
            ("folder", "Confidential goes to the Local folder, never to Outputs"),
            ("check", "Outputs denied by default, reopened one extension at a time"),
            ("hand", "No memory or skill file written before its text is approved"),
            ("search", "Rename anything, then grep the tree for what points at it")]
    o = head("Safety rails", "What keeps it from leaking")
    y = 108
    for g, t in rows:
        o += f'<rect x="36" y="{y}" width="408" height="32" rx="8" fill="{PANEL}" stroke="{STROKE}"/>'
        o += gl(g, 48, y+6, 0.72)
        o += f'<text x="82" y="{y+21}" fill="{INK}" font-size="11">{esc(t)}</text>'
        y += 36
    return o

# ---- node table: (anchor, filename-suffix, fragment) ----
SPEC = []
def add(a, name, frag): SPEC.append((a, f"{PFX}_{name}.svg", frag))

add("a8a82304-6e1a-4f62-aa9c-23752a178a1a", "01_copy-pasteable-unit", f_copy())
add("ab0a6a34-213b-4f66-a829-9fcc0836f570", "02_shared-root", f_hub())
add("4de898b4-6d22-4eba-bb02-1dbb32a244b0", "03_project-skeleton", f_skeleton())
add("d7eb6ead-6771-4a84-a26c-3a142a6539c6", "04_folders-today", f_folders())
add("e8125d20-12ea-4a59-ae80-0ce29ca5a8bf", "05_what-is-inherited", f_inherit())
add("e5415c6e-99fa-4aa4-afb7-f8f96fb5a360", "06_where-a-rule-goes", f_routing())
add("4d235480-31d4-48d9-9eec-cbe72176f710", "07_safety-rails", f_rails())

write_all(OUT, SPEC, [
 "# Design of 00 and the projects — visual assets", "",
 "Flat-vector SVGs for the Xmind map `AP0rhLDy`, one per top-level branch.", "",
 "Naming: `Projects_Architecture_<NN>_<branch-slug>.svg` — NN = branch order.", "",
 f"Raw base: `{RAWBASE}/`", "",
 "| Xmind node id | file |", "|---|---|"])
