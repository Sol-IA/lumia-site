/* =========================================================================
   ANNONCES LUMIA · bannières et fenêtres d'annonce
   =========================================================================
   Fichier ÉCRIT PAR L'ADMINISTRATION (php/admin/) : ne pas le modifier à la
   main, il serait écrasé. Il ne contient que les annonces publiées et non
   terminées, de la plus récente à la plus ancienne ; js/annonces.js affiche
   la première en cours. Dates au format AAAA-MM-JJ, inclusives.
   ========================================================================= */
window.ANNONCES = {
    "bannieres": [
        {
            "debut": "2026-11-23",
            "fin": "2026-11-30",
            "texte": "BLACK FRIDAY · 3 séances laser offertes pour l'achat d'une cure de 7",
            "libelle": "J'en profite",
            "lien": "https://www.planity.com/lumia-04100-manosque",
            "active": true
        }
    ],
    "popups": [
        {
            "active": true,
            "titre": "Black Friday chez LUMIA",
            "texte": [
                "Pour l'achat d'une cure d'épilation laser de 7 séances, 3 séances vous sont offertes, soit une cure de 10 séances au prix de 7.",
                "Paiement en 3 fois sans frais disponible."
            ],
            "note": [
                "Offre valable jusqu'au 30 novembre 2026.",
                "L'achat doit être réalisé pendant cette période."
            ],
            "image": "assets/laserhomme.webp",
            "imageAlt": "Séance d'épilation laser à l'institut LUMIA à Manosque",
            "bouton": "Profiter de l'offre",
            "lien": "https://www.planity.com/lumia-04100-manosque",
            "debut": "2026-11-23",
            "fin": "2026-11-30",
            "frequence": "jour"
        }
    ]
};
