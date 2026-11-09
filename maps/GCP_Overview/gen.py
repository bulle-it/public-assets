#!/usr/bin/env python3
# Flat-vector SVG set for the Xmind sheet "GCP" of the map CV_UpdateSkills (UZWWd58n).
# One flow diagram per tool (caller -> script -> auth -> Google) plus a gotcha line.
# Palette and primitives: ../../lib/flatvec.py — shared with every image set in this repo.
import os, sys

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT, os.pardir, os.pardir, "lib"))
from flatvec import *  # noqa: F401,F403

PFX = "GCP_Overview"
RAWBASE = "https://raw.githubusercontent.com/bulle-it/public-assets/main/maps/GCP_Overview"

def f_flow(eb, title, boxes, gotcha):
    """boxes: 4 x (role, label); gotcha: one sentence shown under the flow."""
    o = eyebrow(eb) + wrap(title, 38, 76, 22, INK, 32, weight=700)[0]
    bw, gap, x0, y0, bh = 96, 18, 21, 100, 84
    for i, (role, label) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        o += f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="10" fill="{PANEL}" stroke="{STROKE}"/>'
        o += f'<rect x="{x}" y="{y0}" width="{bw}" height="22" rx="10" fill="{SOFT}"/><rect x="{x}" y="{y0+12}" width="{bw}" height="10" fill="{SOFT}"/>'
        o += f'<text x="{x+bw/2}" y="{y0+15}" fill="{MUTE}" font-size="9" text-anchor="middle" letter-spacing="1">{esc(role.upper())}</text>'
        o += wrap(label, x + bw/2, y0 + 41, 10.5, INK, 15, lh=12.5, anchor="middle", weight=600)[0]
        if i < 3:
            ax = x + bw + 2
            o += f'<path d="M{ax} {y0+bh/2} h{gap-8}" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round"/>'
            o += f'<path d="M{ax+gap-12} {y0+bh/2-5} l6 5 l-6 5" fill="none" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    o += f'<rect x="21" y="212" width="438" height="58" rx="10" fill="{PANEL}" stroke="{STROKE}"/>'
    o += f'<rect x="21" y="212" width="5" height="58" rx="2" fill="{ACCENT}"/>'
    o += f'<text x="40" y="232" fill="{ACCENT}" font-size="10" font-weight="700" letter-spacing="1.5">GOTCHA</text>'
    o += wrap(gotcha, 40, 249, 11.5, INK, 66, lh=14)[0]
    return o

SPEC = []
def add(a, name, frag): SPEC.append((a, f"{PFX}_{name}.svg", frag))

add("ca0d2260-f13d-4189-aacb-b62d143b7f10", "01_oauth-setup", f_flow(
    "Why one OAuth setup", "One consent, one shared token",
    [("you", "google-auth.py auth, once"), ("store", "one token file, copied into rclone.conf"),
     ("tools", "rclone, Docs, Contacts, Apps Script"), ("Google", "drive, contacts, script scopes")],
    "In Testing the refresh token dies after 7 days; In production removes that limit (first renewal to confirm)."))
add("37423968-d3be-4fd7-812c-e6107333fc61", "02_drive-rclone", f_flow(
    "Tool example", "Drive through rclone",
    [("caller", "project script"), ("tool", "rclone, gdrive remote"),
     ("auth", "shared token, refreshed"), ("Google", "Drive, whole or one folder")],
    "Never list recursively over a folder holding shortcuts: one run produced about 400 MB of JSON."))
add("ae031105-ff92-4726-b11d-221c4a988741", "03_docs-sheets-api", f_flow(
    "Tool example", "Docs and Sheets API",
    [("caller", "project script"), ("tool", "gdoc-api-client.py"),
     ("auth", "drive-scope token"), ("Google", "Docs, Sheets, Drive REST")],
    "No API call adds a tab to a Doc or anchors a comment to an exact text range."))
add("6f445530-71cf-4ca7-b393-3e5293121a96", "04_sheet-web-app", f_flow(
    "Tool example", "Sheet writes through a web app",
    [("caller", "gsheet-webapp-client.js"), ("request", "JSON and SHARED_SECRET"),
     ("web app", "Apps Script, Execute as Me"), ("Google", "row written in the Sheet")],
    "Editing the code changes nothing live until a new version is deployed; the old code keeps serving."))
add("752210dc-9a3b-4d71-a13e-aa8687acaab2", "05_apps-script-api", f_flow(
    "Tool example", "Apps Script by API",
    [("push", "gapps-script-client.py push"), ("project", "Apps Script files"),
     ("deploy", "same id, new version"), ("result", "web app page, same URL")],
    "Push alone changes nothing live; always deploy, and keep the deployment id to keep the URL."))
add("f1818560-9b74-4f7a-b60b-3ec804e1c53f", "06_contacts-people-api", f_flow(
    "Tool example", "Contacts through the People API",
    [("caller", "project script"), ("tool", "gcontacts-api-client.py"),
     ("auth", "contacts scope"), ("Google", "perso account contacts")],
    "Right after a write, search lags for a while: verify with get, not search."))
add("d2a44da8-d2f9-4651-8a69-e6f1b5d2079f", "07_gmail-smtp", f_flow(
    "Tool example", "Gmail sending without OAuth",
    [("caller", "project script"), ("tool", "send-email.py, account key"),
     ("auth", "App Password, no OAuth"), ("Gmail", "perso, project, annexe, pro")],
    "Outlook blocks SMTP, so those three accounts stay on Playwright, clicking Send on a draft."))
add("5b0aebc4-feb2-45ab-8f47-88ef10ac03f3", "08_connectors", f_flow(
    "Tool example", "Connectors, no GCP involved",
    [("caller", "Claude, MCP tool call"), ("auth", "claude.ai holds the OAuth"),
     ("connector", "Gmail, Calendar, Drive"), ("Google", "perso account")],
    "Drive create_file takes inline base64 only, about 30 KB in practice; no connector writes Sheet cells."))

write_all(OUT, SPEC, [
 "# GCP sheet — visual assets", "",
 "Flat-vector SVGs for the sheet `GCP` (id `5aca8eda-b12a-4e57-beb1-37cadaea9640`) of the Xmind map `UZWWd58n`.", "",
 "Naming: `GCP_Overview_<NN>_<slug>.svg` — NN = order of the topic in the sheet.", "",
 f"Raw base: `{RAWBASE}/`", "",
 "| Xmind node id | file |", "|---|---|"])
