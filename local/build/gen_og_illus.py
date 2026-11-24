#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exporte chaque illustration SVG d'article en image de partage JPEG 1200x630
(Facebook, WhatsApp et LinkedIn n'affichent pas les SVG). À lancer AVANT gen_blog.py,
sans -I (Playwright est dans les site-packages utilisateur)."""
import os, glob, io
from playwright.sync_api import sync_playwright
from PIL import Image
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "SITE")
SRC = os.path.join(ROOT, "assets", "illustrations")
OUT = os.path.join(SRC, "og")
os.makedirs(OUT, exist_ok=True)
svgs = sorted(glob.glob(os.path.join(SRC, "*.svg")))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 630})
    for f in svgs:
        pg.set_content('<body style="margin:0"><img src="data:image/svg+xml;base64,%s" style="width:1200px;height:630px;object-fit:cover;display:block"></body>'
                       % __import__("base64").b64encode(open(f, "rb").read()).decode())
        pg.wait_for_timeout(150)
        png = pg.screenshot()
        dst = os.path.join(OUT, os.path.basename(f).replace(".svg", ".jpg"))
        Image.open(io.BytesIO(png)).convert("RGB").save(dst, "JPEG", quality=86, optimize=True, progressive=True)
        print("%s  %d Ko" % (os.path.basename(dst), os.path.getsize(dst) // 1024))
    b.close()
