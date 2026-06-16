#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages services, à-propos, tarifs, contact, légales, 404."""
from build_pages import *

# ============================ LPG CELLU M6 ============================
lpg_faq = [
 ("Combien de séances pour un résultat ?", "Une cure de 10 à 12 séances est souvent recommandée pour un objectif marqué (cellulite, fermeté), avec des photos de suivi à la 1re, la 6e et la 12e séance. Le bilan personnalisé précise votre programme."),
 ("À quel rythme faire les séances ?", "En général une à deux séances par semaine au début, pour enclencher les résultats, puis on espace en entretien. Le rythme est adapté à votre objectif et à votre peau."),
 ("Est-ce que le LPG fait maigrir ?", "Le LPG n'est pas un traitement amaigrissant. Il agit sur l'aspect de la peau, la cellulite, la fermeté et le drainage. Associé à une bonne hygiène de vie, il affine et lisse la silhouette."),
 ("Est-ce douloureux ?", "Non. La séance est confortable, beaucoup la décrivent comme un palper-rouler agréable et relaxant. L'intensité est réglée selon votre sensibilité."),
 ("Quelle différence entre le LPG corps et le LPG visage ?", "Le LPG corps cible la cellulite, le drainage et la fermeté sur des zones comme le ventre, les cuisses ou les bras. Le LPG visage travaille en douceur l'ovale, le regard, le cou et le décolleté pour raffermir et lisser."),
]
lpg_body = header_block(
  [("Accueil","./"),("LPG endermologie",None)],
  "LPG endermologie à Manosque",
  "Minceur, fermeté et drainage avec la technologie LPG Cellu M6 Alliance, pour le corps et le visage.") + """
<main id="main"><article class="article-body"><div class="container">
<p>Le LPG endermologie de LUMIA à Manosque utilise la technologie Cellu M6 Alliance pour agir sur la cellulite, la fermeté, le drainage et la silhouette, sur le corps comme sur le visage, chez les femmes et les hommes. Chaque programme démarre par un bilan personnalisé avec photos de suivi, et le bilan est offert pour tout achat de forfait. La technique est non invasive, confortable et adaptée à votre objectif.</p>
<div class="hero__actions"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a><a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA">04 92 87 63 72</a></div>

<h2>Le LPG pour le corps</h2>
<p>Sur le corps, l'endermologie cible la cellulite sous toutes ses formes, adipeuse, aqueuse ou fibreuse, et relance les échanges de la peau. Plusieurs protocoles existent : anti-cellulite, soin jeune maman, détox et palper-rouler drainant, ou simplement relaxation. Le travail mécanique de la tête Alliance stimule la peau en profondeur pour la lisser et la raffermir.</p>

<img src="assets/soinLPG.webp" class="portrait" alt="Soin LPG endermologie des jambes à l'institut LUMIA à Manosque" width="765" height="1020" loading="lazy">

<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Premier échange gratuit, réservez votre bilan</a></p>

<h2>Le LPG pour le visage</h2>
<p>Sur le visage, le LPG travaille zone par zone, du front au cou en passant par le regard, l'ovale, les mains ou le décolleté. Il raffermit, lisse et redonne de l'éclat, sans aiguille ni chirurgie. C'est une réponse douce aux premiers signes de l'âge, qui se marie très bien avec les soins du visage.</p>

<h2>Un suivi personnalisé</h2>
<p>Chaque parcours commence par un bilan où l'on définit ensemble vos objectifs. Des photos de suivi sont prises à la première, la sixième et la douzième séance pour mesurer la progression. Les cures se règlent en plusieurs fois sans frais, pour avancer sereinement.</p>

<h2>Questions fréquentes sur le LPG</h2>
%s
<p>Le LPG complète idéalement nos <a href="soins-visage-manosque.html">soins du visage</a> et notre <a href="epilation-laser-manosque.html">épilation laser</a>. Retrouvez le détail des prix sur la <a href="tarifs.html">page tarifs</a> et faites connaissance avec <a href="a-propos.html">la praticienne</a>.</p>
</div></article>
%s</main>
""" % (PLANITY, PLANITY, faq_html(lpg_faq), cta('Retrouvez une silhouette <span class="accent">légère</span>', "Réservez votre bilan LPG à Manosque. Il est offert pour tout achat de forfait."))
lpg_schema = (schema_service("LPG endermologie","LPG Cellu M6 à Manosque","Endermologie Cellu M6 Alliance pour la minceur, la fermeté et le drainage, corps et visage, à Manosque, par une infirmière diplômée d'État.","https://lumia-salon.fr/lpg-cellu-m6-manosque.html")
 + schema_faq(lpg_faq) + schema_breadcrumb([("Accueil",BASE),("LPG endermologie",BASE+"lpg-cellu-m6-manosque.html")]))
page("lpg-cellu-m6-manosque.html",
     "LPG Cellu M6 à Manosque : minceur & fermeté | LUMIA",
     "LPG endermologie à Manosque : minceur, fermeté et drainage avec Cellu M6 Alliance, corps et visage. Bilan offert pour tout achat de forfait. RDV en ligne.",
     "https://lumia-salon.fr/lpg-cellu-m6-manosque.html", lpg_body, lpg_schema)

# ============================ COSMELAN ============================
cos_faq = [
 ("Pour quels types de taches le Cosmelan est-il adapté ?", "Le protocole vise le mélasma, les taches solaires, l'hyperpigmentation post-inflammatoire et les taches liées à l'âge. Un diagnostic de peau préalable vérifie que votre type de taches s'y prête."),
 ("Combien de temps pour voir un résultat ?", "Une amélioration du teint s'observe souvent dans les premières semaines. Le protocole complet s'étale sur environ six mois, avec un suivi mensuel, car régulariser la pigmentation demande du temps."),
 ("Y a-t-il une éviction sociale ?", "Après la pose en cabine, la peau peut rougir et peler quelques jours, comme après un coup de soleil léger. On adapte le protocole à votre rythme de vie et on vous accompagne à chaque étape."),
 ("Quel entretien après le protocole ?", "Une routine d'entretien à la maison et une protection solaire quotidienne sont indispensables pour préserver les résultats. Des soins ponctuels peuvent compléter l'entretien."),
 ("Quelle différence avec un peeling ou un laser ?", "Le Cosmelan agit à la fois en estompant les taches et en régulant la production de mélanine, ce qui limite la réapparition. C'est un protocole dépigmentant progressif, distinct d'un peeling ponctuel ou d'un laser."),
]
cos_body = header_block(
  [("Accueil","./"),("Soins dépigmentants Cosmelan",None)],
  "Atténuer les taches du visage à Manosque",
  "Le protocole Cosmelan de Mesoestetic pour un teint plus uniforme, encadré par une infirmière D.E.") + """
<main id="main"><article class="article-body"><div class="container">
<p>Les soins dépigmentants Cosmelan de LUMIA à Manosque s'adressent à celles et ceux qui veulent atténuer les taches du visage : mélasma, taches solaires, hyperpigmentation post-inflammatoire ou taches liées à l'âge. Le protocole Cosmelan de Mesoestetic agit en deux temps, en cabine puis à la maison, avec un suivi sur plusieurs mois. Tout commence par un diagnostic de peau obligatoire, déductible du soin, pour vérifier que votre peau est adaptée.</p>
<div class="hero__actions"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a><a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA">04 92 87 63 72</a></div>

<h2>Comment agit le Cosmelan ?</h2>
<p>Le Cosmelan a une double action : il estompe les taches déjà présentes et régule la production de mélanine pour limiter leur réapparition. C'est cette approche en deux temps qui en fait un protocole de fond, et non un simple gommage de surface. Aucun résultat n'est garanti, mais le protocole est reconnu pour son efficacité sur les hyperpigmentations.</p>

<img src="assets/cosmelan.jpg" class="portrait" alt="Soin du teint et atténuation des taches du visage à l'institut LUMIA" width="600" height="750" loading="lazy">

<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Premier échange gratuit, réservez votre diagnostic</a></p>

<h2>Le déroulé du protocole</h2>
<p>Le parcours est cadré et accompagné de bout en bout.</p>
<ul>
<li><strong>Diagnostic de peau</strong> obligatoire (déductible du soin) pour évaluer vos taches et votre peau.</li>
<li><strong>Phase 1, en cabine</strong> : application du masque dépigmentant Cosmelan 1, remise d'un home pack.</li>
<li><strong>Phase 2, à la maison</strong> : application du Cosmelan 2 et d'une routine adaptée, selon un protocole précis.</li>
<li><strong>Suivi mensuel</strong> sur environ six mois, pour ajuster et préserver les résultats.</li>
</ul>
<p>Un soin apaisant post-Cosmelan est disponible pour accompagner la peau. La protection solaire quotidienne est indispensable pendant et après le protocole.</p>

<h2>Questions fréquentes sur le Cosmelan</h2>
%s
<p>Le Cosmelan se prolonge naturellement avec nos <a href="soins-visage-manosque.html">soins du visage</a>. Découvrez aussi <a href="a-propos.html">la praticienne</a> et les <a href="tarifs.html">tarifs</a>.</p>
</div></article>
%s</main>
""" % (PLANITY, PLANITY, faq_html(cos_faq), cta('Retrouvez un teint <span class="accent">uniforme</span>', "Réservez votre diagnostic de peau à Manosque. Il est déductible du soin en cabine."))
cos_schema = (schema_service("Soin dépigmentant","Soins dépigmentants Cosmelan à Manosque","Protocole Cosmelan de Mesoestetic pour atténuer les taches du visage (mélasma, taches solaires, hyperpigmentation) à Manosque, encadré par une infirmière diplômée d'État.","https://lumia-salon.fr/soin-cosmelan-taches-manosque.html")
 + schema_faq(cos_faq) + schema_breadcrumb([("Accueil",BASE),("Soins dépigmentants Cosmelan",BASE+"soin-cosmelan-taches-manosque.html")]))
page("soin-cosmelan-taches-manosque.html",
     "Traitement des taches Cosmelan à Manosque | LUMIA",
     "Soins dépigmentants Cosmelan à Manosque : atténuer mélasma et taches du visage avec Mesoestetic, encadré par une infirmière D.E. Diagnostic de peau préalable.",
     "https://lumia-salon.fr/soin-cosmelan-taches-manosque.html", cos_body, cos_schema)

print("services OK")
