# LUMIA · construire le site

## La règle, et il n'y en a qu'une

**Deux dossiers.**

| Dossier | Contenu | En ligne ? |
|---|---|---|
| **`SITE/`** | **le site, et rien d'autre** | ✅ **oui, intégralement** |
| **`local/`** | tout le reste : générateurs, images brutes, propale, plans, module abandonné | ❌ **jamais** |

🔴 **Tout `SITE/` va en ligne. Rien d'autre n'y va.**
Pour un envoi FTP : on pointe `SITE/`, on envoie tout. Rien à trier, donc rien à se tromper.

`CLAUDE.md` reste à la racine : c'est imposé par le système de mémoire et par le chargement automatique du contexte projet.

### Pourquoi `SITE/`

C'est la **convention MGE** : « `SITE/` est le miroir EXACT et COMPLET d'OVH, source de vérité unique ». ⚠️ Surtout pas `docs/` : chez MGE ce nom désigne la **documentation interne**, et le même mot voulant dire l'inverse d'un projet à l'autre, c'est l'ambiguïté qui produit une erreur le jour du FTP.

GitHub Pages ne sachant servir que la racine ou `/docs` en mode branche, la publication passe par `.github/workflows/pages.yml`, qui copie `SITE/` à la racine d'une branche **`gh-pages`**.

🔴 **Ne pas retenter la voie officielle par artefact.** Testée le 23/11/2026 : `upload-pages-artifact` dépose bien l'artefact, `deploy-pages` ne le retrouve pas. Versions à jour, permission `actions: read` ajoutée, aucun incident GitHub : sans effet. La branche `gh-pages` n'utilise ni artefact, ni API, ni action tierce.

Ce fichier ne bouge jamais, et il devient inutile à la bascule OVH.

### Ce que git suit

Tout `SITE/` **sauf `SITE/php/`**, qui contient des identifiants et ne part qu'en FTP.
Dans `local/`, **seul `build/` est versionné** : les générateurs sont la source du site. Le reste est ignoré en bloc, dont les 81 Mo d'images brutes.

## Régénérer

Depuis la racine du projet, dans cet ordre :

```bash
python3 local/build/gen_core.py       # accueil, laser, soins du visage, mentions légales
python3 local/build/gen_services.py   # LPG, COSMELAN, microneedling, cosmétiques
python3 local/build/gen_pages2.py     # à propos, tarifs, contact, 404, confidentialité
python3 local/build/gen_local.py      # les 9 pages locales
python3 local/build/gen_og_illus.py   # images de partage JPEG des illustrations (Playwright, sans -I)
python3 local/build/gen_blog.py       # le blog et ses articles
```

### Blog : illustrations et maillage (règles du 24/11/2026)

- **Une illustration SVG unique par article**, jamais réutilisée : `SITE/assets/illustrations/<slug>.svg` (1200 × 600, palette LUMIA, sans or ni texte, style des deux témoins validés par Thomas : microneedling et cellulite). Elle s'affiche en tête d'article et sur la carte ; la vraie photo reste dans le corps. Texte alternatif dans la clé `illu_alt`. `gen_og_illus.py` en tire l'image de partage `illustrations/og/<slug>.jpg` (1200 × 630).
- **Ordre** : le blog liste du plus récent au plus ancien (tri sur `iso`). On n'affiche que le mois et l'année ; un article par mois, le 15.
- **Maillage calculé à chaque génération** : « À lire aussi » = 3 articles, jamais l'article lui-même ni un article déjà cité dans son texte ; priorité au même thème, puis au thème voisin, puis au moins cité, puis au plus récent. Un ancien article cite donc les nouveaux. `gen_blog.py` **s'arrête** si la règle est violée ou si un article n'est cité nulle part.
- **Nouvel article** : l'ajouter à `ARTICLES` avec son illustration, régénérer, puis renvoyer **toutes** les pages d'articles (leurs « À lire aussi » changent).

## Règles absolues

1. 🔴 **Ne jamais éditer un `.html` de `SITE/`.** Il est écrasé à la régénération suivante. On modifie le générateur.
2. **Menu et pied de page : uniquement dans `build_pages.py`.** Les oublier ailleurs a déjà rendu une prestation invisible sur tout le site.
3. **`img_size()`** lit les dimensions réelles des images. Toujours l'utiliser plutôt que de saisir des valeurs à la main.
4. **`style.css` ET `style.min.css`** se modifient tous les deux, idem `js/*.js` et `js/*.min.js`. Aucun script ne les synchronise.
5. **Les chiffres d'avis** sont des constantes en tête de `build_pages.py`, injectées partout via `{{NOTE}}`, `{{AVIS_PLANITY}}`, `{{AVIS_GOOGLE}}`, `{{AVIS_TOTAL}}`, `{{AVIS_GOOGLE_URL}}`.
6. Les vignettes de prestation sont recadrées par le CSS en **16/10 paysage** avec `object-fit: cover`. Fournir les images déjà à ce format, sinon le navigateur recadre une seconde fois au centre et ampute le sujet.

## Valider, puis prévisualiser

Depuis `Sol.IA/` :

```bash
python3 "docs/tools/validate-solia.py" LUMIA/SITE
```

Zéro bloquant exigé avant tout push. Prévisualisation : configuration `lumia`, port 8093, qui sert `SITE/`.

## Règles ajoutées le 24/11/2026 (correctifs de l'audit)

- **Typographie** : `page()` pose une espace insécable avant « : ; ? ! » dans le texte visible (jamais dans les balises, scripts, styles). Écrire les textes avec une espace ordinaire, la génération s'en charge.
- **JSON-LD** : l'institut a un seul identifiant, `"@id": "https://lumia-salon.fr/#institut"`, à réutiliser dans tout nouveau bloc (`provider`, `publisher`, `worksFor`).
- **Blog** : `MAJ_BLOG` (gen_blog.py) donne le `dateModified` des articles. L'avancer seulement après une vraie révision du contenu.
- **Images** : la première image visible d'une page (LCP) en `loading="eager"` + `fetchpriority="high"`, toutes les autres en `lazy`.
- **Recette OVH** : servie en `X-Robots-Tag: noindex` par le `.htaccess` (hôte `*.hosting.ovh.net`), donc Lighthouse y affiche SEO 69 : normal.
- **Pages de villes** : similarité par mots < 70 % entre deux villes (`scratchpad/lot4/sim.py`), trajets mesurés (OSRM), jamais de fait local sans source.
- **Annonces (24/11/2026)** : `SITE/annonces.js` est réécrit par l'administration (`php/admin/`). La version du serveur fait foi : la récupérer avant tout envoi SFTP, ne jamais l'écraser avec la copie locale.
- **Annonces planifiées (24/11/2026)** : `annonces.js` contient des listes `bannieres` et `popups` (la plus récente en premier) ; `js/annonces.js` et `js/annonces-tete.js` affichent la première en cours. La mémoire complète (brouillons, archives) est dans `php/admin/annonces-data.php`, sur le serveur seulement.
- **Lighthouse sur la recette (25/11/2026)** : ajouter `--chrome-flags="--headless=new --disable-features=HttpsUpgrades,HttpsFirstBalancedModeAutoEnable"`, sinon Chrome tente le HTTPS, que l'hôte technique OVH refuse, et la mesure échoue (NO_FCP). Faire au moins 3 passages : un passage isolé peut sortir de la norme.
