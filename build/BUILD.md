# LUMIA · comment on construit le site

## Arborescence

| Dossier | Contenu | Va en ligne ? |
|---|---|---|
| **`docs/`** | **le site, et rien d'autre** · pages, assets, css, js, blog, php | ✅ **oui, intégralement** |
| `build/` | les générateurs et ce fichier | ❌ non |
| `interne/` | sources d'images brutes, propale, module de réservation abandonné | ❌ **jamais** |
| racine | `CLAUDE.md` et les deux plans | ❌ non, et ignorés par git |

🔴 **Règle unique : ce qui doit aller en ligne vit dans `docs/`, et tout `docs/` va en ligne.**
Pour un envoi FTP, on pointe `docs/` et on envoie tout. Il n'y a rien à trier, donc rien à se tromper.

`docs/` s'appelle ainsi parce que **GitHub Pages sert nativement ce dossier** en mode branche, sans workflow à maintenir. Le nom est imposé par GitHub, pas choisi.

## Régénérer

Depuis la racine du projet, dans cet ordre :

```bash
python3 build/gen_core.py       # accueil, épilation laser, soins du visage, mentions légales
python3 build/gen_services.py   # LPG, COSMELAN, microneedling, cosmétiques
python3 build/gen_pages2.py     # à propos, tarifs, contact, 404, confidentialité
python3 build/gen_local.py      # les 9 pages locales
python3 build/gen_blog.py       # le blog et ses articles
```

## Règles absolues

1. 🔴 **Ne jamais éditer un `.html` de `docs/`.** Il est écrasé à la régénération suivante. On modifie le générateur.
2. **Menu et pied de page : uniquement dans `build/build_pages.py`.** Les oublier ailleurs a déjà rendu une prestation invisible.
3. **`img_size()` lit les dimensions réelles** des images, sans dépendance. Toujours l'utiliser plutôt que de saisir des valeurs à la main.
4. **`css/style.css` ET `css/style.min.css`** doivent être modifiés tous les deux, idem pour `js/*.js` et `js/*.min.js`. Aucun script ne les synchronise.
5. **Les chiffres d'avis** sont des constantes en tête de `build_pages.py`, substituées partout via les jetons `{{NOTE}}`, `{{AVIS_PLANITY}}`, `{{AVIS_GOOGLE}}`, `{{AVIS_TOTAL}}`, `{{AVIS_GOOGLE_URL}}`.
6. Les vignettes de prestation sont recadrées par le CSS en **16/10 paysage**, avec `object-fit: cover`. Fournir des images déjà au bon format, sinon le navigateur recadre une seconde fois au centre et ampute le sujet.

## Valider

```bash
python3 "../docs/tools/validate-solia.py" docs
```

Zéro bloquant exigé avant tout push.

## Prévisualiser

Configuration `lumia`, port 8093, qui sert `docs/`.
