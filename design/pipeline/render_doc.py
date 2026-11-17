"""Render design_document.md to a styled, self-contained HTML file beside it.

Markdown carries no styling, so the required look (white background, Arial 10pt body,
compact spacing, greyscale headings and rules, colour only inside Mermaid diagrams)
lives in design_document.html. Usage: python render_doc.py
"""
from __future__ import annotations

import html
import re

import markdown

from common import DESIGN_DOC

CSS = """
body{background:#fff;color:#111;font-family:Arial,Helvetica,sans-serif;font-size:10pt;line-height:1.35;
max-width:1000px;margin:24px auto;padding:0 24px}
h1,h2,h3,h4{color:#333;font-family:Arial,Helvetica,sans-serif;margin:1.1em 0 .4em}
h1{font-size:18pt;border-bottom:2px solid #555;padding-bottom:4px}
h2{font-size:14pt;border-bottom:1px solid #999;padding-bottom:3px}
h3{font-size:11.5pt}h4{font-size:10.5pt;color:#555}
p,ul,ol,table,pre{margin:.35em 0}li{margin:.1em 0}
hr{border:0;border-top:1px solid #aaa;margin:1em 0}
table{border-collapse:collapse;font-size:9pt}th,td{border:1px solid #bbb;padding:2px 6px;vertical-align:top}
th{background:#eee;color:#222}
code,pre{font-family:Consolas,Menlo,monospace;font-size:8.5pt;background:#f4f4f4}
pre{padding:6px;overflow-x:auto}
img{max-width:100%;border:1px solid #ccc}a{color:#333}
blockquote{border-left:3px solid #aaa;margin:.4em 0;padding-left:8px;color:#444}
"""


def main() -> None:
    src = DESIGN_DOC.read_text(encoding="utf-8")
    blocks: list[str] = []

    def stash(m: re.Match) -> str:
        blocks.append(f'<pre class="mermaid">{html.escape(m.group(1))}</pre>')
        return f"\n\nMERMAIDBLOCK{len(blocks) - 1}\n\n"

    src = re.sub(r"```mermaid\n(.*?)```", stash, src, flags=re.S)
    body = markdown.markdown(src, extensions=["tables", "fenced_code", "toc", "sane_lists"])
    for i, b in enumerate(blocks):
        body = body.replace(f"<p>MERMAIDBLOCK{i}</p>", b)
    out = DESIGN_DOC.with_suffix(".html")
    out.write_text(
        "<!doctype html><html><head><meta charset='utf-8'><title>Design document</title>"
        f"<style>{CSS}</style></head><body>{body}"
        "<script type='module'>import m from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';"
        "m.initialize({startOnLoad:true,theme:'default'});</script></body></html>",
        encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
