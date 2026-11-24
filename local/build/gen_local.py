#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les 9 pages locales d'épilation laser, contenu unique par ville.

Révision du 24/11/2026 (accord de Thomas) : chaque ville porte ses propres sections
(introduction, trajet, déroulement, accès, FAQ) pour que les pages soient réellement distinctes.
Faits de trajet : calcul d'itinéraire OSRM (router.project-osrm.org) depuis la mairie de chaque commune
vers l'institut (43.8294, 5.7861). Repères locaux : Wikipédia (pages des communes) et Insee.
Les accroches « lead », slugs, images, liens Planity et JSON-LD de service restent inchangés.
Syntaxe : {P:texte} dans un paragraphe = lien vers la page de Manosque.
"""
import re
from build_pages import *

PARKING = "place du Docteur Joubert (45 minutes gratuites), Monoprix (1 h 30), La Poste (3 h) et Souvenir Français (3 h)"

CITIES = [
 {
  "slug":"forcalquier",
  "meta":"Épilation laser définitive depuis Forcalquier : environ 25 minutes par la D16 et la D5, ou par la D4100, jusqu'à l'institut LUMIA, à Manosque. Infirmière D.E. et esthéticienne.",
  "voisines":[('villeneuve', 'Villeneuve'), ('volx', 'Volx')],
  "lead":"Depuis la cité comtale de Forcalquier, vingt à vingt-cinq minutes de route suffisent pour rejoindre l'institut, au centre de Manosque.","ville":"Forcalquier","img":"machinelaserlunettes.webp",
  "intro":"Forcalquier s'étend entre la montagne de Lure et le Luberon, à une vingtaine de kilomètres au nord de Manosque. Pour votre épilation laser, l'institut LUMIA vous attend au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Tout commence par un bilan préalable : il valide votre éligibilité, fixe les zones à traiter et estime le nombre de séances.",
  "h2_why":"Une vingtaine de kilomètres entre Forcalquier et l'institut",
  "why":"Deux itinéraires relient Forcalquier à Manosque. Le plus rapide passe par la D16 puis la D5 : environ 20 km, 25 minutes sans trafic. L'autre suit la D4100, la D105 et la D907, sur près de 23 km, pour une durée voisine. Comme les séances sont espacées de 6 à 8 semaines, ce trajet reste occasionnel. Margaux, infirmière diplômée d'État et esthéticienne, assure elle-même chaque séance.",
  "h2_seance":"Prévoir la durée d'une séance",
  "seance":"Après le bilan, chaque séance suit le même cadre : lunettes de protection, rasage de la zone la veille ou sur place, passage du laser avec refroidissement, puis conseils pour la suite. La durée varie de 10 minutes à 1 h 30 selon la zone, ce qu'il faut garder en tête pour caler le retour vers Forcalquier. La méthode complète est détaillée sur {P:la page de Manosque}.",
  "h2_acces":"Venir de Forcalquier et se garer",
  "access":"Depuis le centre de Forcalquier, comptez environ 25 minutes. L'institut se situe au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Quatre parkings se trouvent à proximité : " + PARKING + ". Pour une zone longue à traiter, mieux vaut viser les deux derniers.",
  "faq_access":("Quel itinéraire prendre de Forcalquier à l'institut ?","Le calcul d'itinéraire propose deux options : la D16 puis la D5 (environ 20 km, 25 minutes), ou la D4100, la D105 et la D907 (environ 23 km, durée voisine). L'institut se trouve avenue Jean Giono, sur la D907."),
  "faq_tail":"Depuis Forcalquier, chaque rendez-vous représente un trajet d'environ 25 minutes.",
  "faq_extra":[
    ("La durée d'une séance est-elle la même pour toutes les zones ?","Non : de 10 minutes à 1 h 30 selon la zone. Une petite zone du visage va vite, des jambes entières demandent bien plus de temps. Le bilan préalable fixe le protocole de chaque zone."),
    ("Les poils blancs, blonds ou roux peuvent-ils être traités ?","Le laser cible la mélanine, donc le poil foncé. Les poils blancs, blonds, roux et le duvet n'en contiennent pas assez pour réagir. Le bilan vérifie que votre pilosité est adaptée."),
  ],
  "voisin":"Vos voisins de Villeneuve et de Volx ont aussi une page dédiée : lisez l'{A1}, puis celle de {A2}.",
  "aussi":1,
  "cta":"Réservez votre bilan à Manosque, à environ 25 minutes de Forcalquier. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"greoux-les-bains",
  "meta":"Épilation laser définitive depuis Gréoux-les-Bains, station thermale à environ 20 minutes de l'institut LUMIA, à Manosque. Infirmière D.E. et esthéticienne.",
  "voisines":[('valensole', 'Valensole'), ('pierrevert', 'Pierrevert')],
  "lead":"Station thermale où l'on prend soin de soi, Gréoux-les-Bains n'est qu'à une vingtaine de minutes de route de l'institut.","ville":"Gréoux-les-Bains","img":"laserhomme.webp",
  "intro":"Gréoux-les-Bains est bâtie sur une butte dont les maisons occupent le versant sud, sur le cours du Verdon. La commune fait partie de l'aire d'attraction de Manosque, où se trouve l'institut LUMIA, au 10 Bis avenue Jean Giono. Pour une épilation laser, tout démarre par un bilan : on examine la peau et le poil, on répond à vos questions, puis on construit le protocole.",
  "h2_why":"Quinze kilomètres de départementales",
  "why":"Depuis le village, le trajet emprunte la D952, puis la D82 sur plus de 8 km, avant de rejoindre la D4 et la D907 : environ 15 km, soit une vingtaine de minutes, sans autoroute. La D907 conduit directement avenue Jean Giono. Vous retrouvez à chaque séance la même praticienne, Margaux, esthéticienne et infirmière diplômée d'État, ce qui permet d'ajuster le protocole au fil du temps.",
  "h2_seance":"Soleil et rythme des séances",
  "seance":"Les séances sont espacées de 6 à 8 semaines, et le laser impose d'éviter soleil, UV et autobronzant pendant les 10 jours qui précèdent et les 10 jours qui suivent. Concrètement, on repère sur le calendrier les périodes où la peau sera le moins exposée, puis on cale chaque rendez-vous en conséquence. Aucun médicament photosensibilisant non plus dans les 7 jours avant et après. {P:Les précautions sont détaillées sur la page de Manosque.}",
  "h2_acces":"S'organiser pour le stationnement",
  "access":"Comptez une vingtaine de minutes de route depuis Gréoux-les-Bains. À Manosque, l'institut se situe au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Pour une zone courte, la place du Docteur Joubert laisse 45 minutes gratuites ; le Monoprix en autorise 1 h 30, La Poste et le Souvenir Français 3 h.",
  "faq_access":("Gréoux-les-Bains est-elle loin de l'institut ?","Non : environ 15 km par la D82 et la D907, soit une vingtaine de minutes. Le trajet ne comporte pas d'autoroute, et l'institut se trouve avenue Jean Giono, directement sur la D907."),
  "faq_tail":"Vous restez à une vingtaine de minutes à chaque rendez-vous.",
  "faq_extra":[
    ("Peut-on venir juste après des vacances au soleil ?","Une peau récemment bronzée fait reporter la séance. Il faut éviter soleil, UV et autobronzant 10 jours avant et 10 jours après, puis appliquer une protection solaire élevée sur les zones exposées."),
    ("Combien de temps puis-je rester garé près de l'institut ?","Place du Docteur Joubert, 45 minutes gratuites ; au Monoprix, 1 h 30 ; à La Poste et au Souvenir Français, 3 h. Une séance dure de 10 minutes à 1 h 30 selon la zone."),
  ],
  "voisin":"Les habitants de Valensole et de Pierrevert ont aussi une page : lisez l'{A1}, ainsi que celle de {A2}.",
  "aussi":2,
  "cta":"Réservez votre bilan à Manosque, à une vingtaine de minutes de Gréoux-les-Bains. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"pierrevert",
  "meta":"Épilation laser définitive depuis Pierrevert, entre golf et vignes : l'institut LUMIA, à Manosque, à environ 10 minutes. Infirmière D.E. et esthéticienne.",
  "voisines":[('sainte-tulle', 'Sainte-Tulle'), ('greoux-les-bains', 'Gréoux-les-Bains')],
  "lead":"Entre le golf et les vignes de l'AOC Pierrevert, l'institut LUMIA n'est qu'à une dizaine de minutes de votre village.","ville":"Pierrevert","img":"enseigne.webp","img_class":"portrait",
  "alt":"Façade de l'institut LUMIA à Manosque, enseigne rouge et olivier en pot, à dix minutes de Pierrevert",
  "intro":"Pierrevert se situe à 5 km à l'ouest de Manosque, dans le parc naturel régional du Luberon, et le GR4 traverse la commune. Pour une épilation laser, l'institut LUMIA, au 10 Bis avenue Jean Giono, est donc tout proche : comptez entre 7 et 10 minutes de route. Un bilan préalable précise ensuite votre protocole.",
  "h2_why":"Cinq kilomètres, deux itinéraires",
  "why":"Depuis le village, deux itinéraires mènent à Manosque : l'un d'environ 4,5 km par des voies communales, l'autre d'environ 5,5 km par la D105, la D6 et la D907. Dans les deux cas, le trajet reste sous les 10 minutes. Un trajet aussi court se prête bien à un rendez-vous précis. Margaux, infirmière diplômée d'État et esthéticienne, y assure l'ensemble des séances.",
  "h2_seance":"Visage ou corps : quelles zones ?",
  "seance":"Presque toutes les zones se traitent. Au visage : lèvre supérieure, menton, joues, tempes, inter-sourcils et cou. Sur le corps : aisselles, maillot simple, échancré ou intégral, jambes entières ou demi-jambes. Les zones non listées sont examinées lors du bilan, qui précise le protocole. {P:La page de Manosque détaille la méthode.}",
  "h2_acces":"À moins de dix minutes, et où se garer",
  "access":"Depuis Pierrevert, le trajet dure entre 7 et 10 minutes. Vous trouvez l'institut au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Pour un rendez-vous court, le plus simple est la place du Docteur Joubert, avec 45 minutes gratuites ; au Monoprix, comptez 1 h 30, et 3 h à La Poste comme au Souvenir Français.",
  "faq_access":("Pierrevert est-elle vraiment proche de l'institut ?","Oui : le village est à environ 5 km à l'ouest de Manosque, soit entre 7 et 10 minutes en voiture selon l'itinéraire et la circulation."),
  "faq_tail":"Depuis Pierrevert, cela revient à un court trajet toutes les 6 à 8 semaines.",
  "faq_extra":[
    ("Puis-je m'épiler à la cire entre deux séances ?","Non : entre les séances, seul le rasage est autorisé. La cire, la pince et l'épilateur retirent le poil avec sa racine, alors que le laser agit justement sur la racine."),
    ("Le laser s'adresse-t-il aussi aux hommes ?","Oui, aux femmes comme aux hommes. Côté hommes, les zones les plus demandées sont la barbe et les oreilles, le dos, le torse et les épaules."),
  ],
  "voisin":"Dans le secteur, lisez aussi l'{A1} et la page de {A2}.",
  "aussi":3,
  "cta":"Réservez votre bilan à Manosque, à moins de 10 minutes de Pierrevert. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"oraison",
  "meta":"Épilation laser définitive depuis Oraison, au bord de la Durance : l'institut LUMIA, à Manosque, à environ 20 minutes. Infirmière D.E. et esthéticienne.",
  "voisines":[('valensole', 'Valensole'), ('volx', 'Volx')],
  "lead":"Au bord de la Durance, Oraison est à une vingtaine de minutes de l'institut LUMIA, par la D4096 puis la D907.","ville":"Oraison","img":"machinelaser.webp","img_class":"portrait",
  "intro":"Oraison se trouve au confluent de la Durance et de l'Asse, au pied de la colline du Tholonet, à un kilomètre de l'échangeur de La Brillanne sur l'A51. Pour votre épilation laser, l'institut LUMIA vous reçoit à Manosque, au 10 Bis avenue Jean Giono. Le bilan préalable, obligatoire, ouvre le parcours : il fixe les zones et le protocole.",
  "h2_why":"Par l'A51 ou par la D4096",
  "why":"Depuis Oraison, l'itinéraire le plus rapide rejoint l'A51 à l'échangeur de La Brillanne (sortie 19), roule près de 14 km jusqu'à la sortie de Manosque (sortie 18), puis suit la D907 : environ 21 km, une vingtaine de minutes. L'ancienne nationale D4096, par Villeneuve et Volx, reste possible pour une durée comparable. Margaux, esthéticienne et infirmière diplômée d'État, vous suit d'une séance à l'autre.",
  "h2_seance":"Préparer sa peau et son poil",
  "seance":"Avant chaque séance, la zone est rasée, la veille ou sur place, pour que le laser agisse sur la racine. Les aisselles demandent en plus de ne pas mettre de déodorant le jour même. Entre deux séances, seul le rasage est autorisé : ni cire, ni pince, ni épilateur. Tout le reste de la méthode est présenté sur {P:la page de Manosque}.",
  "h2_acces":"Arriver d'Oraison, stationner à Manosque",
  "access":"Au volant, comptez une vingtaine de minutes depuis Oraison. L'institut est situé au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Pour stationner dans le quartier : " + PARKING + ".",
  "faq_access":("Faut-il prendre l'autoroute pour venir d'Oraison ?","Ce n'est pas obligatoire. L'A51 est la voie la plus rapide, avec l'échangeur de La Brillanne à un kilomètre d'Oraison, mais la D4096 mène aussi à Manosque en une vingtaine de minutes environ."),
  "faq_tail":"Depuis Oraison, comptez une vingtaine de minutes à chaque fois.",
  "faq_extra":[
    ("Comment préparer la zone avant la séance ?","Rasez la zone la veille, ou faites-le sur place. Pas de déodorant sur les aisselles le jour de la séance, et pas de cire, de pince ni d'épilateur entre deux séances : seul le rasage est autorisé."),
    ("Quelles zones peut-on faire traiter à l'institut ?","Presque toutes les zones du visage et du corps : lèvre supérieure, menton, joues, aisselles, maillot, jambes, et pour les hommes barbe, dos, torse et épaules. Pour les autres, le bilan précise le protocole."),
  ],
  "voisin":"Pour les communes proches, lisez aussi l'{A1} et la page de {A2}.",
  "aussi":2,
  "cta":"Réservez votre bilan à Manosque, à une vingtaine de minutes d'Oraison. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"sainte-tulle",
  "meta":"Épilation laser définitive depuis Sainte-Tulle, à 5,5 km de Manosque : une zone courte tient dans une pause déjeuner. Infirmière D.E. et esthéticienne.",
  "voisines":[('pierrevert', 'Pierrevert'), ('greoux-les-bains', 'Gréoux-les-Bains')],
  "lead":"Voisine immédiate de Manosque, à 5,5 kilomètres, Sainte-Tulle permet de traiter une zone courte le temps d'une pause déjeuner, trajet compris.","ville":"Sainte-Tulle","img":"accueil.webp",
  "alt":"Accueil de l'institut LUMIA à Manosque, comptoir en bois clair et étagères de soins, à moins de dix minutes de Sainte-Tulle",
  "intro":"Avec sa tour de l'horloge de 1544 et ses lavoirs de la fontaine Plus-basse, Sainte-Tulle est la commune voisine de Manosque, à 5,5 km au sud. Pour une épilation laser, l'institut LUMIA est au 10 Bis avenue Jean Giono, à moins de 10 minutes de route. Le bilan préalable, obligatoire, définit les zones et le rythme des séances.",
  "h2_why":"Un seul axe, la D4096",
  "why":"Le trajet le plus direct suit la D4096 sur environ 5,5 km et arrive avenue Jean Giono. Il dure entre 7 et 10 minutes, ce qui rend possible un rendez-vous pris entre deux obligations. Margaux, infirmière diplômée d'État et esthéticienne, y reçoit chaque cliente avec un protocole suivi d'une séance à l'autre.",
  "h2_seance":"Une zone courte, un rendez-vous court",
  "seance":"La durée d'une séance va de 10 minutes à 1 h 30 selon la zone, et les petites zones comme la lèvre supérieure, le menton ou les aisselles sont les plus rapides. La zone est rasée au préalable, la veille ou sur place, et les lunettes de protection sont portées tout du long. {P:Les autres zones sont détaillées sur la page de Manosque.}",
  "h2_acces":"Se garer pour un rendez-vous rapide",
  "access":"Depuis Sainte-Tulle, comptez moins de 10 minutes, soit 5,5 km. L'institut est au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Pour une séance rapide, le parking de la place du Docteur Joubert laisse 45 minutes gratuites ; le Monoprix en accorde 1 h 30, La Poste et le Souvenir Français 3 h.",
  "faq_access":("Une séance tient-elle dans une pause déjeuner depuis Sainte-Tulle ?","Pour une zone courte, c'est envisageable : le trajet dure moins de 10 minutes dans chaque sens et une séance démarre à 10 minutes. Une zone plus étendue demande davantage, jusqu'à 1 h 30."),
  "faq_tail":"Sainte-Tulle étant à 5,5 km, chaque rendez-vous reste un déplacement de quelques minutes.",
  "faq_extra":[
    ("Où me garer pour une séance courte ?","Le parking de la place du Docteur Joubert laisse 45 minutes gratuites, ce qui convient à une petite zone. Pour davantage de temps : Monoprix (1 h 30), La Poste ou Souvenir Français (3 h)."),
    ("Quelles zones se prêtent à un rendez-vous court ?","Les petites zones : lèvre supérieure, menton, aisselles. Le bilan préalable précise le protocole de chacune."),
  ],
  "voisin":"Les communes limitrophes ont aussi leur page : l'{A1} et celle de {A2}.",
  "aussi":3,
  "cta":"Réservez votre bilan à Manosque, à moins de 10 minutes de Sainte-Tulle. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"volx",
  "meta":"Épilation laser définitive depuis Volx : environ 8 km par la D4096, soit une dizaine de minutes jusqu'à l'institut LUMIA, à Manosque. Infirmière D.E. et esthéticienne.",
  "voisines":[('villeneuve', 'Villeneuve'), ('forcalquier', 'Forcalquier')],
  "lead":"Adossé à son rocher, Volx rejoint Manosque par la D4096 : environ huit kilomètres, soit une dizaine de minutes jusqu'à l'institut.","ville":"Volx","img":"cabinedesoin.webp","img_class":"portrait",
  "alt":"Cabine de soin de l'institut LUMIA sous sa voûte en pierre, lampe LED et table de soin, à dix minutes de Volx",
  "intro":"Volx s'étire le long de la D4096, à environ 8 km de Manosque, son vieux village dominant la plaine une cinquantaine de mètres plus haut. La commune abrite notamment un écomusée de l'olivier, installé dans d'anciens fours à chaux. Pour votre épilation laser, l'institut LUMIA, au centre de Manosque, est à une dizaine de minutes.",
  "h2_why":"Une dizaine de minutes par la D4096",
  "why":"Depuis le centre de Volx, la D4096 conduit à Manosque sur environ 7,5 km : une dizaine de minutes, sans autoroute et sans changer de route. Margaux, infirmière diplômée d'État et esthéticienne, connaît votre peau et votre protocole d'une séance à l'autre, ce qui compte sur un parcours étalé dans le temps.",
  "h2_seance":"Le ressenti pendant la séance",
  "seance":"La sensation ressemble à de petits picotements de chaleur, parfois comparés à un léger claquement d'élastique. Le système de refroidissement intégré au laser apaise la peau, et les lunettes de protection restent portées pendant toute la séance. Ces séances se répètent tous les 6 à 8 semaines, après le bilan. {P:Plus d'explications sur la page de Manosque.}",
  "h2_acces":"Arriver de Volx, stationner à Manosque",
  "access":"Comptez une dizaine de minutes depuis Volx, soit environ 8 km. L'institut est au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Parkings voisins : place du Docteur Joubert (45 minutes gratuites), Monoprix (1 h 30), La Poste et Souvenir Français (3 h chacun).",
  "faq_access":("Combien de kilomètres séparent Volx de l'institut ?","Environ 8 km par la D4096, soit une dizaine de minutes en voiture, sans autoroute."),
  "faq_tail":"Volx étant à une dizaine de minutes, ce rythme s'organise sans difficulté.",
  "faq_extra":[
    ("La séance est-elle douloureuse ?","Plutôt des picotements de chaleur, parfois comparés à un léger claquement d'élastique. Le refroidissement du laser rend la séance bien supportable."),
    ("Comment se déroule une séance, étape par étape ?","Lunettes de protection, rasage préalable de la zone (la veille ou sur place), passage du laser avec refroidissement, puis conseils d'après-séance et planification de la suivante."),
  ],
  "voisin":"Vos voisins de Villeneuve et de Forcalquier ont leur propre page : l'{A1}, et celle de {A2}.",
  "aussi":1,
  "cta":"Réservez votre bilan à Manosque, à une dizaine de minutes de Volx. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"villeneuve",
  "title":"Épilation laser à Villeneuve (04) | LUMIA Manosque",
  "meta":"Épilation laser définitive depuis Villeneuve, perché sur le Luberon : une quinzaine de minutes jusqu'à LUMIA, à Manosque. Infirmière D.E. et esthéticienne.",
  "voisines":[('volx', 'Volx'), ('forcalquier', 'Forcalquier')],
  "lead":"Perché à 450 mètres contre le versant oriental du Luberon, Villeneuve rejoint l'institut en une quinzaine de minutes par la vallée de la Durance.","ville":"Villeneuve","img":"laserhomme.webp",
  "intro":"Le vieux village de Villeneuve domine la vallée de la Durance, à 11 km de Manosque, entre Volx et La Brillanne. La D4096 relie ces communes, et la D216 monte vers Forcalquier. Pour votre épilation laser, l'institut LUMIA vous reçoit au 10 Bis avenue Jean Giono, après un bilan préalable.",
  "h2_why":"Onze kilomètres par la D4096",
  "why":"Depuis Villeneuve, la D4096 traverse Volx puis rejoint Manosque : environ 11 km, une quinzaine de minutes. Le trajet reste le même à chaque séance, et la même praticienne vous suit : Margaux, infirmière diplômée d'État et esthéticienne.",
  "h2_seance":"Après la séance",
  "seance":"À la fin de chaque séance viennent les conseils d'après-séance et la planification du rendez-vous suivant, 6 à 8 semaines plus tard. Pour apaiser la peau, un gel d'aloe vera convient, avec une protection solaire élevée sur les zones exposées. Entre deux séances, seul le rasage est autorisé. {P:Les règles complètes sont sur la page de Manosque.}",
  "h2_acces":"De Villeneuve à l'avenue Jean Giono",
  "access":"Depuis Villeneuve, comptez une quinzaine de minutes en suivant la D4096. L'institut est au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Stationnement à proximité : 45 minutes gratuites place du Docteur Joubert, 1 h 30 au Monoprix, 3 h à La Poste et au Souvenir Français.",
  "faq_access":("Quelle distance sépare Villeneuve de l'institut ?","Environ 11 km par la D4096, via Volx, soit une quinzaine de minutes en voiture."),
  "faq_tail":"Depuis Villeneuve, une quinzaine de minutes suffisent à chaque rendez-vous.",
  "faq_extra":[
    ("Que faire si j'ai la peau bronzée ?","Une peau récemment bronzée fait reporter la séance, le temps que le bronzage s'estompe. Soleil, UV et autobronzant sont à éviter 10 jours avant et 10 jours après chaque séance."),
    ("Que faire dans les jours qui suivent une séance ?","Apaiser la peau avec un gel d'aloe vera, appliquer une protection solaire élevée sur les zones exposées et éviter soleil et UV pendant 10 jours. Pour les poils qui repoussent, le rasage reste autorisé."),
  ],
  "voisin":"Lisez aussi les pages voisines : l'{A1} et celle de {A2}.",
  "aussi":2,
  "cta":"Réservez votre bilan à Manosque, à une quinzaine de minutes de Villeneuve. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"sisteron",
  "meta":"Épilation laser depuis Sisteron : 54 km par l'A51, un déplacement tous les deux mois (séances espacées de 6 à 8 semaines). Infirmière D.E. et esthéticienne.",
  "title":"Épilation laser depuis Sisteron | LUMIA Manosque",
  "lead":"Entre la citadelle et le rocher de la Baume, Sisteron est à 54 kilomètres : avec des séances espacées de 6 à 8 semaines, le trajet reste occasionnel.","ville":"Sisteron","img":"machinelaserlunettes.webp","img_class":"portrait",
  "intro":"Surnommée « la porte de la Provence », Sisteron se tient là où la Durance franchit la cluse de la Baume. L'institut LUMIA, à Manosque, accueille régulièrement des clientes et clients de Sisteron pour leur épilation laser : 54 km par l'A51, environ 40 minutes de route. Le bilan préalable permet de savoir si le déplacement convient à votre projet.",
  "h2_why":"Cinquante-quatre kilomètres, un déplacement tous les deux mois",
  "why":"Soyons honnêtes : depuis Sisteron, il faut compter environ 40 minutes de route, dont 45 km d'A51 entre l'échangeur de Sisteron-Centre et la sortie de Manosque. Un parcours complet compte 8 à 12 séances espacées de 6 à 8 semaines, soit en moyenne un déplacement tous les deux mois. Si des clientes font le trajet, c'est pour le suivi par Margaux, infirmière diplômée d'État et esthéticienne, et pour un protocole personnalisé.",
  "h2_seance":"Regrouper les zones pour limiter les allers-retours",
  "seance":"Quand on vient de loin, on regroupe : les séances peuvent traiter plusieurs zones le même jour, chacune demandant de 10 minutes à 1 h 30. Le bilan, obligatoire avant la première séance, comprend un questionnaire de santé, la présentation du laser et un flash test. Mieux vaut le préparer à l'avance avec {P:la page de Manosque}.",
  "h2_acces":"De Sisteron à l'avenue Jean Giono",
  "access":"L'itinéraire suit la D4085 puis la D4 jusqu'à l'échangeur de Sisteron-Centre, l'A51 sur 45 km, puis la sortie de Manosque et la D907 : environ 54 km, 40 minutes. L'institut est au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL. Pour une séance qui regroupe plusieurs zones, garez-vous plutôt à La Poste ou au Souvenir Français (3 h) ; la place du Docteur Joubert laisse 45 minutes gratuites, le Monoprix 1 h 30.",
  "faq_access":("Cela vaut-il le déplacement depuis Sisteron ?","Sisteron est à environ 54 km de Manosque, soit environ 40 minutes par l'A51. Les séances étant espacées de 6 à 8 semaines, le déplacement reste occasionnel, et plusieurs zones peuvent être traitées le même jour pour le limiter."),
  "faq_tail":"Depuis Sisteron, cela représente en moyenne un déplacement tous les deux mois.",
  "faq_extra":[
    ("Quel est l'itinéraire de Sisteron à l'institut ?","Par la D4085 et la D4 jusqu'à l'échangeur de Sisteron-Centre, puis l'A51 pendant 45 km jusqu'à la sortie de Manosque, et enfin la D907, qui mène avenue Jean Giono."),
    ("Peut-on regrouper plusieurs zones sur une même journée ?","Oui, les séances peuvent être regroupées pour traiter plusieurs zones le même jour. Prévoyez alors un temps de présence plus long, et choisissez un parking où le stationnement dure 3 h."),
  ],
  "voisin":"Les clientes et clients de {A1} sont aussi accueillis à l'institut, et toute la méthode est détaillée sur la page consacrée à l'{P2}.",
  "aussi":3,
  "cta":"Réservez votre bilan à Manosque et regroupez vos zones pour limiter les trajets. Il est offert pour tout achat de séance ou de cure.",
 },
 {
  "slug":"valensole",
  "meta":"Épilation laser définitive depuis le plateau de Valensole : environ 25 minutes par la D6 jusqu'à l'institut LUMIA, à Manosque. Infirmière D.E. et esthéticienne.",
  "voisines":[('oraison', 'Oraison'), ('greoux-les-bains', 'Gréoux-les-Bains')],
  "lead":"Du plateau de Valensole et de ses champs de lavande, comptez environ 25 minutes par la D6 pour rejoindre l'institut, au centre de Manosque.","ville":"Valensole","img":"machinelaserlunettes.webp",
  "intro":"Le bourg de Valensole, à 595 m d'altitude, s'étage en amphithéâtre sur une colline entre le plateau et la vallée de Notre-Dame. Pour votre épilation laser, l'institut LUMIA se trouve à Manosque, au 10 Bis avenue Jean Giono, à environ 21 km par la D6 puis la D907. On y commence toujours par un bilan.",
  "h2_why":"La D6 jusqu'à Manosque",
  "why":"Depuis le village, la D6 parcourt une quinzaine de kilomètres jusqu'à la D907, qui mène à l'avenue Jean Giono : environ 21 km au total, 25 minutes. La commune compte aussi plusieurs hameaux, parfois plus éloignés : ajoutez quelques minutes si vous partez de l'un d'eux. La même praticienne, Margaux, infirmière diplômée d'État et esthéticienne, suit chaque protocole.",
  "h2_seance":"Ce que contient le bilan",
  "seance":"Le bilan précède toute première séance. Il comprend un questionnaire de santé, la présentation du laser, une fiche d'information et de consentement à signer, puis un flash test qui valide votre éligibilité. Les séances s'enchaînent ensuite tous les 6 à 8 semaines. {P:La page de Manosque reprend chaque étape.}",
  "h2_acces":"Rejoindre Manosque et se garer",
  "access":"Comptez environ 25 minutes depuis le village de Valensole. L'institut se situe au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL, sur l'axe de la D907. Quatre parkings voisins : " + PARKING + ".",
  "faq_access":("Combien de temps faut-il pour aller de Valensole à l'institut ?","Environ 25 minutes depuis le village, pour 21 km par la D6 puis la D907. Les hameaux plus éloignés demandent quelques minutes de plus."),
  "faq_tail":"Depuis Valensole, comptez environ 25 minutes à chaque rendez-vous.",
  "faq_extra":[
    ("Que se passe-t-il lors du bilan avant la première séance ?","On examine votre peau et votre poil, on répond à vos questions, on réalise un flash test et on définit votre protocole. Le questionnaire de santé et la fiche d'information et de consentement sont traités à ce moment."),
    ("Quel intervalle entre deux séances ?","En général 6 à 8 semaines au début, puis on espace au fil de la repousse. L'intervalle est ajusté à chaque séance."),
  ],
  "voisin":"Au-delà du plateau, lisez aussi l'{A1} et la page de {A2}.",
  "aussi":1,
  "cta":"Réservez votre bilan à Manosque, à environ 25 minutes de Valensole. Il est offert pour tout achat de séance ou de cure.",
 },
]

def de(nom):
    """Élision : « de » devient « d' » devant une voyelle ou un h muet (de Manosque, d'Oraison)."""
    return ("d'" if nom[:1].lower() in "aeiouyàâäéèêëîïôöùûüh" else "de ") + nom

def lk(txt):
    """{P:texte} devient un lien vers la page pilier de Manosque."""
    return re.sub(r"\{P:([^}]+)\}", r'<a href="epilation-laser-manosque.html">\1</a>', txt)

AUSSI = [
 'Découvrez aussi <a href="a-propos.html">Margaux, la praticienne de LUMIA</a>, nos <a href="soins-visage-manosque.html">soins du visage</a> et les <a href="tarifs.html">tarifs</a>.',
 'Pour faire connaissance, rendez-vous sur la page de <a href="a-propos.html">Margaux, la praticienne</a> ; les <a href="tarifs.html">tarifs</a> et les <a href="soins-visage-manosque.html">soins du visage</a> sont à portée de clic.',
 'Les <a href="tarifs.html">tarifs</a>, les <a href="soins-visage-manosque.html">soins du visage</a> et la présentation de <a href="a-propos.html">la praticienne</a> complètent cette page.',
]

for c in CITIES:
    ville = c["ville"]; slug = c["slug"]
    url = "https://lumia-salon.fr/epilation-laser-%s.html" % slug
    imgcls = c.get("img_class","landscape")
    # R10 (23/11/2026) : l'alt décrit la photo réelle quand elle ne montre pas le laser
    alt = c.get("alt", "Épilation laser diode Leaseir à l'institut LUMIA, près %s" % de(ville))
    w,h = img_size(c["img"])
    # FAQ : 1 question commune aux 9 villes (nombre de séances), les 3 autres propres à la ville
    commune = ("Combien de séances d'épilation laser faut-il ?",
               "En moyenne 8 à 12 séances selon la zone, la couleur du poil et votre type de peau, espacées de 6 à 8 semaines. Le bilan préalable précise votre protocole et le nombre de séances estimé. " + c["faq_tail"])
    faq = [c["faq_access"], commune] + c["faq_extra"]
    if c["slug"] == "sisteron":
        voisin = c["voisin"].replace("{A1}", '<a href="epilation-laser-forcalquier.html">Forcalquier</a>').replace(
                 "{P2}", '<a href="epilation-laser-manosque.html">épilation laser à Manosque</a>')
    else:
        (s1, n1), (s2, n2) = c["voisines"]
        a1 = '<a href="epilation-laser-%s.html">épilation laser à %s</a>' % (s1, n1)
        a2 = '<a href="epilation-laser-%s.html">%s</a>' % (s2, n2)
        voisin = c["voisin"].replace("{A1}", a1).replace("{A2}", a2)
    aussi = AUSSI[(c["aussi"] - 1) % 3]
    body = header_block(
      [("Accueil","./"),("Épilation laser",("epilation-laser-manosque.html")),("Épilation laser à %s" % ville, None)],
      "Épilation laser définitive à %s" % ville,
      c["lead"]) + ("""
<main id="main"><article class="article-body"><div class="container">
<p>%s</p>
<div class="hero__actions"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a><a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA au 04 92 87 63 72">04 92 87 63 72</a></div>

<h2>%s</h2>
<p>%s</p>

<img src="assets/%s" class="%s" alt="%s" width="%s" height="%s" loading="lazy">

<p class="text-center mt-2"><a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Réserver mon bilan laser</a><span class="btn-note">Bilan à 20 €, offert pour tout achat de séance ou de cure.</span></p>

<h2>%s</h2>
<p>%s</p>

<h2>%s</h2>
<p>%s</p>

<h2>Questions fréquentes</h2>
%s
<p>%s</p>
<p>%s</p>
</div></article>
%s</main>
""" % (c["intro"], PLANITY, c["h2_why"], c["why"], c["img"], imgcls, alt, w, h, PLANITY,
       c["h2_seance"], lk(c["seance"]), c["h2_acces"], c["access"], faq_html(faq), voisin, aussi,
       cta('Épilation laser à <span class="accent">%s</span>' % ville, c["cta"])))
    schema = (schema_service("Épilation laser","Épilation laser définitive à %s" % ville,
              "Épilation laser définitive pour les habitants %s, réalisée à Manosque par une infirmière diplômée d'État et esthéticienne. Laser diode adapté à de nombreux phototypes, bilan offert pour tout achat." % de(ville), url)
              .replace('"areaServed":{"@type":"City","name":"Manosque"}', '"areaServed":{"@type":"City","name":"%s"}' % ville)
              + schema_faq(faq)
              + schema_breadcrumb([("Accueil",BASE),("Épilation laser",BASE+"epilation-laser-manosque.html"),("Épilation laser à %s" % ville, url)]))
    page("epilation-laser-%s.html" % slug,
         c.get("title", "Épilation laser à %s | LUMIA Manosque" % ville),
         c["meta"],
         url, body, schema)
print("locales OK")
