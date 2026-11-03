#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère le blog : articles.json, blog.html (listing) et les 6 articles."""
import json, os
from build_pages import *

def schema_article(title, desc, img, iso, url):
    return ('<script type="application/ld+json">\n'
    '{ "@context":"https://schema.org","@type":"Article","headline":"%s","description":"%s",'
    '"image":"https://lumia-salon.fr/assets/%s","datePublished":"%s","dateModified":"%s",'
    '"author":{"@type":"Person","name":"Margaux","url":"https://lumia-salon.fr/a-propos.html"},'
    '"publisher":{"@type":"Organization","name":"LUMIA","url":"https://lumia-salon.fr","logo":{"@type":"ImageObject","url":"https://lumia-salon.fr/assets/logo.png"}},'
    '"mainEntityOfPage":"%s" }\n</script>\n' % (title, desc, img, iso, iso, url))

ARTICLES = [
 {
  "slug":"epilation-laser-combien-de-seances.html","tag":"Épilation laser","date":"Janvier 2026","iso":"2026-01-15","read":"7 min",
  "img":"machinelaserlunettes.webp",
  "title":"Épilation laser : combien de séances faut-il vraiment ?",
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
  "slug":"epilation-laser-peau-bronzee.html","tag":"Épilation laser","date":"Février 2026","iso":"2026-02-15","read":"6 min",
  "img":"ambiance-2.jpg",
  "title":"Épilation laser et peau bronzée : ce qu'il faut savoir avant l'été",
  "desc":"Bronzage et laser ne font pas bon ménage. On explique pourquoi, combien de temps attendre, et comment organiser ses séances avant et après l'été.",
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
  "slug":"epilation-laser-ou-lumiere-pulsee.html","tag":"Épilation laser","date":"Mars 2026","iso":"2026-03-15","read":"7 min",
  "img":"machinelaser.webp",
  "title":"Épilation laser ou lumière pulsée : quelles différences ?",
  "desc":"Laser et lumière pulsée (IPL) reposent sur des principes proches mais ne se valent pas. On compare efficacité, précision et usage en institut.",
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
  "slug":"epilation-laser-homme.html","tag":"Épilation laser","date":"Avril 2026","iso":"2026-04-15","read":"6 min",
  "img":"laserhomme.webp",
  "title":"Épilation laser homme : torse, dos, barbe",
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
  "slug":"preparer-premiere-seance-epilation-laser.html","tag":"Conseils","date":"Mai 2026","iso":"2026-05-15","read":"6 min",
  "img":"brochure.jpg",
  "title":"Préparer sa première séance d'épilation laser",
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
  "slug":"taches-visage-comprendre-attenuer.html","tag":"Soins du visage","date":"Juin 2026","iso":"2026-06-15","read":"8 min",
  "img":"cosmelan.jpg",
  "title":"Taches sur le visage : comprendre et atténuer",
  "desc":"Mélasma, taches solaires, taches de l'âge : d'où viennent les taches du visage et comment les atténuer durablement, notamment avec le protocole Cosmelan.",
  "lead":"Les taches du visage sont l'un des motifs de consultation esthétique les plus fréquents. Avant de chercher à les atténuer, encore faut-il comprendre d'où elles viennent. Tour d'horizon, et solutions.",
  "sections":[
   ("D'où viennent les taches ?",[
    "Les taches du visage résultent presque toujours d'un excès localisé de mélanine, le pigment qui colore la peau. Plusieurs causes se combinent : l'exposition au soleil, qui reste le premier facteur, les variations hormonales (grossesse, contraception) à l'origine du mélasma, l'inflammation après un bouton ou une lésion (hyperpigmentation post-inflammatoire), et le vieillissement, avec les taches dites de l'âge.",
    "Identifier l'origine est essentiel, car toutes les taches ne répondent pas aux mêmes soins."]),
   ("Le rôle central de la protection solaire",[
    "Quelle que soit la tache, la protection solaire est la base. Sans elle, les taches reviennent ou s'aggravent, et tout soin dépigmentant perd en efficacité. Une protection élevée, appliquée tous les jours et renouvelée, est le geste le plus rentable contre les taches.",
    "C'est aussi pour cela que les protocoles dépigmentants s'accompagnent toujours de conseils de protection au quotidien."]),
   ("Le protocole Cosmelan",[
    "Pour atténuer durablement les taches, le protocole Cosmelan de Mesoestetic agit en deux temps. Une première phase en cabine, avec un masque dépigmentant, puis une phase d'entretien à la maison avec une routine adaptée, suivie sur environ six mois. Son intérêt : il estompe les taches existantes tout en régulant la production de mélanine, ce qui limite leur réapparition.",
    "À l'institut LUMIA, le protocole débute par un diagnostic de peau obligatoire, déductible du soin, pour vérifier qu'il est adapté à votre type de taches. Aucun résultat n'est garanti, mais l'approche est reconnue sur les hyperpigmentations."]),
   ("Entretenir les résultats",[
    "Une fois les taches atténuées, le maintien passe par une routine de soin adaptée et, encore et toujours, une protection solaire quotidienne. Des soins ponctuels peuvent compléter l'entretien selon votre peau.",
    "Si vous hésitez sur la nature de vos taches, le mieux reste un diagnostic de peau en institut, qui orientera vers le soin le plus adapté."]),
  ],
  "faq":[
   ("Le Cosmelan efface-t-il toutes les taches ?","Il est reconnu sur le mélasma, les taches solaires, l'hyperpigmentation post-inflammatoire et les taches de l'âge. Un diagnostic de peau vérifie que vos taches s'y prêtent. Aucun résultat n'est garanti."),
   ("Pourquoi la protection solaire est-elle si importante ?","Parce que le soleil est la première cause des taches. Sans protection quotidienne, elles reviennent et tout soin dépigmentant perd en efficacité."),
  ],
 },
]

# articles.json (source unique, chemins relatifs au dossier blog/)
data = [{"slug":a["slug"],"title":a["title"],"desc":a["desc"],"tag":a["tag"],
         "date":a["date"],"readTime":a["read"],"image":"../assets/"+a["img"]} for a in ARTICLES]
os.makedirs(os.path.join(ROOT,"blog"), exist_ok=True)
with open(os.path.join(ROOT,"blog","articles.json"),"w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("articles.json écrit")

# Pages articles
def article_card(a, prefix_img="assets/", prefix_link=""):
    return ('<a href="%s%s" class="card"><img src="%s%s" alt="%s" width="640" height="400" loading="lazy">'
            '<div class="card__body"><span class="card__tag">%s</span><h3 class="card__title">%s</h3>'
            '<p class="card__excerpt">%s</p><p class="card__meta">%s · %s</p></div></a>'
            % (prefix_link, a["slug"], prefix_img, a["img"], a["title"], a["tag"], a["title"], a["desc"], a["date"], a["read"]))

n = len(ARTICLES)
for i, a in enumerate(ARTICLES):
    url = "https://lumia-salon.fr/blog/%s" % a["slug"]
    secs = ""
    for j,(h2, paras) in enumerate(a["sections"]):
        secs += "<h2>%s</h2>\n" % h2
        for k,par in enumerate(paras):
            secs += "<p>%s</p>\n" % par
        if j == 0:  # image + CTA après la première section
            iw, ih = img_size(a["img"])
            icls = "landscape" if iw >= ih else "portrait"
            secs += ('<img src="../assets/%s" class="%s" alt="%s" width="%d" height="%d" loading="lazy">\n'
                     '<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Réserver mon bilan offert</a></p>\n'
                     % (a["img"], icls, a["title"], iw, ih, PLANITY))
    # fallback statique : 2 articles suivants
    sib = [ARTICLES[(i+1)%n], ARTICLES[(i+2)%n]]
    related = "".join(article_card(s, "../assets/", "") for s in sib)
    body = header_block(
        [("Accueil","../"),("Blog","../blog.html"),(a["title"], None)],
        a["title"], "") + ("""
<main id="main"><article class="article-body"><div class="container">
<p class="card__meta" style="margin-bottom:1.5rem;">%s · %s · Par Margaux</p>
<p class="lead">%s</p>
%s
<h2>Questions fréquentes</h2>
%s
<h2>À lire aussi</h2>
<div class="related-grid" data-related>
%s
</div>
</div></article>
%s</main>
""" % (a["date"], a["read"], a["lead"], secs, faq_html(a["faq"]), related,
       cta('Envie de vous lancer ?', "Le premier bilan est offert pour tout achat. Réservez en ligne ou appelez le 04 92 87 63 72.")))
    schema = (schema_article(a["title"], a["desc"], a["img"], a["iso"], url)
              + schema_faq(a["faq"])
              + schema_breadcrumb([("Accueil",BASE),("Blog",BASE+"blog.html"),(a["title"], url)]))
    page("blog/%s" % a["slug"],
         a["title"] + " | LUMIA",
         a["desc"], url, body, schema, og_type="article", in_sub=True)

# blog.html (listing)
cards = "\n".join(article_card(a, "assets/", "blog/") for a in ARTICLES)
blog_body = header_block(
    [("Accueil","./"),("Blog",None)],
    "Le blog de LUMIA",
    "Conseils et explications sur l'épilation laser, les soins du visage et la beauté, par une infirmière D.E. à Manosque.") + ("""
<main id="main"><section class="section"><div class="container">
<div class="blog-grid">
%s
</div>
</div></section></main>
""" % cards)
page("blog.html","Blog | LUMIA, institut de beauté à Manosque",
     "Le blog de l'institut LUMIA à Manosque : épilation laser, soins du visage, conseils beauté par une infirmière diplômée d'État.",
     "https://lumia-salon.fr/blog.html", blog_body,
     schema_breadcrumb([("Accueil",BASE),("Blog",BASE+"blog.html")]))
print("blog OK")
