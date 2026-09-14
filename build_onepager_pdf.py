#!/usr/bin/env python3
"""
Render a one-pager Markdown file to a styled, single-page PDF.

Converts Markdown -> themed HTML, then prints to PDF with headless Chrome.

Usage:  python3 build_onepager_pdf.py <input.md> <output.pdf>
Default: one-pager-denver-international-airport.md -> one-pager-denver-international-airport.pdf
Requires: python 'markdown' package and Google Chrome on PATH.
"""

import sys
import subprocess
import tempfile
import os
import shutil
import markdown

IN = sys.argv[1] if len(sys.argv) > 1 else "one-pager-denver-international-airport.md"
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(IN)[0] + ".pdf"

CSS = """
@page { size: Letter; margin: 11mm 12mm; }
* { box-sizing: border-box; }
body {
  font-family: Helvetica, Arial, "Segoe UI", sans-serif;
  color: #1b1f2a; font-size: 10.3px; line-height: 1.36; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
h1 {
  font-size: 20px; color: #10131c; margin: 0 0 6px 0; line-height: 1.15;
  border-bottom: 3px solid #00bceb; padding-bottom: 5px;
}
h2 {
  font-size: 12px; color: #0a5e7a; text-transform: uppercase; letter-spacing: .4px;
  margin: 12px 0 4px 0; padding-left: 8px; border-left: 4px solid #00bceb;
}
p { margin: 4px 0; }
ul { margin: 3px 0 3px 0; padding-left: 18px; }
li { margin: 1.5px 0; }
strong { color: #10131c; }
blockquote {
  margin: 6px 0 8px 0; padding: 8px 12px; background: #eef6fb;
  border-left: 4px solid #00bceb; border-radius: 3px; font-size: 10.6px;
}
blockquote p { margin: 0; }
table { width: 100%; border-collapse: collapse; margin: 5px 0 6px 0; font-size: 9.4px; }
th, td { border: 1px solid #d3d9e0; padding: 3.5px 6px; text-align: left; vertical-align: top; }
th { background: #10131c; color: #fff; font-weight: 600; }
tbody tr:nth-child(even) { background: #f4f7fa; }
tbody tr:last-child { background: #eaf6fb; font-weight: 600; }
em { color: #5a6472; }
hr { border: none; border-top: 1px solid #d3d9e0; margin: 8px 0; }
hr + p em, p:last-of-type em { font-size: 8.6px; color: #6b7482; }
a { color: #0a5e7a; text-decoration: none; }
"""

html_body = markdown.markdown(
    open(IN, encoding="utf-8").read(),
    extensions=["tables", "sane_lists", "attr_list"],
)
doc = f"""<!doctype html><html><head><meta charset="utf-8">
<style>{CSS}</style></head><body>{html_body}</body></html>"""

chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
if not chrome:
    sys.exit("No Chrome/Chromium found on PATH.")

with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
    f.write(doc)
    html_path = f.name
profile = tempfile.mkdtemp(prefix="chrome-onepager-")

cmd = [chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
       "--disable-dev-shm-usage", f"--user-data-dir={profile}",
       "--no-pdf-header-footer", "--virtual-time-budget=4000",
       f"--print-to-pdf={OUT}", f"file://{html_path}"]
try:
    # Headless Chrome sometimes writes the PDF but does not self-exit;
    # cap the wait and accept the result if the file was produced.
    subprocess.run(cmd, timeout=60, capture_output=True, text=True)
except subprocess.TimeoutExpired:
    subprocess.run(["pkill", "-9", "-f", profile], capture_output=True)
finally:
    os.unlink(html_path)
    shutil.rmtree(profile, ignore_errors=True)

if not (os.path.exists(OUT) and os.path.getsize(OUT) > 1024):
    sys.exit("PDF was not generated.")
print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")
