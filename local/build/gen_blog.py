#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère le blog : articles.json, blog.html (listing) et ses articles."""
import json, os
from build_pages import *

# Date de la dernière révision du blog (illustrations, maillage, relecture). À avancer
# à chaque révision réelle des articles, jamais sans changement de contenu.
MAJ_BLOG = "2026-11-24"

def schema_article(title, desc, img, iso, url, maj=None):
    return ('<script type="application/ld+json">\n'
    '{ "@context":"https://schema.org","@type":"Article","headline":"%s","description":"%s",'
    '"image":"https://lumia-salon.fr/assets/%s","datePublished":"%s","dateModified":"%s",'
    '"author":{"@type":"Person","name":"Margaux","url":"https://lumia-salon.fr/a-propos.html"},'
    '"publisher":{"@type":"Organization","@id":"https://lumia-salon.fr/#institut","name":"LUMIA","url":"https://lumia-salon.fr","logo":{"@type":"ImageObject","url":"https://lumia-salon.fr/assets/logo.png"}},'
    '"mainEntityOfPage":"%s" }\n</script>\n' % (title, desc, img, iso, max(iso, maj or iso), url))

ARTICLES = [
 {
  "maillage":(0,"Avant la toute première séance, quelques gestes simples comptent : ils sont détaillés dans notre article pour <a href=\"preparer-premiere-seance-epilation-laser.html\">bien préparer sa première séance d'épilation laser</a>."),
  "illu_alt":"Illustration : dix cercles du plein au pâle sur un arc, avec un poil qui s'affine à chaque séance, comme un calendrier",
  "slug":"epilation-laser-combien-de-seances.html","tag":"Épilation laser","date":"Janvier 2026","iso":"2026-01-15","read":"7 min",
  "img":"machinelaserlunettes.webp",
  "title":"Épilation laser : combien de séances faut-il vraiment ?",
  "seo_title":"Épilation laser : combien de séances faut-il ? | LUMIA",
  "lien_sec":3,"lien":"Pour la méthode, les zones traitées et le déroulement d'une séance, consultez notre page sur l'<a href=\"../epilation-laser-manosque.html\">épilation laser définitive à Manosque</a>.",
  "desc":"Le nombre de séances d'épilation laser dépend de la zone, du poil et de la peau. On vous explique ce qui fait varier ce chiffre et à quoi vous attendre.",
  "lead":"C'est la première question que l'on nous pose : combien de séances pour en finir avec le poil ? La réponse honnête tient en une fourchette, 8 à 12 séances en moyenne, mais le vrai chiffre dépend de vous. Voici ce qui le fait varier.",
  "sections":[
   ("Une moyenne de 8 à 12 séances",[
    "En épilation laser définitive, on observe le plus souvent un résultat durable au bout de 8 à 12 séances. Cette fourchette n'est pas un hasard : le laser n'agit que sur les poils en phase de croissance, et à un instant donné, seule une partie de votre pilosité est dans cette phase. Il faut donc plusieurs passages, espacés dans le temps, pour traiter l'ensemble des poils au bon moment de leur cycle.",
    "Chez LUMIA, le nombre de séances estimé est précisé lors du bilan, qui est obligatoire avant la première séance et offert pour tout achat. C'est à ce moment que l'on examine votre peau et votre poil pour construire un protocole réaliste."]),
   ("Ce qui fait varier le nombre de séances",[
    "Trois facteurs principaux pèsent sur le compteur. D'abord la zone : le visage et les zones influencées par les hormones, comme le menton ou le maillot, demandent souvent davantage de séances que les jambes ou les aisselles. Ensuite la couleur et l'épaisseur du poil : un poil foncé et épais réagit mieux qu'un poil fin ou clair. Enfin votre type de peau et votre pilosité de départ, plus ou moins dense.",
    "Les facteurs hormonaux jouent un rôle particulier. Une grossesse, certains traitements ou des déséquilibres hormonaux peuvent relancer la pousse et nécessiter des séances d'entretien. Cela ne remet pas en cause le résultat, mais explique pourquoi deux personnes n'auront pas exactement le même parcours."]),
   ("Quel espacement entre les séances ?",[
    "Au début, les séances sont espacées de 6 à 8 semaines, le temps que la repousse se manifeste. Au fil du protocole, comme il reste de moins en moins de poils actifs, on espace progressivement les rendez-vous. L'intervalle est ajusté à chaque séance en fonction de ce que l'on observe, plutôt que figé à l'avance.",
    "Respecter cet espacement est important : revenir trop tôt n'accélère pas le résultat, car les poils ciblés ne sont pas encore en phase de croissance."]),
   ("Et après, est-ce vraiment définitif ?",[
    "On parle d'épilation durable plutôt que définitive à 100 pour cent. Concrètement, la grande majorité des poils traités ne repoussent plus. Quelques poils peuvent réapparaître avec le temps, souvent plus fins et plus clairs, et une simple séance d'entretien annuelle suffit en général à les maîtriser.",
    "L'objectif réaliste, c'est une peau nette et un confort retrouvé au quotidien, sans le cycle sans fin du rasage et de la cire."]),
  ],
  "faq":[
   ("Pourquoi faut-il plusieurs séances ?","Parce que le laser n'agit que sur les poils en phase de croissance, et qu'ils n'y sont pas tous en même temps. Plusieurs séances espacées permettent de traiter l'ensemble de la pilosité au bon moment."),
   ("Combien de séances pour le maillot ou le visage ?","Ces zones, souvent influencées par les hormones, demandent fréquemment plus de séances que les jambes ou les aisselles. Le bilan précise une estimation adaptée à votre cas."),
  ],
 },
 {
  "maillage":(2,"Pour estimer la durée totale de votre parcours, lisez aussi <a href=\"epilation-laser-combien-de-seances.html\">combien de séances d'épilation laser prévoir</a>."),
  "illu_alt":"Illustration : un soleil tenu à distance par une ombrelle rayée, à côté d'un calendrier de dix cases cochées",
  "slug":"epilation-laser-peau-bronzee.html","tag":"Épilation laser","date":"Février 2026","iso":"2026-02-15","read":"6 min",
  "img":"ambiance-2.webp",
  "title":"Épilation laser et peau bronzée : ce qu'il faut savoir avant l'été",
  "seo_title":"Épilation laser et peau bronzée avant l'été | LUMIA",
  "lien_sec":1,"lien":"Retrouvez la méthode et les zones traitées sur notre page <a href=\"../epilation-laser-manosque.html\">épilation laser à Manosque</a>.",
  "desc":"Bronzage et laser ne font pas bon ménage. On explique pourquoi, combien de temps attendre (10 jours avant et après) et organiser ses séances avant l'été.",
  "lead":"Chaque printemps, la même question revient : peut-on faire du laser quand on est bronzé ? La réponse demande un peu de nuance, car c'est surtout une affaire de sécurité pour votre peau. Voici les repères à connaître avant l'été.",
  "sections":[
   ("Pourquoi le bronzage pose problème",[
    "Le laser cible la mélanine, le pigment qui colore le poil. Or le bronzage, c'est justement une augmentation de la mélanine dans la peau. Sur une peau bronzée, le laser risque de ne plus faire la différence entre le poil et la peau, ce qui augmente le risque de réaction (rougeurs, taches, voire brûlure superficielle).",
    "C'est pour cette raison qu'une peau récemment exposée n'est pas traitée : on attend que le bronzage s'estompe pour travailler en sécurité."]),
   ("Combien de temps attendre ?",[
    "La règle de prudence est d'éviter le soleil, les UV et l'autobronzant pendant 10 jours avant chaque séance, et 10 jours après. L'autobronzant compte aussi, car il colore la peau et fausse le repère du laser.",
    "Si vous avez prévu des vacances au soleil, mieux vaut anticiper et caler vos séances en dehors de ces périodes. Le bilan permet d'organiser le calendrier avec vous."]),
   ("Comment organiser ses séances autour de l'été",[
    "L'idéal est de commencer son protocole à l'automne ou en hiver, lorsque la peau n'est pas bronzée et que l'exposition est faible. On enchaîne ainsi plusieurs séances dans de bonnes conditions, et l'on arrive à l'été avec une pilosité déjà bien réduite.",
    "En été, on peut poursuivre à condition de protéger scrupuleusement les zones traitées et d'éviter le soleil direct. C'est pourquoi de nombreuses clientes profitent de la saison froide pour avancer le plus gros du parcours."]),
   ("Les bons réflexes avant et après une séance",[
    "Avant la séance, on rase la zone (on n'arrache pas le poil), on ne s'expose pas et on signale tout changement de traitement ou de peau. Après la séance, on apaise la peau, on applique une protection solaire élevée sur les zones exposées et on évite la chaleur intense pendant 48 heures.",
    "Ces précautions simples garantissent à la fois l'efficacité du traitement et la sécurité de votre peau."]),
  ],
  "faq":[
   ("Peut-on faire du laser en été ?","Oui, à condition de ne pas être bronzé et de protéger soigneusement les zones traitées. Beaucoup préfèrent toutefois avancer leur protocole en automne et en hiver."),
   ("L'autobronzant empêche-t-il une séance ?","Oui. L'autobronzant colore la peau et fausse le repère du laser. Il faut l'éviter 10 jours avant une séance."),
  ],
 },
 {
  "maillage":(1,"Quelle que soit la technique, une peau récemment bronzée impose d'attendre : notre article sur <a href=\"epilation-laser-peau-bronzee.html\">l'épilation laser et la peau bronzée</a> explique pourquoi."),
  "illu_alt":"Illustration : un faisceau fin et précis face à un large éventail de lumière diffuse, vers une même cible ronde",
  "slug":"epilation-laser-ou-lumiere-pulsee.html","tag":"Épilation laser","date":"Mars 2026","iso":"2026-03-15","read":"7 min",
  "img":"machinelaser.webp",
  "title":"Épilation laser ou lumière pulsée : quelles différences ?",
  "seo_title":"Épilation laser ou lumière pulsée : les différences | LUMIA",
  "lien_sec":3,"lien":"Notre page sur l'<a href=\"../epilation-laser-manosque.html\">épilation laser diode à Manosque</a> détaille la méthode et le déroulement d'une séance.",
  "desc":"Laser et lumière pulsée (IPL) reposent sur des principes proches mais ne se valent pas. On compare efficacité, précision et usage en institut pour bien choisir.",
  "lead":"On confond souvent le laser et la lumière pulsée, ou IPL. Les deux ciblent la mélanine du poil, mais leur fonctionnement et leurs résultats diffèrent. Voici de quoi y voir clair avant de vous lancer.",
  "sections":[
   ("Deux technologies, un même objectif",[
    "Le laser et la lumière pulsée visent le même but : détruire le follicule pileux en chauffant la mélanine du poil. La différence se joue dans la lumière émise. Le laser produit une lumière monochromatique, d'une seule longueur d'onde, très ciblée. La lumière pulsée émet un spectre large, moins concentré.",
    "Cette distinction technique a des conséquences concrètes sur la précision et l'efficacité du traitement."]),
   ("Précision et efficacité",[
    "Parce qu'il est monochromatique et concentré, le laser cible le poil avec davantage de précision et délivre son énergie de façon plus homogène. En pratique, il est souvent considéré comme plus efficace et plus régulier, notamment sur les poils foncés et les zones étendues.",
    "La lumière pulsée peut donner de bons résultats, mais son spectre large se disperse davantage. C'est une technologie que l'on retrouve aussi dans des appareils domestiques, généralement moins puissants que le matériel professionnel."]),
   ("L'importance de la personne qui réalise le soin",[
    "La technologie ne fait pas tout. Le réglage de l'appareil selon votre peau et votre poil, le respect des contre-indications et le suivi des séances comptent autant que la machine. À l'institut LUMIA, l'épilation laser est réalisée par une infirmière diplômée d'État formée au laser, qui adapte chaque paramètre à votre cas.",
    "C'est cette combinaison, un laser diode professionnel et un encadrement rigoureux, qui fait la différence sur la durée."]),
   ("Que choisir ?",[
    "Pour un objectif d'épilation durable sur des poils foncés, le laser diode reste la référence en institut. La lumière pulsée domestique peut convenir pour entretenir ou dépanner, mais avec des résultats généralement moins nets et moins durables.",
    "Le bilan préalable est l'occasion d'évaluer votre pilosité et de vérifier que le laser est adapté à votre peau."]),
  ],
  "faq":[
   ("Le laser est-il plus efficace que la lumière pulsée ?","Le laser, monochromatique et concentré, cible le poil avec plus de précision et donne généralement des résultats plus réguliers, en particulier sur les poils foncés."),
   ("Les appareils maison valent-ils l'institut ?","Ils sont généralement moins puissants et moins précis. Pour un résultat durable et encadré, le matériel professionnel et le suivi d'une praticienne font la différence."),
  ],
 },
 {
  "maillage":(0,"Et si vous hésitez encore sur la technique, notre comparatif <a href=\"epilation-laser-ou-lumiere-pulsee.html\">laser ou lumière pulsée</a> fait le point."),
  "illu_alt":"Illustration : un profil masculin tracé d'un seul trait, une barbe en pointillés qui s'estompe et un rasoir de sûreté",
  "slug":"epilation-laser-homme.html","tag":"Épilation laser","date":"Avril 2026","iso":"2026-04-15","read":"6 min",
  "img":"laserhomme.webp",
  "title":"Épilation laser homme : torse, dos, barbe",
  "lien_sec":3,"lien":"Les zones traitées, la méthode et les précautions sont détaillées sur notre page <a href=\"../epilation-laser-manosque.html\">épilation laser à Manosque</a>.",
  "desc":"L'épilation laser n'est pas réservée aux femmes. Torse, dos, épaules, nuque ou contour de barbe : ce que les hommes peuvent traiter et comment ça se passe.",
  "lead":"De plus en plus d'hommes franchissent le pas de l'épilation laser, par confort, par esthétique ou pour en finir avec les poils incarnés. Voici les zones les plus demandées et ce qu'il faut savoir.",
  "sections":[
   ("Une demande qui n'a plus rien d'exceptionnel",[
    "Le dos, le torse, les épaules, la nuque, le contour de barbe ou encore les oreilles : autant de zones où la pilosité masculine peut gêner. L'épilation laser y répond de façon durable, sans le cycle du rasage qui irrite et favorise les poils incarnés.",
    "À l'institut LUMIA, les hommes sont accueillis comme les femmes, avec le même bilan préalable et le même suivi personnalisé."]),
   ("Les zones les plus traitées chez l'homme",[
    "Le torse et le dos arrivent en tête, souvent pour une question de confort et d'esthétique. Le contour de barbe est très demandé pour dessiner une ligne nette et réduire les poils incarnés au niveau du cou. La nuque, les épaules et les oreilles complètent les zones courantes.",
    "Chaque zone a ses particularités : la barbe, par exemple, est une zone dense et parfois influencée par les hormones, ce qui peut demander davantage de séances."]),
   ("Comment se passe une séance",[
    "Le déroulement est identique à celui des autres zones : bilan obligatoire avant de commencer, port de lunettes de protection, rasage préalable, puis passage du laser avec refroidissement. La sensation ressemble à de petits picotements de chaleur, bien supportables grâce au système de refroidissement.",
    "Sur les grandes surfaces comme le dos, la séance dure plus longtemps, mais le laser diode permet de couvrir efficacement de larges zones."]),
   ("Combien de séances et quel entretien",[
    "Comme pour tout le monde, comptez en moyenne 8 à 12 séances, parfois davantage sur les zones denses ou hormonales. Entre les séances, on ne s'épile qu'au rasoir, jamais à la cire ni à la pince. Un entretien ponctuel peut être utile sur certaines zones.",
    "Le bilan permet d'estimer le protocole adapté à votre pilosité et à vos objectifs."]),
  ],
  "faq":[
   ("Les hommes peuvent-ils faire épiler leur barbe au laser ?","On traite le contour de barbe pour dessiner une ligne nette et limiter les poils incarnés. La barbe étant une zone dense et hormonale, elle peut demander plus de séances. Le bilan fait le point."),
   ("Le dos est-il une zone difficile ?","C'est une grande surface, donc la séance est plus longue, mais le laser diode la couvre efficacement. C'est l'une des zones les plus demandées par les hommes."),
  ],
 },
 {
  "maillage":(2,"Si vous revenez de vacances, notre article sur <a href=\"epilation-laser-peau-bronzee.html\">l'épilation laser et la peau bronzée</a> précise combien de temps attendre."),
  "illu_alt":"Illustration : liste de préparation aux cases cochées, rasoir et soleil voilé par un nuage avant la première séance de laser",
  "slug":"preparer-premiere-seance-epilation-laser.html","tag":"Conseils","date":"Mai 2026","iso":"2026-05-15","read":"6 min",
  "guide":True,
  "img":"brochure.jpg",
  "title":"Préparer sa première séance d'épilation laser",
  "lien_sec":3,"lien":"Le déroulement d'une séance chez LUMIA est détaillé sur notre page <a href=\"../epilation-laser-manosque.html\">épilation laser à Manosque</a>.",
  "desc":"Bilan, rasage, soleil, médicaments : tout ce qu'il faut faire (et éviter) avant votre première séance d'épilation laser pour qu'elle se passe au mieux.",
  "lead":"Une première séance d'épilation laser bien préparée, c'est une séance efficace et sereine. Voici la checklist simple à suivre, du bilan jusqu'au jour J.",
  "sections":[
   ("Le bilan, étape obligatoire",[
    "Avant toute première séance, un bilan est obligatoire. C'est un vrai rendez-vous : examen de la peau et du poil, questionnaire de santé, remise d'une fiche d'information et de consentement, présentation du laser et de votre protocole. Chez LUMIA, il coûte 20 euros et il est offert pour tout achat de séance ou de cure.",
    "Ce moment permet de vérifier que votre peau et votre pilosité sont adaptées, et de répondre à toutes vos questions sans précipitation."]),
   ("Raser, ne pas arracher",[
    "Dans les jours qui précèdent la séance, on rase la zone à traiter, idéalement la veille. Surtout, on n'arrache pas le poil : pas de cire, pas de pince, pas d'épilateur électrique dans les semaines précédentes. Le laser a besoin de la racine du poil pour agir, alors que la cire la retire.",
    "Un rasage propre permet au laser de cibler la racine sans brûler le poil en surface."]),
   ("Éviter le soleil et signaler vos traitements",[
    "On évite le soleil, les UV et l'autobronzant 10 jours avant la séance. Une peau bronzée fait reporter le rendez-vous. Pensez aussi à signaler tout médicament, en particulier les traitements photosensibilisants, ainsi qu'une grossesse en cours : certains cas conduisent à reporter ou adapter la séance.",
    "Mieux vaut tout mentionner lors du bilan, même un détail qui vous paraît anodin."]),
   ("Le jour de la séance",[
    "Venez avec une peau propre, sans crème, parfum ni maquillage sur la zone. Évitez les déodorants pour une séance des aisselles. Sur place, vous porterez des lunettes de protection pendant toute la durée du soin. La séance dure de quelques minutes à plus d'une heure selon la zone.",
    "Après la séance, on apaise la peau et on applique une protection solaire sur les zones exposées. Vous repartez avec les conseils d'après-soin et la date de la séance suivante."]),
  ],
  "faq":[
   ("Faut-il raser avant la première séance ?","Oui, idéalement la veille. On rase la zone mais on n'arrache jamais le poil à la cire ou à la pince, car le laser a besoin de la racine pour agir."),
   ("Que faut-il signaler avant une séance ?","Tout traitement médical, notamment photosensibilisant, une grossesse, un bronzage récent ou un problème de peau. Ces éléments sont examinés lors du bilan."),
  ],
 },
 {
  "maillage":(3,"Si vous hésitez entre plusieurs soins, notre guide pour <a href=\"quel-soin-du-visage-choisir-selon-sa-peau.html\">choisir son soin du visage selon sa peau</a> vous aide à vous orienter."),
  "illu_alt":"Illustration : profil de visage au trait fin, taches sur la joue qui s'estompent, soleil discret et bouclier de protection solaire",
  "slug":"taches-visage-comprendre-attenuer.html","tag":"Soins du visage","date":"Juin 2026","iso":"2026-06-15","read":"8 min",
  "img":"cosmelan.jpg",
  "title":"Taches sur le visage : comprendre et atténuer",
  "seo_title":"Taches du visage : causes et solutions | LUMIA",
  "cta_label":"Réserver mon diagnostic de peau",
  "cta_txt":"Le diagnostic de peau (20 €) est déductible du soin. Réservez en ligne ou appelez le 04 92 87 63 72.",
  "lien_sec":2,"lien":"Le déroulé du protocole est détaillé sur la page <a href=\"../soin-cosmelan-taches-manosque.html\">soins dépigmentants COSMELAN à Manosque</a>.",
  "desc":"Mélasma, taches solaires, taches de l'âge : d'où viennent les taches du visage et comment les atténuer durablement, notamment avec le protocole COSMELAN.",
  "lead":"Les taches du visage sont l'un des motifs de consultation esthétique les plus fréquents. Avant de chercher à les atténuer, encore faut-il comprendre d'où elles viennent. Tour d'horizon, et solutions.",
  "sections":[
   ("D'où viennent les taches ?",[
    "Les taches du visage résultent presque toujours d'un excès localisé de mélanine, le pigment qui colore la peau. Plusieurs causes se combinent : l'exposition au soleil, qui reste le premier facteur, les variations hormonales (grossesse, contraception) à l'origine du mélasma, l'inflammation après un bouton ou une lésion (hyperpigmentation post-inflammatoire), et le vieillissement, avec les taches dites de l'âge.",
    "Identifier l'origine est essentiel, car toutes les taches ne répondent pas aux mêmes soins."]),
   ("Le rôle central de la protection solaire",[
    "Quelle que soit la tache, la protection solaire est la base. Sans elle, les taches reviennent ou s'aggravent, et tout soin dépigmentant perd en efficacité. Une protection élevée, appliquée tous les jours et renouvelée, est le geste le plus rentable contre les taches.",
    "C'est aussi pour cela que les protocoles dépigmentants s'accompagnent toujours de conseils de protection au quotidien."]),
   ("Le protocole COSMELAN",[
    "Pour atténuer durablement les taches, le protocole COSMELAN de Mesoestetic agit en deux temps. Une première phase en cabine, avec un masque dépigmentant, puis une phase d'entretien à la maison avec une routine adaptée, suivie sur environ six mois. Son intérêt : il estompe les taches existantes tout en régulant la production de mélanine, ce qui limite leur réapparition.",
    "À l'institut LUMIA, le protocole débute par un diagnostic de peau obligatoire, déductible du soin, pour vérifier qu'il est adapté à votre type de taches. Aucun résultat n'est garanti, mais l'approche est reconnue sur les hyperpigmentations."]),
   ("Entretenir les résultats",[
    "Une fois les taches atténuées, le maintien passe par une routine de soin adaptée et, encore et toujours, une protection solaire quotidienne. Des soins ponctuels peuvent compléter l'entretien selon votre peau.",
    "Si vous hésitez sur la nature de vos taches, le mieux reste un diagnostic de peau en institut, qui orientera vers le soin le plus adapté."]),
  ],
  "faq":[
   ("Le COSMELAN efface-t-il toutes les taches ?","Il est reconnu sur le mélasma, les taches solaires, l'hyperpigmentation post-inflammatoire et les taches de l'âge. Un diagnostic de peau vérifie que vos taches s'y prêtent. Aucun résultat n'est garanti."),
   ("Pourquoi la protection solaire est-elle si importante ?","Parce que le soleil est la première cause des taches. Sans protection quotidienne, elles reviennent et tout soin dépigmentant perd en efficacité."),
  ],
 },
 {
  "illu_alt":"Illustration : stylo de microneedling au-dessus de la peau, micro-points à 0,25 mm, exosomes et fragment de PDRN",
  "slug":"microneedling-exosomes-pdrn-soin-025-mm.html","tag":"Soins du visage","date":"Octobre 2026","iso":"2026-10-15","read":"5 min",
  "img":"microneedling-soin.webp",
  "title":"Microneedling, exosomes et PDRN : le soin à 0,25 mm",
  "seo_title":"Microneedling Manosque : exosomes, PDRN, 0,25 mm | LUMIA",
  "cta_label":"Réserver mon diagnostic visage",
  "cta_txt":"Le diagnostic visage (30 min, 20 €) définit votre protocole. Réservez en ligne ou appelez le 04 92 87 63 72.",
  "lien_sec":2,
  "lien":"Pour le détail du protocole, des tarifs et des précautions, consultez notre page <a href=\"../microneedling-manosque.html\">microneedling à Manosque</a>.",
  "desc":"Microneedling à Manosque : stylo médical à 0,25 mm, sans injection, actifs aux exosomes et au PDRN, cure de 6 séances. On vous explique le soin pas à pas.",
  "lead":"Microneedling, exosomes, PDRN : des mots qui intriguent autant qu'ils intimident. Voici, simplement, ce que contient ce soin, ce qu'il demande et ce qu'on peut raisonnablement en attendre.",
  "sections":[
   ("Le microneedling à 0,25 mm : l'essentiel",[
    "Chez LUMIA, le microneedling est un soin sans aucune injection, réalisé avec un stylo médical à une profondeur de 0,25 mm, en cure de 6 séances espacées de 15 jours. La séance dure 1 heure pour le visage et le cou et coûte 145 €, après un diagnostic visage préalable de 30 minutes à 20 €.",
    "Le principe est simple. Le stylo crée de minuscules micro-perforations contrôlées à la surface de la peau. Ces canaux ne sont pas un but en soi : ils déclenchent la réponse naturelle de régénération de la peau, qui stimule sa production de collagène et d'élastine. C'est pourquoi on parle aussi de micro-stimulation.",
    "Le soin est réalisé par Margaux, infirmière diplômée d'État et esthéticienne. Il est adapté à tous les phototypes, des peaux claires aux peaux foncées, sous réserve des vérifications faites lors du diagnostic."]),
   ("Exosomes et PDRN : de quoi parle-t-on ?",[
    "Les actifs appliqués pendant la séance sont de la marque Mesoestetic et contiennent des exosomes et du PDRN. Ces deux mots n'ont rien de magique, mais ils méritent une explication claire.",
    "Le PDRN, pour polydésoxyribonucléotide, est constitué de fragments d'ADN. Les exosomes sont de toutes petites vésicules qui transportent des signaux d'une cellule à l'autre. Ce sont des actifs étudiés pour leur rôle dans la communication entre cellules et dans les mécanismes de régénération de la peau.",
    "Nous restons volontairement prudents : il ne s'agit pas de produits qui « réparent » à coup sûr, et nous ne chiffrons aucun résultat. Le microneedling prépare la peau, les actifs l'accompagnent, et c'est la réponse de votre propre peau qui fait le travail."]),
   ("Ce que comprend la séance, pas à pas",[
    "Tout commence par un diagnostic visage de 30 minutes. Nous discutons de votre projet et de vos préoccupations, nous examinons votre peau et nous définissons ensemble un protocole personnalisé. Le choix des actifs se fait avec vous, selon votre objectif : anti-âge fermeté, anti-âge global, contour des yeux ou dépigmentation.",
    "Avant de commencer, vous signez un questionnaire de santé, un consentement mutuel et une fiche d'information sur le microneedling. Cette étape est obligatoire, et elle permet de vérifier les contre-indications avant le moindre geste. Elle montre aussi le sérieux de la démarche : on ne traite pas la peau à la légère, même à 0,25 mm.",
    "La séance dure ensuite 1 heure et traite le visage et le cou. Il est aussi possible de traiter uniquement le décolleté. La LED est incluse pendant la pose du masque, pour apaiser la peau. La sensation est celle de petits picotements, variable selon la zone, et la profondeur est adaptée à votre peau."]),
   ("Une cure de 6 séances, et ce qu'on peut en attendre",[
    "Le protocole recommandé est une cure de 6 séances, une tous les 15 jours. Des séances d'entretien, environ une fois tous les deux mois, sont ensuite fortement conseillées pour maintenir le bénéfice. C'est un soin de régénération progressif, pas un effet immédiat.",
    "Le microneedling s'adresse aux rides et ridules, au teint terne ou fatigué, au manque d'éclat, au relâchement cutané, aux pores dilatés, à l'excès de sébum et aux cicatrices d'acné. Pour les taches, un actif de dépigmentation peut être choisi ; si elles sont installées, lisez aussi notre article pour <a href=\"taches-visage-comprendre-attenuer.html\">comprendre et atténuer les taches du visage</a>.",
    "Aucun résultat n'est garanti : il dépend de votre peau, de votre régularité et de votre protection solaire. Nous préférons vous le dire dès le diagnostic plutôt que promettre l'impossible."]),
   ("Les précautions à connaître",[
    "Aucune exposition au soleil ni aux UV n'est permise dans les 7 jours qui précèdent et les 7 jours qui suivent la séance. Une protection solaire SPF 50+ est obligatoire.",
    "Certaines situations contre-indiquent le soin : grossesse et allaitement, acné inflammatoire, traitement à l'isotrétinoïne, plaies ouvertes, herpès, tatouage sur la zone, anticoagulants, maladies auto-immunes à expression cutanée, antécédents de radiothérapie ou de cancer de moins de cinq ans. Tout est vérifié lors du diagnostic.",
    "Si vous hésitez entre le microneedling et un autre soin, notre guide pour <a href=\"quel-soin-du-visage-choisir-selon-sa-peau.html\">choisir son soin du visage selon sa peau</a> vous aidera à vous orienter."]),
  ],
  "faq":[
   ("Le microneedling, est-ce une injection ?","Non. Le stylo médical crée de micro-perforations contrôlées à une profondeur de 0,25 mm, sans aucune injection de produit. Les actifs sont appliqués en surface pendant le soin."),
   ("Combien coûte le microneedling à Manosque ?","La séance visage et cou d'une heure coûte 145 €, précédée d'un diagnostic visage de 30 minutes à 20 €. Le protocole recommandé comprend 6 séances, une tous les 15 jours."),
   ("Que sont les exosomes et le PDRN ?","Le PDRN est fait de fragments d'ADN, et les exosomes sont de petites vésicules qui transportent des signaux entre cellules. Ce sont des actifs étudiés pour la régénération de la peau. Aucun résultat n'est garanti."),
  ],
 },
 {
  "illu_alt":"Illustration : miroir ovale entouré de quatre pictogrammes reliés par des pointillés : LED, hydratation, microneedling et LPG",
  "slug":"quel-soin-du-visage-choisir-selon-sa-peau.html","tag":"Soins du visage","date":"Juillet 2026","iso":"2026-07-15","read":"5 min",
  "img":"soinvisage.webp",
  "title":"Quel soin du visage choisir selon sa peau ?",
  "seo_title":"Quel soin du visage choisir à Manosque ? | LUMIA",
  "cta_label":"Réserver mon diagnostic visage",
  "cta_txt":"Le diagnostic visage (30 min, 20 €) vous aide à choisir le bon soin. Réservez en ligne ou appelez le 04 92 87 63 72.",
  "lien_sec":2,
  "lien":"Pour comparer les soins en détail, consultez nos pages <a href=\"../soins-visage-manosque.html\">soins du visage LUMINEA et LED</a>, <a href=\"../microneedling-manosque.html\">microneedling</a>, <a href=\"../soin-cosmelan-taches-manosque.html\">soins dépigmentants COSMELAN</a> et <a href=\"../lpg-cellu-m6-manosque.html\">LPG visage</a>.",
  "desc":"Teint terne, taches, rides ou relâchement : quel soin du visage choisir ? LUMINEA, LED, microneedling, COSMELAN ou LPG, notre guide d'orientation à Manosque.",
  "lead":"Entre les soins LUMINEA, la LED, le microneedling, le COSMELAN et le LPG visage, il est normal de ne plus savoir lequel choisir. Voici un guide simple, par besoin de peau, pour vous orienter avant le rendez-vous.",
  "sections":[
   ("La règle de base : partir de votre besoin, pas du soin",[
    "Pour choisir un soin du visage, partez de votre besoin principal : éclat et hydratation, taches, rides et fermeté, ou relâchement. À chaque besoin correspond un soin de départ chez LUMIA, et un diagnostic visage de 30 minutes, à 20 €, permet de confirmer le choix.",
    "Un même visage peut avoir plusieurs besoins à la fois, et les soins peuvent se compléter. L'idée n'est donc pas de trouver le soin parfait seul, mais de définir par quoi commencer. C'est ce que fait le diagnostic avant tout protocole.",
    "Quelques repères aident à s'y retrouver. Les soins LUMINEA et la LED misent sur l'éclat, l'hydratation et la douceur. Le microneedling travaille la qualité de la peau en profondeur, sur la durée. Le COSMELAN cible les taches, et le LPG visage le relâchement. Quatre approches, quatre besoins, et un point commun : une praticienne infirmière D.E. qui adapte chaque protocole à votre peau."]),
   ("Teint terne, peau déshydratée : les soins LUMINEA et la LED",[
    "Si votre problème est un teint fatigué, un manque d'éclat, une peau déshydratée ou des imperfections, les soins LUMINEA sont le bon point de départ. Ils associent plusieurs technologies sur la machine EsthéSkin : nettoyage profond, hydradermabrasion, ultrasons, radiofréquence, micro-courants, jet peel à la vitamine C, masque et modelage.",
    "Le soin existe en formules express de 30 minutes dès 45 €, puis en Découverte (1h15, 95 €), Avancé (1h15, 115 €) et Prestige (1h30, 135 €), ce dernier incluant le LPG visage ou la LED. La luminothérapie LED, une lumière froide sans chaleur ni douleur, se pratique aussi seule, dès 35 € la séance.",
    "Pour entretenir la peau, un soin par mois est un bon rythme. Pour un objectif précis, on travaille souvent en cure de plusieurs séances rapprochées, puis on espace."]),
   ("Rides, pores, cicatrices : le microneedling",[
    "Le microneedling vise les rides et ridules, le relâchement cutané, les pores dilatés, l'excès de sébum et les cicatrices d'acné. C'est un soin de régénération, sans injection, à 0,25 mm de profondeur, à 145 € la séance de 1 heure pour le visage et le cou.",
    "Il se pratique en cure de 6 séances, une tous les 15 jours. C'est un engagement plus important qu'un soin d'éclat, mais aussi un travail plus profond. Les contre-indications, comme la grossesse, l'acné inflammatoire ou un traitement à l'isotrétinoïne, sont vérifiées lors du diagnostic. Pour comprendre le soin en détail, lisez notre article sur le <a href=\"microneedling-exosomes-pdrn-soin-025-mm.html\">microneedling, les exosomes et le PDRN</a>."]),
   ("Taches et pigmentation : le protocole COSMELAN",[
    "Pour le mélasma, les taches solaires, l'hyperpigmentation post-inflammatoire ou les taches liées à l'âge, le protocole COSMELAN de Mesoestetic est conçu pour atténuer les taches. Il se déroule en deux temps, en cabine puis à la maison, avec un suivi sur environ six mois, à partir de 650 €.",
    "Un diagnostic de peau à 20 €, déductible du soin, est obligatoire : il vérifie que votre peau et vos taches s'y prêtent. Aucun résultat n'est garanti, et la protection solaire quotidienne reste indispensable. Notre article pour <a href=\"taches-visage-comprendre-attenuer.html\">comprendre et atténuer les taches du visage</a> détaille la démarche."]),
   ("Fermeté et ovale du visage : le LPG visage",[
    "Pour raffermir, lisser et redonner de l'éclat en douceur, le LPG visage travaille zone par zone, du front au cou en passant par le regard, l'ovale, les mains ou le décolleté. La technique est non invasive, sans aiguille ni chirurgie.",
    "Les soins zones sont facturés selon la durée, dès 20 € pour 10 minutes. Un bilan personnalisé de 40 €, offert pour tout achat de forfait, définit vos objectifs. Le LPG visage se marie très bien avec les soins LUMINEA et le microneedling.",
    "Avant n'importe quel soin, quelques précautions s'imposent. Pour les soins LUMINEA, évitez le soleil et les UV 48 heures avant, les peelings et dermabrasions 15 jours avant, ainsi que le rétinol fortement concentré. Grossesse, allaitement, traitement aux rétinoïdes ou injections récentes de botox ou d'acide hyaluronique (attendre 5 semaines) peuvent faire reporter ou adapter le soin. Tout cela se vérifie ensemble lors du diagnostic."]),
  ],
  "faq":[
   ("Quel soin du visage pour un teint terne ?","Les soins LUMINEA, dès 45 € en version express de 30 minutes, nettoient, hydratent et illuminent la peau. La luminothérapie LED peut s'y ajouter ou se pratiquer seule."),
   ("Peut-on associer plusieurs soins du visage ?","Oui, un même visage a souvent plusieurs besoins. Le diagnostic visage de 30 minutes, à 20 €, permet de choisir par quoi commencer et d'organiser les soins dans le bon ordre."),
   ("Comment savoir si un soin est adapté à ma peau ?","Chaque soin commence par un diagnostic qui vérifie vos contre-indications et votre objectif. Aucun résultat n'est garanti, mais le protocole est ajusté à votre peau."),
  ],
 },
 {
  "illu_alt":"Illustration : un cercle partagé entre une peau d'orange et une peau lissée, avec gouttes d'eau et feuille",
  "slug":"cellulite-ce-qui-marche-ce-qui-ne-marche-pas.html","tag":"Corps et silhouette","date":"Septembre 2026","iso":"2026-09-15","read":"5 min",
  "img":"lpg-corps.webp",
  "title":"Cellulite : ce qui marche, ce qui ne marche pas",
  "seo_title":"Cellulite à Manosque : ce qui marche ou non | LUMIA",
  "cta_label":"Réserver mon bilan LPG",
  "cta_txt":"Le bilan LPG (40 €) est offert pour tout achat de forfait. Réservez en ligne ou appelez le 04 92 87 63 72.",
  "lien_sec":4,"lien":"Pour découvrir la méthode, les protocoles et le déroulement des séances, consultez notre page <a href=\"../lpg-cellu-m6-manosque.html\">LPG endermologie à Manosque</a>.",
  "desc":"Crèmes, sport, alimentation, LPG : que peut-on vraiment attendre contre la cellulite ? Un point honnête sur ce qui aide, ce qui ne suffit pas, sans promesse.",
  "lead":"Entre les crèmes miracle et les promesses trop belles, difficile de s'y retrouver. Je préfère être claire : il n'existe pas de solution magique contre la cellulite, mais il existe des moyens d'en améliorer l'aspect. Voici ce qui aide, ce qui ne suffit pas, et ce que je propose à l'institut.",
  "sections":[
   ("Pas de miracle, mais un aspect de la peau qui peut s'améliorer",[
    "Aucun soin ne fait disparaître la cellulite pour de bon, mais certains en améliorent l'aspect : chez LUMIA, une cure de 10 à 12 séances de LPG est souvent recommandée pour un objectif marqué. Le LPG n'est pas un traitement amaigrissant, il agit sur l'aspect de la peau, la fermeté et le drainage.",
    "L'approche qui a du sens se joue en deux temps : des soins mécaniques réguliers, et une hygiène de vie qui les accompagne. Aucun résultat n'est garanti, car chaque peau réagit à son rythme, mais une promesse honnête vaut mieux qu'un slogan."]),
   ("La cellulite, de quoi parle-t-on ?",[
    "La cellulite est très fréquente chez les femmes. Ce n'est ni une maladie ni un défaut : c'est un aspect de la peau, la fameuse « peau d'orange », qui apparaît lorsque le tissu adipeux situé sous la peau se répartit de façon irrégulière. Les hormones et la circulation y jouent un rôle, ce qui explique qu'elle touche des silhouettes très différentes.",
    "En institut, on parle de cellulite adipeuse, aqueuse ou fibreuse, et il est courant que ces formes se mélangent chez une même personne. C'est l'une des raisons pour lesquelles un bilan personnalisé est utile avant de choisir un protocole.",
    "Parce qu'elle est si courante, il est utile de la dédramatiser. Beaucoup de femmes la vivent comme un complexe alors qu'elle fait partie de la diversité des corps. Vouloir en améliorer l'aspect est légitime, à condition de partir d'attentes réalistes et de ne pas se comparer aux images retouchées."]),
   ("Ce qui ne marche pas, ou pas seul",[
    "Les crèmes, d'abord. Elles peuvent hydrater, adoucir et rendre la peau agréable au toucher, et c'est déjà appréciable, mais utilisées seules, elles ne font pas disparaître la cellulite. Méfiez-vous des promesses de résultat rapide, quelle que soit la marque.",
    "La perte de poids, ensuite. Perdre du poids peut affiner la silhouette, mais cela ne supprime pas toujours la cellulite : certaines personnes minces en ont aussi, et elle peut rester présente après un régime. Se priver n'est donc pas la solution, et ce n'est pas ce que je recommande.",
    "Enfin, la cellulite se travaille dans la durée. Un geste ponctuel ne change pas l'aspect de la peau, c'est la régularité qui compte, que l'on parle de soins, d'activité physique ou de routine du quotidien. Mieux vaut un rythme tenable qu'un programme intense abandonné au bout de trois semaines."]),
   ("Ce qui aide vraiment",[
    "Du côté de l'hygiène de vie, trois leviers simples comptent : une activité physique régulière, qui entretient la circulation et le tonus de la peau, une bonne hydratation, et une alimentation équilibrée. Ils ne font pas de miracle à eux seuls, mais ils créent le terrain sur lequel un soin peut mieux travailler.",
    "Inutile de viser la performance : une activité qui vous plaît, pratiquée dans la durée, vaut mieux qu'un effort spectaculaire sans lendemain. Boire régulièrement dans la journée et composer des repas variés sont des gestes simples, accessibles à toutes, et qui font du bien au-delà de la peau.",
    "Du côté des soins, les techniques mécaniques comme le LPG agissent par un palper-rouler qui stimule la peau en profondeur, pour la lisser, la raffermir et relancer le drainage. Elles ne remplacent pas l'hygiène de vie, elles la complètent. Pour aller plus loin sur le drainage, lisez aussi notre article sur <a href=\"drainage-lymphatique-lpg-cure-silhouette.html\">le drainage lymphatique et la cure silhouette</a>."]),
   ("Le LPG chez LUMIA : à quoi s'attendre",[
    "Nous utilisons la technologie Cellu M6 Alliance, non invasive et confortable. Le soin anti-cellulite dure 30 minutes et s'adapte à votre sensibilité. Les séances ont lieu en général une à deux fois par semaine au début, pour enclencher la dynamique, puis on espace pour l'entretien.",
    "Selon votre objectif, on choisit parmi plusieurs protocoles : anti-cellulite, jeune maman, détox avec palper-rouler drainant, ou relaxation. Les soins anti-cellulite, jeune maman et relaxation sont à 60 euros pour 30 minutes, et le soin détox à 70 euros pour 40 minutes.",
    "Tout commence par un bilan à 40 €, offert pour tout achat de forfait, où l'on définit vos objectifs. Des photos de suivi sont prises aux 1re, 6e et 12e séances pour mesurer la progression, et les cures se règlent en plusieurs fois sans frais. Les tarifs détaillés sont sur notre <a href=\"../tarifs.html\">page tarifs</a>."]),
  ],
  "faq":[
   ("Peut-on faire disparaître la cellulite ?","Aucun soin ne la fait disparaître de façon certaine. On peut en améliorer l'aspect avec des soins mécaniques comme le LPG et une bonne hygiène de vie, sans garantie de résultat."),
   ("Les crèmes anti-cellulite suffisent-elles ?","Utilisées seules, elles ne font pas disparaître la cellulite. Elles peuvent hydrater et adoucir la peau, et accompagner utilement un soin."),
   ("Le LPG fait-il maigrir ?","Non. Le LPG n'est pas un traitement amaigrissant. Il agit sur l'aspect de la peau, la cellulite, la fermeté et le drainage."),
  ],
 },
 {
  "illu_alt":"Illustration : lignes fluides qui convergent en un courant doux, accompagnées de deux feuilles, pour la cure de drainage et LPG",
  "slug":"drainage-lymphatique-lpg-cure-silhouette.html","tag":"Corps et silhouette","date":"Août 2026","iso":"2026-08-15","read":"5 min",
  "img":"soinLPG.webp",
  "title":"Drainage lymphatique et LPG : la cure silhouette",
  "seo_title":"Drainage lymphatique et LPG à Manosque | LUMIA",
  "cta_label":"Réserver ma cure Silhouette",
  "cta_txt":"Réservez en ligne ou appelez le 04 92 87 63 72 pour la Cure Expertise Silhouette. Paiement des cures en plusieurs fois sans frais.",
  "lien_sec":2,"lien":"Les protocoles et le déroulement des séances sont détaillés sur notre page <a href=\"../lpg-cellu-m6-manosque.html\">LPG endermologie à Manosque</a>.",
  "desc":"La Cure Expertise Silhouette associe drainage lymphatique et LPG sur 6 séances, avec Emana by Sophie et LUMIA à Manosque. On vous explique son déroulement.",
  "lead":"Et si l'on associait deux gestes complémentaires, un drainage doux et un soin mécanique ? C'est l'idée de la Cure Expertise Silhouette, que nous proposons avec Sophie d'Emana, dans nos locaux. Voici comment elle fonctionne, et ce que l'on peut raisonnablement en attendre.",
  "sections":[
   ("La Cure Expertise Silhouette en bref",[
    "La Cure Expertise Silhouette compte 6 séances, chacune associant 45 minutes de drainage lymphatique et 30 minutes de LPG, soit 1h15 de soin. La première séance est à 120 euros, et la cure est réalisée avec Emana by Sophie, installée dans nos locaux.",
    "Elle est disponible pour le bas du corps ou pour le ventre et la taille, avec un bilan de 20 minutes avant la cure. Ce n'est pas un traitement amaigrissant, et aucun résultat n'est garanti : la cure vise l'aspect de la peau et la silhouette.",
    "Pourquoi une cure plutôt qu'une séance isolée ? Parce que l'aspect de la peau se travaille dans la durée : en répétant les séances, on donne au drainage et au LPG le temps de s'additionner. C'est la logique de toute cure, et c'est pour cela que les cures se règlent en plusieurs fois sans frais."]),
   ("Le drainage lymphatique : un geste doux, pas un soin médical",[
    "Le drainage lymphatique esthétique est un massage lent et très doux, fait de gestes légers et répétés. Il est proposé pour le bien-être, pour accompagner le drainage et pour la silhouette. Il ne s'agit pas d'un soin médical, et il ne remplace pas l'avis d'un professionnel de santé si vous avez un doute sur votre circulation.",
    "Chez Emana by Sophie, le drainage fait partie d'un domaine plus large, « drainage et madérothérapie », décrit par Sophie comme remodelant, drainant et sculptant. Sa signature : « L'expertise par le toucher ».",
    "C'est aussi un vrai moment de détente, ce qui compte quand on veut prendre soin de soi dans la durée."]),
   ("Le LPG, l'autre moitié de la cure",[
    "Le LPG est réalisé par LUMIA, avec la technologie Cellu M6 Alliance, non invasive. Son palper-rouler stimule la peau en profondeur et agit sur la cellulite, la fermeté et le drainage. C'est un soin confortable, dont l'intensité est réglée selon votre sensibilité.",
    "Les deux gestes se répondent : le drainage prépare avec douceur, le LPG travaille l'aspect de la peau. Si vous voulez comprendre ce que l'on peut espérer côté cellulite, lisez aussi notre article <a href=\"cellulite-ce-qui-marche-ce-qui-ne-marche-pas.html\">Cellulite : ce qui marche, ce qui ne marche pas</a>.",
    "Chez LUMIA, le LPG corps existe aussi en séances seules : anti-cellulite, jeune maman et relaxation à 60 euros pour 30 minutes, détox à 70 euros pour 40 minutes. Dans la cure, les 30 minutes de LPG s'inscrivent dans une séance plus longue, associée au drainage."]),
   ("Qui fait quoi : LUMIA et Emana by Sophie",[
    "Soyons clairs sur ce point. Emana by Sophie est une activité indépendante, distincte de l'institut LUMIA. Sophie exerce le massage bien-être dans nos locaux, au 10 Bis avenue Jean Giono à Manosque, sous sa propre responsabilité. L'institut LUMIA n'est pas responsable des prestations réalisées par Emana by Sophie, et réciproquement.",
    "Dans la cure, le drainage lymphatique est réalisé par Sophie, et le LPG par LUMIA. Deux savoir-faire, deux entités, un même lieu et un protocole pensé pour s'enchaîner. Concrètement, vous venez au même endroit pour toute la cure, et vous retrouvez deux praticiennes selon l'étape du soin. Elles ne se substituent pas l'une à l'autre : chacune reste responsable de sa propre prestation, et vous savez toujours à qui vous vous adressez, pour une question sur le drainage ou sur le LPG."]),
   ("Comment se déroule la cure ?",[
    "Tout commence par le bilan de 20 minutes, qui permet de poser votre objectif et de vérifier que la cure vous convient. Viennent ensuite les 6 séances, de 1h15 chacune. Le rythme est défini ensemble, selon votre emploi du temps et votre peau.",
    "Comme pour tout soin du corps, l'hygiène de vie complète le travail : activité physique régulière, bonne hydratation et alimentation équilibrée. Si vous avez un doute sur votre situation, parlez-en lors du bilan, nous vous orienterons.",
    "Les cures se règlent en plusieurs fois sans frais. Le détail du tarif figure sur notre <a href=\"../tarifs.html\">page tarifs</a>, et la réservation se fait en ligne ou par téléphone."]),
  ],
  "faq":[
   ("Que contient la Cure Expertise Silhouette ?","6 séances, chacune de 45 minutes de drainage lymphatique et 30 minutes de LPG, soit 1h15, pour le bas du corps ou pour le ventre et la taille, avec un bilan de 20 minutes avant la cure."),
   ("Le drainage lymphatique est-il un soin médical ?","Non. Le drainage lymphatique proposé ici est esthétique, orienté bien-être et silhouette. Il ne remplace pas un avis médical."),
   ("Qui réalise le drainage et qui réalise le LPG ?","Le drainage lymphatique est réalisé par Sophie, d'Emana by Sophie, activité indépendante installée dans nos locaux. Le LPG est réalisé par l'institut LUMIA."),
  ],
 },
]

# ---------------------------------------------------------------------------
# Ordre, illustrations et maillage (24/11/2026, demande de Thomas)
# - le blog et articles.json listent les articles du plus récent au plus ancien ;
# - chaque article a une illustration SVG unique (assets/illustrations/<slug>.svg),
#   en tête d'article et sur sa carte ; la vraie photo reste dans le corps ;
#   image de partage JPEG 1200x630 (assets/illustrations/og/<slug>.jpg) ;
# - « À lire aussi » : 3 articles calculés à chaque génération, jamais un article
#   déjà cité dans le texte, jamais l'article lui-même ; priorité au même thème,
#   puis au thème voisin, puis au moins cité, puis au plus récent. Un ancien article
#   peut donc citer un plus récent ; tout ajout recalcule toutes les pages.
# ---------------------------------------------------------------------------
import re as _re
ARTICLES.sort(key=lambda a: a["iso"], reverse=True)
SLUGS = [a["slug"] for a in ARTICLES]
ILLU_DIR = os.path.join(ROOT, "assets", "illustrations")
def illu(a):
    return os.path.exists(os.path.join(ILLU_DIR, a["slug"].replace(".html", ".svg")))
def card_img(a):
    return ("illustrations/" + a["slug"].replace(".html", ".svg")) if illu(a) else a["img"]
def theme(a):
    if "laser" in a["tag"].lower() or "laser" in a["slug"]: return "laser"
    if a["tag"] == "Corps et silhouette": return "corps"
    return "visage"
VOISIN = {("visage","corps"),("corps","visage"),("visage","laser"),("laser","visage")}
def cites(a):
    txt = " ".join(" ".join(p) for _, p in a["sections"]) + " " + a.get("lien", "") + " " + a.get("maillage", (0, ""))[1]
    return [h for h in dict.fromkeys(_re.findall(r'href="([a-z0-9-]+\.html)"', txt)) if h in SLUGS]
CITES = {a["slug"]: cites(a) for a in ARTICLES}
recus = {s_: 0 for s_ in SLUGS}
for a in ARTICLES:
    for c_ in CITES[a["slug"]]: recus[c_] += 1
RANG = {s_: k for k, s_ in enumerate(SLUGS)}  # 0 = le plus récent
CONNEXES = {}
for a in sorted(ARTICLES, key=lambda x: x["iso"]):  # les anciens choisissent d'abord
    deja = set(CITES[a["slug"]]) | {a["slug"]}
    cands = [b for b in ARTICLES if b["slug"] not in deja]
    def cle(b):
        aff = 2 if theme(b) == theme(a) else (1 if (theme(a), theme(b)) in VOISIN else 0)
        return (-aff, recus[b["slug"]], RANG[b["slug"]])
    choix = sorted(cands, key=cle)[:3]
    for b in choix: recus[b["slug"]] += 1
    CONNEXES[a["slug"]] = [b["slug"] for b in choix]
# Garde-fous : la génération s'arrête si la règle est violée
for a in ARTICLES:
    s_ = a["slug"]; tout = CITES[s_] + CONNEXES[s_]
    assert s_ not in tout, "%s se cite lui-même" % s_
    assert len(tout) == len(set(tout)), "%s cite deux fois le même article" % s_
    assert len(CONNEXES[s_]) == 3, "%s : moins de 3 articles connexes" % s_
orphelins = [s_ for s_ in SLUGS if recus[s_] == 0]
assert not orphelins, "articles jamais cités : %s" % orphelins
print("maillage OK · liens entrants :", ", ".join("%s %d" % (s_[:18], recus[s_]) for s_ in SLUGS))
BYSLUG = {a["slug"]: a for a in ARTICLES}

# articles.json (source unique, chemins relatifs au dossier blog/)
data = [{"slug":a["slug"],"title":a["title"],"desc":a["desc"],"tag":a["tag"],
         "date":a["date"],"readTime":a["read"],"image":"../assets/"+card_img(a)} for a in ARTICLES]
os.makedirs(os.path.join(ROOT,"blog"), exist_ok=True)
with open(os.path.join(ROOT,"blog","articles.json"),"w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("articles.json écrit")

# Pages articles
GUIDE_LASER = """<div class="callout">
  <h3>Faites le point avant votre bilan</h3>
  <p>Phototype, zones traitables, situations qui imposent d'attendre : notre guide gratuit <strong>« Êtes-vous éligible à l'épilation laser ? »</strong> vous aide à préparer votre bilan, en 3 pages.</p>
  <p><a href="%sassets/guide-epilation-laser-lumia.pdf" class="btn btn-outline" download>Télécharger le guide (PDF)</a></p>
</div>
"""

def article_card(a, prefix_img="assets/", prefix_link=""):
    return ('<a href="%s%s" class="card"><img src="%s%s" alt="%s" width="640" height="400" loading="lazy">'
            '<div class="card__body"><span class="card__tag">%s</span><h3 class="card__title">%s</h3>'
            '<p class="card__excerpt">%s</p><p class="card__meta">%s · %s</p></div></a>'
            % (prefix_link, a["slug"], prefix_img, card_img(a), a.get("illu_alt", a["title"]) if illu(a) else a["title"], a["tag"], a["title"], a["desc"], a["date"], a["read"]))

n = len(ARTICLES)
for i, a in enumerate(ARTICLES):
    url = "https://lumia-salon.fr/blog/%s" % a["slug"]
    secs = ""
    for j,(h2, paras) in enumerate(a["sections"]):
        secs += "<h2>%s</h2>\n" % h2
        for k,par in enumerate(paras):
            secs += "<p>%s</p>\n" % par
        if a.get("maillage") and j == a["maillage"][0]:  # phrase de lien vers un autre article
            secs += "<p>%s</p>\n" % a["maillage"][1]
        if j == a.get("lien_sec"):
            secs += "<p>%s</p>\n" % a["lien"]
        if j == 0:  # image + CTA après la première section
            iw, ih = img_size(a["img"])
            icls = "landscape" if iw >= ih else "portrait"
            secs += ('<img src="../assets/%s" class="%s" alt="%s" width="%d" height="%d" loading="lazy">\n'
                     '<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">%s</a></p>\n'
                     % (a["img"], icls, a["title"], iw, ih, PLANITY, a.get("cta_label", "Réserver mon bilan laser")))
    # « À lire aussi » : 3 articles calculés (voir CONNEXES)
    sib = [BYSLUG[x] for x in CONNEXES[a["slug"]]]
    related = "".join(article_card(s, "../assets/", "") for s in sib)
    hero = ('<img src="../assets/illustrations/%s" class="article-hero" alt="%s" width="1200" height="600" loading="eager" fetchpriority="high">\n'
            % (a["slug"].replace(".html", ".svg"), a.get("illu_alt", a["title"]))) if illu(a) else ""
    body = header_block(
        [("Accueil","../"),("Blog","../blog.html"),(a["title"], None)],
        a["title"], "") + ("""
<main id="main"><article class="article-body"><div class="container">
<p class="card__meta" style="margin-bottom:1.5rem;">%s · %s · Par Margaux</p>
%s<p class="lead">%s</p>
%s
%s<h2>Questions fréquentes</h2>
%s
<h2>À lire aussi</h2>
<div class="related-grid" data-related>
%s
</div>
</div></article>
%s</main>
""" % (a["date"], a["read"], hero, a["lead"], secs, (GUIDE_LASER % "../") if a.get("guide") else "", faq_html(a["faq"]), related,
       cta('Envie de vous lancer ?', a.get("cta_txt", "Le premier bilan est offert pour tout achat. Réservez en ligne ou appelez le 04 92 87 63 72."))))
    og_rel = "illustrations/og/" + a["slug"].replace(".html", ".jpg")
    og_ok = os.path.exists(os.path.join(ROOT, "assets", og_rel))
    schema = (schema_article(a["title"], a["desc"], og_rel if og_ok else a["img"], a["iso"], url, a.get("maj", MAJ_BLOG))
              + schema_faq(a["faq"])
              + schema_breadcrumb([("Accueil",BASE),("Blog",BASE+"blog.html"),(a["title"], url)]))
    page("blog/%s" % a["slug"],
         a.get("seo_title", a["title"] + " | LUMIA"),
         a["desc"], url, body, schema, og_type="article", in_sub=True,
         og_img=("https://lumia-salon.fr/assets/" + og_rel) if og_ok else None,
         og_alt=a.get("illu_alt", a["title"]))

# blog.html (listing)
cards = "\n".join(article_card(a, "assets/", "blog/") for a in ARTICLES)
blog_body = header_block(
    [("Accueil","./"),("Blog",None)],
    "Le blog de LUMIA",
    "Conseils et explications sur l'épilation laser, les soins du visage et la beauté, par une infirmière D.E. à Manosque.") + ("""
<main id="main"><section class="section"><div class="container">
<h2 class="sr-only">Tous les articles</h2>
<div class="blog-grid">
%s
</div>
</div></section></main>
""" % cards.replace('loading="lazy"', 'loading="eager" fetchpriority="high"', 1))  # 1re carte = image principale (LCP)
page("blog.html","Blog | LUMIA, institut de beauté à Manosque",
     "Le blog de l'institut LUMIA à Manosque : épilation laser, soins du visage, taches et conseils beauté pratiques, par Margaux, infirmière D.E. et esthéticienne.",
     "https://lumia-salon.fr/blog.html", blog_body,
     schema_breadcrumb([("Accueil",BASE),("Blog",BASE+"blog.html")]))
print("blog OK")
