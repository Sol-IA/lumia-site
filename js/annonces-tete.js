/*
 * LUMIA · réservation de la place de la bannière, avant le premier rendu.
 * Chargé de façon BLOQUANTE dans le <head>, juste après annonces.js.
 * Pose la classe has-banniere sur <html> si une bannière est en cours,
 * pour que le CSS réserve sa hauteur : zéro décalage de mise en page.
 * Accepte une bannière seule (« banniere ») ou une liste planifiée
 * (« bannieres », la première en cours l'emporte, 24/11/2026).
 * Fichier externe et non script inline : la CSP du .htaccess (script-src 'self')
 * bloque tout script inline (défaut constaté sur la recette OVH le 23/11/2026).
 * Modifier aussi annonces-tete.min.js.
 */
(function () {
  var A = window.ANNONCES || {}, n = new Date(), b = A.banniere;
  function enCours(o) {
    return !!(o && o.active && !(o.debut && new Date(o.debut + 'T00:00:00') > n) && !(o.fin && new Date(o.fin + 'T23:59:59') < n));
  }
  if (A.bannieres) { b = null; for (var i = 0; i < A.bannieres.length; i++) { if (enCours(A.bannieres[i])) { b = A.bannieres[i]; break; } } }
  if (!enCours(b)) return;
  try {
    if (localStorage.getItem('lumiaBanniere|' + (b.titre || b.texte || '') + '|' + (b.debut || '') + '|' + (b.fin || ''))) return;
  } catch (e) {}
  document.documentElement.classList.add('has-banniere');
})();
