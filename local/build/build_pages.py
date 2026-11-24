#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de pages statiques LUMIA.
Centralise l'en-tête / pied de page partagés et émet du HTML statique pur.
Outil de build (comme la minification) ; la sortie reste 100% statique.
Lancer : python3 build_pages.py
"""
import os, re, datetime, hashlib
# Le site vit dans docs/, les générateurs dans build/. ROOT désigne toujours la
# racine du site : le seul dossier qui part en ligne, et plus tard en FTP.
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "SITE")

PLANITY = "https://www.planity.com/lumia-04100-manosque"
IG = "https://www.instagram.com/lumiamanosque"
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.81.36 1.6.7 2.34a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.74-1.27a2 2 0 0 1 2.11-.45c.74.34 1.53.57 2.34.7A2 2 0 0 1 22 16.92z"/></svg>'

# Avis clients, relevés à la source le 23/11/2026.
# Une seule source de vérité : ces valeurs irriguent tout le site via page().
# À revérifier au rapprochement trimestriel (voir plan-editorial-lumia.md).
NOTE = "5,0"
AVIS_PLANITY = 57
AVIS_GOOGLE = 39
# Lien de dépôt d'avis Google. Celui-ci ouvre la fiche : la cliente doit ensuite
# trouver le bouton d'avis. À remplacer par le lien g.page/r/… de l'admin Google
# Business, qui ouvre directement la fenêtre de notation.
AVIS_GOOGLE_URL = "https://g.page/r/Cac_6DiW22YiEBM/review"
# Consultation des avis Google. Vérifié : ce lien ouvre bien la fiche LUMIA.
AVIS_GOOGLE_VOIR = "https://www.google.com/maps?cid=2478910083160358823"

def img_size(name, base=None):
    """Dimensions reelles d'une image, lues dans l'en-tete du fichier.

    Evite de declarer des width/height faux dans le HTML, ce qui provoque un
    decalage de mise en page au chargement (CLS). Sans dependance externe :
    lecture directe des en-tetes PNG, JPEG et WebP.
    """
    import os, struct
    if base is None:
        base = os.path.join(ROOT, "assets")
    elif not os.path.isabs(base):
        base = os.path.join(ROOT, base)
    path = name if os.path.isabs(name) else os.path.join(base, name)
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

def nav(p, cur=None):
    # cur : nom du fichier de la page en cours, pour aria-current="page" sur le lien correspondant
    def a(name, label):
        courant = ' aria-current="page"' if name == cur else ''
        return '<a href="%s%s"%s>%s</a>' % (p, name, courant, label)
    return (
'<nav id="nav" aria-label="Navigation principale"><div class="container">'
'<a href="%s" class="nav__logo" aria-label="LUMIA, accueil"><img src="%sassets/logo.png" alt="LUMIA, institut de beauté à Manosque" width="132" height="33" loading="eager"></a>'
'<div class="nav__menu" id="nav-menu">'
% (p, p)
+ ('<a href="%s"%s>Accueil</a>' % (p, ' aria-current="page"' if cur == "index.html" else ''))
+ '<div class="nav__dropdown"><a href="%s#prestations">Prestations</a><div class="nav__dropdown-menu">' % p
+ a("epilation-laser-manosque.html", "Épilation LASER CE Médical")
+ a("soins-visage-manosque.html", "Soins du visage")
+ a("lpg-cellu-m6-manosque.html", "LPG endermologie")
+ a("microneedling-manosque.html", "Microneedling")
+ a("soin-cosmelan-taches-manosque.html", "Soins dépigmentants COSMELAN")
+ a("cosmetiques-manosque.html", "Cosmétiques") + '</div></div>'
+ a("a-propos.html", "À propos")
+ a("tarifs.html", "Tarifs")
+ a("blog.html", "Blog")
+ a("contact.html", "Contact")
+ ('<a href="%s" target="_blank" rel="noopener" class="btn-cta-nav">Prendre rendez-vous</a></div>' % PLANITY)
+ '<button class="nav__toggle" id="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>'
'</div></nav>')

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
'<p>&copy; 2026 LUMIA &middot; Site réalisé par <a href="https://sol-ia.tech" target="_blank" rel="noopener">SOL&middot;IA</a></p>'
'<p><a href="%smentions-legales.html">Mentions légales</a> &middot; <a href="%spolitique-confidentialite.html">Confidentialité</a></p>'
'</div></div></footer>' % (p, p, p, p, p, p, p, p, p, p, p, IG, IG_SVG, p, p))

def mobile_cta():
    return (
'<nav class="mobile-cta" aria-label="Actions rapides">'
'<a href="tel:+33492876372" class="btn btn-outline">%s Appeler</a>'
'<a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre RDV</a></nav>' % (PHONE_SVG, PLANITY))

# Versionnage des CSS et JS : ?v= = empreinte du contenu. Le cache navigateur
# (30 jours, voir .htaccess) est invalidé dès que le fichier change, et seulement
# à ce moment-là. Ajouté le 23/11/2026 après la recette OVH. annonces.js n'est pas
# versionné : il est servi en no-cache, l'admin PHP l'écrira sans régénérer le HTML.
VERSIONNES = ("css/style.min.css", "js/main.min.js", "js/annonces.min.js",
              "js/annonces-tete.min.js")


def variante_800(m):
    avant, prefixe, nom, apres = m.groups()
    if "srcset" in avant + apres or not os.path.exists(os.path.join(ROOT, "assets", nom + "-800.webp")):
        return m.group(0)
    w, _ = img_size(nom + ".webp")
    return ('<img %ssrc="%s%s.webp" srcset="%s%s-800.webp 800w, %s%s.webp %dw" '
            'sizes="(max-width: 768px) 100vw, 50vw"%s>'
            % (avant, prefixe, nom, prefixe, nom, prefixe, nom, w, apres))


def nouvel_onglet(m):
    attrs, contenu = m.group(1), m.group(2)
    if "nouvel onglet" in attrs or "nouvel onglet" in contenu:
        return m.group(0)
    if 'aria-label="' in attrs:
        attrs = re.sub(r'aria-label="([^"]*)"', lambda n: 'aria-label="%s (nouvel onglet)"' % n.group(1), attrs, count=1)
        return '<a %s>%s</a>' % (attrs, contenu)
    return '<a %s>%s<span class="sr-only"> (nouvel onglet)</span></a>' % (attrs, contenu)


def version(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


# ---------------------------------------------------------------------------
# Bandeau d'avis des pages intérieures, prix d'entrée et accès rapide aux tarifs.
# Tout est inséré par post-traitement dans page(), selon le nom du fichier.
# ---------------------------------------------------------------------------
BANDEAU_PAGES = frozenset((
    "epilation-laser-manosque.html", "soins-visage-manosque.html",
    "lpg-cellu-m6-manosque.html", "microneedling-manosque.html",
    "soin-cosmelan-taches-manosque.html", "cosmetiques-manosque.html",
    "tarifs.html", "contact.html", "a-propos.html",
) + tuple("epilation-laser-%s.html" % s for s in (
    "forcalquier", "greoux-les-bains", "pierrevert", "oraison", "sainte-tulle",
    "volx", "villeneuve", "sisteron", "valensole")))

# Prix d'entrée affiché près du premier bouton : (sections de tarifs.html à lire,
# filtre facultatif sur l'intitulé de la ligne). Les prix sont lus dans gen_pages2.py,
# jamais saisis ici. Les cosmétiques n'ont aucun prix sur la page tarifs : pas de ligne.
PRIX_PAGES = {
    "epilation-laser-manosque.html": (("laser",), None),
    "soins-visage-manosque.html": (("visage",), None),
    "lpg-cellu-m6-manosque.html": (("lpg", "lpg-visage"), None),
    "microneedling-manosque.html": (("microneedling",), None),
    "soin-cosmelan-taches-manosque.html": (("cosmelan",), "Soin cabine"),
}


def prix_entree_bloc(fragment, filtre=None):
    """Plus petit prix numérique d'un tableau. Les bilans, diagnostics (offerts ou
    déductibles) et tenues ne comptent pas. Renvoie None s'il n'y a aucun prix."""
    prix = []
    for tr in re.findall(r'<tr>(.*?)</tr>', fragment, re.S):
        cellules = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
        if not cellules or re.match(r'\s*((RDV\s+)?(bilan|diagnostic)|tenue)', cellules[0], re.I):
            continue
        if filtre and not cellules[0].startswith(filtre):
            continue
        m = re.search(r'class="price">\s*(\d+)\s*euros', tr)
        if m:
            prix.append(int(m.group(1)))
    return min(prix) if prix else None


def _blocs_details(fragment):
    """(intitulé, contenu) de chaque accordéon, hors cures et forfaits (pas de prix de séance)."""
    for m in re.finditer(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', fragment, re.S):
        if not re.search(r'cure|forfait', m.group(1), re.I):
            yield m.group(1), m.group(2)


def prix_depuis(ids, filtre=None):
    """(prix, id de section) du prix d'entrée le plus bas parmi des sections de tarifs.html,
    lu dans le source de gen_pages2.py. None si aucune n'a de prix."""
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_pages2.py"), encoding="utf-8") as f:
        src = f.read()
    meilleur = None
    for sec in ids:
        m = re.search(r'<h2 id="%s">(.*?)(?=<h2 id="|</div></article>)' % re.escape(sec), src, re.S)
        if not m:
            continue
        for _, contenu in _blocs_details(m.group(1)):
            p = prix_entree_bloc(contenu, filtre)
            if p is not None and (meilleur is None or p < meilleur[0]):
                meilleur = (p, sec)
    return meilleur


def prix_dans_intitules(html):
    """Ajoute « dès X € » à chaque intitulé d'accordéon dont le tableau a un prix de séance."""
    def un(m):
        intitule, contenu = m.group(1), m.group(2)
        if re.search(r'cure|forfait', intitule, re.I):
            return m.group(0)
        p = prix_entree_bloc(contenu)
        if p is None:
            return m.group(0)
        return '<details>\n<summary>%s <span class="summary-prix">&middot; dès %d&nbsp;€</span></summary>%s</details>' % (intitule, p, contenu)
    return re.sub(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', un, html, flags=re.S)


def bandeau_avis(pa, rose=True):
    """Bandeau compact d'avis (même composant que l'accueil). pa : préfixe des assets."""
    return (
'<section class="section%s avis-bandeau" aria-label="Avis de nos clientes"><div class="container">'
'<p class="avis-bandeau__titre">{{NOTE}} / 5 &middot; {{AVIS_TOTAL}} avis sur Planity et Google</p>'
'<div class="review-sources">'
'<a class="review-source" href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener"><img class="review-source__logo" src="%sassets/logo-planity.svg" alt="Planity" width="140" height="16" loading="lazy">'
'<div class="review-source__note">{{NOTE}} / 5</div><div class="review-source__label">{{AVIS_PLANITY}} avis</div></a>'
'<a class="review-source" href="{{AVIS_GOOGLE_VOIR}}" target="_blank" rel="noopener"><img class="review-source__logo" src="%sassets/logo-google.svg" alt="Google" width="74" height="24" loading="lazy">'
'<div class="review-source__note">{{NOTE}} / 5</div><div class="review-source__label">{{AVIS_GOOGLE}} avis</div></a>'
'</div></div></section>\n' % (" section--alt" if rose else "", pa, pa))


def _precede_rose(avant):
    """Vrai si le dernier bloc de contenu avant l'appel final est déjà sur fond rosé."""
    blocs = re.findall(r'<(?:article|section|div) class="((?:article-body|section)(?:\s[^"]*)?)"', avant)
    return bool(blocs) and "section--alt" in blocs[-1]


def page(filename, title, desc, canonical, body, schema="", robots="index, follow",
         prefix="./", og_type="website", in_sub=False, extra_tail="", og_img=None, og_alt=None):
    p = "../" if in_sub else "./"
    pa = "../" if in_sub else ""  # pour assets/css/js (chemin relatif sans ./)
    if prefix == "/":  # chemins absolus depuis la racine (page 404, servie depuis n'importe quel dossier)
        p = pa = "/"
    head = (
'<!DOCTYPE html>\n<html lang="fr">\n<head>\n'
'<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
'<title>%s</title>\n<meta name="description" content="%s">\n'
'<meta name="robots" content="%s">\n<link rel="canonical" href="%s">\n'
'<meta property="og:type" content="%s">\n<meta property="og:title" content="%s">\n'
'<meta property="og:description" content="%s">\n<meta property="og:url" content="%s">\n'
'<meta property="og:image" content="https://lumia-salon.fr/assets/og-image.jpg">\n'
'<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
'<meta property="og:image:alt" content="Accueil de l\'institut LUMIA à Manosque, mur rouge en arche et comptoir en bois clair">\n'
'<meta property="og:site_name" content="LUMIA">\n<meta name="twitter:card" content="summary_large_image">\n'
'<meta property="og:locale" content="fr_FR">\n<meta name="theme-color" content="#A63524">\n'
'<link rel="icon" type="image/png" sizes="32x32" href="%sassets/favicon-32.png">\n'
'<link rel="apple-touch-icon" sizes="180x180" href="%sassets/apple-touch-icon.png">\n'
'<link rel="preload" href="%sassets/fonts/cormorant-garamond-600.woff2" as="font" type="font/woff2" crossorigin>\n'
'<link rel="preload" href="%sassets/fonts/nunito-sans.woff2" as="font" type="font/woff2" crossorigin>\n'
'<link rel="stylesheet" href="%scss/style.min.css">\n'
'<script src="%sannonces.js"></script>\n'
'<script src="%sjs/annonces-tete.min.js"></script>\n'
'%s</head>\n<body>\n'
% (title, desc, robots, canonical, og_type, title, desc, canonical, pa, pa, pa, pa, pa, pa, pa, schema))
    if og_img:  # image de partage propre à la page (articles illustrés)
        head = head.replace('content="https://lumia-salon.fr/assets/og-image.jpg"', 'content="%s"' % og_img)
        head = head.replace('content="Accueil de l\'institut LUMIA à Manosque, mur rouge en arche et comptoir en bois clair"', 'content="%s"' % og_alt)
    html = (head
        + '<a href="#main" class="skip-link">Aller au contenu principal</a>\n'
        + '<header class="site-header">' + topbar() + nav(p, filename) + '</header>\n'  # repère « banner » (24/11/2026)
        + body + footer(p) + mobile_cta()
        + '\n<script src="%sjs/main.min.js" defer></script>\n<script src="%sjs/annonces.min.js" defer></script>\n' % (pa, pa)
        + extra_tail
        + '</body>\n</html>\n')
    # M3 (24/11/2026) : bandeau d'avis avant l'appel final des pages intérieures.
    if filename in BANDEAU_PAGES:
        i = html.find('<section class="cta-section">')
        if i < 0:  # page sans appel final (contact) : bandeau en fin de contenu
            i = html.find('</main>')
        if i >= 0:
            html = html[:i] + bandeau_avis(pa, not _precede_rose(html[:i])) + html[i:]
    # M4c (24/11/2026) : « À partir de X € » sous le premier bloc de boutons, prix lu dans les tarifs.
    if filename in PRIX_PAGES:
        ids, filtre = PRIX_PAGES[filename]
        trouve = prix_depuis(ids, filtre)
        if trouve:
            ligne = ('<p class="prix-depuis">À partir de %d&nbsp;€ &middot; '
                     '<a href="%starifs.html#%s">voir les tarifs</a></p>' % (trouve[0], pa, trouve[1]))
            html = re.sub(r'(<div class="hero__actions">.*?</div>)', lambda m: m.group(1) + ligne, html, count=1, flags=re.S)
    for jeton, valeur in (("{{NOTE}}", NOTE), ("{{AVIS_PLANITY}}", AVIS_PLANITY),
                          ("{{AVIS_GOOGLE}}", AVIS_GOOGLE),
                          ("{{AVIS_TOTAL}}", AVIS_PLANITY + AVIS_GOOGLE),
                          ("{{AVIS_GOOGLE_URL}}", AVIS_GOOGLE_URL),
                          ("{{AVIS_GOOGLE_VOIR}}", AVIS_GOOGLE_VOIR)):
        html = html.replace(jeton, str(valeur))
    # R12 (23/11/2026) : l'en-tête de page (fil d'Ariane, H1) entre dans <main>,
    # sinon le lien d'évitement saute le H1 et l'en-tête devient un repère « banner » en double.
    html = re.sub(r'(<header class="page-header">.*?</header>)\s*<main id="main">',
                  lambda m: '<main id="main">\n' + m.group(1), html, count=1, flags=re.S)
    # R14 (23/11/2026) : un lien qui ouvre un nouvel onglet l'annonce aux lecteurs d'écran.
    html = re.sub(r'<a ([^>]*target="_blank"[^>]*)>(.*?)</a>', nouvel_onglet, html, flags=re.S)
    # R16 (23/11/2026) : variante 800 px servie aux écrans qui n'ont pas besoin de plus.
    html = re.sub(r'<img ([^>]*?)src="((?:\.\./|\./)?assets/)([\w-]+)\.webp"([^>]*)>', variante_800, html)
    for rel in VERSIONNES:
        html = html.replace(rel + '"', rel + "?v=" + version(rel) + '"')
    # Typographie française (24/11/2026) : espace insécable avant « : ; ? ! » dans le texte visible,
    # jamais dans les balises, les scripts ni les styles.
    morceaux = re.split(r'(<script\b.*?</script>|<style\b.*?</style>|<[^>]+>)', html, flags=re.S)
    for k in range(0, len(morceaux), 2):
        morceaux[k] = re.sub(r'(?<=\S) ([:;?!])(?=\s|$)', '\u00a0\\1', morceaux[k])
    html = ''.join(morceaux)
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
            '"provider":{"@type":"BeautySalon","@id":"https://lumia-salon.fr/#institut","name":"LUMIA","url":"https://lumia-salon.fr","telephone":"+33492876372",'
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
