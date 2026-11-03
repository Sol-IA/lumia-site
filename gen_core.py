#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages coeur du site : accueil, épilation laser, soins du visage,
mentions légales et réservation.

Ces cinq pages étaient maintenues à la main, ce qui faisait que toute évolution
de l'en-tête ou du pied de page ne les atteignait pas. Elles passent ici par les
mêmes helpers que le reste du site, pour que le menu et le pied restent cohérents
partout. Seul le corps de chaque page est spécifique.
"""
from build_pages import *

# ============================ INDEX.HTML ============================
index_body = r'''

<main id="main">

<!-- HERO -->
<section class="hero">
  <div class="container">
    <div class="hero__inner">
      <div class="hero__content">
        <span class="eyebrow">La science de la beauté</span>
        <h1>Institut de beauté &amp; <span class="accent">épilation LASER</span> à Manosque</h1>
        <p class="hero__lead">Épilation laser définitive et soins du visage, réalisés par une infirmière diplômée d'État, dans un cocon au centre de Manosque. Premier bilan personnalisé offert.</p>
        <div class="hero__actions">
          <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
          <a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA au 04 92 87 63 72">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.81.36 1.6.7 2.34a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.74-1.27a2 2 0 0 1 2.11-.45c.74.34 1.53.57 2.34.7A2 2 0 0 1 22 16.92z"/></svg>
            04 92 87 63 72
          </a>
        </div>
      </div>
      <div class="hero__media">
        <img src="assets/soinvisage.webp" alt="Soin du visage à l'institut LUMIA à Manosque" width="470" height="1020" loading="eager">
      </div>
    </div>
  </div>
</section>

<!-- BANDEAU CONFIANCE -->
<section class="trust-bar" aria-label="Nos engagements">
  <div class="container">
    <div class="trust-item">
      <div class="trust-item__value">Infirmière D.E.</div>
      <div class="trust-item__label">Praticienne diplômée d'État</div>
    </div>
    <div class="trust-item">
      <div class="trust-item__value">Laser diode</div>
      <div class="trust-item__label">Adapté à de nombreux phototypes</div>
    </div>
    <div class="trust-item">
      <div class="trust-item__value">Bilan offert</div>
      <div class="trust-item__label">Pour tout achat de séance ou de cure</div>
    </div>
    <div class="trust-item">
      <div class="trust-item__value">5,0 / 5</div>
      <div class="trust-item__label">32 avis sur Planity</div>
    </div>
  </div>
</section>

<!-- PRESTATIONS -->
<section class="section" id="prestations">
  <div class="container">
    <div class="section__header">
      <span class="eyebrow">Nos prestations</span>
      <h2 class="section__title-rule">Un institut complet, à Manosque</h2>
      <p>Du laser au soin du visage, en passant par la silhouette et le teint, chaque protocole est choisi et réalisé par la même infirmière. Voici nos cinq univers de soin.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="service-card__img"><img src="assets/laserhomme.webp" alt="Épilation laser du torse chez un homme à l'institut LUMIA" width="1360" height="907" loading="lazy"></div>
        <div class="service-card__body">
          <h3>Épilation LASER CE Médical</h3>
          <p>En finir avec le rasage et la cire. Laser diode adapté à de nombreux types de peau, sur le visage et le corps, pour les femmes comme pour les hommes.</p>
          <span class="service-card__cta">Découvrir</span>
        </div>
        <a href="epilation-laser-manosque.html" class="service-card__link" aria-label="Épilation laser définitive à Manosque"></a>
      </article>
      <article class="service-card">
        <div class="service-card__img"><img src="assets/cabinedesoin.webp" alt="Cabine de soin du visage et luminothérapie LED à l'institut LUMIA" width="765" height="1020" loading="lazy"></div>
        <div class="service-card__body">
          <h3>Soins du visage</h3>
          <p>Soins LUMINEA réalisés avec la machine EsthéSkin et luminothérapie LED, pour nettoyer, hydrater, raffermir et redonner de l'éclat à la peau.</p>
          <span class="service-card__cta">Découvrir</span>
        </div>
        <a href="soins-visage-manosque.html" class="service-card__link" aria-label="Soins du visage à Manosque"></a>
      </article>
      <article class="service-card">
        <div class="service-card__img"><img src="assets/soinLPG.webp" alt="Soin LPG endermologie des jambes à l'institut LUMIA" width="765" height="1020" loading="lazy"></div>
        <div class="service-card__body">
          <h3>LPG endermologie</h3>
          <p>Cellu M6 Alliance pour la minceur, la fermeté et le drainage. Corps et visage, avec un suivi photo de votre progression.</p>
          <span class="service-card__cta">Découvrir</span>
        </div>
        <a href="lpg-cellu-m6-manosque.html" class="service-card__link" aria-label="LPG Cellu M6 à Manosque"></a>
      </article>
      <article class="service-card">
        <div class="service-card__img"><img src="assets/microneedling.webp" alt="Stylo de microneedling utilisé pour la micro-stimulation du visage à l'institut LUMIA à Manosque" width="904" height="1600" loading="lazy"></div>
        <div class="service-card__body">
          <h3>Microneedling</h3>
          <p>Micro-stimulation de la peau avec les actifs MESOESTETIC aux exosomes : rides, éclat, pores dilatés et cicatrices d'acné. Sans injection.</p>
          <span class="service-card__cta">Découvrir</span>
        </div>
        <a href="microneedling-manosque.html" class="service-card__link" aria-label="Microneedling à Manosque"></a>
      </article>
      <article class="service-card">
        <div class="service-card__img"><img src="assets/produits2.webp" alt="Cosmétiques et nutricosmétiques Mesoestetic à l'institut LUMIA" width="765" height="1020" loading="lazy"></div>
        <div class="service-card__body">
          <h3>Soins dépigmentants COSMELAN</h3>
          <p>Protocole COSMELAN de Mesoestetic pour atténuer les taches du visage : mélasma, taches solaires, hyperpigmentation.</p>
          <span class="service-card__cta">Découvrir</span>
        </div>
        <a href="soin-cosmelan-taches-manosque.html" class="service-card__link" aria-label="Soins dépigmentants COSMELAN à Manosque"></a>
      </article>
    </div>
  </div>
</section>

<!-- POURQUOI LUMIA -->
<section class="section section--alt">
  <div class="container">
    <div class="section__header">
      <span class="eyebrow">Pourquoi LUMIA</span>
      <h2 class="section__title-rule">La rigueur du soin, l'attention d'un institut</h2>
    </div>
    <div class="feature-grid">
      <div class="feature">
        <div class="feature__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.4 4.9 5.4.8-3.9 3.8.9 5.4L12 14.8 7.2 17l.9-5.4L4.2 7.7l5.4-.8z"/></svg></div>
        <h3>Une expertise d'infirmière</h3>
        <p>Margaux est infirmière diplômée d'État. Questionnaire de santé, consentement éclairé, fiche de suivi : la rigueur du soin appliquée à l'esthétique.</p>
      </div>
      <div class="feature">
        <div class="feature__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg></div>
        <h3>Un institut complet</h3>
        <p>Épilation laser, visage, silhouette, teint, cosmétiques : un seul lieu pour prendre soin de vous, sans courir d'un prestataire à l'autre.</p>
      </div>
      <div class="feature">
        <div class="feature__icon"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
        <h3>Un accompagnement personnalisé</h3>
        <p>La même interlocutrice à chaque séance, un protocole défini ensemble lors du bilan, et un suivi dans le temps. Tout l'inverse d'une chaîne.</p>
      </div>
    </div>
  </div>
</section>

<!-- LA PRATICIENNE -->
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media">
        <img src="assets/margaux.jpg" alt="Margaux, infirmière D.E. et fondatrice de l'institut LUMIA à Manosque" width="820" height="820" loading="lazy">
      </div>
      <div class="split__content">
        <span class="eyebrow">La praticienne</span>
        <h2 class="section__title-rule">Margaux, infirmière D.E.</h2>
        <p>Après plusieurs années comme infirmière diplômée d'État, Margaux s'est formée à l'épilation laser, aux soins du visage EsthéSkin et au protocole COSMELAN de Mesoestetic pour ouvrir LUMIA. Son approche : la précision et l'écoute du soin infirmier, au service de votre beauté.</p>
        <p>Concrètement, chaque parcours commence par un bilan : on examine votre peau, on répond à vos questions, on définit ensemble un protocole adapté. Puis on avance à votre rythme, séance après séance.</p>
        <p><a href="a-propos.html" class="btn btn-outline">En savoir plus sur LUMIA</a></p>
      </div>
    </div>
  </div>
</section>

<!-- AVIS -->
<section class="section section--alt">
  <div class="container">
    <div class="section__header">
      <span class="eyebrow">Vos avis</span>
      <h2 class="section__title-rule">5,0 / 5 sur Planity, 32 avis</h2>
      <p>La confiance se construit séance après séance. Retrouvez les avis vérifiés de nos clientes et clients sur Planity.</p>
    </div>
    <div class="reviews-grid">
      <div class="review">
        <div class="review__stars" aria-label="5 étoiles sur 5">★★★★★</div>
        <p class="review__text">〔Avis client réel à reprendre depuis Planity ou Google, à valider avec la cliente〕</p>
        <p class="review__author">〔Prénom〕</p>
      </div>
      <div class="review">
        <div class="review__stars" aria-label="5 étoiles sur 5">★★★★★</div>
        <p class="review__text">〔Avis client réel à reprendre depuis Planity ou Google, à valider avec la cliente〕</p>
        <p class="review__author">〔Prénom〕</p>
      </div>
      <div class="review">
        <div class="review__stars" aria-label="5 étoiles sur 5">★★★★★</div>
        <p class="review__text">〔Avis client réel à reprendre depuis Planity ou Google, à valider avec la cliente〕</p>
        <p class="review__author">〔Prénom〕</p>
      </div>
    </div>
    <p class="text-center mt-2"><a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-outline">Voir tous les avis sur Planity</a></p>
  </div>
</section>

<!-- FAQ COURTE -->
<section class="section">
  <div class="container">
    <div class="section__header">
      <span class="eyebrow">Questions fréquentes</span>
      <h2 class="section__title-rule">Ce qu'on nous demande souvent</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Faut-il un bilan avant la première séance d'épilation laser ?</summary>
        <p>Oui. Un bilan personnalisé est obligatoire avant la première séance : examen de la peau et du poil, questionnaire de santé, présentation du protocole. Il coûte 20 € et il est offert pour tout achat de séance ou de cure.</p>
      </details>
      <details>
        <summary>Qui réalise les soins chez LUMIA ?</summary>
        <p>Tous les soins sont réalisés par Margaux, infirmière diplômée d'État formée à l'épilation laser, aux soins du visage EsthéSkin et au protocole COSMELAN. Vous avez la même interlocutrice à chaque séance.</p>
      </details>
      <details>
        <summary>Quels moyens de paiement acceptez-vous ?</summary>
        <p>Nous acceptons la carte bancaire et les espèces. Le paiement en 3 fois sans frais est possible sur les cures.</p>
      </details>
    </div>
    <p class="text-center mt-2"><a href="epilation-laser-manosque.html" class="text-accent"><strong>Tout savoir sur l'épilation laser définitive →</strong></a></p>
  </div>
</section>

<!-- CONTACT / ACCES -->
<section class="section section--alt" id="contact">
  <div class="container">
    <div class="section__header">
      <span class="eyebrow">Nous trouver</span>
      <h2 class="section__title-rule">L'institut LUMIA à Manosque</h2>
    </div>
    <div class="contact-grid">
      <div>
        <ul class="info-list">
          <li>
            <span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
            <span><strong>Adresse</strong>10 Bis avenue Jean Giono, 04100 Manosque (à côté de l'opticien ATOL)</span>
          </li>
          <li>
            <span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.81.36 1.6.7 2.34a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.74-1.27a2 2 0 0 1 2.11-.45c.74.34 1.53.57 2.34.7A2 2 0 0 1 22 16.92z"/></svg></span>
            <span><strong>Téléphone</strong><a href="tel:+33492876372">04 92 87 63 72</a></span>
          </li>
          <li>
            <span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>
            <span><strong>Horaires</strong>Du lundi au vendredi, 10h-19h. Fermé le samedi et le dimanche.</span>
          </li>
          <li>
            <span class="info-ico"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg></span>
            <span><strong>Paiement</strong>Carte bancaire et espèces. Paiement en 3 fois sans frais sur les cures.</span>
          </li>
        </ul>
      </div>
      <div>
        <p><strong>Stationnement</strong> : plusieurs parkings gratuits à proximité immédiate, Dr Joubert (45 min), Monoprix (1h30), La Poste (3h) et Souvenir Français (3h).</p>
        <p>La réservation se fait en ligne sur Planity, ou par téléphone aux horaires d'ouverture.</p>
        <div class="hero__actions mt-2">
          <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
          <a href="https://www.google.com/maps/search/?api=1&amp;query=LUMIA+10+Bis+avenue+Jean+Giono+Manosque" target="_blank" rel="noopener" class="btn btn-outline">Ouvrir dans Google Maps</a>
        </div>
      </div>
    </div>
  </div>
</section>

</main>

<!-- CTA FINAL -->
<section class="cta-section">
  <div class="container">
    <h2>Envie de prendre soin de <span class="accent">vous</span> ?</h2>
    <p>Réservez votre premier rendez-vous à Manosque. Le bilan est offert pour tout achat de séance ou de cure.</p>
    <div class="cta-actions">
      <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
      <a href="tel:+33492876372" class="btn btn-ghost-light">04 92 87 63 72</a>
    </div>
  </div>
</section>

<!-- FOOTER -->
'''
index_head = r'''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BeautySalon",
  "name": "LUMIA",
  "description": "Institut de beauté et centre d'épilation laser à Manosque. Épilation laser définitive par une infirmière D.E., soins du visage, LPG.",
  "url": "https://lumia-salon.fr",
  "telephone": "+33492876372",
  "image": "https://lumia-salon.fr/assets/og-image.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "10 Bis avenue Jean Giono",
    "addressLocality": "Manosque",
    "postalCode": "04100",
    "addressCountry": "FR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 43.8294, "longitude": 5.7861 },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "10:00", "closes": "19:00" }
  ],
  "areaServed": [
    { "@type": "City", "name": "Manosque" },
    { "@type": "City", "name": "Forcalquier" },
    { "@type": "City", "name": "Gréoux-les-Bains" },
    { "@type": "City", "name": "Pierrevert" },
    { "@type": "City", "name": "Oraison" },
    { "@type": "City", "name": "Valensole" }
  ],
  "priceRange": "€€€",
  "currenciesAccepted": "EUR",
  "paymentAccepted": "Cash, Credit Card",
  "founder": {
    "@type": "Person",
    "name": "Margaux",
    "jobTitle": "Infirmière diplômée d'État, praticienne en épilation laser"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "32",
    "bestRating": "5"
  },
  "sameAs": [
    "https://www.planity.com/lumia-04100-manosque",
    "https://www.instagram.com/lumiamanosque"
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Faut-il un bilan avant la première séance d'épilation laser ?",
      "acceptedAnswer": { "@type": "Answer", "text": "Oui. Un bilan personnalisé est obligatoire avant la première séance : examen de la peau et du poil, questionnaire de santé, présentation du protocole. Il coûte 20 € et il est offert pour tout achat de séance ou de cure." }
    },
    {
      "@type": "Question",
      "name": "Qui réalise les soins chez LUMIA ?",
      "acceptedAnswer": { "@type": "Answer", "text": "Tous les soins sont réalisés par Margaux, infirmière diplômée d'État formée à l'épilation laser, aux soins du visage EsthéSkin et au protocole COSMELAN. Vous avez la même interlocutrice à chaque séance." }
    },
    {
      "@type": "Question",
      "name": "Quels moyens de paiement acceptez-vous ?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nous acceptons la carte bancaire et les espèces. Le paiement en 3 fois sans frais est possible sur les cures." }
    }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://lumia-salon.fr/" }
  ]
}
</script>
'''
page("index.html", r"""Institut de beauté &amp; épilation laser à Manosque | LUMIA""", r"""LUMIA, institut de beauté à Manosque. Épilation laser définitive par une infirmière D.E., soins du visage, LPG. Bilan offert. Réservation en ligne.""", "https://lumia-salon.fr/", index_body, schema=index_head)

# ============================ SOINS-VISAGE-MANOSQUE.HTML ============================
soins_visage_manosque_body = r'''

<header class="page-header">
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="./">Accueil</a> <span>›</span> Soins du visage
    </nav>
    <h1>Soins du visage à Manosque</h1>
    <p>Nettoyer, hydrater, raffermir et illuminer la peau, avec la technologie et la rigueur d'une infirmière D.E.</p>
  </div>
</header>

<main id="main">
<article class="article-body">
  <div class="container">

    <p>Les soins du visage de LUMIA à Manosque associent le modelage et des technologies de pointe pour répondre à chaque besoin de peau : manque d'éclat, déshydratation, premiers signes de l'âge, imperfections. Ils sont réalisés par Margaux, infirmière diplômée d'État et esthéticienne, formée aux protocoles EsthéSkin. Chaque soin commence par un diagnostic de peau pour choisir le protocole le plus adapté.</p>

    <div class="hero__actions">
      <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
      <a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA">04 92 87 63 72</a>
    </div>

    <h2>Les soins LUMINEA, la technologie EsthéSkin</h2>
    <p>Les soins LUMINEA réunissent en une séance plusieurs technologies sur une machine EsthéSkin. Selon votre peau, le protocole combine nettoyage profond, hydradermabrasion, ultrasons, radiofréquence, micro-courants, jet peel à la vitamine C, masque et modelage. Le résultat : une peau nettoyée en profondeur, repulpée et lumineuse.</p>

    <img src="assets/cabinedesoin.webp" class="portrait" alt="Cabine de soin du visage de l'institut LUMIA à Manosque, équipée pour la luminothérapie LED" width="765" height="1020" loading="lazy">

    
    <h3>Trois niveaux de soin LUMINEA</h3>
    <p>Pour s'adapter à votre temps et à vos objectifs, le soin existe en trois formules.</p>
    <ul>
      <li><strong>Découverte</strong> (1h15) : un soin complet pour faire connaissance avec votre peau.</li>
      <li><strong>Avancé</strong> (1h15) : un protocole personnalisé selon votre diagnostic.</li>
      <li><strong>Prestige</strong> (1h30) : le soin Avancé enrichi du LPG visage ou de la luminothérapie LED.</li>
    </ul>

    <h2>La luminothérapie LED</h2>
    <p>La LED est une lumière froide qui stimule les cellules de la peau, sans chaleur ni douleur. Cette photobiomodulation soutient la production de collagène, d'acide hyaluronique et d'élastine. Selon la couleur de la lumière, on cible l'éclat, les imperfections, les taches, la fermeté ou l'apaisement des peaux sensibles. La LED se pratique seule ou en complément d'un soin du visage.</p>

    <h2>Contre-indications et préparation</h2>
    <p>Certaines situations nécessitent de reporter ou d'adapter le soin. Elles sont vérifiées lors du diagnostic.</p>
    <div class="callout callout--legal">
      <p><strong>Contre-indications</strong> : grossesse et allaitement, maladie cardiaque (stent, pacemaker), chimiothérapie ou radiothérapie, traitement aux rétinoïdes, injections d'acide hyaluronique ou de botox (attendre 5 semaines), lifting (attendre 3 mois). <strong>Avant le soin</strong> : pas de soleil ni d'UV 48h avant, pas de peeling ni de dermabrasion 15 jours avant, pas de rétinol fortement concentré.</p>
    </div>

    <h2>Questions fréquentes sur les soins du visage</h2>
    <div class="faq">
      <details><summary>À quelle fréquence faire un soin du visage ?</summary><p>Pour entretenir la peau, un soin par mois est un bon rythme. Pour un objectif précis (éclat, anti-âge, peau grasse), on travaille souvent en cure de plusieurs séances rapprochées, puis on espace en entretien.</p></details>
      <details><summary>Voit-on un résultat dès la première séance ?</summary><p>La peau est généralement plus nette, plus lumineuse et plus repulpée dès la première séance. Les effets sur le long terme, comme la fermeté, s'installent au fil des séances.</p></details>
      <details><summary>Les soins conviennent-ils aux peaux sensibles ?</summary><p>Oui, les protocoles sont adaptés à votre type de peau lors du bilan. Certaines technologies sont modulées ou évitées en cas de sensibilité, et la luminothérapie LED est douce et sans chaleur.</p></details>
      <details><summary>Quelle différence avec un soin du visage classique ?</summary><p>Au modelage manuel s'ajoutent des technologies (radiofréquence, micro-courants, ultrasons, LED) qui agissent plus en profondeur sur l'hydratation, la fermeté et l'éclat, avec une infirmière formée à leur usage.</p></details>
      <details><summary>La luminothérapie LED, qu'est-ce que c'est ?</summary><p>C'est une lumière froide qui stimule les cellules de la peau. Selon la couleur, elle cible l'éclat, les imperfections, la fermeté ou l'apaisement, sans douleur ni éviction sociale.</p></details>
    </div>

    <p>Découvrez aussi notre <a href="lpg-cellu-m6-manosque.html">LPG endermologie</a> pour le corps et le visage, nos <a href="soin-cosmelan-taches-manosque.html">soins dépigmentants COSMELAN</a>, et le parcours de <a href="a-propos.html">la praticienne</a>. Les tarifs détaillés sont sur la <a href="tarifs.html">page tarifs</a>.</p>

  </div>
</article>

<section class="cta-section">
  <div class="container">
    <h2>Offrez à votre peau <span class="accent">un vrai moment</span></h2>
    <p>Réservez votre soin du visage à Manosque.</p>
    <div class="cta-actions">
      <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
      <a href="tel:+33492876372" class="btn btn-ghost-light">04 92 87 63 72</a>
    </div>
  </div>
</section>
</main>

'''
soins_visage_manosque_head = r'''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Soin du visage",
  "name": "Soins du visage à Manosque",
  "description": "Soins du visage LUMINEA réalisés avec la technologie EsthéSkin et luminothérapie LED à Manosque, par une infirmière diplômée d'État et esthéticienne. Nettoyage profond, hydratation, anti-âge, éclat.",
  "url": "https://lumia-salon.fr/soins-visage-manosque.html",
  "provider": {
    "@type": "BeautySalon",
    "name": "LUMIA",
    "url": "https://lumia-salon.fr",
    "telephone": "+33492876372",
    "address": { "@type": "PostalAddress", "streetAddress": "10 Bis avenue Jean Giono", "addressLocality": "Manosque", "postalCode": "04100", "addressCountry": "FR" }
  },
  "areaServed": { "@type": "City", "name": "Manosque" }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "À quelle fréquence faire un soin du visage ?", "acceptedAnswer": { "@type": "Answer", "text": "Pour entretenir la peau, un soin par mois est un bon rythme. Pour un objectif précis (éclat, anti-âge, peau grasse), on travaille souvent en cure de plusieurs séances rapprochées, puis on espace en entretien." } },
    { "@type": "Question", "name": "Voit-on un résultat dès la première séance ?", "acceptedAnswer": { "@type": "Answer", "text": "La peau est généralement plus nette, plus lumineuse et plus repulpée dès la première séance. Les effets sur le long terme, comme la fermeté, s'installent au fil des séances." } },
    { "@type": "Question", "name": "Les soins conviennent-ils aux peaux sensibles ?", "acceptedAnswer": { "@type": "Answer", "text": "Oui, les protocoles sont adaptés à votre type de peau lors du bilan. Certaines technologies sont modulées ou évitées en cas de sensibilité, et la luminothérapie LED est douce et sans chaleur." } },
    { "@type": "Question", "name": "Quelle différence avec un soin du visage classique ?", "acceptedAnswer": { "@type": "Answer", "text": "Au modelage manuel s'ajoutent des technologies (radiofréquence, micro-courants, ultrasons, LED) qui agissent plus en profondeur sur l'hydratation, la fermeté et l'éclat, avec une infirmière formée à leur usage." } },
    { "@type": "Question", "name": "La luminothérapie LED, qu'est-ce que c'est ?", "acceptedAnswer": { "@type": "Answer", "text": "C'est une lumière froide qui stimule les cellules de la peau (photobiomodulation). Selon la couleur, elle cible l'éclat, les imperfections, la fermeté ou l'apaisement, sans douleur ni éviction sociale." } }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://lumia-salon.fr/" },
    { "@type": "ListItem", "position": 2, "name": "Soins du visage", "item": "https://lumia-salon.fr/soins-visage-manosque.html" }
  ]
}
</script>
'''
page("soins-visage-manosque.html", r"""Soin du visage à Manosque | LUMIA""", r"""Soins du visage à Manosque : LUMINEA avec la technologie EsthéSkin et luminothérapie LED. Nettoyage, hydratation, anti-âge, éclat. Bilan offert.""", "https://lumia-salon.fr/soins-visage-manosque.html", soins_visage_manosque_body, schema=soins_visage_manosque_head)

# ============================ EPILATION-LASER-MANOSQUE.HTML ============================
epilation_laser_manosque_body = r'''

<!-- PAGE HEADER -->
<header class="page-header">
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="./">Accueil</a> <span>›</span> Épilation laser
    </nav>
    <h1>Épilation laser définitive à Manosque</h1>
    <p>En finir avec le rasage et la cire, en confiance, avec une infirmière diplômée d'État.</p>
  </div>
</header>

<main id="main">
<article class="article-body">
  <div class="container">

    <p>L'épilation laser définitive à Manosque chez LUMIA est réalisée par Margaux, infirmière diplômée d'État formée à l'épilation laser. Elle s'adresse aux femmes comme aux hommes qui veulent en finir durablement avec le rasage et la cire, sur le visage comme sur le corps. Avant la première séance, un bilan personnalisé est offert pour tout achat de séance ou de cure : on examine votre peau et votre poil, on répond à vos questions et on définit ensemble votre protocole.</p>

    <div class="hero__actions">
      <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
      <a href="tel:+33492876372" class="hero__phone" aria-label="Appeler LUMIA au 04 92 87 63 72">04 92 87 63 72</a>
    </div>

    <h2>Comment fonctionne l'épilation laser ?</h2>
    <p>Le laser cible la mélanine, le pigment qui colore le poil, pour chauffer puis neutraliser le follicule : c'est le principe de la photothermolyse sélective. Plus le poil est foncé et la peau claire, plus le contraste est marqué et plus le traitement est efficace. Comme seul le poil en phase de croissance réagit, plusieurs séances espacées sont nécessaires pour traiter l'ensemble de la pilosité.</p>

    <div class="callout">
      <h3>Le bilan, étape obligatoire avant la première séance</h3>
      <p>Chez LUMIA, aucune séance n'est réalisée sans un bilan préalable. Ce rendez-vous comprend un questionnaire de santé, la remise d'une fiche d'information et de consentement, la présentation du laser et un <strong>flash test</strong>. Il coûte <strong>20 €</strong> et il est <strong>offert pour tout achat de séance ou de cure</strong>. C'est le moment où l'on valide votre éligibilité à l'épilation LASER, où l'on vérifie que votre peau et votre poil sont adaptés, et où l'on construit votre protocole.</p>
      <p>À l'issue du diagnostic, une <strong>cure</strong> peut vous être proposée selon les zones à traiter et le nombre de séances estimé. Elle donne accès à des <strong>tarifs avantageux</strong> par rapport aux séances à l'unité, et elle est réglable en <strong>3 fois sans frais</strong>.</p>
    </div>

    <img src="assets/laserhomme.webp" class="landscape" alt="Séance d'épilation laser à l'institut LUMIA à Manosque, le laser convient aussi aux hommes" width="1360" height="907" loading="lazy">

    <p class="text-center mt-2"><a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Premier échange gratuit, réservez votre bilan</a></p>

    <h2>Quelles zones peut-on traiter ?</h2>
    <p>Presque toutes les zones du visage et du corps peuvent être traitées, chez les femmes comme chez les hommes. Voici les zones les plus demandées à l'institut.</p>
    <div class="table-wrap">
      <table class="data">
        <thead>
          <tr><th>Visage</th><th>Corps</th></tr>
        </thead>
        <tbody>
          <tr><td>Lèvre supérieure, menton</td><td>Aisselles</td></tr>
          <tr><td>Joues, tempes, inter-sourcils</td><td>Maillot (simple, échancré, intégral)</td></tr>
          <tr><td>Cou</td><td>Jambes (demi ou entières)</td></tr>
          <tr><td>Barbe et oreilles (hommes)</td><td>Dos, torse, épaules (hommes)</td></tr>
        </tbody>
      </table>
    </div>
    <p>Vous retrouvez le détail des tarifs par zone sur notre <a href="tarifs.html">page tarifs</a>. Pour les zones non listées, le bilan précise le protocole et le prix.</p>

    <h2>Combien de séances faut-il ?</h2>
    <p>En moyenne, comptez 8 à 12 séances pour un résultat durable. Le nombre exact dépend de la zone, de la densité et de la couleur du poil, et de votre type de peau. Les zones influencées par les hormones, comme le menton ou le maillot, peuvent en demander davantage. Le bilan permet d'estimer votre protocole, qui reste ajusté séance après séance.</p>

    <h2>Est-ce que c'est douloureux ?</h2>
    <p>La sensation ressemble à de petits picotements de chaleur, parfois comparés à un léger claquement d'élastique. Le système de refroidissement intégré au laser apaise la peau pendant la séance et la rend bien supportable.</p>

    <h2>Le déroulement d'une séance chez LUMIA</h2>
    <p>Tout commence par le bilan obligatoire décrit plus haut. Une fois le protocole défini, chaque séance suit le même cadre rassurant.</p>
    <ul>
      <li>Port des lunettes de protection oculaire pendant toute la durée de la séance.</li>
      <li>Rasage préalable de la zone (la veille ou sur place) pour que le laser agisse sur la racine.</li>
      <li>Passage du laser, avec refroidissement, de 10 minutes à 1h30 selon la zone.</li>
      <li>Conseils d'après-séance et planification de la séance suivante.</li>
    </ul>

    <h2>Le laser convient-il à tous les types de peau ?</h2>
    <p>Le laser diode utilisé à l'institut est adapté à de nombreux phototypes. Quelques règles s'appliquent toutefois : une peau récemment bronzée nécessite de reporter la séance, et les poils blancs, blonds, roux ainsi que le duvet ne contiennent pas assez de mélanine pour réagir. Le bilan vérifie l'adéquation entre votre pilosité, votre peau et le traitement.</p>

    <h2>Avant et après la séance</h2>
    <p>Quelques précautions simples garantissent l'efficacité et la sécurité du traitement.</p>
    <ul>
      <li>Ne pas s'exposer au soleil, aux UV ni à l'autobronzant <strong>10 jours avant et 10 jours après</strong> la séance.</li>
      <li>Pas de prise de médicament photosensibilisant <strong>7 jours avant et 7 jours après</strong> la séance.</li>
      <li>Pas de déodorant sur les aisselles <strong>le jour de la séance</strong>.</li>
      <li>Ne pas épiler à la cire, à la pince ni à l'épilateur entre les séances : seul le rasage est autorisé.</li>
      <li>Apaiser la peau après la séance, par exemple avec un gel d'aloe vera, et appliquer une protection solaire élevée sur les zones exposées.</li>
    </ul>

    <h2>Questions fréquentes sur l'épilation laser</h2>
    <div class="faq">
      <details>
        <summary>Combien de séances faut-il ?</summary>
        <p>En moyenne 8 à 12 séances selon la zone, la couleur du poil et votre type de peau. Le visage et les zones hormonales en demandent souvent davantage. Le bilan précise votre protocole.</p>
      </details>
      <details>
        <summary>Est-ce que ça fait mal ?</summary>
        <p>La sensation ressemble à de petits picotements de chaleur. Le refroidissement du laser rend la séance bien supportable.</p>
      </details>
      <details>
        <summary>Le laser marche-t-il sur tous les poils ?</summary>
        <p>Le laser cible la mélanine, donc le poil foncé. Les poils blancs, blonds, roux et le duvet ne réagissent pas. Le bilan vérifie que votre pilosité est adaptée.</p>
      </details>
      <details>
        <summary>Et sur peau bronzée ou mate ?</summary>
        <p>Une peau récemment bronzée doit attendre que le bronzage s'estompe pour éviter tout risque. On évite soleil, UV et autobronzant 10 jours avant et 10 jours après.</p>
      </details>
      <details>
        <summary>Quel espacement entre les séances ?</summary>
        <p>En général 6 à 8 semaines au début, puis on espace au fil de la repousse. L'intervalle est ajusté à chaque séance.</p>
      </details>
      <details>
        <summary>L'épilation est-elle vraiment définitive ?</summary>
        <p>On parle d'épilation durable : la grande majorité des poils traités ne repoussent plus. Quelques poils peuvent réapparaître plus fins ; une séance d'entretien suffit souvent.</p>
      </details>
      <details>
        <summary>Y a-t-il des contre-indications ?</summary>
        <p>Grossesse, certaines affections de la peau, prise de médicaments photosensibilisants ou bronzage récent peuvent reporter ou écarter une séance. Le bilan préalable fait le point.</p>
      </details>
      <details>
        <summary>Comment se passe la première fois ?</summary>
        <p>On commence par un bilan offert : examen de la peau et du poil, réponses à vos questions, définition du protocole. Les lunettes de protection sont portées pendant toute la séance.</p>
      </details>
    </div>

    <h2>Épilation laser dans tout le territoire de Manosque</h2>
    <p>L'institut accueille aussi les clientes et clients des communes voisines. Découvrez nos pages dédiées à l'épilation laser à <a href="epilation-laser-sainte-tulle.html">Sainte-Tulle</a>, <a href="epilation-laser-pierrevert.html">Pierrevert</a>, <a href="epilation-laser-volx.html">Volx</a>, <a href="epilation-laser-villeneuve.html">Villeneuve</a>, <a href="epilation-laser-forcalquier.html">Forcalquier</a>, <a href="epilation-laser-greoux-les-bains.html">Gréoux-les-Bains</a>, <a href="epilation-laser-oraison.html">Oraison</a>, <a href="epilation-laser-valensole.html">Valensole</a> et <a href="epilation-laser-sisteron.html">Sisteron</a>. Pour faire connaissance avec la praticienne, rendez-vous sur la page <a href="a-propos.html">à propos</a>.</p>

    <div class="callout callout--legal">
      <p><strong>Information réglementaire.</strong> L'épilation laser à visée non thérapeutique pratiquée chez LUMIA est réalisée par une infirmière diplômée d'État titulaire de l'attestation de formation prévue par l'arrêté du 19 février 2025 〔numéro et organisme de l'attestation à fournir〕. La protection oculaire est obligatoire pendant toute la séance. Comme tout traitement de la peau, l'épilation laser comporte des contre-indications et des risques qui sont examinés lors du bilan ; une fiche d'information et de consentement est signée avant la première séance. Aucun résultat n'est garanti.</p>
    </div>

  </div>
</article>

<section class="cta-section">
  <div class="container">
    <h2>Prête à dire <span class="accent">adieu au rasage</span> ?</h2>
    <p>Réservez votre bilan d'épilation laser à Manosque. Il est offert pour tout achat de séance ou de cure.</p>
    <div class="cta-actions">
      <a href="https://www.planity.com/lumia-04100-manosque" target="_blank" rel="noopener" class="btn btn-primary">Prendre rendez-vous</a>
      <a href="tel:+33492876372" class="btn btn-ghost-light">04 92 87 63 72</a>
    </div>
  </div>
</section>
</main>

<!-- FOOTER -->
'''
epilation_laser_manosque_head = r'''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Épilation laser",
  "name": "Épilation laser définitive à Manosque",
  "description": "Épilation laser définitive à Manosque réalisée par une infirmière diplômée d'État. Laser diode adapté à de nombreux phototypes, sur le visage et le corps, femmes et hommes. Bilan personnalisé obligatoire avant la première séance, offert pour tout achat.",
  "url": "https://lumia-salon.fr/epilation-laser-manosque.html",
  "provider": {
    "@type": "BeautySalon",
    "name": "LUMIA",
    "url": "https://lumia-salon.fr",
    "telephone": "+33492876372",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "10 Bis avenue Jean Giono",
      "addressLocality": "Manosque",
      "postalCode": "04100",
      "addressCountry": "FR"
    }
  },
  "areaServed": [
    { "@type": "City", "name": "Manosque" },
    { "@type": "City", "name": "Forcalquier" },
    { "@type": "City", "name": "Gréoux-les-Bains" },
    { "@type": "City", "name": "Pierrevert" },
    { "@type": "City", "name": "Oraison" },
    { "@type": "City", "name": "Valensole" }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Combien de séances faut-il ?", "acceptedAnswer": { "@type": "Answer", "text": "En moyenne 8 à 12 séances selon la zone, la couleur du poil et votre type de peau. Le visage et les zones hormonales en demandent souvent davantage. Le bilan précise votre protocole." } },
    { "@type": "Question", "name": "Est-ce que ça fait mal ?", "acceptedAnswer": { "@type": "Answer", "text": "La sensation ressemble à de petits picotements de chaleur. Le refroidissement du laser rend la séance bien supportable." } },
    { "@type": "Question", "name": "Le laser marche-t-il sur tous les poils ?", "acceptedAnswer": { "@type": "Answer", "text": "Le laser cible la mélanine, donc le poil foncé. Les poils blancs, blonds, roux et le duvet ne réagissent pas. Le bilan vérifie que votre pilosité est adaptée." } },
    { "@type": "Question", "name": "Et sur peau bronzée ou mate ?", "acceptedAnswer": { "@type": "Answer", "text": "Une peau récemment bronzée doit attendre que le bronzage s'estompe pour éviter tout risque. On évite soleil, UV et autobronzant 10 jours avant et 10 jours après." } },
    { "@type": "Question", "name": "Quel espacement entre les séances ?", "acceptedAnswer": { "@type": "Answer", "text": "En général 6 à 8 semaines au début, puis on espace au fil de la repousse. L'intervalle est ajusté à chaque séance." } },
    { "@type": "Question", "name": "L'épilation est-elle vraiment définitive ?", "acceptedAnswer": { "@type": "Answer", "text": "On parle d'épilation durable : la grande majorité des poils traités ne repoussent plus. Quelques poils peuvent réapparaître plus fins ; une séance d'entretien suffit souvent." } },
    { "@type": "Question", "name": "Y a-t-il des contre-indications ?", "acceptedAnswer": { "@type": "Answer", "text": "Grossesse, certaines affections de la peau, prise de médicaments photosensibilisants ou bronzage récent peuvent reporter ou écarter une séance. Le bilan préalable fait le point." } },
    { "@type": "Question", "name": "Comment se passe la première fois ?", "acceptedAnswer": { "@type": "Answer", "text": "On commence par un bilan offert : examen de la peau et du poil, réponses à vos questions, définition du protocole. Les lunettes de protection sont portées pendant toute la séance." } }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://lumia-salon.fr/" },
    { "@type": "ListItem", "position": 2, "name": "Épilation laser", "item": "https://lumia-salon.fr/epilation-laser-manosque.html" }
  ]
}
</script>
'''
page("epilation-laser-manosque.html", r"""Épilation laser définitive à Manosque | LUMIA""", r"""Épilation laser définitive à Manosque par une infirmière D.E. Laser diode adapté à tous types de peau. Bilan personnalisé offert. RDV en ligne.""", "https://lumia-salon.fr/epilation-laser-manosque.html", epilation_laser_manosque_body, schema=epilation_laser_manosque_head)

# ============================ MENTIONS-LEGALES.HTML ============================
mentions_legales_body = r'''

<header class="page-header">
  <div class="container">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <a href="./">Accueil</a> <span>›</span> Mentions légales
    </nav>
    <h1>Mentions légales</h1>
  </div>
</header>

<main id="main">
<article class="article-body">
  <div class="container">

    <h2>Éditeur du site</h2>
    <p>Le présent site est édité par LUMIA, institut de beauté et centre d'épilation laser.</p>
    <ul>
      <li>Dénomination / exploitante : Margaux Libereau (LUMIA)</li>
      <li>Forme juridique : 〔à fournir〕</li>
      <li>Adresse : 10 Bis avenue Jean Giono, 04100 Manosque</li>
      <li>Téléphone : <a href="tel:+33492876372">04 92 87 63 72</a></li>
      <li>Email : 〔email professionnel à fournir〕</li>
      <li>SIRET : 〔à fournir〕</li>
      <li>Numéro de TVA intracommunautaire : 〔à fournir si applicable〕</li>
      <li>Directrice de la publication : Margaux Libereau</li>
    </ul>

    <h2>Hébergement</h2>
    <p>Le site est hébergé par O2switch, SAS au capital de 100 000 €, 222-224 boulevard Gustave Flaubert, 63000 Clermont-Ferrand, France. Téléphone : 04 44 44 60 40.</p>

    <h2>Épilation laser : information réglementaire</h2>
    <p>L'épilation laser à visée non thérapeutique proposée par LUMIA est réalisée par une infirmière diplômée d'État titulaire de l'attestation de formation prévue par le décret n° 2024-470 du 24 mai 2024 et l'arrêté du 19 février 2025 〔numéro et organisme de l'attestation à fournir〕.</p>
    <div class="callout callout--legal">
      <p><strong>Avertissement.</strong> L'épilation laser comporte des contre-indications (notamment grossesse, certaines affections cutanées, prise de médicaments photosensibilisants, bronzage récent) et des risques qui sont examinés lors d'un bilan préalable obligatoire. Le <strong>port de lunettes de protection oculaire est obligatoire</strong> pendant toute la durée de la séance. Une <strong>fiche d'information et de consentement</strong> est remise et signée par le client avant la première séance, puis conservée pendant la durée légale. Aucun résultat n'est garanti.</p>
    </div>

    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des contenus de ce site (textes, images, logo, charte graphique) est protégé par le droit de la propriété intellectuelle. Toute reproduction, même partielle, est interdite sans autorisation préalable.</p>

    <h2>Données personnelles</h2>
    <p>Les informations transmises via le formulaire de contact sont utilisées uniquement pour répondre à votre demande. Pour en savoir plus sur le traitement de vos données et exercer vos droits, consultez notre <a href="politique-confidentialite.html">politique de confidentialité</a>.</p>

    <h2>Médiation de la consommation</h2>
    <p>Conformément aux articles L.611-1 et suivants du Code de la consommation, le client peut recourir gratuitement à un médiateur de la consommation en vue de la résolution amiable d'un litige 〔médiateur à désigner par la cliente, ex. MEDICYS, www.medicys.fr〕. La plateforme européenne de règlement en ligne des litiges est accessible à l'adresse https://ec.europa.eu/consumers/odr.</p>

  </div>
</article>
</main>

<!-- FOOTER -->
'''
page("mentions-legales.html", r"""Mentions légales | LUMIA""", r"""Mentions légales de l'institut LUMIA à Manosque.""", "https://lumia-salon.fr/mentions-legales.html", mentions_legales_body, robots="noindex, follow")
