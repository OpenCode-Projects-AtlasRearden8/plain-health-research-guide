# Plain Health Research Guide

*Reading health research and headlines without a PhD.*

A beginner-friendly, **education-only** manual for making sense of health news, study abstracts, and medical statistics — written in plain English, like a friend would explain it. It is never medical advice; your healthcare team stays your team.

## What's inside

Nine short chapters in `docs/`, plus three tools you'll actually use:

| Chapter / tool | What it covers |
|---|---|
| [Reading Health Research Without a PhD](docs/index.md) | Start here — who it's for and how to use the manual |
| [Abstracts, Decoded](docs/01-abstracts-decoded.md) | Reading a study's abstract section by section (IMRaD) |
| [Numbers in Plain English](docs/02-numbers-in-plain-english.md) | What absolute vs. relative risk, odds ratios, p-values, confidence intervals, and sample sizes actually hint |
| [Spotting Misleading Health Claims](docs/03-spotting-misleading-claims.md) | Nine recurring shapes of bad health reporting |
| [Use AI to Translate — Then Verify](docs/04-using-ai-to-translate-then-verify.md) | Using AI chat as a jargon translator, then verifying it yourself |
| [Questions for Your Care Team](docs/05-questions-for-your-care-team.md) | How to bring research *questions* (not verdicts) to a clinician |
| [Avoiding Miracle-Cure Traps](docs/06-avoiding-miracle-cure-traps.md) | The eight signatures of health-product scams, and gentler alternatives |
| [The Study-Reading Worksheet](docs/07-study-reading-worksheet.md) | A fill-in worksheet for reading any single paper seriously |
| [The Red-Flag Checklist](docs/08-red-flag-checklist.md) | Twelve yes/no flags to run any health headline past |
| [Glossary](docs/09-glossary.md) | Plain-English definitions of the words research actually uses |

Companion guide: **Spot Fake Media** covers misinformation across the wider news landscape; this manual stays in the health lane. Both live on the [Dylan Asdale hub](https://dylanasdale.github.io).

## Run it locally

Build the static HTML site (default output: `site/`):

```bash
python3 build.py
```

Options: `--out DIR` to choose the output directory, `--clean` to wipe it first. Requires Python 3.10+ and the [`markdown`](https://pypi.org/project/Markdown/) package (`pip3 install markdown`, or on Debian/Ubuntu `sudo apt install python3-markdown`). No network, no accounts, no tracking — open `site/index.html` and read offline.

## Test it

```bash
python3 -m unittest discover -s tests
```

The tests rebuild the site into a temporary directory twice and verify: every page builds, footers carry the education-only disclaimer and copyright, internal links resolve, the glossary/checklist/worksheet contain their expected content, rebuilds are byte-identical, and the LICENSE/README carry the required credit.

## Repo layout

```
build.py            static site builder (markdown -> site/)
docs/               the manual (markdown, the editable source)
site/               generated static HTML site (run build.py to refresh)
tests/test_build.py build tests
LICENSE             MIT License
STATUS.md           current project status and known gaps
```

## Design notes

- **Local-first**: everything renders offline from a single dependency (`markdown`); the output is plain static HTML with one small stylesheet.
- **Warm, not condescending**: verdicts are boring on purpose; skepticism is framed as a skill you're practicing, not a test you're failing.
- **Education only, never medical advice**: every page carries the disclaimer, and health questions are consistently routed to the reader's own care team.

## LICENSE

MIT License — [LICENSE](LICENSE)

Copyright (c) 2026 Asdale Dynamics, LLC

Created by [Dylan Asdale](https://dylanasdale.github.io) and published by **Asdale Dynamics, LLC**.
