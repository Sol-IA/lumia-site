/* Affichage de la bannière et de la popup d'annonce.
   Le contenu vit dans annonces.js, à la racine du site.
   Ce fichier ne contient que la logique : il n'y a jamais à le modifier
   pour changer une offre. */
(function () {
  'use strict';

  var A = window.ANNONCES || {};
  var d = document;

  /* Les chemins relatifs des annonces (image, lien) sont écrits depuis la racine
     du site : on les résout depuis l'emplacement de annonces.js, pour qu'ils
     marchent aussi dans les sous-dossiers comme /blog/. */
  var racine = '';
  var scripts = d.getElementsByTagName('script');
  for (var i = 0; i < scripts.length; i++) {
    var s = scripts[i].src || '';
    if (/\/annonces\.js(\?|$)/.test(s) && !/\/js\/annonces\.js/.test(s)) { racine = s.replace(/annonces\.js.*$/, ''); break; }
  }
  function resoudre(u) {
    if (!u || /^([a-z][a-z0-9+.-]*:|\/|#)/i.test(u)) return u;
    return racine + u;
  }

  /* Une annonce est en cours si elle est active et dans sa fenêtre de dates. */
  function enCours(o) {
    if (!o || !o.active) return false;
    var maintenant = new Date();
    if (o.debut) {
      var debut = new Date(o.debut + 'T00:00:00');
      if (isNaN(debut) || debut > maintenant) return false;
    }
    if (o.fin) {
      var fin = new Date(o.fin + 'T23:59:59');
      if (isNaN(fin) || fin < maintenant) return false;
    }
    return true;
  }

  /* La clé dépend du contenu : une nouvelle campagne se réaffiche,
     même si la précédente avait été fermée. */
  function cle(prefixe, o) {
    return prefixe + '|' + (o.titre || o.texte || '') + '|' + (o.debut || '') + '|' + (o.fin || '');
  }

  function lire(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function ecrire(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  function lienExterne(a, url) {
    if (/^https?:/i.test(url)) {
      a.target = '_blank'; a.rel = 'noopener';
      var s = d.createElement('span'); s.className = 'sr-only'; s.textContent = ' (nouvel onglet)'; a.appendChild(s);
    }
  }

  /* ----------------------------------------------------------- Bannière */
  function bandeau() {
    var b = A.banniere;
    if (!enCours(b)) return;
    if (lire(cle('lumiaBanniere', b))) return;

    var el = d.createElement('div');
    el.className = 'banniere';
    el.setAttribute('role', 'region');
    el.setAttribute('aria-label', 'Annonce de l’institut');

    var inner = d.createElement('div');
    inner.className = 'banniere__inner';

    var texte = d.createElement('span');
    texte.className = 'banniere__texte';
    texte.textContent = b.texte || '';
    inner.appendChild(texte);

    if (b.lien && b.libelle) {
      var a = d.createElement('a');
      a.className = 'banniere__lien';
      a.href = resoudre(b.lien);
      a.textContent = b.libelle;
      lienExterne(a, b.lien);
      inner.appendChild(a);
    }

    var fermer = d.createElement('button');
    fermer.type = 'button';
    fermer.className = 'banniere__fermer';
    fermer.setAttribute('aria-label', 'Fermer l’annonce');
    fermer.textContent = '×';
    fermer.addEventListener('click', function () {
      ecrire(cle('lumiaBanniere', b), '1');
      d.documentElement.classList.remove('has-banniere');
      el.parentNode && el.parentNode.removeChild(el);
    });
    inner.appendChild(fermer);

    el.appendChild(inner);
    var saut = d.querySelector('.skip-link');
    d.body.insertBefore(el, saut ? saut.nextSibling : d.body.firstChild);
  }

  /* -------------------------------------------------------------- Popup */
  function fenetre() {
    var p = A.popup;
    if (!enCours(p)) return;
    if (typeof HTMLDialogElement === 'undefined') return;

    var k = cle('lumiaPopup', p);
    var vu = lire(k);
    if (vu) {
      if (p.frequence === 'once') return;
      var jours = p.frequence === 'semaine' ? 7 : 1;
      if (Date.now() - parseInt(vu, 10) < jours * 86400000) return;
    }

    var dlg = d.createElement('dialog');
    dlg.className = 'popup';
    dlg.setAttribute('aria-labelledby', 'popupTitre');

    var fermer = d.createElement('button');
    fermer.type = 'button';
    fermer.className = 'popup__fermer';
    fermer.setAttribute('aria-label', 'Fermer');
    fermer.textContent = '×';
    fermer.addEventListener('click', function () { dlg.close(); });
    dlg.appendChild(fermer);

    if (p.image) {
      var img = d.createElement('img');
      img.className = 'popup__img';
      img.setAttribute('data-src', resoudre(p.image)); /* chargée à l'ouverture seulement */
      img.alt = p.imageAlt || '';
      img.loading = 'lazy';
      dlg.appendChild(img);
    }

    var corps = d.createElement('div');
    corps.className = 'popup__corps';

    var h = d.createElement('h2');
    h.className = 'popup__titre';
    h.id = 'popupTitre';
    h.textContent = p.titre || '';
    corps.appendChild(h);

    if (p.texte) {
      var phrases = Array.isArray(p.texte) ? p.texte : [p.texte];
      phrases.forEach(function (phrase) {
        var pt = d.createElement('p');
        pt.className = 'popup__phrase';
        pt.textContent = phrase;
        corps.appendChild(pt);
      });
    }

    if (p.lien && p.bouton) {
      var cta = d.createElement('a');
      cta.className = 'btn btn-primary popup__cta';
      cta.href = resoudre(p.lien);
      cta.textContent = p.bouton;
      lienExterne(cta, p.lien);
      corps.appendChild(cta);
    }

    if (p.note) {
      var lignes = Array.isArray(p.note) ? p.note : [p.note];
      var notes = d.createElement('div');
      notes.className = 'popup__notes';
      lignes.forEach(function (texte) {
        var note = d.createElement('p');
        note.textContent = texte;
        notes.appendChild(note);
      });
      corps.appendChild(notes);
    }

    dlg.appendChild(corps);
    d.body.appendChild(dlg);

    /* Fermeture au clic sur le fond. */
    dlg.addEventListener('click', function (e) {
      if (e.target === dlg) dlg.close();
    });

    /* Déclenchement : après un délai, ou à mi-page, au premier des deux. */
    var lance = false;
    var minuteur = setTimeout(ouvrir, 18000);
    window.addEventListener('scroll', auScroll, { passive: true });

    function auScroll() {
      var h = d.documentElement;
      var vu = (h.scrollTop + window.innerHeight) / h.scrollHeight;
      if (vu > 0.5) ouvrir();
    }

    function ouvrir() {
      if (lance) return;
      lance = true;
      clearTimeout(minuteur);
      window.removeEventListener('scroll', auScroll);
      ecrire(k, String(Date.now()));
      var im = dlg.querySelector('img[data-src]');
      if (im) im.src = im.getAttribute('data-src');
      dlg.showModal();
    }
  }

  function demarrer() { bandeau(); fenetre(); }

  if (d.readyState === 'loading') {
    d.addEventListener('DOMContentLoaded', demarrer);
  } else {
    demarrer();
  }
})();
