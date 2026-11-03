#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère à-propos, tarifs, contact, politique de confidentialité, 404."""
from build_pages import *

# ============================ À PROPOS ============================
apropos_schema = ('<script type="application/ld+json">\n'
'{ "@context":"https://schema.org","@type":"Person","name":"Margaux",'
'"jobTitle":"Infirmière diplômée d\'État, praticienne en épilation laser",'
'"worksFor":{"@type":"BeautySalon","name":"LUMIA","url":"https://lumia-salon.fr"},'
'"url":"https://lumia-salon.fr/a-propos.html" }\n</script>\n'
'<script type="application/ld+json">\n'
'{ "@context":"https://schema.org","@type":"BeautySalon","name":"LUMIA","url":"https://lumia-salon.fr",'
'"telephone":"+33492876372","address":{"@type":"PostalAddress","streetAddress":"10 Bis avenue Jean Giono","addressLocality":"Manosque","postalCode":"04100","addressCountry":"FR"},'
'"founder":{"@type":"Person","name":"Margaux","jobTitle":"Infirmière diplômée d\'État, praticienne en épilation laser"} }\n</script>\n'
+ schema_breadcrumb([("Accueil",BASE),("À propos",BASE+"a-propos.html")]))
apropos_body = header_block(
  [("Accueil","./"),("À propos",None)],
  "LUMIA, votre institut à Manosque",
  "Une infirmière diplômée d'État qui apporte la rigueur du soin à l'esthétique.") + """
<main id="main"><article class="article-body"><div class="container">
<p>LUMIA est l'institut de Margaux, infirmière diplômée d'État, à Manosque. Après plusieurs années au service des patients, elle a choisi de mettre la précision et l'écoute du soin infirmier au service de la beauté : épilation laser, soins du visage, LPG et soins dépigmentants. L'institut a ouvert à l'automne 2024 et s'est construit autour d'une idée simple, vous accompagner sur-mesure, avec la même interlocutrice à chaque rendez-vous.</p>

<img src="assets/margaux.jpg" class="portrait" alt="Margaux, infirmière diplômée d'État et fondatrice de l'institut LUMIA à Manosque" width="900" height="900" loading="lazy">

<h2>Le fil conducteur : du soin à l'esthétique</h2>
<p>Margaux est infirmière diplômée d'État (2015-2018). Elle s'est ensuite formée à l'épilation laser (Formation Socle LASER, 2024), aux soins du visage EsthéSkin et Corpoderm (2025), puis au protocole COSMELAN de Mesoestetic (2025). Cette formation continue se retrouve dans sa façon de travailler : questionnaire de santé, consentement éclairé, fiche de suivi. C'est la rigueur du soin appliquée à votre beauté, et c'est le cœur de la confiance que vous accordent ses clientes et clients.</p>

<h2>L'institut</h2>
<p>L'institut se trouve au 10 Bis avenue Jean Giono, à côté de l'opticien ATOL, dans un cadre cocon aux arches de pierre et aux matières chaleureuses. On y travaille avec des marques exigeantes, Mesoestetic et les nutricosmétiques D-LAB, et un matériel professionnel : un laser diode Leaseir, la machine EsthéSkin pour les soins du visage et la LPG Cellu M6 Alliance. Un soin du visage PEELING de Mesoestetic est à venir.</p>

<img src="assets/acceuil.webp" class="landscape" alt="L'accueil de l'institut LUMIA à Manosque, mur en arche et comptoir en bois" width="1360" height="907" loading="lazy">

<h2>Des qualifications datées et vérifiables</h2>
<p>La transparence fait partie du soin. Voici les repères de formation de la praticienne.</p>
<ul>
<li>2015 à 2018 : diplôme d'État d'infirmière.</li>
<li>2024 : Formation Socle LASER (épilation laser à visée non thérapeutique).</li>
<li>2025 : formation soins du visage EsthéSkin (Corpoderm).</li>
<li>2025 : formation au protocole COSMELAN de Mesoestetic.</li>
</ul>
<p>L'attestation de formation à l'épilation laser est affichée à l'institut. Découvrez nos prestations : <a href="epilation-laser-manosque.html">épilation laser</a>, <a href="soins-visage-manosque.html">soins du visage</a>, <a href="lpg-cellu-m6-manosque.html">LPG</a> et <a href="soin-cosmelan-taches-manosque.html">Cosmelan</a>.</p>
</div></article>
%s</main>
""" % cta('Faisons <span class="accent">connaissance</span>', "Le premier échange est gratuit. Réservez votre bilan à l'institut LUMIA à Manosque.")
page("a-propos.html",
     "La praticienne | Infirmière D.E. & épilation laser à Manosque | LUMIA",
     "Margaux, infirmière diplômée d'État, vous accueille à l'institut LUMIA de Manosque : épilation laser, soins du visage, LPG, Cosmelan. Parcours et qualifications.",
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
<p>Voici les tarifs de l'institut LUMIA à Manosque, à la séance et en forfait. Les prix indiqués sont donnés à titre indicatif et peuvent évoluer ; ils sont confirmés lors du bilan. Le paiement en 3 fois sans frais est possible sur les cures. Pour l'épilation laser, un bilan personnalisé est obligatoire avant la première séance : il coûte 20 euros et il est offert pour tout achat de séance ou de cure.</p>

<div class="callout"><h3>Bon à savoir</h3><p>Carte bancaire et espèces acceptées. Le bilan laser (20 euros) et le bilan LPG (40 euros) sont offerts pour tout achat de séance, de cure ou de forfait. Le diagnostic de peau Cosmelan (20 euros) est déductible du soin en cabine.</p></div>

<h2>Épilation laser</h2>
<p>Tarifs à la séance. Un bilan personnalisé est obligatoire avant la première séance.</p>

<h3>Femme</h3>
<div class="table-wrap"><table class="data"><thead><tr><th>Zone</th><th>Tarif à la séance</th></tr></thead><tbody>
<tr><td>Inter-sourcils</td><td class="price">31 euros</td></tr><tr><td>Lèvre supérieure</td><td class="price">39 euros</td></tr><tr><td>Menton</td><td class="price">37 euros</td></tr><tr><td>Tempes ou joues</td><td class="price">55 euros</td></tr><tr><td>Aisselles</td><td class="price">54 euros</td></tr><tr><td>Aréoles des seins</td><td class="price">47 euros</td></tr><tr><td>Bas du ventre</td><td class="price">51 euros</td></tr><tr><td>Bas du dos</td><td class="price">61 euros</td></tr><tr><td>Sillon inter-fessier</td><td class="price">44 euros</td></tr><tr><td>Maillot simple</td><td class="price">65 euros</td></tr><tr><td>Maillot échancré</td><td class="price">100 euros</td></tr><tr><td>Maillot intégral</td><td class="price">133 euros</td></tr><tr><td>Avant-bras</td><td class="price">99 euros</td></tr><tr><td>Cuisses</td><td class="price">202 euros</td></tr><tr><td>Demi-jambes</td><td class="price">153 euros</td></tr><tr><td>Jambes entières</td><td class="price">274 euros</td></tr>
</tbody></table></div>

<h3>Homme</h3>
<div class="table-wrap"><table class="data"><thead><tr><th>Zone</th><th>Tarif à la séance</th></tr></thead><tbody>
<tr><td>Inter-sourcils</td><td class="price">31 euros</td></tr><tr><td>Oreilles</td><td class="price">39 euros</td></tr><tr><td>Col de chemise</td><td class="price">58 euros</td></tr><tr><td>Barbe</td><td class="price">110 euros</td></tr><tr><td>Aisselles</td><td class="price">63 euros</td></tr><tr><td>Épaules</td><td class="price">103 euros</td></tr><tr><td>Avant-bras</td><td class="price">106 euros</td></tr><tr><td>Bras complets</td><td class="price">159 euros</td></tr><tr><td>Torse</td><td class="price">121 euros</td></tr><tr><td>Ventre</td><td class="price">121 euros</td></tr><tr><td>Fesses</td><td class="price">121 euros</td></tr><tr><td>Dos</td><td class="price">223 euros</td></tr><tr><td>Cuisses</td><td class="price">202 euros</td></tr><tr><td>Demi-jambes</td><td class="price">206 euros</td></tr><tr><td>Jambes entières</td><td class="price">303 euros</td></tr>
</tbody></table></div>

<p>Des cures existent sur la plupart des zones, à des tarifs avantageux par rapport aux séances à l'unité et réglables en 3 fois sans frais. Le montant vous est communiqué lors du bilan, en fonction de votre peau et du nombre de séances nécessaires.</p>
<p class="lead">Bilan / diagnostic laser : 20 euros, offert pour tout achat de séance ou de cure.</p>

<h2>Soins du visage LUMINEA (EsthéSkin)</h2>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>LUMINEA Express nettoyage</td><td>30 min</td><td class="price">45 euros</td></tr><tr><td>LUMINEA Express radiofréquence (visage ou cou)</td><td>30 min</td><td class="price">49 euros</td></tr><tr><td>LUMINEA Découverte</td><td>1h15</td><td class="price">95 euros</td></tr><tr><td>LUMINEA Avancé</td><td>1h15</td><td class="price">115 euros</td></tr><tr><td>LUMINEA Prestige + LPG visage</td><td>1h30</td><td class="price">135 euros</td></tr><tr><td>LUMINEA Prestige + LED</td><td>1h30</td><td class="price">135 euros</td></tr>
</tbody></table></div>

<h2>Soins du visage avec LED</h2>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Détail</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Soin anti-âge + LED</td><td>1h</td><td class="price">95 euros</td></tr><tr><td>Nettoyage &amp; hydratation + LED</td><td>60 min (cure 10+2 offertes)</td><td class="price">80 euros</td></tr><tr><td>Séance LED visage</td><td>30 min</td><td class="price">35 euros</td></tr><tr><td>Cure LED visage 10+2</td><td>12 séances</td><td class="price">350 euros</td></tr>
</tbody></table></div>

<h2>Micro-stimulation, microneedling Mesoestetic</h2>
<p>Stimulation de la peau par micro-perforations contrôlées, avec des actifs Mesoestetic aux exosomes. Sans injection de produit. La LED est incluse lors de la pose du masque.</p>
<div class="table-wrap"><table class="data"><thead><tr><th>Prestation</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>RDV diagnostic visage</td><td>30 min</td><td class="price">20 euros</td></tr><tr><td>Microneedling visage et cou</td><td>60 min</td><td class="price">145 euros</td></tr>
</tbody></table></div>
<p>Recommandé en cure, une séance tous les quinze jours pendant six séances, puis un entretien tous les deux mois.</p>

<h2>Cure Expertise Silhouette</h2>
<p>Cure de six séances associant 45 minutes de drainage lymphatique et 30 minutes de LPG, soit une séance complète d'1h15, avec un bilan de 20 minutes avant la cure. Disponible pour le bas du corps ou pour le ventre et la taille. Cure réalisée avec Emana Massages.</p>
<div class="table-wrap"><table class="data"><thead><tr><th>Prestation</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Première séance : drainage lymphatique 45 min et LPG 30 min</td><td>1h15</td><td class="price">120 euros</td></tr>
</tbody></table></div>
<p class="lead">120 euros d'économies pour l'achat de la cure, jusqu'au 31 décembre 2026.</p>

<h2>Soins dépigmentants Cosmelan</h2>
<div class="table-wrap"><table class="data"><thead><tr><th>Prestation</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Diagnostic de peau</td><td>RDV préalable</td><td class="price">20 euros (déductible)</td></tr><tr><td>Soin cabine (diagnostic + home pack)</td><td>45 min</td><td class="price">650 euros</td></tr><tr><td>Soin apaisant post-Cosmelan</td><td>45 min</td><td class="price">50 euros</td></tr>
</tbody></table></div>

<h2>LPG Cellu M6, corps</h2>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Bilan personnalisé</td><td>30 min</td><td class="price">40 euros (offert pour un forfait)</td></tr><tr><td>Anti-cellulite</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Jeune maman</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Relaxation</td><td>30 min</td><td class="price">60 euros</td></tr><tr><td>Détox drainant</td><td>40 min</td><td class="price">70 euros</td></tr><tr><td>Tenue Endermowear</td><td>obligatoire pour le corps</td><td class="price">20 euros (offerte pour tout achat de soin corps)</td></tr>
</tbody></table></div>

<h2>LPG Cellu M6, visage</h2>
<p>Soins zones, de 1 à 9 zones au choix (front, regard anti-rides, poches et cernes, bouche, double menton, ovale, cou, décolleté, mains), facturés selon la durée.</p>
<div class="table-wrap"><table class="data"><thead><tr><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>10 minutes</td><td class="price">20 euros</td></tr>
<tr><td>20 minutes</td><td class="price">40 euros</td></tr>
<tr><td>30 minutes</td><td class="price">60 euros</td></tr>
<tr><td>40 minutes</td><td class="price">80 euros</td></tr>
</tbody></table></div>

<h3>Soins classiques visage</h3>
<div class="table-wrap"><table class="data"><thead><tr><th>Soin</th><th>Durée</th><th>Tarif</th></tr></thead><tbody>
<tr><td>Éclat</td><td>15 min</td><td class="price">35 euros</td></tr><tr><td>Détox</td><td>sur mesure</td><td class="price">45 euros</td></tr><tr><td>Anti-âge repulpant</td><td>sur mesure</td><td class="price">65 euros</td></tr><tr><td>Anti-âge fermeté</td><td>sur mesure</td><td class="price">65 euros</td></tr><tr><td>Anti-âge affinant</td><td>sur mesure</td><td class="price">65 euros</td></tr>
</tbody></table></div>

<h3>Forfaits LPG, corps et visage</h3>
<p>Forfaits Booster et Optimisation, au même tarif, selon la durée de la séance.</p>
<div class="table-wrap"><table class="data"><thead><tr><th>Durée de séance</th><th>Forfait Booster</th><th>Forfait Optimisation</th></tr></thead><tbody>
<tr><td>10 minutes</td><td class="price">200 euros</td><td class="price">sur devis</td></tr><tr><td>20 minutes</td><td class="price">400 euros</td><td class="price">400 euros</td></tr><tr><td>30 minutes</td><td class="price">600 euros</td><td class="price">600 euros</td></tr><tr><td>40 minutes</td><td class="price">800 euros</td><td class="price">800 euros</td></tr>
</tbody></table></div>
<p>Le bilan LPG de 40 euros est offert pour tout achat de forfait.</p>

<h2>Modelage</h2>
<p>Modelage visage, buste et épaules (30 minutes) : 39 euros, forfait 5 séances plus une offerte.</p>
<p>Une question sur un tarif ou un forfait ? <a href="contact.html">Contactez-nous</a> ou réservez votre bilan en ligne.</p>
</div></article>
%s</main>
""" % cta('Prête à <span class="accent">réserver</span> ?', "Premier bilan offert pour tout achat. Réservez en ligne ou appelez-nous.")
page("tarifs.html",
     "Tarifs & forfaits | LUMIA Manosque",
     "Tarifs de l'institut LUMIA à Manosque : épilation laser, soins du visage LUMINEA et LED, Cosmelan, LPG. Forfaits dégressifs, paiement en 3 fois sans frais.",
     "https://lumia-salon.fr/tarifs.html", tarifs_body,
     schema_breadcrumb([("Accueil",BASE),("Tarifs",BASE+"tarifs.html")]))

# ============================ CONTACT ============================
contact_schema = ('<script type="application/ld+json">\n'
'{ "@context":"https://schema.org","@type":"BeautySalon","name":"LUMIA","url":"https://lumia-salon.fr",'
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
<div class="hero__actions mt-2">
<a href="%s" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
<a href="https://www.google.com/maps/search/?api=1&amp;query=LUMIA+10+Bis+avenue+Jean+Giono+Manosque" target="_blank" rel="noopener" class="btn btn-outline">Ouvrir dans Google Maps</a>
</div>
</div>
<div>
<h2 id="formulaire">Écrivez-nous</h2>
<p>Une question avant de réserver ? Laissez-nous un message, nous vous répondons rapidement.</p>
<form id="contactForm" class="form" action="php/send.php" method="post">
<div class="hp-field" aria-hidden="true"><label>Ne pas remplir<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<div class="form__group"><label class="form__label" for="nom">Nom</label><input class="form__input" type="text" id="nom" name="nom" required autocomplete="name"></div>
<div class="form__row">
<div class="form__group"><label class="form__label" for="email">Email</label><input class="form__input" type="email" id="email" name="email" required autocomplete="email"></div>
<div class="form__group"><label class="form__label" for="telephone">Téléphone</label><input class="form__input" type="tel" id="telephone" name="telephone" autocomplete="tel"></div>
</div>
<div class="form__group"><label class="form__label" for="message">Votre message</label><textarea class="form__textarea" id="message" name="message" required></textarea></div>
<div class="form__group"><label class="form__checkbox"><input type="checkbox" name="rgpd_consent" required> J'accepte que mes informations soient utilisées pour répondre à ma demande, conformément à la <a href="politique-confidentialite.html">politique de confidentialité</a>.</label></div>
<button type="submit" class="btn btn-primary">Envoyer le message</button>
<div class="form__message" id="formStatus" role="status" aria-live="polite"></div>
</form>
</div>
</div>
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
<p>Le responsable du traitement des données collectées sur ce site est l'institut LUMIA, 10 Bis avenue Jean Giono, 04100 Manosque 〔coordonnées de l'éditeur à compléter〕.</p>
<h2>Données collectées et finalité</h2>
<p>Le formulaire de contact collecte votre nom, votre adresse e-mail, votre numéro de téléphone (facultatif) et votre message. Ces données sont utilisées uniquement pour répondre à votre demande. Aucune donnée n'est cédée ni revendue à des tiers.</p>
<h2>Base légale</h2>
<p>Le traitement repose sur votre consentement (article 6.1.a du RGPD), recueilli via la case à cocher du formulaire.</p>
<h2>Durée de conservation</h2>
<p>Les messages sont conservés le temps nécessaire au traitement de votre demande, puis archivés ou supprimés conformément aux durées légales.</p>
<h2>Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et d'opposition sur vos données. Pour les exercer, écrivez-nous à 〔email professionnel à fournir〕 ou par courrier à l'adresse de l'institut. Vous pouvez également introduire une réclamation auprès de la CNIL (www.cnil.fr).</p>
<h2>Cookies</h2>
<p>Ce site n'utilise aucun cookie publicitaire ni aucun traceur tiers. La réservation Planity et la localisation Google Maps sont proposées sous forme de liens externes, sans intégration sur le site.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par O2switch, 222-224 boulevard Gustave Flaubert, 63000 Clermont-Ferrand, France.</p>
</div></article></main>
"""
page("politique-confidentialite.html","Politique de confidentialité | LUMIA",
     "Politique de confidentialité de l'institut LUMIA à Manosque : données collectées, finalité, base légale, droits RGPD.",
     "https://lumia-salon.fr/politique-confidentialite.html", pc_body,
     schema_breadcrumb([("Accueil",BASE),("Politique de confidentialité",BASE+"politique-confidentialite.html")]),
     robots="noindex, follow")

# ============================ 404 ============================
e404_body = ('<main id="main"><section class="section" style="min-height:50vh;display:flex;align-items:center;text-align:center;">'
'<div class="container">'
'<span class="eyebrow">Erreur 404</span>'
'<h1 style="font-size:clamp(3rem,8vw,5rem);color:var(--accent-deep);">404</h1>'
'<h2 class="section__title-rule">Cette page est introuvable</h2>'
'<p class="lead" style="max-width:560px;margin:1rem auto 2rem;">La page que vous cherchez n\'existe pas ou a été déplacée. Revenez à l\'accueil ou prenez rendez-vous.</p>'
'<div class="cta-actions" style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">'
'<a href="./" class="btn btn-primary">Retour à l\'accueil</a>'
'<a href="contact.html" class="btn btn-outline">Nous contacter</a></div>'
'</div></section></main>\n')
page("404.html","Page introuvable | LUMIA",
     "La page demandée est introuvable. Retournez à l'accueil de l'institut LUMIA à Manosque.",
     "https://lumia-salon.fr/404.html", e404_body,
     robots="noindex, follow")

print("pages2 OK")
