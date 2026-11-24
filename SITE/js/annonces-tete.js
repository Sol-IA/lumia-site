/*
 * LUMIA · réservation de la place de la bannière, avant le premier rendu.
 * Chargé de façon BLOQUANTE dans le <head>, juste après annonces.js.
 * Pose la classe has-banniere sur <html> si une bannière est active,
 * pour que le CSS réserve sa hauteur : zéro décalage de mise en page.
 * Fichier externe et non script inline : la CSP du .htaccess (script-src 'self')
 * bloque tout script inline (défaut constaté sur la recette OVH le 23/11/2026).
 * Modifier aussi annonces-tete.min.js.
 */
(function () {
  var b = (window.ANNONCES || {}).banniere;
  if (!b || !b.active) return;
  var n = new Date();
  if (b.debut && new Date(b.debut + 'T00:00:00') > n) return;
  if (b.fin && new Date(b.fin + 'T23:59:59') < n) return;
  try {
    if (localStorage.getItem('lumiaBanniere|' + (b.titre || b.texte || '') + '|' + (b.debut || '') + '|' + (b.fin || ''))) return;
  } catch (e) {}
  document.documentElement.classList.add('has-banniere');
})();
