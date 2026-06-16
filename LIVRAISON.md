# LUMIA — Note de livraison

Site statique pour l'institut LUMIA (Manosque), réalisé par Sol·IA. Document à remettre à Margaux Libereau avec le site.

## 1. Données à valider avant publication
Tout a été collecté en ligne (fiche Planity, site Wix, Google, photos). Merci de **confirmer que rien n'a changé** :
- **Tarifs** (page Tarifs) : repris de Planity, à revalider.
- **Horaires** : lundi-vendredi 10h-19h, fermé samedi et dimanche.
- **Parcours / formations**, **parkings gratuits**, **moyens de paiement** (CB, espèces, 3× sans frais sur les cures).

## 2. Éléments non publics à fournir (placeholders 〔…〕 visibles dans le site)
| Donnée | Où |
|---|---|
| SIRET, forme juridique, éditeur, directrice de publication | Mentions légales |
| Email professionnel (créer `contact@lumia-salon.fr`) | Mentions légales, Politique de confidentialité, config PHP |
| Numéro et organisme de l'attestation de formation laser | Mentions légales, page Épilation laser |
| Médiateur de la consommation (ex. MEDICYS) | Mentions légales |
| 3 avis clients réels + note/nombre Google exacts | Accueil (section avis) |

> Le **modèle de laser est identifié** sur vos photos : diode **Leaseir**. Mentionné sur la page À propos.

## 3. Photos
Les photos actuelles sont **provisoires**, récupérées sur votre Google / site Wix / Instagram. Elles sont en place pour la démonstration. Pour la version finale, vous pouvez fournir vos **fichiers photo définitifs** (idéalement en WebP) : institut, praticienne, matériel, avant/après autorisés. Les remplacer se fait en gardant les mêmes noms de fichiers dans `assets/`.

## 4. Recommandations (hors périmètre du code)
1. **Facebook** : le compte actuel est un profil personnel. Le convertir en **Page professionnelle** (avis, statistiques, lien propre).
2. **Avis Google** : excellente dynamique sur Planity (5,0/32). Mettre en place une routine de collecte d'avis **Google** (message après chaque prestation). Voir le guide GBP.
3. **Affichage légal en institut** : afficher physiquement l'attestation de formation laser et l'avertissement risques / contre-indications / protection oculaire (obligation réglementaire).
4. **Email pro** : créer et utiliser `contact@lumia-salon.fr` partout (cohérence et crédibilité).

## 5. Mise en ligne
### Démo
- Le site est d'abord présenté sur **GitHub Pages** (statique). Sur cette démo, le **formulaire de contact est volontairement désactivé** (GitHub Pages n'exécute pas PHP) : il affiche un message invitant à réserver sur Planity ou à appeler. Il fonctionnera en production.

### Production (O2switch)
1. Déposer tout le dossier par **FTP** sur O2switch, **sauf** : les dossiers `assets/scrape/`, `assets/*_files/`, les fichiers `*.html` de sauvegarde (lumiere, laserday, vidéoentrée), et les scripts `*.py`.
2. Déposer les fichiers PHP (`php/config.php`, `php/send.php`, `php/ratelimit.php`) **uniquement par FTP** (ils sont en `.gitignore`, jamais sur GitHub). Mettre à jour `CONTACT_EMAIL` dans `php/config.php`.
3. Vérifier que le `.htaccess` est bien uploadé (HTTPS, www→sans-www, en-têtes de sécurité, cache).
4. **Migration depuis Wix** : récupérer la liste des URL Wix indexées (Search Console) et compléter les **redirections 301** dans `.htaccess` avant la bascule DNS du domaine `lumia-salon.fr`.
5. Soumettre `sitemap.xml` dans Google Search Console et surveiller les 404 pendant 2-3 semaines.

## 6. Notes techniques (pour Sol·IA)
- **CSS** : source `css/style.css`, minifier vers `css/style.min.css` après toute modification (préserver les espaces dans `calc()`).
- **JS** : source `js/main.js`, minifier vers `js/main.min.js`. ⚠️ Ne stripper que les lignes **100% commentaire** (`^\s*//`), jamais un `//` en milieu de ligne (casse les regex comme `/^\.\.\//` et les URLs).
- **Pages** : générées par `build_pages.py` + `gen_*.py` (en-tête/pied centralisés). Le blog lit `blog/articles.json`.
- **Couleur de marque** : terracotta `#A63524` (échantillonnée sur le logo).
