#!/usr/bin/env python3
"""Démos Claude: one content file -> Xmind markdown per sheet, then SVG thumbnails keyed by topic id.

  demos.py md   <content.txt> <outdir>              write <tab>.md (Xmind markdown, marks kept, ::kinds stripped)
  demos.py svg  <content.txt> <idsdir> <svgdir>     read <tab>.ids.md (anchored markdown returned by Xmind),
                                                    pair topics by preorder + title, write SVGs, INDEX.md, items.json
"""
import json, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib")); sys.path.insert(0, os.path.join(HERE, "..", "..", "lib"))  # repo layout: maps/Demos_Claude/gen.py -> ../../lib

# Example prompts shown in the browser mock of each Claude Web demo (keyed by demo title).
WEB_PROMPTS = {
    "La barrette de RAM 16 Go la moins chère en France": "Quelle est la barrette de RAM 16 Go la moins chère en France aujourd'hui ?",
    "Un quiz interactif créé en une phrase": "Crée-moi un quiz de dix questions de culture générale, avec le score à la fin.",
    "Réécrire un e-mail délicat": "Rends ce mail plus diplomate et plus court, sans rien promettre.",
    "Résumer un long document et préparer une réunion": "Résume ce document en dix lignes et propose un ordre du jour.",
    "Un Project pour le quotidien": "Voici mes deux fichiers de référence : utilise-les à chaque réponse.",
}


def f_browser2(fv,title,url,umsg,blines,ph,model="Claude Sonnet"):
    o=f'<rect x="20" y="22" width="440" height="258" rx="12" fill="{fv.PANEL}" stroke="{fv.STROKE}"/>'
    o+=f'<path d="M20 34a12 12 0 0 1 12-12h416a12 12 0 0 1 12 12v12H20z" fill="#EFECE6"/>'
    o+=f'<circle cx="38" cy="34" r="4" fill="{fv.ACCENT}"/><circle cx="52" cy="34" r="4" fill="{fv.STROKE}"/><circle cx="66" cy="34" r="4" fill="{fv.STROKE}"/>'
    o+=f'<rect x="86" y="25" width="356" height="18" rx="9" fill="{fv.PANEL}" stroke="{fv.STROKE}"/><text x="98" y="38" fill="{fv.MUTE}" font-size="11">{fv.esc(url)}</text>'
    o+=f'<rect x="20" y="46" width="120" height="234" fill="#FAF8F5"/>'
    o+=f'<rect x="34" y="62" width="92" height="20" rx="10" fill="{fv.ACCENT}" opacity="0.14"/><text x="44" y="76" fill="{fv.ACCENT}" font-size="10" font-weight="600">+ Nouveau chat</text>'
    for i,yy in enumerate((96,112,128,144)): o+=f'<rect x="34" y="{yy}" width="{86-i*6}" height="9" rx="4.5" fill="{fv.BUBBLE}"/>'
    o+=fv.wrap(title,154,60,12,fv.INK,44,weight=600)[0]
    if umsg:
        um,nn=fv.wrap(umsg,208,90,10,fv.INK,40,lh=13)
        o+=f'<rect x="196" y="76" width="250" height="{12+nn*13}" rx="8" fill="{fv.BUBBLE}"/>'+um; yb=76+12+nn*13+12
    else: yb=88
    for ln in blines:
        bl,nn=fv.wrap(ln,158,yb+13,10,fv.SUB,44,lh=13)
        o+=f'<rect x="154" y="{yb}" width="286" height="{12+nn*13}" rx="7" fill="{fv.SOFT}"/>'+bl; yb+=12+nn*13+8
    o+=f'<rect x="154" y="212" width="118" height="18" rx="9" fill="{fv.PANEL}" stroke="{fv.STROKE}"/><circle cx="166" cy="221" r="3" fill="{fv.ACCENT}"/><text x="176" y="225" fill="{fv.MUTE}" font-size="10">{fv.esc(model)}</text>'
    o+=f'<rect x="154" y="240" width="292" height="30" rx="15" fill="{fv.PANEL}" stroke="{fv.STROKE}"/><text x="168" y="259" fill="{fv.MUTE}" font-size="11">{fv.esc(ph)}</text>'
    o+=f'<circle cx="430" cy="255" r="9" fill="{fv.ACCENT}"/><path d="M430 251v8 M426 255l4-4 4 4" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    return o



def f_cover(fv, eb, title, blurb, items):
    t, nn = fv.wrap(title, 38, 84, 28, fv.INK, 26, lh=32, weight=700)
    yb = 84 + nn * 32 + 6
    b, nb = fv.wrap(blurb, 40, yb, 13, fv.SUB, 62, lh=17)
    ytiles = max(196, yb + nb * 17 + 10)
    return fv.eyebrow(eb) + t + b + fv.motif_tiles(items, y=min(ytiles, 196))


def f_steps2(fv, eb, title, items):
    t, nn = fv.wrap(title, 38, 66, 22, fv.INK, 34, lh=26, weight=700)
    o = fv.eyebrow(eb) + t
    yy = 66 + nn * 26 + 18
    step = 34 if len(items) <= 4 else 30
    for i, s in enumerate(items, 1):
        o += f'<circle cx="52" cy="{yy}" r="12" fill="{fv.ACCENT}"/><text x="52" y="{yy+4}" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">{i}</text>'
        o += fv.wrap(s, 76, yy + 4, 12, fv.INK, 60, lh=14)[0]
        yy += step
    return o


def f_card2(fv, title, sub, g, tg):
    W, H = fv.W, fv.H
    o = f'<rect x="24" y="26" width="{W-48}" height="{H-52}" rx="14" fill="{fv.PANEL}" stroke="{fv.STROKE}"/>'
    o += f'<rect x="24" y="26" width="{W-48}" height="7" rx="7" fill="{fv.ACCENT}" opacity="0.85"/>'
    o += fv.gl(g, 52, 56, 1.15)
    if tg:
        tw = 14 + len(tg) * 6.2
        o += (f'<rect x="{W-48-tw:.0f}" y="58" width="{tw:.0f}" height="20" rx="10" fill="{fv.ACCENT}" opacity="0.14"/>'
              f'<text x="{W-48-tw/2:.0f}" y="72" fill="{fv.ACCENT}" font-size="10" font-weight="700" text-anchor="middle">{fv.esc(tg)}</text>')
    t, nn = fv.wrap(title, 56, 124, 20, fv.INK, 34, lh=26, weight=600)
    o += t
    if sub:
        o += fv.wrap(sub, 56, 124 + nn * 26 + 14, 12.5, fv.SUB, 54, lh=16)[0]
    return o

TABCOL = {"chapeau": "#E8683F", "web": "#E8683F", "desktop": "#2F8F83", "code": "#3D5A80"}
TYPECOL = {"Claude Web": "#E8683F", "Claude Desktop": "#2F8F83", "Claude Code": "#3D5A80"}
TABNAME = {"chapeau": "Démos Claude", "web": "Claude Web", "desktop": "Claude Desktop", "code": "Claude Code"}
ORDER = ["chapeau", "web", "desktop", "code"]


def parse(path):
    sheets, cur = {}, None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("=== "):
            key, title = [s.strip() for s in line[4:].split("|")]
            cur = sheets[key] = {"title": title, "nodes": []}
            continue
        if line.startswith(">"):
            cur["nodes"][-1]["note"].append(line[1:].strip())
            continue
        m = re.match(r"^(#{1,3}) (.*)$", line) or re.match(r"^(  -|-) (.*)$", line)
        lvl = {"#": 0, "##": 1, "###": 2, "-": None, "  -": None}[m.group(1)]
        body = m.group(2)
        kind = None
        if " ::" in body:
            body, kind = body.rsplit(" ::", 1)
        marks = ""
        mm = re.search(r"\s(\{[^}]*\})$", body)
        if mm:
            marks = mm.group(1); body = body[:mm.start()]
        label = None
        lm = re.search(r"label:\s*([^,}]+)", marks)
        if lm:
            label = lm.group(1).strip()
        if lvl is None:  # bullet: depth = parent heading + 1
            parent_lvl = max(n["lvl"] for n in cur["nodes"] if n["heading"]) if False else None
            hs = [n for n in cur["nodes"] if n["heading"]]
            lvl = hs[-1]["lvl"] + 1
            heading = False
        else:
            heading = True
        cur["nodes"].append({"lvl": lvl, "title": body.strip(), "marks": marks, "kind": kind,
                             "label": label, "note": [], "heading": heading, "md": m.group(1)})
    # parents
    for s in sheets.values():
        stack = []
        for n in s["nodes"]:
            while stack and stack[-1]["lvl"] >= n["lvl"]:
                stack.pop()
            n["parent"] = stack[-1] if stack else None
            n["kids"] = []
            if n["parent"]:
                n["parent"]["kids"].append(n)
            stack.append(n)
    return sheets


def to_md(sheet):
    out = []
    for n in sheet["nodes"]:
        t = n["title"] + (" " + n["marks"] if n["marks"] else "")
        out.append(f'{n["md"]} {t}')
        for nl in n["note"]:
            out.append(f"> {nl}")
    return "\n".join(out) + "\n"


def slug(s, n=44):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:n].strip("-") or "x"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def read_ids(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^(?:#+|\s*-)\s+(.*?)\s*<!--t:([0-9a-f-]{36})(?:\|[^>]*)?-->", line)
        if m:
            rows.append((norm(m.group(1)), m.group(2)))
    return rows


def split_title(t):
    if " : " in t:
        a, b = t.split(" : ", 1); return a, b
    if " ; " in t:
        a, b = t.split(" ; ", 1); return a, b
    return t, ""


def short(t, n):
    t = norm(t)
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


GLYPH_BY_PREFIX = [("Ce que voit", "eye"), ("Sous le capot", "gear"), ("Pourquoi", "target"),
                   ("Limite", "warn"), ("Garde-fou", "shield"), ("Signal", "flag"), ("Alors", "rocket"),
                   ("/email", "mail"), ("/transcript", "doc"), ("/sick-leave", "folder"),
                   ("Automatiser", "clock"), ("Sous-agents", "split")]


def render(fv, tab, n):
    kind = (n["kind"] or "").split(":")
    k = kind[0]
    title = n["title"]
    tag = TABNAME[tab]
    if k == "cover":
        items = [(short(c["title"].split(" : ")[0], 22), "dot") for c in n["kids"]][:4]
        glyphs = ["globe", "device", "term", "target", "layers", "flag"]
        items = [(lab, glyphs[i % len(glyphs)]) for i, (lab, _) in enumerate(items)]
        blurb = n["note"][0].split(". ")[0] + "." if n["note"] else ""
        return f_cover(fv, tag, title, short(blurb, 120), items)
    if k == "section":
        return f_steps2(fv, tag, title, [short(c["title"], 60) for c in n["kids"]][:5])
    if k == "project":
        rows = [(short(c["title"], 52), c["label"] or "") for c in n["kids"]][:5]
        return fv.f_panel(title, rows, tg=n["label"] or "")
    if k == "demo":
        lines = [short(split_title(c["title"])[1] or c["title"], 120) for c in n["kids"]]
        if tab == "web":
            prompt = WEB_PROMPTS.get(title, title)
            return f_browser2(fv, short(title, 44), "claude.ai", short(prompt, 80), [short(l[:1].upper()+l[1:], 44) for l in lines[:2]],
                                "Répondre à Claude…")
        if tab == "desktop":
            badge = "Mode " + (kind[1] if len(kind) > 1 else "Chat")
            return fv.f_desktop(title, badge, [short(l, 110) for l in lines[:3]], foot="Claude Desktop")
        proj = kind[1] if len(kind) > 1 else "projet"
        cmd = kind[2] if len(kind) > 2 else ""
        cwd = "~/Projects/" + {"office": "Office_git", "accounting": "Accounting_git", "training": "Training_git",
                               "jobseeking": "JobSeeking_git", "lucerna": "Lucerna_git",
                               "00": "00_Head_AI_Transverse_AI_git"}.get(proj, proj)
        return fv.f_terminal(title, cwd, cmd, ["› " + short(l, 120) for l in lines[:4]])
    # cards: explicit ::card:glyph, or leaves under demo/project
    glyph = kind[1] if k == "card" and len(kind) > 1 else None
    if glyph is None:
        for p, g in GLYPH_BY_PREFIX:
            if title.startswith(p):
                glyph = g; break
    glyph = glyph or "dot"
    head, sub = split_title(title)
    sub = sub[:1].upper() + sub[1:]
    ctag = n["label"] or tag
    return f_card2(fv, short(head, 90), short(sub, 210), glyph, ctag)


def recolor(svgtxt, col):
    return svgtxt.replace("#E8683F", col)


def cmd_md(content, outdir):
    os.makedirs(outdir, exist_ok=True)
    sheets = parse(content)
    for key in ORDER:
        p = os.path.join(outdir, f"{key}.md")
        open(p, "w", encoding="utf-8").write(to_md(sheets[key]))
        print(p, len(sheets[key]["nodes"]), "topics")


def cmd_svg(content, idsdir, svgdir, base):
    import flatvec as fv
    sheets = parse(content)
    os.makedirs(svgdir, exist_ok=True)
    items, index, problems = {}, [], []
    for ti, key in enumerate(ORDER):
        ids = read_ids(os.path.join(idsdir, f"{key}.ids.md"))
        nodes = sheets[key]["nodes"]
        if len(ids) != len(nodes):
            problems.append(f"{key}: {len(ids)} ids vs {len(nodes)} nodes")
        items[key] = []
        for i, (n, (t_id, tid)) in enumerate(zip(nodes, ids)):
            if norm(n["title"]) != t_id:
                problems.append(f"{key}#{i}: title mismatch {n['title']!r} vs {t_id!r}")
                continue
            fname = f"DC_{ti:02d}{key}_{i:03d}_{slug(n['title'])}.svg"
            col = TABCOL[key]
            if key == "chapeau" and n["label"] in TYPECOL and not n["kind"]:
                col = TYPECOL[n["label"]]
            frag = render(fv, key, n)
            open(os.path.join(svgdir, fname), "w", encoding="utf-8").write(recolor(fv.svg(frag), col))
            items[key].append({"topicId": tid, "imageUrl": base + fname})
            index.append(f"| `{tid}` | {key} | {fname} |")
    open(os.path.join(svgdir, "INDEX.md"), "w", encoding="utf-8").write(
        "# Démos Claude — vignettes\n\nOne SVG per topic of the Xmind file \"Démos Claude par type de Claude\".\n"
        "Built by `gen/demos.py svg` from `gen/content.txt` (the single source of every title).\n\n"
        "| Xmind topic id | tab | file |\n|---|---|---|\n" + "\n".join(index) + "\n")
    json.dump(items, open(os.path.join(svgdir, "..", "items.json") if False else os.path.join(idsdir, "items.json"), "w"), indent=0)
    print("svg written:", sum(len(v) for v in items.values()))
    print("problems:", problems or "none")


if __name__ == "__main__":
    if sys.argv[1] == "md":
        cmd_md(sys.argv[2], sys.argv[3])
    else:
        cmd_svg(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
