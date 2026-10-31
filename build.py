#!/usr/bin/env python3
"""Static site builder for the Plain Health Research Guide.

Builds docs/*.md into a self-contained static HTML site (default: site/).
Local-first: no network access, no accounts, no tracking.

Usage:
    python3 build.py            # build the site
    python3 build.py --out DIR  # build into a specific directory
    python3 build.py --clean    # remove the output directory, then build

Requires the `markdown` package:
    pip3 install markdown
    (Debian/Ubuntu: sudo apt install python3-markdown)
"""

import argparse
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print(
        "error: the 'markdown' package is required to build.\n"
        "  pip3 install markdown\n"
        "  (Debian/Ubuntu: sudo apt install python3-markdown)",
        file=sys.stderr,
    )
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"

MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists"]

TITLE = "Reading Health Research Without a PhD"
SUBTITLE = "A plain-English manual for headlines, abstracts, and study numbers"
FOOTER_DISCLAIMER = (
    "This guide is for education only — it is never medical advice. "
    "If something here raises a question about your own health, "
    "that question belongs with your healthcare team."
)
FOOTER_COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"
FOOTER_HUB = "https://dylanasdale.github.io"


def md_to_html(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


def build_pages() -> list[tuple[str, str, str]]:
    """Return list of (source_stem, filename, html) in reading order."""
    order = build_order()
    paths = [DOCS / name for name in order]
    src_names = set(p.name for p in DOCS.glob("*.md"))
    if src_names != set(order):
        extra = sorted(src_names - set(order))
        raise SystemExit(f"docs/ contains files unknown to the build: {extra}")
    filenames = []
    for p in paths:
        if p.name == "index.md":
            filenames.append("index.html")
        else:
            filenames.append(p.stem + ".html")
    labels = ["Home" if p.name == "index.md" else nav_label(p.read_text(encoding="utf-8"))
              for p in paths]
    titles = [ TITLE if p.name == "index.md"
               else f"{nav_label(p.read_text(encoding='utf-8'))} — {TITLE}"
                for p in paths ]
    pages = []
    for i, (p, filename) in enumerate(zip(paths, filenames)):
        html = md_to_html(p)
        page = compose(
            titles[i],
            html,
            list(zip(labels, filenames)),
            "index.html",
            filename,
            filenames[i - 1] if i > 0 else None,
            filenames[i + 1] if i + 1 < len(filenames) else None,
        )
        pages.append((p.stem, filename, page))
    return pages


def nav_label(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].replace("*", "").split(" — ")[0].split(":")[0].strip()
    return "Untitled"


CSS_SUFFIX = "style.css"


def compose(title, body, nav_items, index_name, current, prev_name, next_name) -> str:
    nav_links = []
    for label, filename in nav_items:
        active = ' class="active"' if filename == current else ""
        nav_links.append(f'<li><a href="{filename}"{active}>{label}</a></li>')
    prev_link = f'<a href="{prev_name}" class="pager">&larr; Previous</a>' if prev_name else ""
    next_link = f'<a href="{next_name}" class="pager next">Next &rarr;</a>' if next_name else ""
    index_href = index_name
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Beginner manual: read health research and headlines without a PhD. Education only, never medical advice.">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="masthead">
<a class="brand" href="{index_href}">{TITLE}</a>
<p>{SUBTITLE}</p>
</header>
<nav><ul>{''.join(nav_links)}</ul></nav>
<main>
{body}
<div class="pager-row">{prev_link}{next_link}</div>
</main>
<footer>
<p>{FOOTER_DISCLAIMER}</p>
<p>{FOOTER_COPYRIGHT} &middot; <a href="{FOOTER_HUB}">dylanasdale.github.io</a> &middot; MIT License</p>
</footer>
</body>
</html>
"""


STYLE = """
:root { --ink:#26333d; --soft:#5b6b76; --accent:#0e6b6b; --paper:#fffdf8; --line:#e3ddd0; }
* { box-sizing: border-box; }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink);
  background:var(--paper); line-height:1.65; }
header.masthead { padding:2.2rem 1rem 1.2rem; text-align:center; border-bottom:1px solid var(--line); }
header.masthead .brand { font-size:1.5rem; font-weight:bold; color:var(--accent); text-decoration:none; }
header.masthead p { margin:.35rem 0 0; color:var(--soft); font-style:italic; }
nav { background:#f4f0e6; border-bottom:1px solid var(--line); }
nav ul { margin:0; padding:.55rem .5rem; list-style:none; display:flex; flex-wrap:wrap;
  gap:.2rem .9rem; justify-content:center; }
nav a { color:var(--ink); text-decoration:none; font-size:.92rem; }
nav a:hover { color:var(--accent); }
nav a.active { color:var(--accent); font-weight:bold; }
main { max-width:46rem; margin:0 auto; padding:2rem 1.1rem 1rem; }
h1, h2, h3 { line-height:1.25; }
h1 { font-size:1.9rem; margin-top:0; }
h2 { font-size:1.35rem; margin-top:2.2rem; border-bottom:1px solid var(--line); padding-bottom:.25rem; }
h3 { font-size:1.1rem; margin-top:1.6rem; }
a { color:var(--accent); }
blockquote { margin:1rem 0; padding:.2rem 1rem; border-left:3px solid var(--accent);
  background:#f6f3ea; color:var(--soft); }
table { border-collapse:collapse; width:100%; margin:1rem 0; font-size:.95rem; }
th, td { border:1px solid var(--line); padding:.5rem .6rem; text-align:left; vertical-align:top; }
th { background:#f4f0e6; }
code { background:#f4f0e6; padding:.1em .35em; border-radius:3px; font-size:.9em;
  font-family:'SFMono-Regular', Consolas, monospace; }
li { margin:.25rem 0; }
hr { border:0; border-top:1px solid var(--line); margin:2rem 0; }
.pager-row { display:flex; justify-content:space-between; margin-top:2.5rem; font-size:.95rem; }
.pager-row a { text-decoration:none; }
footer { border-top:1px solid var(--line); margin-top:2.5rem; padding:1.4rem 1.1rem 2rem;
  text-align:center; color:var(--soft); font-size:.9rem; }
footer a { color:var(--soft); }
@media (prefers-reduced-motion: reduce) { * { scroll-behavior:auto; } }
"""


def write_site(pages, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for _stem, filename, html in pages:
        (out_dir / filename).write_text(html, encoding="utf-8")
    (out_dir / "style.css").write_text(STYLE, encoding="utf-8")


def build_order() -> list[str]:
    """One source of truth for the reading order; validated against docs/"""
    names = sorted(p.name for p in DOCS.glob("*.md"))
    if "index.md" not in names:
        raise SystemExit("docs/index.md is missing; it is the site home page")
    return ["index.md"] + [n for n in names if n != "index.md"]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="site", help="output directory (default: site)")
    parser.add_argument("--clean", action="store_true", help="wipe output dir before building")
    args = parser.parse_args(argv)

    out_dir = (ROOT / args.out).resolve()
    order = build_order()

    if args.clean and out_dir.exists():
        shutil.rmtree(out_dir)

    pages = build_pages()
    write_site(pages, out_dir)
    print(f"built {len(pages)} pages + style.css -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
