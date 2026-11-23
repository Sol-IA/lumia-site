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

GitHub Pages ne sachant servir que la racine ou `/docs` en mode branche, la publication passe par `.github/workflows/pages.yml`. Ce fichier ne bouge jamais, et il devient inutile à la bascule OVH.

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
python3 local/build/gen_blog.py       # le blog et ses articles
```

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
