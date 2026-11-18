#!/usr/bin/env python3
"""Deploy step for Huether Heating & Cooling: collects public files into _site/ for GitHub Pages.

Runs automatically in GitHub Actions after every change on main (.github/workflows/objava.yml).
Local check:  python3 objava.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

import objava_cms  # noqa: E402

objava_cms.collect(ROOT, [
    "index.html", "services.html", "style.css", "app.js", "fonts", "img", "uredi.html", "cms",
], demo_pages=("index.html", "services.html"),
   demo_buttons=(("uredi.html?demo", "Edit this website (demo)"),))
