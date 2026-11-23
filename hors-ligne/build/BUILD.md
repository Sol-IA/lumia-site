# LUMIA · construire le site

## La règle, et il n'y en a qu'une

**Deux dossiers.**

| Dossier | Contenu | En ligne ? |
|---|---|---|
| **`docs/`** | **le site, et rien d'autre** | ✅ **oui, intégralement** |
| **`hors-ligne/`** | tout le reste : générateurs, images brutes, propale, plans, module abandonné | ❌ **jamais** |

🔴 **Tout `docs/` va en ligne. Rien d'autre n'y va.**
Pour un envoi FTP : on pointe `docs/`, on envoie tout. Rien à trier, donc rien à se tromper.

`CLAUDE.md` reste à la racine : c'est imposé par le système de mémoire et par le chargement automatique du contexte projet.

### Pourquoi `docs/` et pas `site/`

En mode branche, **GitHub Pages ne sait servir que la racine ou `/docs`**. Le nom vient de cette contrainte. L'appeler `site/` imposerait de passer Pages en déploiement par workflow, donc un fichier de plus à maintenir et une fenêtre de coupure, pour un résultat identique.

### Ce que git suit

Tout `docs/` **sauf `docs/php/`**, qui contient des identifiants et ne part qu'en FTP.
Dans `hors-ligne/`, **seul `build/` est versionné** : les générateurs sont la source du site. Le reste est ignoré en bloc, dont les 81 Mo d'images brutes.

## Régénérer

Depuis la racine du projet, dans cet ordre :

```bash
python3 hors-ligne/build/gen_core.py       # accueil, laser, soins du visage, mentions légales
python3 hors-ligne/build/gen_services.py   # LPG, COSMELAN, microneedling, cosmétiques
python3 hors-ligne/build/gen_pages2.py     # à propos, tarifs, contact, 404, confidentialité
python3 hors-ligne/build/gen_local.py      # les 9 pages locales
python3 hors-ligne/build/gen_blog.py       # le blog et ses articles
```

## Règles absolues

1. 🔴 **Ne jamais éditer un `.html` de `docs/`.** Il est écrasé à la régénération suivante. On modifie le générateur.
2. **Menu et pied de page : uniquement dans `build_pages.py`.** Les oublier ailleurs a déjà rendu une prestation invisible sur tout le site.
3. **`img_size()`** lit les dimensions réelles des images. Toujours l'utiliser plutôt que de saisir des valeurs à la main.
4. **`style.css` ET `style.min.css`** se modifient tous les deux, idem `js/*.js` et `js/*.min.js`. Aucun script ne les synchronise.
5. **Les chiffres d'avis** sont des constantes en tête de `build_pages.py`, injectées partout via `{{NOTE}}`, `{{AVIS_PLANITY}}`, `{{AVIS_GOOGLE}}`, `{{AVIS_TOTAL}}`, `{{AVIS_GOOGLE_URL}}`.
6. Les vignettes de prestation sont recadrées par le CSS en **16/10 paysage** avec `object-fit: cover`. Fournir les images déjà à ce format, sinon le navigateur recadre une seconde fois au centre et ampute le sujet.

## Valider, puis prévisualiser

```bash
python3 "../docs/tools/validate-solia.py" docs
```

Zéro bloquant exigé avant tout push. Prévisualisation : configuration `lumia`, port 8093, qui sert `docs/`.
