#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repointe les CTA « Prendre rendez-vous » de Planity vers reservation.html.

A LANCER APRES build_pages.py / gen_*.py. Les generateurs produisent encore des
CTA vers Planity ; le site publie, lui, pointe vers le module de reservation.
Ce script rend cette etape explicite et rejouable, au lieu d'une retouche
manuelle qui se perd a chaque regeneration.

Les liens Planity NON-CTA (avis clients, sameAs des donnees structurees) sont
volontairement conserves.
"""
import glob, io, os, re, sys

PLANITY = "https://www.planity.com/lumia-04100-manosque"
# CTA uniquement : un <a> vers Planity portant une classe de bouton
CTA = re.compile(
    r'<a href="' + re.escape(PLANITY) + r'"\s+target="_blank"\s+rel="noopener"\s+'
    r'(class="(?:btn btn-primary|btn-cta-nav|btn btn-ghost-light)")',
)

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    total, touched = 0, []
    pages = sorted(glob.glob(os.path.join(root, "*.html"))) + \
            sorted(glob.glob(os.path.join(root, "blog", "*.html")))
    for path in pages:
        # profondeur : les pages de blog/ remontent d'un cran
        prefix = "../" if os.path.basename(os.path.dirname(path)) == "blog" else ""
        src = io.open(path, encoding="utf-8").read()
        new, n = CTA.subn(r'<a href="%sreservation.html" \1' % prefix, src)
        if n:
            io.open(path, "w", encoding="utf-8").write(new)
            touched.append((os.path.relpath(path, root), n)); total += n
    for name, n in touched:
        print("  %-42s %d CTA" % (name, n))
    print("%d CTA repointees vers reservation.html dans %d fichiers" % (total, len(touched)))
    reste = sum(io.open(p, encoding="utf-8").read().count(PLANITY) for p in pages)
    print("liens Planity restants (avis + sameAs, normaux) :", reste)

if __name__ == "__main__":
    main()
