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

<img src="assets/lpg-corps.webp" class="portrait" alt="Séance de LPG Cellu M6 Alliance en tenue Endermowear à l'institut LUMIA à Manosque" width="1066" height="1600" loading="lazy">

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
 ("Pour quels types de taches le COSMELAN est-il adapté ?", "Le protocole vise le mélasma, les taches solaires, l'hyperpigmentation post-inflammatoire et les taches liées à l'âge. Un diagnostic de peau préalable vérifie que votre type de taches s'y prête."),
 ("Combien de temps pour voir un résultat ?", "Une amélioration du teint s'observe souvent dans les premières semaines. Le protocole complet s'étale sur environ six mois, avec un suivi mensuel, car régulariser la pigmentation demande du temps."),
 ("Y a-t-il une éviction sociale ?", "Après la pose en cabine, la peau peut rougir et peler quelques jours, comme après un coup de soleil léger. On adapte le protocole à votre rythme de vie et on vous accompagne à chaque étape."),
 ("Quel entretien après le protocole ?", "Une routine d'entretien à la maison et une protection solaire quotidienne sont indispensables pour préserver les résultats. Des soins ponctuels peuvent compléter l'entretien."),
 ("Quelle différence avec un peeling ou un laser ?", "Le COSMELAN agit à la fois en estompant les taches et en régulant la production de mélanine, ce qui limite la réapparition. C'est un protocole dépigmentant progressif, distinct d'un peeling ponctuel ou d'un laser."),
]
cos_body = header_block(
  [("Accueil","./"),("Soins dépigmentants COSMELAN",None)],
  "Atténuer les taches du visage à Manosque",
  "Le protocole COSMELAN de Mesoestetic pour un teint plus uniforme, encadré par une infirmière D.E.") + """
<main id="main"><article class="article-body"><div class="container">
<p>Les soins dépigmentants COSMELAN de LUMIA à Manosque s'adressent à celles et ceux qui veulent atténuer les taches du visage : mélasma, taches solaires, hyperpigmentation post-inflammatoire ou taches liées à l'âge. Le protocole COSMELAN de Mesoestetic agit en deux temps, en cabine puis à la maison, avec un suivi sur plusieurs mois. Tout commence par un diagnostic de peau obligatoire, déductible du soin, pour vérifier que votre peau est adaptée.</p>
<div class="hero__actions"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a><a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA">04 92 87 63 72</a></div>

<h2>Comment agit le COSMELAN ?</h2>
<p>Le COSMELAN a une double action : il estompe les taches déjà présentes et régule la production de mélanine pour limiter leur réapparition. C'est cette approche en deux temps qui en fait un protocole de fond, et non un simple gommage de surface. Aucun résultat n'est garanti, mais le protocole est reconnu pour son efficacité sur les hyperpigmentations.</p>

<img src="assets/cosmelan.jpg" class="portrait" alt="Soin du teint et atténuation des taches du visage à l'institut LUMIA" width="732" height="1100" loading="lazy">

<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Premier échange gratuit, réservez votre diagnostic</a></p>

<h2>Le déroulé du protocole</h2>
<p>Le parcours est cadré et accompagné de bout en bout.</p>
<ul>
<li><strong>Diagnostic de peau</strong> obligatoire (déductible du soin) pour évaluer vos taches et votre peau.</li>
<li><strong>Phase 1, en cabine</strong> : application du masque dépigmentant COSMELAN 1, remise d'un home pack.</li>
<li><strong>Phase 2, à la maison</strong> : application du COSMELAN 2 et d'une routine adaptée, selon un protocole précis.</li>
<li><strong>Suivi mensuel</strong> sur environ six mois, pour ajuster et préserver les résultats.</li>
</ul>
<p>Un soin apaisant post-COSMELAN est disponible pour accompagner la peau. La protection solaire quotidienne est indispensable pendant et après le protocole.</p>

<h2>Questions fréquentes sur le COSMELAN</h2>
%s
<p>Le COSMELAN se prolonge naturellement avec nos <a href="soins-visage-manosque.html">soins du visage</a>. Découvrez aussi <a href="a-propos.html">la praticienne</a> et les <a href="tarifs.html">tarifs</a>.</p>
</div></article>
%s</main>
""" % (PLANITY, PLANITY, faq_html(cos_faq), cta('Retrouvez un teint <span class="accent">uniforme</span>', "Réservez votre diagnostic de peau à Manosque. Il est déductible du soin en cabine."))
cos_schema = (schema_service("Soin dépigmentant","Soins dépigmentants COSMELAN à Manosque","Protocole COSMELAN de Mesoestetic pour atténuer les taches du visage (mélasma, taches solaires, hyperpigmentation) à Manosque, encadré par une infirmière diplômée d'État.","https://lumia-salon.fr/soin-cosmelan-taches-manosque.html")
 + schema_faq(cos_faq) + schema_breadcrumb([("Accueil",BASE),("Soins dépigmentants COSMELAN",BASE+"soin-cosmelan-taches-manosque.html")]))
page("soin-cosmelan-taches-manosque.html",
     "Traitement des taches COSMELAN à Manosque | LUMIA",
     "Soins dépigmentants COSMELAN à Manosque : atténuer mélasma et taches du visage avec Mesoestetic, encadré par une infirmière D.E. Diagnostic de peau préalable.",
     "https://lumia-salon.fr/soin-cosmelan-taches-manosque.html", cos_body, cos_schema)

print("services OK")


# ============================ MICRONEEDLING ============================
mn_faq = [
 ("Le microneedling, est-ce une injection ?", "Non, il n'y a aucune injection de produit. Le stylo crée de micro-perforations contrôlées à la surface de la peau, à une profondeur de 0,25 mm, qui déclenchent sa régénération naturelle et font pénétrer les actifs appliqués."),
 ("Est-ce que c'est douloureux ?", "La sensation est celle de petits picotements, variable selon la zone et la profondeur réglée. La profondeur est adaptée à votre peau et à la zone traitée, et la séance reste confortable."),
 ("Combien de séances faut-il prévoir ?", "Le protocole conseillé est une cure de six séances, à raison d'une séance tous les quinze jours, pour une régénération complète et des résultats durables. Des séances d'entretien tous les deux mois sont ensuite vivement recommandées."),
 ("Est-ce adapté à ma peau ?", "Le microneedling convient à tous les phototypes, des peaux claires aux peaux foncées. Un rendez-vous de diagnostic préalable permet de vérifier qu'aucune contre-indication ne s'applique et de choisir les actifs adaptés à votre peau."),
 ("Quelles sont les précautions à prendre ?", "Aucune exposition au soleil dans les sept jours qui précèdent et les sept jours qui suivent la séance, avec une protection SPF 50+ obligatoire. Le soin est contre-indiqué en cas de grossesse ou d'allaitement, d'acné inflammatoire, de traitement à l'isotrétinoïne, de plaie ouverte, d'herpès, de traitement anticoagulant, ou de radiothérapie et cancer de moins de cinq ans. Tout est vérifié lors du diagnostic."),
]

mn_body = header_block(
  [("Accueil","./"),("Microneedling",None)],
  "Microneedling à Manosque",
  "La micro-stimulation de la peau avec les actifs Mesoestetic aux exosomes : rides, éclat, pores dilatés et cicatrices d'acné.") + """
<main id="main"><article class="article-body"><div class="container">
<p>Le microneedling, ou micro-stimulation, est un soin de régénération de la peau proposé à l'institut LUMIA à Manosque. Grâce à de micro-perforations contrôlées, réalisées à une profondeur de 0,25 mm, il stimule la production naturelle de collagène et d'élastine, pour une peau plus lisse, plus ferme, plus lumineuse et un grain de peau affiné. Il est réalisé par une infirmière diplômée d'État, avec des actifs brevetés de la marque Mesoestetic.</p>
<div class="hero__actions"><a href="" + PLANITY + "" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a><a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA">04 92 87 63 72</a></div>

<div class="callout"><h3>Sans aucune injection</h3><p>Le microneedling ne comporte <strong>aucune injection de produit</strong>. Le stylo médical crée de minuscules canaux à la surface de la peau : c'est la réponse naturelle de régénération de votre peau qui fait le travail, aidée par les actifs appliqués en surface.</p></div>

<h2>Ce que le microneedling traite</h2>
<p>Ce soin agit sur les rides et les ridules, le teint terne ou fatigué, le manque d'éclat, le relâchement cutané du visage, les pores dilatés, l'excès de sébum et les cicatrices d'acné. Il est adapté à tous les phototypes de peau, des plus claires aux plus foncées.</p>

<img src="assets/microneedling.webp" class="portrait" alt="Stylo de microneedling réglé à 0,25 mm, utilisé pour la micro-stimulation du visage à l'institut LUMIA à Manosque" width="904" height="1600" loading="lazy">

<h2>Les actifs Mesoestetic aux exosomes</h2>
<p>Les actifs utilisés sont de la marque Mesoestetic, brevetés pour leur efficacité grâce aux exosomes et au PDRN présents dans leur formule. Le choix des actifs se fait avec vous avant la séance, selon votre objectif : anti-âge fermeté, anti-âge global, contour des yeux pour les cernes, les poches, les pattes d'oie et la pigmentation, ou dépigmentation pour les taches, le mélasma et les marques post-inflammatoires.</p>

<h2>Comment se déroule une séance</h2>
<p>Tout commence par un rendez-vous de diagnostic du visage de 30 minutes. Nous discutons de votre projet et de vos problématiques, et nous définissons ensemble le protocole personnalisé. Un questionnaire de santé, un consentement mutuel et une fiche d'information sur le microneedling sont signés avant de pouvoir débuter les soins.</p>
<p>La séance de microneedling dure ensuite une heure et traite le visage et le cou. La LED est incluse lors de la pose du masque, pour apaiser la peau et potentialiser les résultats. Il est également possible de traiter uniquement le décolleté.</p>

<img src="assets/microneedling-soin.webp" class="portrait" alt="Séance de microneedling du visage à l'institut LUMIA à Manosque, stylo de micro-stimulation et luminothérapie" width="898" height="1600" loading="lazy">

<p class="text-center mt-2"><a href="" + PLANITY + "" target="_blank" rel="noopener" class="btn btn-primary">Réservez votre diagnostic visage</a></p>

<h2>Le protocole recommandé</h2>
<p>Pour une régénération complète et des résultats durables, le microneedling se pratique en cure : une séance tous les quinze jours, pendant six séances. Des séances d'entretien, une fois tous les deux mois, sont ensuite fortement conseillées pour maintenir le bénéfice.</p>

<div class="callout"><h3>Avant et après la séance</h3><p>Aucune exposition au soleil ni aux UV dans les sept jours avant et les sept jours après la séance. Une protection solaire SPF 50+ est <strong>obligatoire</strong>. Les contre-indications, notamment la grossesse et l'allaitement, l'acné inflammatoire, les traitements à base d'isotrétinoïne, les plaies ouvertes, l'herpès, les tatouages sur la zone, les anticoagulants, les maladies auto-immunes à expression cutanée et les antécédents de radiothérapie ou de cancer de moins de cinq ans, sont systématiquement vérifiées lors du diagnostic.</p></div>

<h2>Questions fréquentes sur le microneedling</h2>
%s
<p>Le microneedling se marie très bien avec nos <a href="soins-visage-manosque.html">soins du visage</a> et avec le <a href="lpg-cellu-m6-manosque.html">LPG visage</a>. Pour les taches pigmentaires installées, découvrez aussi le <a href="soin-cosmelan-taches-manosque.html">protocole COSMELAN</a>. Les prix sont détaillés sur la <a href="tarifs.html">page tarifs</a>, et vous pouvez faire connaissance avec <a href="a-propos.html">la praticienne</a>.</p>
</div></article>
%s</main>
""" % (faq_html(mn_faq), cta('Réveillez l\'<span class="accent">éclat</span> de votre peau', "Réservez votre diagnostic visage à Manosque. Nous définissons ensemble le protocole adapté à votre peau."))

mn_schema = (schema_service("Microneedling","Microneedling à Manosque","Micro-stimulation de la peau avec actifs Mesoestetic aux exosomes à Manosque : rides, éclat, pores dilatés, cicatrices d'acné. Par une infirmière diplômée d'État.","https://lumia-salon.fr/microneedling-manosque.html")
 + schema_faq(mn_faq) + schema_breadcrumb([("Accueil",BASE),("Microneedling",BASE+"microneedling-manosque.html")]))
page("microneedling-manosque.html",
     "Microneedling à Manosque : anti-âge & éclat | LUMIA",
     "Microneedling à Manosque avec les actifs Mesoestetic aux exosomes : rides, pores dilatés, cicatrices d'acné, éclat. Sans injection, tous phototypes. RDV en ligne.",
     "https://lumia-salon.fr/microneedling-manosque.html", mn_body, mn_schema)
