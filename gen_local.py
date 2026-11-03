#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les 5 pages locales d'épilation laser, contenu unique par ville."""
from build_pages import *

CITIES = [
 {
  "slug":"forcalquier","ville":"Forcalquier","img":"machinelaserlunettes.webp",
  "intro":"Vous habitez Forcalquier ou ses environs et cherchez une épilation laser définitive sérieuse ? L'institut LUMIA vous accueille à Manosque, à une vingtaine de minutes de la cité comtale par la D4100 puis la D13. L'épilation laser y est réalisée par Margaux, infirmière diplômée d'État formée au laser, avec un bilan personnalisé offert pour tout achat de séance ou de cure.",
  "why":"Depuis Forcalquier, le trajet est direct et rapide, et l'institut est facile d'accès au centre de Manosque, avec plusieurs parkings gratuits à proximité. Vous y trouvez un cadre cocon, une praticienne unique qui vous suit d'une séance à l'autre, et un laser diode Leaseir adapté à de nombreux phototypes. De quoi en finir durablement avec le rasage et la cire sans renoncer à la proximité.",
  "access":"Comptez environ 25 minutes depuis Forcalquier. L'institut se situe au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL.",
  "faq_access":("Depuis Forcalquier, combien de temps pour venir à l'institut ?","L'institut LUMIA est à environ 25 minutes de Forcalquier, au centre de Manosque, par la D4100 puis la D13. Plusieurs parkings gratuits se trouvent à proximité immédiate."),
 },
 {
  "slug":"greoux-les-bains","ville":"Gréoux-les-Bains","img":"laserhomme.webp",
  "intro":"À Gréoux-les-Bains, station thermale réputée, prendre soin de soi est une habitude. Pour une épilation laser définitive, l'institut LUMIA vous reçoit à Manosque, à une vingtaine de minutes par la D8 puis la D907. Les séances sont assurées par une infirmière diplômée d'État formée au laser, et le premier bilan est offert pour tout achat de séance ou de cure.",
  "why":"Curistes de passage ou habitants de Gréoux-les-Bains, vous profitez à LUMIA d'un accompagnement personnalisé et d'un laser diode Leaseir adapté à de nombreux types de peau. La même praticienne vous suit à chaque séance, dans un cadre calme et confidentiel, pour un parcours d'épilation construit sur-mesure.",
  "access":"Comptez environ 20 minutes depuis Gréoux-les-Bains. L'institut se situe au 10 Bis avenue Jean Giono, à Manosque, à côté de l'opticien ATOL.",
  "faq_access":("Depuis Gréoux-les-Bains, comment venir à l'institut ?","Gréoux-les-Bains est à une vingtaine de minutes de Manosque par la D8 puis la D907. L'institut LUMIA se trouve au centre, 10 Bis avenue Jean Giono, avec des parkings gratuits à proximité."),
 },
 {
  "slug":"pierrevert","ville":"Pierrevert","img":"enseigne.webp","img_class":"portrait",
  "intro":"Pierrevert est la porte sud de Manosque : l'institut LUMIA n'est qu'à une dizaine de minutes de votre village, au cœur de la commune voisine. Pour une épilation laser définitive de proximité, vous y êtes accueilli par Margaux, infirmière diplômée d'État formée au laser, avec un bilan personnalisé offert pour tout achat de séance ou de cure.",
  "why":"Entre le golf, le vignoble de l'AOC Pierrevert et le centre de Manosque, le trajet est court et pratique. À LUMIA, vous bénéficiez d'un suivi par une infirmière, d'un laser diode Leaseir adapté à de nombreux phototypes et d'un cadre cocon, à deux pas de chez vous. L'idéal pour traiter le visage comme le corps, à votre rythme.",
  "access":"Comptez environ 10 minutes depuis Pierrevert. L'institut se situe au 10 Bis avenue Jean Giono, à Manosque, à côté de l'opticien ATOL.",
  "faq_access":("Depuis Pierrevert, à quelle distance se trouve l'institut ?","Pierrevert jouxte Manosque : comptez environ 10 minutes en voiture. L'institut LUMIA est au 10 Bis avenue Jean Giono, avec des parkings gratuits à proximité immédiate."),
 },
 {
  "slug":"oraison","ville":"Oraison","img":"machinelaser.webp","img_class":"portrait",
  "intro":"Vous venez d'Oraison, au bord de la Durance, et souhaitez vous lancer dans l'épilation laser définitive ? L'institut LUMIA vous reçoit à Manosque, à une vingtaine de minutes par la D4096 puis la D907. Les séances sont réalisées par une infirmière diplômée d'État formée au laser, et le bilan personnalisé est offert pour tout achat de séance ou de cure.",
  "why":"Depuis Oraison, l'accès à Manosque est simple et le centre-ville facile à rejoindre. À LUMIA, vous trouvez une praticienne unique qui vous suit dans le temps, un laser diode Leaseir adapté à de nombreux types de peau et un accueil chaleureux. En finir avec le rasage et la cire devient un projet serein et accompagné.",
  "access":"Comptez environ 20 minutes depuis Oraison. L'institut se situe au 10 Bis avenue Jean Giono, à Manosque, à côté de l'opticien ATOL.",
  "faq_access":("Depuis Oraison, combien de temps de trajet ?","Oraison est à une vingtaine de minutes de Manosque par la D4096 puis la D907. L'institut LUMIA se situe au centre, 10 Bis avenue Jean Giono, avec des parkings gratuits à proximité."),
 },
 {
  "slug":"valensole","ville":"Valensole","img":"machinelaserlunettes.webp",
  "intro":"Sur le plateau de Valensole, célèbre pour ses champs de lavande, l'épilation laser définitive se prépare à l'institut LUMIA, à Manosque, à environ 25 minutes par la D6. Les séances sont assurées par Margaux, infirmière diplômée d'État formée au laser, avec un premier bilan offert pour tout achat de séance ou de cure.",
  "why":"Depuis Valensole, descendre à Manosque pour ses soins est l'occasion d'un vrai moment pour soi. À LUMIA, vous profitez d'un suivi par une infirmière, d'un laser diode Leaseir adapté à de nombreux phototypes et d'un cadre cocon. Le protocole est défini ensemble lors du bilan, puis ajusté séance après séance.",
  "access":"Comptez environ 25 minutes depuis Valensole. L'institut se situe au 10 Bis avenue Jean Giono, à Manosque, à côté de l'opticien ATOL.",
  "faq_access":("Depuis Valensole, comment rejoindre l'institut ?","Valensole est à environ 25 minutes de Manosque par la D6. L'institut LUMIA se trouve au 10 Bis avenue Jean Giono, au centre, avec des parkings gratuits à proximité."),
 },
]

for c in CITIES:
    ville = c["ville"]; slug = c["slug"]
    url = "https://lumia-salon.fr/epilation-laser-%s.html" % slug
    imgcls = c.get("img_class","landscape")
    w,h = ("1360","907") if imgcls=="landscape" else ("765","1020")
    faq = [
      c["faq_access"],
      ("Combien de séances d'épilation laser faut-il ?","En moyenne 6 à 10 séances selon la zone, la couleur du poil et votre type de peau. Le bilan préalable précise votre protocole et le nombre de séances estimé."),
      ("Le laser convient-il à ma peau ?","Le laser diode utilisé cible la mélanine du poil et convient à de nombreux phototypes. Une peau récemment bronzée fait reporter la séance, et les poils blancs, blonds ou roux ne réagissent pas. Le bilan vérifie l'adéquation."),
      ("Le bilan est-il vraiment offert ?","Le bilan personnalisé, obligatoire avant la première séance, coûte 20 euros et il est offert pour tout achat de séance ou de cure."),
    ]
    body = header_block(
      [("Accueil","./"),("Épilation laser",("epilation-laser-manosque.html")),("Épilation laser à %s" % ville, None)],
      "Épilation laser définitive à %s" % ville,
      "L'institut LUMIA accueille les habitants de %s à Manosque, avec une infirmière D.E." % ville) + ("""
<main id="main"><article class="article-body"><div class="container">
<p>%s</p>
<div class="hero__actions"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a><a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA">04 92 87 63 72</a></div>

<h2>Pourquoi venir de %s chez LUMIA ?</h2>
<p>%s</p>

<img src="assets/%s" class="%s" alt="Épilation laser diode Leaseir à l'institut LUMIA, près de %s" width="%s" height="%s" loading="lazy">

<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Premier échange gratuit, réservez votre bilan</a></p>

<h2>L'épilation laser à l'institut</h2>
<p>Le déroulement est le même pour toutes nos clientes et clients : un bilan obligatoire avant la première séance, le port de lunettes de protection, un rasage préalable de la zone, puis le passage du laser avec refroidissement. Pour tout savoir sur la méthode, les zones traitées et les précautions, consultez notre page complète sur l'<a href="epilation-laser-manosque.html">épilation laser définitive à Manosque</a>.</p>

<h2>Accès depuis %s</h2>
<p>%s Plusieurs parkings gratuits se trouvent à proximité : Dr Joubert, Monoprix, La Poste et Souvenir Français.</p>

<h2>Questions fréquentes</h2>
%s
<p>Découvrez aussi <a href="a-propos.html">la praticienne</a>, nos <a href="soins-visage-manosque.html">soins du visage</a> et les <a href="tarifs.html">tarifs</a>.</p>
</div></article>
%s</main>
""" % (c["intro"], PLANITY, ville, c["why"], c["img"], imgcls, ville, w, h, PLANITY, ville, c["access"], faq_html(faq),
       cta('Épilation laser à <span class="accent">%s</span>' % ville, "Réservez votre bilan à Manosque. Il est offert pour tout achat de séance ou de cure.")))
    schema = (schema_service("Épilation laser","Épilation laser définitive à %s" % ville,
              "Épilation laser définitive pour les habitants de %s, réalisée à Manosque par une infirmière diplômée d'État. Laser diode adapté à de nombreux phototypes, bilan offert." % ville, url)
              .replace('"areaServed":{"@type":"City","name":"Manosque"}', '"areaServed":{"@type":"City","name":"%s"}' % ville)
              + schema_faq(faq)
              + schema_breadcrumb([("Accueil",BASE),("Épilation laser",BASE+"epilation-laser-manosque.html"),("Épilation laser à %s" % ville, url)]))
    page("epilation-laser-%s.html" % slug,
         "Épilation laser à %s | LUMIA Manosque" % ville,
         "Épilation laser définitive pour %s : l'institut LUMIA vous accueille à Manosque, par une infirmière D.E. Laser diode, bilan offert. Réservation en ligne." % ville,
         url, body, schema)
print("locales OK")
