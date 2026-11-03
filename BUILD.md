# Régénérer le site

Toutes les pages sont produites par les générateurs. **Ne jamais éditer un `.html`
directement** : la modification serait perdue à la prochaine génération.

```
python3 gen_core.py       # accueil, épilation laser, soins du visage, mentions légales
python3 gen_services.py   # LPG, COSMELAN, microneedling
python3 gen_pages2.py     # à propos, tarifs, contact, 404, confidentialité
python3 gen_local.py      # les 9 pages locales d'épilation laser
python3 gen_blog.py       # le blog et ses articles
```

`build_pages.py` ne génère rien : il fournit l'en-tête, le menu, le pied de page,
les blocs communs et l'utilitaire `img_size()`, qui lit les dimensions réelles des
images pour éviter les décalages de mise en page.

Le menu et le pied de page se modifient **uniquement** dans `build_pages.py`.
