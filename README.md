# public-assets
Public, non-sensitive visual assets (images for Xmind maps and trainings). Nothing from project data, memory or credentials.

## Layout

- `lib/flatvec.py` — shared palette + SVG primitives. Defined once, imported by every generator.
- `trainings/<name>/` — one folder per training deck: `gen.py`, `INDEX.md` (Xmind node id -> file), `BUILD.md`, the SVGs.
- `maps/<name>/` — same, for a standalone Xmind map.

Each `gen.py` is the single source of truth for its folder's SVGs: edit the script, rerun it,
push. Output is deterministic. Raw URLs (`https://raw.githubusercontent.com/bulle-it/public-assets/main/<path>`)
are what Xmind fetches, so a file's name is part of its contract — see the folder's `BUILD.md`.
