# STATUS — Plain Health Research Guide

Last updated: 2026-10-31

## What was built

A beginner-friendly, education-only manual for reading health research and
headlines without a PhD, published as **Asdale Dynamics, LLC** material.

- `docs/` — 9 markdown chapters (~9,600 words), warm plain-English tone:
  1. `index.md` — start here; how to use the manual
  2. `01-abstracts-decoded.md` — abstracts section by section (IMRaD), study
     design ladder, worked micro-example, 60-second drill
  3. `02-numbers-in-plain-english.md` — absolute vs. relative risk, odds
     ratios, RR/HR, p-values, confidence intervals, sample sizes, why
     "significant" ≠ "important"
  4. `03-spotting-misleading-claims.md` — nine shapes of misleading health
     reporting, with repair questions and a worked example
  5. `04-using-ai-to-translate-then-verify.md` — AI-as-translator workflow
     with verification steps (fresh-session checks, quote-first prompts,
     hallucinated-citation defenses)
  6. `05-questions-for-your-care-team.md` — bringing questions (not verdicts)
     to clinicians, second opinions, disagreeing with grace
  7. `06-avoiding-miracle-cure-traps.md` — eight signatures of health scams,
     a run-any-product flowchart, supplement trust table, helping a loved one
  8. `07-study-reading-worksheet.md` — fillable 17-question study-reading
     worksheet with a scoring closer
  9. `08-red-flag-checklist.md` — 12 yes/no red flags with honest scoring
  10. `09-glossary.md` — ~35 plain-English terms in a table
- `build.py` — local-first static site builder (markdown → `site/`, one
  stylesheet, nav, prev/next pagers, per-page disclaimer + copyright footer);
  no network, single dependency (`markdown`), deterministic output
- `site/` — generated static HTML (10 pages + `style.css`); open
  `site/index.html` offline
- `tests/test_build.py` — 18 unittest cases
- `README.md`, MIT `LICENSE` (© 2026 Asdale Dynamics, LLC), `.gitignore`
- Git repo initialized with an initial commit (no remote configured, never
  pushed)

## How to run it

```bash
python3 build.py            # build the site into site/
python3 build.py --out DIR  # build elsewhere
python3 build.py --clean    # wipe output first
python3 -m unittest discover -s tests   # run the test suite
```

Requires Python 3.10+ and the `markdown` package
(`pip3 install markdown`, or `sudo apt install python3-markdown`).

## Verification results

- `python3 build.py --clean` → built 10 pages + `style.css`, exit 0
- `python3 -m unittest discover -s tests` → **18/18 OK**, including:
  - every docs page builds to a complete HTML document
  - education-only disclaimer and © Asdale Dynamics, LLC footer on every page
  - all internal links resolve; no leftover raw `.md` links; external links
    limited to `https://dylanasdale.github.io`
  - checklist contains all 12 flags; glossary renders its table with key
    terms; worksheet retains its fillable fields
  - rebuilds are byte-identical (deterministic build)
  - LICENSE line exact and README credits the LLC; no embedded credentials
- Cleaned several drafting typos and unverified references during review;
  final pass done over all nine source files

## Known gaps

- The builder depends on the `markdown` PyPI package; there is no
  dependency-free fallback (documented in README and the build error message).
- Companion repo **Spot Fake Media** is referenced by name only — no cross
  link exists until that project publishes its own location.
- `dylanasdale.github.io` is linked as the author hub as instructed; content
  there is outside this repo's control.
- Worksheet checkbox rendering is plain-text `[ ]` HTML bullets, not
  interactive checkboxes (intentional for offline/print use, no JS).
- The `site/` directory is generated and gitignored; it exists locally after
  running the build but is not stored in the repo.
- No CI config; running tests is a local step (`python3 -m unittest discover
  -s tests`).
