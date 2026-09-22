#!/usr/bin/env python3
# Flat-vector SVG set for the merged Xmind sheet "Souhila: your thesis checker" (file mKRiB2a3,
# sheet 53b1949c-...). One image on the centre topic, one per top-level branch, one per step of
# "How a run goes", one per check in "The four checks".
# Palette and primitives: ../../lib/flatvec.py (shared).
# Public repo: no personal names and no project data, only generic wording.
import os, sys
OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT, os.pardir, os.pardir, "lib"))
from flatvec import *  # noqa: F401,F403
PFX = "Thesis_Checker"
RAWBASE = "https://raw.githubusercontent.com/bulle-it/public-assets/main/maps/Thesis_Checker"

FOUR = [("Layout", "table"), ("Language", "chat"), ("Originality", "search"), ("Machine text", "brain")]

def f_root():
    return f_section("Thesis checker", "Your thesis checker",
                      "A careful second reader: layout, language, originality and a machine-text signal. It suggests and never rewrites.",
                      motif_tiles(FOUR))

def f_what():
    return f_card("A careful second reader",
                  "It checks four things and gives you suggestions. It never rewrites your text and never touches your original.",
                  "eye", "suggestions only")

def f_run_top():
    return f_card("Five small steps",
                   "From your file on Drive to two links back in your inbox, each step below shown on its own.",
                   "steer", "how a run goes")

def f_step1():
    return f_card("You drop your file", "Save your chapter as a Word file in the shared input folder on Drive.", "folder", "step 1 of 5")

def f_step2():
    return f_card("Christophe starts the checker", "Whenever you are ready. Nothing runs on its own.", "gear", "step 2 of 5")

def f_step3():
    return f_card("The checks run on a copy", "Your original file is never touched; only a copy is checked.", "layers", "step 3 of 5")

def f_step4():
    o = f_card("Your file comes back, with comments", "A commented copy of your chapter, plus a short report, land back on Drive.", "doc", "step 4 of 5")
    o += f'<rect x="24" y="26" width="{W-48}" height="{H-52}" rx="14" fill="none" stroke="{ACCENT}" stroke-width="3"/>'
    o += f'<text x="{W-38}" y="70" fill="{ACCENT}" font-size="10" text-anchor="end" font-weight="700" letter-spacing="1">THIS IS THE MOMENT THAT MATTERS</text>'
    return o

def f_step5():
    return f_card("Two links land in your inbox", "Christophe emails you both: the commented copy and the report. No attachments.", "mail", "step 5 of 5")

def f_checks_top():
    return f_section("Four checks", "Four checks, one report",
                      "Each one below says what it checks, what runs it, and its limit.",
                      motif_tiles(FOUR))

def f_check_layout():
    return f_panel("Layout, with MLA", [
        ("Checks", "margins, line spacing, indents, block quotations, the page header"),
        ("Runs as", "free software on Christophe's computer that reads your file's formatting"),
        ("Limit", "layout only, it does not read what your chapter says"),
    ], tg="check 1 of 4")

def f_check_language():
    return f_panel("Language", [
        ("Checks", "grammar, spelling and phrasing that doesn't read as academic English"),
        ("Runs as", "LanguageTool, a free grammar checker, on his computer; Claude reads only the flagged lines"),
        ("Limit", "suggestions only, a few issues still slip through while this is tuned"),
    ], tg="check 2 of 4")

def f_check_originality():
    return f_panel("Originality", [
        ("Checks", "your sources, your other chapters, open research papers and the open web"),
        ("Runs as", "free software on Christophe's computer; only short phrases ever leave the machine"),
        ("Limit", "not Oran 2's Turnitin, no licensed journals or its archive of past student papers"),
    ], tg="check 3 of 4")

def f_check_machinetext():
    return f_panel("Machine-written text signal", [
        ("Checks", "whether a passage reads more machine-like than your own usual style"),
        ("Runs as", "a free AI model on Christophe's computer, calibrated on writing samples you share"),
        ("Limit", "a signal, never proof, needs a good number of your own texts to be reliable"),
    ], tg="check 4 of 4")

def f_examples():
    return f_panel("Examples of comments", [
        ("Layout", "Page 3: the left margin is 1.25 inch, MLA asks for 1 inch"),
        ("Language", "it's should be its, from a real test"),
        ("Originality", "Chapter 2 paragraph 4 is close to a source you supplied"),
        ("Machine text", "Paragraph 4 reads closer to machine text than your usual style: please check"),
    ], tg="examples", note="Only the language line is from a real test; the others use invented numbers.")

def f_privacy():
    o = head_p("Privacy", "Where your text goes")
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
    o += f'<text x="240" y="256" fill="{SUB}" font-size="12" text-anchor="middle">Your file is never uploaded and nothing is published</text>'
    o += f'<text x="240" y="274" fill="{MUTE}" font-size="10.5" text-anchor="middle">A few short phrases may be searched on the web to look for copies</text>'
    return o

def head_p(eb, title): return eyebrow(eb) + wrap(title, 38, 76, 22, INK, 32, weight=700)[0]

def f_limits():
    return f_card("Suggests, never decides",
                  "It will not rewrite your text, prove that a passage is machine-written, search the whole internet or replace the official check at submission.",
                  "shield", "limits")

def f_part():
    return f_steps("Your part", "Three small things", [
        "Ask your supervisor for the university's thesis layout guide",
        "Tell Christophe which sources to compare with your chapters",
        "Share texts you wrote yourself in the Calibration folder"])

SPEC = []
def add(a, name, frag): SPEC.append((a, f"{PFX}_{name}.svg", frag))

add("18bec776-9234-46ff-88e5-094284a8cab3", "00_root", f_root())
add("5e720e81-d0fa-4344-b272-415f9120795e", "01_what-it-does", f_what())
add("da6fdf74-b8c1-4df7-a5b1-7bf7624dbfb7", "02_how-a-run-goes", f_run_top())
add("2609796e-208d-4afc-a2a1-043033a4ba5c", "02a_step1-drop-file", f_step1())
add("f08bc03a-265b-4487-8e22-f598a4c412f9", "02b_step2-starts-checker", f_step2())
add("e854418b-f485-486f-9c36-a8bb051c8520", "02c_step3-runs-on-copy", f_step3())
add("853bdfda-b0fd-4a2a-b19f-feb4b8184090", "02d_step4-comes-back", f_step4())
add("152ce42e-500f-45b7-8066-36f313f5540e", "02e_step5-two-links", f_step5())
add("dcea6856-003f-4e17-8561-950f9053ea78", "03_four-checks", f_checks_top())
add("1c0d3045-bfd6-41eb-a8fd-8bd8de4849aa", "03a_check-layout", f_check_layout())
add("4316a9ec-4e41-49aa-aa6a-f8ace0cbf8f4", "03b_check-language", f_check_language())
add("24ad85a9-e6e3-40c8-94de-5575d77c82e9", "03c_check-originality", f_check_originality())
add("15f2af3b-27bb-4468-a598-9d89d2cf12a5", "03d_check-machine-text", f_check_machinetext())
add("bb4a35a1-91de-4af1-a596-e5cdbb9eb427", "04_examples", f_examples())
add("de4d3495-cb7b-4a8d-a789-a1e5399b18fa", "05_where-your-text-goes", f_privacy())
add("cc8df081-d73f-41c7-bdb4-dd7aef5dd14d", "06_what-it-will-not-do", f_limits())
add("26ae9f26-6e2a-4337-9b7c-58caefa6697b", "07_what-we-need-from-you", f_part())

write_all(OUT, SPEC, [
 "# Thesis checker — visual assets", "",
 "Flat-vector SVGs for the merged Xmind sheet \"Souhila: your thesis checker\" (file `mKRiB2a3`): centre, one per top branch, one per run-step, one per check.", "",
 "Naming: `Thesis_Checker_<NN[letter]>_<slug>.svg`.", "",
 f"Raw base: `{RAWBASE}/`", "",
 "| Xmind node id | file |", "|---|---|"])
