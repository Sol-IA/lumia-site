import re
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère à-propos, tarifs, contact, politique de confidentialité, 404."""
from build_pages import *

# ============================ À PROPOS ============================
apropos_schema = ('<script type="application/ld+json">\n'
'{ "@context":"https://schema.org","@type":"Person","name":"Margaux",'
'"jobTitle":"Infirmière diplômée d\'État, esthéticienne et praticienne en épilation laser",'
'"worksFor":{"@type":"BeautySalon","@id":"https://lumia-salon.fr/#institut","name":"LUMIA","url":"https://lumia-salon.fr"},'
'"url":"https://lumia-salon.fr/a-propos.html" }\n</script>\n'
'<script type="application/ld+json">\n'
'{ "@context":"https://schema.org","@type":"BeautySalon","@id":"https://lumia-salon.fr/#institut","name":"LUMIA","url":"https://lumia-salon.fr","sameAs":["https://www.planity.com/lumia-04100-manosque","https://www.instagram.com/lumiamanosque"],"hasMap":"https://www.google.com/maps?cid=2478910083160358823",'
'"telephone":"+33492876372","address":{"@type":"PostalAddress","streetAddress":"10 Bis avenue Jean Giono","addressLocality":"Manosque","postalCode":"04100","addressCountry":"FR"},'
'"founder":{"@type":"Person","name":"Margaux","jobTitle":"Infirmière diplômée d\'État, esthéticienne et praticienne en épilation laser"} }\n</script>\n'
+ schema_breadcrumb([("Accueil",BASE),("À propos",BASE+"a-propos.html")]))
apropos_body = header_block(
  [("Accueil","./"),("À propos",None)],
  "Margaux, infirmière diplômée d'État et esthéticienne",
  "Fondatrice de l'institut LUMIA à Manosque, elle apporte la rigueur du soin à l'esthétique.") + """
<main id="main"><article class="article-body"><div class="container">
<p>LUMIA est l'institut de Margaux, infirmière diplômée d'État et esthéticienne, à Manosque, dans les Alpes-de-Haute-Provence. Après plusieurs années au service des patients, elle a choisi de mettre la précision et l'écoute du soin infirmier au service de la beauté : épilation laser, soins du visage, LPG et soins dépigmentants. L'institut a ouvert à l'automne 2024 et s'est construit autour d'une idée simple, vous accompagner sur-mesure, avec la même interlocutrice à chaque rendez-vous.</p>

<img src="assets/margaux.webp" class="portrait" alt="Margaux, infirmière diplômée d'État, esthéticienne et fondatrice de l'institut LUMIA à Manosque" width="900" height="900" loading="eager" fetchpriority="high">

<h2>Le fil conducteur : du soin à l'esthétique</h2>
<p>Margaux est infirmière diplômée d'État (2015-2018). Elle s'est ensuite formée à l'épilation laser (Formation Socle LASER, 2024), aux soins du visage EsthéSkin et Corpoderm (2025), puis au protocole COSMELAN de Mesoestetic (2025). Elle a obtenu le CAP Esthétique en 2026 et s'est formée au microneedling la même année. Cette formation continue se retrouve dans sa façon de travailler : questionnaire de santé, consentement éclairé, fiche de suivi. C'est la rigueur du soin appliquée à votre beauté, et c'est le cœur de la confiance que vous accordent ses clientes et clients.</p>

<h2>L'institut</h2>
<p>L'institut se trouve au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL, dans un cadre cocon aux arches de pierre et aux matières chaleureuses. On y travaille avec des marques exigeantes, Mesoestetic et LPG, pour les cosmétiques corps, les compléments alimentaires et le visage, et un matériel professionnel : un laser diode Leaseir, la machine EsthéSkin pour les soins du visage, la LPG Cellu M6 Alliance et le PEN MESOESTETIC pour le soin microneedling.</p>

<img src="assets/accueil.webp" class="landscape" alt="L'accueil de l'institut LUMIA à Manosque, mur en arche et comptoir en bois" width="1360" height="907" loading="lazy">

<h2>Des qualifications datées et vérifiables</h2>
<p>La transparence fait partie du soin. Voici les repères de formation de la praticienne.</p>

<img src="assets/interieur.webp" class="landscape" alt="Couloir et espace d'attente de l'institut LUMIA à Manosque, arches de pierre et lumière douce" width="1600" height="1066" loading="lazy">

<ul>
<li>2015 à 2018 : diplôme d'État d'infirmière.</li>
<li>2024 : Formation Socle LASER (épilation laser à visée non thérapeutique).</li>
<li>2025 : formation soins du visage EsthéSkin (Corpoderm).</li>
<li>2025 : formation au protocole COSMELAN de Mesoestetic.</li>
<li>2026 : CAP Esthétique.</li>
<li>2026 : formation au microneedling (micro-stimulation).</li>
</ul>
<p>L'attestation de formation à l'épilation laser est affichée à l'institut. Découvrez nos prestations : <a href="epilation-laser-manosque.html">épilation laser</a>, <a href="soins-visage-manosque.html">soins du visage</a>, <a href="lpg-cellu-m6-manosque.html">LPG</a> et <a href="soin-cosmelan-taches-manosque.html">COSMELAN</a>.</p>
</div></article>
%s</main>
""" % cta('Faisons <span class="accent">connaissance</span>', "Une question ? Écrivez-nous ou appelez-nous, nous vous répondons rapidement.")
page("a-propos.html",
     "Margaux, infirmière D.E. et esthéticienne | LUMIA Manosque",
     "Margaux, infirmière diplômée d'État et esthéticienne (CAP 2026), vous accueille à l'institut LUMIA de Manosque. Parcours, formations et qualifications datées.",
     "https://lumia-salon.fr/a-propos.html", apropos_body, apropos_schema)

# ============================ TARIFS ============================
def trow(name, price, forfait=""):
    f = '<td class="price">%s</td>' % forfait if forfait != "" else '<td></td>'
    return '<tr><td>%s</td><td class="price">%s</td>%s</tr>' % (name, price, f)

tarifs_body = header_block(
  [("Accueil","./"),("Tarifs",None)],
  "Tarifs de l'institut LUMIA à Manosque",
  "Tarifs à la séance, forfaits dégressifs. Bilan obligatoire avant la 1re séance laser, offert pour tout achat.") + """
<main id="main"><article class="article-body"><div class="container">
<nav class="tarifs-nav" aria-label="Aller à une catégorie de tarifs"><a href="#laser">Laser</a><a href="#visage">Soins du visage</a><a href="#soins-led">Soins LED</a><a href="#microneedling">Microneedling</a><a href="#silhouette">Silhouette</a><a href="#cosmelan">COSMELAN</a><a href="#lpg">LPG corps</a><a href="#lpg-visage">LPG visage</a><a href="#modelage">Modelage</a></nav>

<p><strong>En bref :</strong> l'épilation laser coûte de {{LASER_MIN}} à {{LASER_MAX}} euros la séance selon la zone, avant forfait. Tarifs en vigueur au 24 novembre 2026.</p>
<p>Voici les tarifs de l'institut LUMIA à Manosque, à la séance et en forfait. Les prix sont indicatifs et confirmés lors du bilan. Paiement en 3 fois sans frais sur les cures, carte bancaire et espèces acceptées. Le bilan laser (20 euros) est offert pour tout achat de séance ou de cure, et le bilan LPG (40 euros) pour tout achat de forfait ; le diagnostic de peau COSMELAN (20 euros) est déductible du soin en cabine.</p>

<h2 id="laser">Épilation laser</h2>
<p>Tarifs à la séance. Un bilan personnalisé est obligatoire avant la première séance.</p>

<details>
<summary>Épilation laser femme, voir les 16 zones et les tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Zone</th><th>Tarif à la séance</th></tr></thead><tbody>
<tr><td>Inter-sourcils</td><td class="price">31 euros</td></tr><tr><td>Lèvre supérieure</td><td class="price">39 euros</td></tr><tr><td>Menton</td><td class="price">37 euros</td></tr><tr><td>Tempes ou joues</td><td class="price">55 euros</td></tr><tr><td>Aisselles</td><td class="price">54 euros</td></tr><tr><td>Aréoles des seins</td><td class="price">47 euros</td></tr><tr><td>Bas du ventre</td><td class="price">51 euros</td></tr><tr><td>Bas du dos</td><td class="price">61 euros</td></tr><tr><td>Sillon inter-fessier</td><td class="price">44 euros</td></tr><tr><td>Maillot simple</td><td class="price">65 euros</td></tr><tr><td>Maillot échancré</td><td class="price">100 euros</td></tr><tr><td>Maillot intégral</td><td class="price">133 euros</td></tr><tr><td>Avant-bras</td><td class="price">99 euros</td></tr><tr><td>Cuisses</td><td class="price">202 euros</td></tr><tr><td>Demi-jambes</td><td class="price">153 euros</td></tr><tr><td>Jambes entières</td><td class="price">274 euros</td></tr>
</tbody></table></div>
</details>


<details>
<summary>Épilation laser homme, voir les 15 zones et les tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Zone</th><th>Tarif à la séance</th></tr></thead><tbody>
<tr><td>Inter-sourcils</td><td class="price">31 euros</td></tr><tr><td>Oreilles</td><td class="price">39 euros</td></tr><tr><td>Col de chemise</td><td class="price">58 euros</td></tr><tr><td>Barbe</td><td class="price">110 euros</td></tr><tr><td>Aisselles</td><td class="price">63 euros</td></tr><tr><td>Épaules</td><td class="price">103 euros</td></tr><tr><td>Avant-bras</td><td class="price">106 euros</td></tr><tr><td>Bras complets</td><td class="price">159 euros</td></tr><tr><td>Torse</td><td class="price">121 euros</td></tr><tr><td>Ventre</td><td class="price">121 euros</td></tr><tr><td>Fesses</td><td class="price">121 euros</td></tr><tr><td>Dos</td><td class="price">223 euros</td></tr><tr><td>Cuisses</td><td class="price">202 euros</td></tr><tr><td>Demi-jambes</td><td class="price">206 euros</td></tr><tr><td>Jambes entières</td><td class="price">303 euros</td></tr>
</tbody></table></div>
</details>


<p>Des cures existent sur la plupart des zones, à des tarifs avantageux par rapport aux séances à l'unité et réglables en 3 fois sans frais. Le montant vous est communiqué lors du bilan, en fonction de votre peau et du nombre de séances nécessaires. La méthode et le déroulement d'une séance sont détaillés sur la page <a href="epilation-laser-manosque.html">épilation laser à Manosque</a>.</p>
<p class="lead">Bilan / diagnostic laser : 20 euros, offert pour tout achat de séance ou de cure.</p>

<h2 id="visage">Soins du visage LUMINEA (EsthéSkin)</h2>
<details>
<summary>Voir les 5 soins LUMINEA et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>LUMINEA Express nettoyage</td><td>30 min</td><td class="price">45 euros</td></tr><tr><td>LUMINEA Express radiofréquence (visage ou cou)</td><td>30 min</td><td class="price">49 euros</td></tr><tr><td>LUMINEA Découverte</td><td>1h15</td><td class="price">95 euros</td></tr><tr><td>LUMINEA Avancé</td><td>1h15</td><td class="price">115 euros</td></tr><tr><td>LUMINEA Prestige LPG Visage OU LED</td><td>1h30</td><td class="price">135 euros</td></tr>
</tbody></table></div>
</details>

<h2 id="soins-led">Soins du visage avec LED</h2>
<details>
<summary>Voir les 4 soins LED et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Détail</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Soin anti-âge + LED</td><td>1h</td><td class="price">95 euros</td></tr><tr><td>Nettoyage &amp; hydratation + LED</td><td>1h (cure 10+2 offertes)</td><td class="price">80 euros</td></tr><tr><td>Séance LED visage</td><td>30 min</td><td class="price">35 euros</td></tr><tr><td>Cure LED visage 10+2</td><td>12 séances</td><td class="price">350 euros</td></tr>
</tbody></table></div>
</details>

<h2 id="microneedling">Micro-stimulation, microneedling Mesoestetic</h2>
<p>Stimulation de la peau par micro-perforations contrôlées à une profondeur de 0,25 mm, avec des actifs Mesoestetic composés d'exosomes et de PDRN. Sans injection de produit. La LED est incluse lors de la pose du masque. Le soin est présenté sur la page <a href="microneedling-manosque.html">microneedling à Manosque</a>.</p>
<details>
<summary>Voir les 2 prestations et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Prestation</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>RDV diagnostic visage</td><td>30 min</td><td class="price">20 euros</td></tr><tr><td>Microneedling visage et cou</td><td>1h</td><td class="price">145 euros</td></tr>
</tbody></table></div>
</details>
<p>Recommandé en cure, une séance tous les quinze jours pendant six séances, puis un entretien tous les deux mois.</p>

<h2 id="silhouette">Cure Expertise Silhouette</h2>
<p>Cure de six séances associant 45 minutes de drainage lymphatique et 30 minutes de LPG, soit une séance complète d'1h15, avec un bilan de 20 minutes avant la cure. Disponible pour le bas du corps ou pour le ventre et la taille. Cure réalisée avec <a href="https://www.sophiemassagebienetre.com" target="_blank" rel="noopener">Emana by Sophie</a>, praticienne en massage bien-être installée dans nos locaux.</p>
<details>
<summary>Voir le détail de la cure et son tarif</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Prestation</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Première séance : drainage lymphatique 45 min et LPG 30 min</td><td>1h15</td><td class="price">120 euros</td></tr>
</tbody></table></div>
</details>
<p class="lead">120 euros d'économies pour l'achat de la cure, jusqu'au 31 décembre 2026.</p>

<h2 id="cosmelan">Soins dépigmentants COSMELAN</h2>
<p>Le protocole, en cabine puis à la maison, est expliqué sur la page <a href="soin-cosmelan-taches-manosque.html">soins dépigmentants COSMELAN à Manosque</a>.</p>
<details>
<summary>Voir les 3 prestations et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Prestation</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Diagnostic de peau</td><td>RDV préalable</td><td class="price">20 euros (déductible)</td></tr><tr><td>Soin cabine (diagnostic + home pack)</td><td>45 min</td><td class="price">650 euros</td></tr><tr><td>Soin apaisant post-COSMELAN</td><td>45 min</td><td class="price">50 euros</td></tr>
</tbody></table></div>
</details>

<h2 id="lpg">LPG Cellu M6, corps</h2>
<p>Les protocoles corps et visage sont présentés sur la page <a href="lpg-cellu-m6-manosque.html">LPG endermologie à Manosque</a>.</p>
<details>
<summary>Voir les 10 soins du corps et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Bilan personnalisé</td><td>30 min</td><td class="price">40 euros (offert pour un forfait)</td></tr><tr><td>Anti-cellulite</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Jeune maman</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Relaxation</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Détox drainant</td><td>40 min</td><td class="price">70 euros</td></tr><tr><td>Soins zones</td><td>10 min</td><td class="price">20 euros</td></tr><tr><td>Soins zones</td><td>20 min</td><td class="price">40 euros</td></tr><tr><td>Soins zones</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Soins zones</td><td>40 min</td><td class="price">80 euros</td></tr><tr><td>Tenue Endermowear</td><td>obligatoire pour le corps</td><td class="price">20 euros (offerte pour tout achat de soin corps)</td></tr>
</tbody></table></div>
</details>

<h2 id="lpg-visage">LPG Cellu M6, visage</h2>
<p>Soins zones, de 1 à 9 zones au choix (front, regard anti-rides, poches et cernes, bouche, double menton, ovale, cou, décolleté, mains), facturés selon la durée.</p>
<details>
<summary>Voir les 5 soins du visage et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Bilan personnalisé</td><td>30 min</td><td class="price">40 euros (offert pour un forfait)</td></tr><tr><td>Soins zones</td><td>10 min</td><td class="price">20 euros</td></tr><tr><td>Soins zones</td><td>20 min</td><td class="price">40 euros</td></tr><tr><td>Soins zones</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Soins zones</td><td>40 min</td><td class="price">80 euros</td></tr>
</tbody></table></div>
</details>

<h3>Soins classiques visage</h3>
<details>
<summary>Voir les 5 soins classiques et leurs tarifs</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Éclat</td><td>15 min</td><td class="price">35 euros</td></tr><tr><td>Détox</td><td>20 min</td><td class="price">45 euros</td></tr><tr><td>Anti-âge repulpant</td><td>30 min</td><td class="price">65 euros</td></tr><tr><td>Anti-âge fermeté</td><td>30 min</td><td class="price">65 euros</td></tr><tr><td>Anti-âge affinant</td><td>30 min</td><td class="price">65 euros</td></tr>
</tbody></table></div>
</details>

<h3>Forfaits LPG, corps et visage</h3>
<p>Forfait de 10 séances plus 2 offertes, Booster ou Optimisation, selon la durée de la séance. La séance de 10 minutes existe uniquement sur le visage.</p>
<details>
<summary>Voir la grille des forfaits</summary>
<div class="table-wrap"><table class="data"><thead><tr><th>Durée de séance</th><th>Forfait Booster ou Optimisation</th></tr></thead><tbody>
<tr><td>10 minutes, visage</td><td class="price">200 euros</td></tr><tr><td>20 minutes</td><td class="price">400 euros</td></tr><tr><td>30 minutes</td><td class="price">600 euros</td></tr><tr><td>40 minutes</td><td class="price">800 euros</td></tr>
</tbody></table></div>
</details>
<p>Le bilan LPG de 40 euros est offert pour tout achat de forfait.</p>

<h2 id="modelage">Modelage</h2>
<p>Modelage visage, buste et épaules (30 minutes) : 39 euros, forfait 5 séances plus une offerte.</p>
<p>Une question sur un tarif ou un forfait ? <a href="contact.html">Contactez-nous</a> ou réservez votre bilan en ligne.</p>
</div></article>
%s</main>
""" % cta('Prête à <span class="accent">réserver</span> ?', "Premier bilan offert pour tout achat. Réservez en ligne ou appelez-nous.")
_laser = tarifs_body.split('<h2 id="laser">',1)[1].split('<h2 ',1)[0]
_px = [int(x) for x in re.findall(r'class="price">\s*(\d+)\s*euros', _laser)]
tarifs_body = tarifs_body.replace('{{LASER_MIN}}', str(min(_px))).replace('{{LASER_MAX}}', str(max(_px)))
tarifs_body = prix_dans_intitules(tarifs_body)  # M4a : « dès X € » dans chaque intitulé d'accordéon
page("tarifs.html",
     "Tarifs épilation laser, soin visage, LPG à Manosque | LUMIA",
     "Tarifs de l'institut LUMIA à Manosque : épilation laser, soins du visage LUMINEA et LED, COSMELAN, LPG. Forfaits dégressifs, paiement en 3 fois sans frais.",
     "https://lumia-salon.fr/tarifs.html", tarifs_body,
     schema_breadcrumb([("Accueil",BASE),("Tarifs",BASE+"tarifs.html")]))

# ============================ CONTACT ============================
contact_schema = ('<script type="application/ld+json">\n'
'{ "@context":"https://schema.org","@type":"BeautySalon","@id":"https://lumia-salon.fr/#institut","name":"LUMIA","url":"https://lumia-salon.fr","sameAs":["https://www.planity.com/lumia-04100-manosque","https://www.instagram.com/lumiamanosque"],"hasMap":"https://www.google.com/maps?cid=2478910083160358823",'
'"telephone":"+33492876372","image":"https://lumia-salon.fr/assets/og-image.jpg",'
'"address":{"@type":"PostalAddress","streetAddress":"10 Bis avenue Jean Giono","addressLocality":"Manosque","postalCode":"04100","addressCountry":"FR"},'
'"geo":{"@type":"GeoCoordinates","latitude":43.8294,"longitude":5.7861},'
'"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"10:00","closes":"19:00"}] }\n</script>\n'
+ schema_breadcrumb([("Accueil",BASE),("Contact",BASE+"contact.html")]))
contact_body = header_block(
  [("Accueil","./"),("Contact",None)],
  "Nous contacter",
  "À Manosque, du lundi au vendredi de 10h à 19h. Réservation en ligne sur Planity.") + """
<main id="main"><section class="section"><div class="container">
<div class="contact-grid">
<div>
<h2>L'institut LUMIA</h2>
<ul class="info-list">
<li><span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span><span><strong>Adresse</strong>10 Bis avenue Jean Giono, 04100 Manosque (à côté de l'opticien ATOL)</span></li>
<li><span class="info-ico">%s</span><span><strong>Téléphone</strong><a href="tel:+33492876372">04 92 87 63 72</a></span></li>
<li><span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span><span><strong>Horaires</strong>Du lundi au vendredi, 10h-19h. Fermé le samedi et le dimanche.</span></li>
<li><span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg></span><span><strong>Paiement</strong>Carte bancaire et espèces. 3 fois sans frais sur les cures.</span></li>
</ul>
<p><strong>Parkings gratuits à proximité</strong> : Dr Joubert (45 min), Monoprix (1h30), La Poste (3h), Souvenir Français (3h).</p>
<p>Pour préparer votre venue, retrouvez le déroulement d'une séance sur la page <a href="epilation-laser-manosque.html">épilation laser à Manosque</a>.</p>
<p><strong>Également à cette adresse</strong> : <a href="https://www.sophiemassagebienetre.com" target="_blank" rel="noopener">Emana by Sophie</a>, massage bien-être, une activité indépendante installée dans nos locaux.</p>
<div class="hero__actions mt-2">
<a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
<a href="https://www.google.com/maps/search/?api=1&amp;query=LUMIA+10+Bis+avenue+Jean+Giono+Manosque" target="_blank" rel="noopener" class="btn btn-outline">Ouvrir dans Google Maps</a>
</div>
</div>
<div>
<h2 id="formulaire">Écrivez-nous</h2>
<p>Une question avant de réserver ? Laissez-nous un message, nous vous répondons rapidement.</p>
<form id="contactForm" class="form" action="php/send.php" method="post">
<p class="form__note">Tous les champs sont obligatoires, sauf le téléphone.</p>
<div class="hp-field" aria-hidden="true"><label>Ne pas remplir<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="form__group"><label class="form__label" for="nom">Nom</label><input class="form__input" type="text" id="nom" name="nom" required minlength="2" autocomplete="name"></div>
<div class="form__row">
<div class="form__group"><label class="form__label" for="email">E-mail</label><input class="form__input" type="email" id="email" name="email" required autocomplete="email"></div>
<div class="form__group"><label class="form__label" for="telephone">Téléphone <span class="form__facultatif">(facultatif)</span></label><input class="form__input" type="tel" id="telephone" name="telephone" autocomplete="tel"></div>
</div>
<div class="form__group"><label class="form__label" for="message">Votre message</label><textarea class="form__textarea" id="message" name="message" required minlength="10"></textarea></div>
<div class="form__group"><label class="form__checkbox"><input type="checkbox" name="rgpd_consent" required> <span>J'accepte que mes informations soient utilisées pour répondre à ma demande, conformément à la <a href="politique-confidentialite.html">politique de confidentialité</a>.</span></label></div>
<button type="submit" class="btn btn-primary">Envoyer le message</button>
<div class="form__message" id="formStatus" role="status" aria-live="polite"></div>
</form>
</div>
</div>
<img src="assets/interieur.webp" alt="Couloir et espace d'attente de l'institut LUMIA à Manosque, arches de pierre et lumière douce" width="1600" height="1066" loading="lazy" style="border-radius:var(--radius);box-shadow:var(--shadow);margin:2.5rem auto 0;">
</div></section></main>
"""  % (PHONE_SVG, PLANITY)
page("contact.html",
     "Contact & accès | LUMIA Manosque",
     "Contacter l'institut LUMIA à Manosque : 10 Bis avenue Jean Giono, 04 92 87 63 72, du lundi au vendredi 10h-19h. Réservation en ligne et formulaire de contact.",
     "https://lumia-salon.fr/contact.html", contact_body, contact_schema)

# ============================ POLITIQUE DE CONFIDENTIALITÉ ============================
pc_body = header_block([("Accueil","./"),("Politique de confidentialité",None)],"Politique de confidentialité","") + """
<main id="main"><article class="article-body"><div class="container">
<h2>Responsable du traitement</h2>
<p>Le responsable du traitement des données collectées sur ce site est la société NOVASIF, enseigne LUMIA, 10 Bis avenue Jean Giono, 04100 Manosque, joignable à l’adresse <a href="mailto:lumia.manosque@gmail.com">lumia.manosque@gmail.com</a>.</p>
<h2>Données collectées et finalité</h2>
<p>Le formulaire de contact collecte votre nom, votre adresse e-mail, votre numéro de téléphone (facultatif) et votre message. Ces données servent uniquement à répondre à votre demande. Dès l'envoi, un message automatique vous confirme la bonne réception de votre demande, à l'adresse e-mail que vous avez indiquée. Aucune donnée n'est cédée ni revendue, et aucune n'est utilisée pour de la prospection.</p>
<h2>Base légale</h2>
<p>Le traitement repose sur votre consentement (article 6.1.a du RGPD), recueilli via la case à cocher du formulaire. Vous pouvez le retirer à tout moment en nous écrivant.</p>
<h2>Destinataires</h2>
<p>Vos données sont destinées à l'institut LUMIA seul. Pour fonctionner, le site s'appuie sur deux prestataires techniques, qui agissent pour notre compte :</p>
<ul>
<li><strong>OVH SAS</strong> (Roubaix, France), qui héberge le site et achemine les e-mails du formulaire ;</li>
<li><strong>Google</strong> (service Gmail), où l'institut reçoit ses e-mails. Google peut traiter des données hors de l'Union européenne, dans le cadre des garanties prévues par le RGPD (décision d'adéquation EU-US Data Privacy Framework).</li>
</ul>
<h2>Durée de conservation</h2>
<p>Les messages reçus sont conservés trois ans à compter de notre dernier échange, puis supprimés.</p>
<p>Pour limiter les envois abusifs, le site garde une empreinte de votre adresse IP pendant une heure, le temps de ce contrôle, puis l'efface automatiquement.</p>
<p>Comme tout hébergeur, OVH enregistre des journaux techniques de connexion (adresse IP, date, page demandée), qu'il conserve pour la sécurité du service et selon ses propres obligations légales.</p>
<h2>Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité sur vos données. Pour les exercer, écrivez-nous à <a href="mailto:lumia.manosque@gmail.com">lumia.manosque@gmail.com</a> ou par courrier à l'adresse de l'institut. Nous vous répondons dans un délai d'un mois au plus. Vous pouvez également introduire une réclamation auprès de la CNIL (www.cnil.fr).</p>
<h2>Cookies et traceurs</h2>
<p>Ce site n'utilise ni cookie publicitaire, ni outil de mesure d'audience, ni traceur tiers. Il dépose seulement deux éléments techniques, dispensés de consentement par la CNIL car indispensables au service que vous demandez :</p>
<ul>
<li>sur la page contact, un <strong>cookie de sécurité</strong> (csrf_token) qui protège le formulaire contre les envois frauduleux. Il est effacé à la fermeture de votre navigateur ;</li>
<li>si vous fermez la bannière ou la fenêtre d'annonce, une <strong>mention enregistrée dans votre navigateur</strong> (stockage local) pour ne pas vous la remontrer. Elle ne contient aucune donnée personnelle, et vous pouvez l'effacer depuis les réglages de votre navigateur.</li>
</ul>
<p>La réservation Planity, la page Instagram et la localisation Google Maps sont proposées sous forme de liens externes, sans intégration sur le site. Ces services appliquent leurs propres règles une fois que vous les ouvrez.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par OVH SAS, 2 rue Kellermann, 59100 Roubaix, France. Téléphone : 1007.</p>
<p><em>Dernière mise à jour : novembre 2026.</em></p>
</div></article></main>
"""
page("politique-confidentialite.html","Politique de confidentialité | LUMIA",
     "Politique de confidentialité de l'institut LUMIA à Manosque : données collectées, destinataires, durée de conservation, cookies et droits RGPD.",
     "https://lumia-salon.fr/politique-confidentialite.html", pc_body,
     robots="noindex, follow")

# ============================ 404 ============================
# OVH sert /404.html pour toute URL absente, y compris dans un sous-dossier (/blog/zzz) :
# tout chemin doit donc être absolu depuis la racine (page() reçoit prefix="/").
e404_body = ('<main id="main"><section class="section" style="min-height:50vh;display:flex;align-items:center;text-align:center;">'
'<div class="container">'
'<span class="eyebrow">Erreur 404</span>'
'<h1 style="font-size:clamp(3rem,8vw,5rem);color:var(--accent-deep);">404</h1>'
'<h2 class="section__title-rule">Cette page est introuvable</h2>'
'<p class="lead" style="max-width:560px;margin:1rem auto 2rem;">Cette page n\'existe pas ou a changé d\'adresse. Retournez à l\'accueil, découvrez nos prestations ou réservez directement.</p>'
'<div class="cta-actions" style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">'
'<a href="/" class="btn btn-primary">Retour à l\'accueil</a>'
'<a href="/#prestations" class="btn btn-outline">Voir les prestations</a>'
'<a href="%s" target="_blank" rel="noopener" class="btn btn-outline">Prendre rendez-vous</a></div>'
'</div></section></main>\n' % PLANITY)
page("404.html","Page introuvable | LUMIA",
     "La page demandée est introuvable. Retournez à l'accueil de l'institut LUMIA à Manosque.",
     "https://lumia-salon.fr/404.html", e404_body,
     robots="noindex, follow", prefix="/")

print("pages2 OK")
