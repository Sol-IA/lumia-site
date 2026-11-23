/* =========================================================================
   ANNONCES LUMIA · bannière et popup
   =========================================================================
   Ce fichier contient UNIQUEMENT le contenu des annonces.
   Il se modifie sans toucher au reste du site, et demain depuis l'interface
   d'administration.

   Les dates sont au format AAAA-MM-JJ et sont inclusives.
   Une annonce s'éteint TOUTE SEULE après sa date de fin : il n'y a rien à
   penser à retirer.

   banniere.active / popup.active : true pour afficher, false pour éteindre.
   popup.frequence : "once" une seule fois, "jour" une fois par jour,
                     "semaine" une fois par semaine.
   ========================================================================= */
window.ANNONCES = {

  banniere: {
    active:  true,
    texte:   "BLACK FRIDAY · 3 séances laser offertes pour l'achat d'une cure de 7",
    lien:    "https://www.planity.com/lumia-04100-manosque",
    libelle: "J'en profite",
    debut:   "2026-11-23",
    fin:     "2026-11-30"
  },

  popup: {
    active:    true,
    titre:     "Black Friday chez LUMIA",
    texte:     "Pour l'achat d'une cure d'épilation laser de 7 séances, 3 séances vous sont offertes, soit une cure de 10 séances au prix de 7. Jusqu'à 450 euros d'économies. Paiement en 2 ou 3 fois disponible.",
    note:      ["Offre valable jusqu'au 30 novembre 2026.",
                "L'achat doit être réalisé pendant cette période."],
    image:     "assets/laserhomme.webp",
    imageAlt:  "Séance d'épilation laser à l'institut LUMIA à Manosque",
    bouton:    "Réserver mon bilan",
    lien:      "https://www.planity.com/lumia-04100-manosque",
    debut:     "2026-11-23",
    fin:       "2026-11-30",
    frequence: "jour"
  }

};
