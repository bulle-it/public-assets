# Démos Claude — how to rebuild

Thumbnails for the Xmind file "Démos Claude par type de Claude" (4 tabs: overview, Claude Web, Claude Desktop, Claude Code).

- `content.txt` is the single source of every topic title, note, label and image kind (`::cover`, `::section`, `::project`, `::demo[:…]`, `::card:<glyph>`).
- `python3 gen.py md content.txt <dir>` writes the Xmind markdown of each tab.
- `ids/<tab>.ids.md` holds the anchored markdown Xmind returned after creation (topic ids).
- `python3 gen.py svg content.txt ids <outdir> <raw-base-url>` pairs topics by order and title, writes one SVG per topic, `INDEX.md`, and `ids/items.json` for `xmind_set_topic_image`.
- Shared palette and primitives: `../../lib/flatvec.py`. Colour per tab: Web orange, Desktop teal, Code blue.
- Public repo: images only, no personal data (names, accounts, amounts, health) in any title.
