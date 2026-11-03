#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de pages statiques LUMIA.
Centralise l'en-tête / pied de page partagés et émet du HTML statique pur.
Outil de build (comme la minification) ; la sortie reste 100% statique.
Lancer : python3 build_pages.py
"""
import os, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))

PLANITY = "https://www.planity.com/lumia-04100-manosque"
IG = "https://www.instagram.com/lumiamanosque"
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.81.36 1.6.7 2.34a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.74-1.27a2 2 0 0 1 2.11-.45c.74.34 1.53.57 2.34.7A2 2 0 0 1 22 16.92z"/></svg>'

def img_size(name, base="assets"):
    """Dimensions reelles d'une image, lues dans l'en-tete du fichier.

    Evite de declarer des width/height faux dans le HTML, ce qui provoque un
    decalage de mise en page au chargement (CLS). Sans dependance externe :
    lecture directe des en-tetes PNG, JPEG et WebP.
    """
    import os, struct
    path = name if os.path.sep in name else os.path.join(base, name)
    with open(path, "rb") as fh:
        head = fh.read(32)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", head[16:24]); return w, h
        if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
            fh.seek(12); chunk = fh.read(8); kind = chunk[:4]
            if kind == b"VP8 ":
                d = fh.read(10); return struct.unpack("<H", d[6:8])[0] & 0x3FFF, struct.unpack("<H", d[8:10])[0] & 0x3FFF
            if kind == b"VP8L":
                d = fh.read(5); n = struct.unpack("<I", d[1:5])[0]
                return (n & 0x3FFF) + 1, ((n >> 14) & 0x3FFF) + 1
            if kind == b"VP8X":
                d = fh.read(10)
                return (int.from_bytes(d[4:7], "little") + 1, int.from_bytes(d[7:10], "little") + 1)
        if head[:2] == b"\xff\xd8":
            fh.seek(2)
            while True:
                b0 = fh.read(1)
                if not b0: break
                if b0 != b"\xff": continue
                marker = fh.read(1)
                while marker == b"\xff": marker = fh.read(1)
                if marker[0] in (0xC0,0xC1,0xC2,0xC3,0xC5,0xC6,0xC7,0xC9,0xCA,0xCB,0xCD,0xCE,0xCF):
                    fh.read(3); h, w = struct.unpack(">HH", fh.read(4)); return w, h
                size = struct.unpack(">H", fh.read(2))[0]; fh.seek(size - 2, 1)
    raise ValueError("dimensions illisibles : %s" % path)

def topbar():
    return (
'<div class="topbar"><div class="container">'
'<div class="topbar__left"><a href="tel:+33492876372">04 92 87 63 72</a>'
'<span class="topbar__hours">Du lundi au vendredi, 10h-19h</span></div>'
'<div class="topbar__right"><a href="%s" target="_blank" rel="noopener noreferrer" aria-label="Instagram de LUMIA">%s</a></div>'
'</div></div>' % (IG, IG_SVG))

def nav(p):
    return (
'<nav id="nav" aria-label="Navigation principale"><div class="container">'
'<a href="%s" class="nav__logo" aria-label="LUMIA, accueil"><img src="%sassets/logo.png" alt="LUMIA, institut de beauté à Manosque" width="132" height="33" loading="eager"></a>'
'<div class="nav__menu" id="nav-menu">'
'<a href="%s">Accueil</a>'
'<div class="nav__dropdown"><a href="%s#prestations">Prestations</a><div class="nav__dropdown-menu">'
'<a href="%sepilation-laser-manosque.html">Épilation LASER CE Médical</a>'
'<a href="%ssoins-visage-manosque.html">Soins du visage</a>'
'<a href="%slpg-cellu-m6-manosque.html">LPG endermologie</a>'
'<a href="%smicroneedling-manosque.html">Microneedling</a>'
'<a href="%ssoin-cosmelan-taches-manosque.html">Soins dépigmentants COSMELAN</a>'
'<a href="%scosmetiques-manosque.html">Cosmétiques</a></div></div>'
'<a href="%sa-propos.html">À propos</a>'
'<a href="%starifs.html">Tarifs</a>'
'<a href="%sblog.html">Blog</a>'
'<a href="%scontact.html">Contact</a>'
'<a href="%s" target="_blank" rel="noopener" class="btn-cta-nav">Prendre rendez-vous</a></div>'
'<button class="nav__toggle" id="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false"><span></span><span></span><span></span></button>'
'</div></nav>' % (p, p, p, p, p, p, p, p, p, p, p, p, p, p, PLANITY))

def footer(p):
    return (
'<footer><div class="container"><div class="footer-grid">'
'<div class="footer__brand"><img src="%sassets/logo-blanc.png" alt="LUMIA" width="150" height="38" loading="lazy" style="margin-bottom:.5rem;">'
'<p>Institut de beauté et centre d\'épilation laser à Manosque. Épilation laser définitive, soins du visage, LPG et soins dépigmentants, réalisés par une infirmière diplômée d\'État.</p></div>'
'<nav class="footer__col" aria-label="Prestations"><p class="footer__title">Prestations</p><ul class="footer__links">'
'<li><a href="%sepilation-laser-manosque.html">Épilation LASER CE Médical</a></li>'
'<li><a href="%ssoins-visage-manosque.html">Soins du visage</a></li>'
'<li><a href="%slpg-cellu-m6-manosque.html">LPG endermologie</a></li>'
'<li><a href="%smicroneedling-manosque.html">Microneedling</a></li>'
'<li><a href="%ssoin-cosmelan-taches-manosque.html">Soins COSMELAN</a></li>'
'<li><a href="%scosmetiques-manosque.html">Cosmétiques</a></li></ul></nav>'
'<nav class="footer__col" aria-label="Navigation"><p class="footer__title">Navigation</p><ul class="footer__links">'
'<li><a href="%sa-propos.html">À propos</a></li>'
'<li><a href="%starifs.html">Tarifs</a></li>'
'<li><a href="%sblog.html">Blog</a></li>'
'<li><a href="%scontact.html">Contact</a></li></ul></nav>'
'<div class="footer__contact"><p class="footer__title">Contact</p>'
'<p>10 Bis avenue Jean Giono</p><p>04100 Manosque</p>'
'<p><a href="tel:+33492876372">04 92 87 63 72</a></p><p>Lun-ven, 10h-19h</p>'
'<div class="footer__social mt-1"><a href="%s" target="_blank" rel="noopener noreferrer" aria-label="Instagram de LUMIA">%s</a></div></div>'
'</div><div class="footer__bottom">'
'<p>&copy; 2026 LUMIA &middot; Site réalisé par <a href="https://sol-ia.tech" target="_blank" rel="noopener">Sol&middot;IA</a></p>'
'<p><a href="%smentions-legales.html">Mentions légales</a> &middot; <a href="%spolitique-confidentialite.html">Confidentialité</a></p>'
'</div></div></footer>' % (p, p, p, p, p, p, p, p, p, p, p, IG, IG_SVG, p, p))

def mobile_cta():
    return (
'<nav class="mobile-cta" aria-label="Actions rapides">'
'<a href="tel:+33492876372" class="btn btn-outline">%s Appeler</a>'
'<a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre RDV</a></nav>' % (PHONE_SVG, PLANITY))

def page(filename, title, desc, canonical, body, schema="", robots="index, follow",
         prefix="./", og_type="website", in_sub=False, extra_tail=""):
    p = "../" if in_sub else "./"
    pa = "../" if in_sub else ""  # pour assets/css/js (chemin relatif sans ./)
    head = (
'<!DOCTYPE html>\n<html lang="fr">\n<head>\n'
'<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
'<title>%s</title>\n<meta name="description" content="%s">\n'
'<meta name="robots" content="%s">\n<link rel="canonical" href="%s">\n'
'<meta property="og:type" content="%s">\n<meta property="og:title" content="%s">\n'
'<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
'<meta property="og:image" content="https://lumia-salon.fr/assets/og-image.jpg">\n'
'<meta property="og:locale" content="fr_FR">\n<meta name="theme-color" content="#A63524">\n'
'<link rel="icon" type="image/svg+xml" href="%sassets/favicon.svg">\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&family=Nunito+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">\n'
'<link rel="stylesheet" href="%scss/style.min.css">\n%s</head>\n<body>\n'
% (title, desc, robots, canonical, og_type, title, desc, canonical, pa, pa, schema))
    html = (head
        + '<a href="#main" class="skip-link">Aller au contenu principal</a>\n'
        + topbar() + nav(p) + body + footer(p) + mobile_cta()
        + '\n<script src="%sjs/main.min.js" defer></script>\n' % pa
        + extra_tail
        + '</body>\n</html>\n')
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit:", filename, len(html), "o")

def header_block(crumbs, h1, lead, p="./"):
    # crumbs : liste de (label, href|None)
    parts = []
    for label, href in crumbs:
        if href:
            parts.append('<a href="%s">%s</a>' % (href, label))
        else:
            parts.append(label)
    bc = ' <span>›</span> '.join(parts)
    leadhtml = '<p>%s</p>' % lead if lead else ''
    return ('<header class="page-header"><div class="container">'
            '<nav class="breadcrumb" aria-label="Fil d\'Ariane">%s</nav>'
            '<h1>%s</h1>%s</div></header>\n' % (bc, h1, leadhtml))

def cta(title_html, text):
    return ('<section class="cta-section"><div class="container">'
            '<h2>%s</h2><p>%s</p><div class="cta-actions">'
            '<a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>'
            '<a href="tel:+33492876372" class="btn btn-ghost-light">04 92 87 63 72</a>'
            '</div></div></section>\n' % (title_html, text, PLANITY))

def schema_service(stype, name, desc, url):
    return ('<script type="application/ld+json">\n{ "@context":"https://schema.org","@type":"Service",'
            '"serviceType":"%s","name":"%s","description":"%s","url":"%s",'
            '"provider":{"@type":"BeautySalon","name":"LUMIA","url":"https://lumia-salon.fr","telephone":"+33492876372",'
            '"address":{"@type":"PostalAddress","streetAddress":"10 Bis avenue Jean Giono","addressLocality":"Manosque","postalCode":"04100","addressCountry":"FR"}},'
            '"areaServed":{"@type":"City","name":"Manosque"} }\n</script>\n' % (stype, name, desc, url))

def schema_faq(qa):
    items = ",".join(
        '{ "@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"} }' % (q, a)
        for q, a in qa)
    return '<script type="application/ld+json">\n{ "@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s] }\n</script>\n' % items

def schema_breadcrumb(items):
    li = ",".join(
        '{ "@type":"ListItem","position":%d,"name":"%s","item":"%s" }' % (i+1, n, u)
        for i, (n, u) in enumerate(items))
    return '<script type="application/ld+json">\n{ "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s] }\n</script>\n' % li

def faq_html(qa):
    rows = "".join('<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in qa)
    return '<div class="faq">%s</div>' % rows

BASE = "https://lumia-salon.fr/"
