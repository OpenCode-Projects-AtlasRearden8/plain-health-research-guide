"""Tests for the Plain Health Research Guide build.

Run with:
    python3 -m unittest discover -s tests
"""

import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build  # noqa: E402


def make_site(tmp_root: Path, dir_name: str) -> Path:
    out = tmp_root / dir_name
    build.main(["--out", str(out), "--clean"])
    return out


class BuildTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="phrg-tests-"))
        cls.site = make_site(cls.tmp, "site")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)


class TestBuildOutput(BuildTestCase):
    def test_all_pages_exist(self):
        expected = {"style.css"}
        for name in build.build_order():
            expected.add("index.html" if name == "index.md" else Path(name).stem + ".html")
        actual = {p.name for p in self.site.iterdir()}
        self.assertEqual(expected, actual)

    def test_page_count_matches_docs(self):
        docs = {p.stem for p in (ROOT / "docs").glob("*.md")}
        self.assertEqual(len(docs), 10)
        built = len(list(self.site.glob("*.html")))
        self.assertEqual(built, 10)

    def test_built_pages_are_html_documents(self):
        for html_file in sorted(self.site.glob("*.html")):
            text = html_file.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("<!DOCTYPE html>"), html_file.name)
            self.assertIn("</html>", text[-30:])


class TestPageChrome(BuildTestCase):
    def test_footer_disclaimer_on_every_page(self):
        for page in sorted(self.site.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            self.assertIn("education only", text, page.name)
            self.assertIn("never medical advice", text, page.name)

    def test_footer_copyright_on_every_page(self):
        for page in sorted(self.site.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", text, page.name)

    def test_home_is_marked_active(self):
        first = (self.site / "index.html").read_text(encoding="utf-8")
        self.assertIn('<a href="index.html" class="active">Home</a>', first)

    def test_prev_next_pagers(self):
        home_and_last = {"index.html", "09-glossary.html"}
        for page in sorted(self.site.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            previous = "Previous" in text
            following = "Next" in text
            if page.name in home_and_last:
                self.assertTrue(previous ^ following, page.name)
            else:
                self.assertTrue(previous and following, page.name)


class TestLinks(BuildTestCase):
    def test_no_unresolved_internal_links(self):
        names = {p.name for p in self.site.iterdir()}
        for page in sorted(self.site.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            for href in re.findall(r'href="([^"]+)"', text):
                if href.startswith(("http://", "https://", "#")):
                    continue
                self.assertIn(href.split("#")[0], names, f"{page.name}: {href}")

    def test_no_raw_markdown_file_links_left(self):
        for page in sorted(self.site.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            self.assertNotRegex(text, r'href="[^"]*\.md"')

    def test_external_links_are_allowlisted(self):
        allowed = {"https://dylanasdale.github.io"}
        for page in sorted(self.site.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            for href in re.findall(r'href="(https?://[^"]+)"', text):
                self.assertIn(href, allowed, f"{page.name}: {href}")


class TestContentSignals(BuildTestCase):
    def test_glossary_has_table_and_key_terms(self):
        text = (self.site / "09-glossary.html").read_text(encoding="utf-8")
        self.assertIn("<table>", text)
        for term in ("Odds ratio (OR)", "p-value", "Confidence interval (CI)",
                     "Sample size (n)"):
            self.assertIn(term, text)

    def test_checklist_has_twelve_flags(self):
        text = (self.site / "08-red-flag-checklist.html").read_text(encoding="utf-8")
        numbers = {int(n) for n in re.findall(r"Flag (\d+)", text)}
        self.assertEqual(sorted(numbers), list(range(1, 13)))

    def test_worksheet_has_fillable_fields(self):
        text = (self.site / "07-study-reading-worksheet.html").read_text(encoding="utf-8")
        self.assertIn("Name of the paper", text)
        self.assertIn("[ ]", text)

    def test_index_links_to_every_other_page(self):
        text = (self.site / "index.html").read_text(encoding="utf-8")
        for name in build.build_order():
            if name == "index.md":
                continue
            self.assertIn(Path(name).stem + ".html", text)


class TestDeterminism(BuildTestCase):
    def test_rebuild_is_byte_identical(self):
        other = make_site(self.tmp, "rebuild")
        for page in sorted(self.site.glob("*")):
            self.assertEqual(page.read_bytes(), (other / page.name).read_bytes())


class TestSourceInvariant(unittest.TestCase):
    CREDENTIAL_PAT = re.compile(
        r"(api[_-]?key|secret|password|access[_-]?token)\s*[:=]\s*\S", re.I
    )

    def test_license_copyright_line_exact(self):
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", license_text)

    def test_readme_credits_llc(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)

    def test_no_embedded_credentials_in_sources(self):
        offenders = []
        for p in sorted(ROOT.rglob("*")):
            rel = p.relative_to(ROOT).as_posix()
            if not p.is_file() or rel.startswith(("site/", ".git/")):
                continue
            if self.CREDENTIAL_PAT.search(p.read_text(encoding="utf-8", errors="ignore")):
                offenders.append(rel)
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
