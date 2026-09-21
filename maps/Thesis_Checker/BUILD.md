# Thesis checker — how this set is built

- `gen.py` draws every SVG with the shared palette and primitives in `../../lib/flatvec.py`
  and writes `INDEX.md` (node id → file). Run `python3 gen.py` from this folder.
- One image per top-level branch of the Xmind sheet "Your thesis checker" plus one on the centre
  topic. The node ids in `gen.py` belong to file `mKRiB2a3`, sheet `34ea33d4-62b1-4092-82c1-ebc77079f7bf`.
- Attach with `xmind_set_topic_image`, using the raw URLs listed in `INDEX.md`.
- Public repo: wording stays generic (no personal names, no project data).
- If a file's content changes but its name does not, re-attach with `?v=N` on the URL.
