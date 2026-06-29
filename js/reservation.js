/* ============================================
   LUMIA — Wizard de réservation (vanilla, fetch)
   Mode LIVE (prod : appels PHP) + mode DÉMO (GitHub Pages : données fictives).
   ============================================ */
(function () {
  'use strict';
  var API = 'api/';
  var IS_DEMO = !/(^|\.)lumia-salon\.fr$/.test(location.hostname); // prod = lumia-salon.fr
  var MONTHS = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'];
  var DOW = ['Lun','Mar','Mer','Jeu','Ven','Sam','Dim'];
  var state = { csrf: '', service: null, date: null, slot: null, monthOffset: 0 };
  var $ = function (s) { return document.querySelector(s); };
  var errBox = $('#b-error');

  // ---- Données de démonstration (extrait réel des prestations) ----
  var DEMO_SERVICES = { categories: [
    { category: 'Épilation laser', services: [
      { id: 1, name: 'Bilan / diagnostic épilation laser', duration_min: 30, price_cents: 2000, requires_bilan: false, is_bilan: true },
      { id: 2, name: 'Lèvre supérieure', duration_min: 15, price_cents: 3900, requires_bilan: true, is_bilan: false },
      { id: 3, name: 'Aisselles', duration_min: 20, price_cents: null, requires_bilan: true, is_bilan: false },
      { id: 4, name: 'Maillot', duration_min: 30, price_cents: null, requires_bilan: true, is_bilan: false },
      { id: 5, name: 'Barbe (homme)', duration_min: 30, price_cents: 11000, requires_bilan: true, is_bilan: false } ] },
    { category: 'Soins du visage', services: [
      { id: 6, name: 'LUMINEA Découverte', duration_min: 75, price_cents: 9500, requires_bilan: false, is_bilan: false },
      { id: 7, name: 'Soin anti-âge + LED', duration_min: 60, price_cents: 9500, requires_bilan: false, is_bilan: false },
      { id: 8, name: 'Séance LED visage', duration_min: 20, price_cents: 3500, requires_bilan: false, is_bilan: false } ] },
    { category: 'LPG endermologie', services: [
      { id: 9, name: 'Anti-cellulite', duration_min: 30, price_cents: 6000, requires_bilan: false, is_bilan: false },
      { id: 10, name: 'Détox drainant', duration_min: 35, price_cents: 7000, requires_bilan: false, is_bilan: false } ] },
    { category: 'Soins Cosmelan', services: [
      { id: 11, name: 'Diagnostic de peau Cosmelan', duration_min: 30, price_cents: 2000, requires_bilan: false, is_bilan: true },
      { id: 12, name: 'Soin cabine Cosmelan', duration_min: 45, price_cents: 65000, requires_bilan: false, is_bilan: false } ] }
  ] };

  function demoSlots(date) {
    var d = new Date(date + 'T00:00:00'); var wd = d.getDay();
    if (wd === 0 || wd === 6) return [];                 // fermé week-end
    var seed = 0, s = date.replace(/-/g, '');
    for (var i = 0; i < s.length; i++) seed = (seed * 31 + s.charCodeAt(i)) % 997;
    var out = [];
    for (var h = 10; h < 19; h++) {
      ['00', '30'].forEach(function (m, k) {
        if (h === 18 && m === '30') return;
        seed = (seed * 7 + h * 3 + k) % 101;
        if (seed % 10 < 6) out.push(String(h).padStart(2, '0') + ':' + m); // ~60% libres, déterministe
      });
    }
    return out;
  }

  // ---- Source de données (bascule live/démo) ----
  var DS = {
    services: function () {
      return IS_DEMO ? Promise.resolve(DEMO_SERVICES)
        : fetch(API + 'services.php').then(function (r) { if (!r.ok) throw 0; return r.json(); });
    },
    availability: function (id, date) {
      return IS_DEMO ? Promise.resolve({ slots: demoSlots(date) })
        : fetch(API + 'availability.php?service_id=' + id + '&date=' + date).then(function (r) { return r.json(); });
    },
    book: function (payload) {
      if (IS_DEMO) return Promise.resolve({ code: 200, j: { ok: true, demo: true } });
      return fetch(API + 'book.php', { method: 'POST', credentials: 'same-origin',
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json().then(function (j) { return { code: r.status, j: j }; }); });
    }
  };

  function showError(msg) { errBox.textContent = msg; errBox.style.display = 'block'; errBox.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
  function clearError() { errBox.style.display = 'none'; }

  function setStep(n) {
    clearError();
    document.querySelectorAll('.b-step').forEach(function (el) { el.classList.remove('active'); });
    $('#step-' + n).classList.add('active');
    document.querySelectorAll('.steps li').forEach(function (li) {
      var s = +li.dataset.step; li.classList.toggle('active', s === n); li.classList.toggle('done', s < n);
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function priceLabel(c) { return c == null ? 'sur bilan' : (c / 100).toLocaleString('fr-FR') + ' €'; }
  function durLabel(m) { return m >= 60 ? (Math.floor(m / 60) + 'h' + (m % 60 ? String(m % 60).padStart(2, '0') : '')) : m + ' min'; }
  function esc(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }

  // ---- Bandeau démo ----
  if (IS_DEMO) {
    var b = document.createElement('div');
    b.style.cssText = 'background:#F7EEE8;border:1px solid #A63524;color:#87291B;border-radius:6px;padding:.75rem 1rem;margin-bottom:1.5rem;font-size:.9rem;text-align:center';
    b.innerHTML = '<strong>Démonstration</strong> — exemple de réservation en ligne LUMIA. Aucune donnée réelle n\'est enregistrée.';
    var host = $('.booking'); host.insertBefore(b, host.firstChild);
  } else {
    fetch(API + 'csrf.php', { credentials: 'same-origin' }).then(function (r) { return r.json(); })
      .then(function (j) { state.csrf = j.csrf || ''; }).catch(function () {});
  }

  // ---- Init services ----
  DS.services().then(renderServices).catch(function () {
    $('#svc-list').innerHTML = '<p class="b-note">Réservation momentanément indisponible. Appelez le 04 92 87 63 72.</p>';
  });

  function renderServices(data) {
    var wrap = $('#svc-list'); wrap.innerHTML = '';
    (data.categories || []).forEach(function (cat) {
      var block = document.createElement('div'); block.className = 'svc-cat';
      var h = document.createElement('h3'); h.textContent = cat.category; block.appendChild(h);
      cat.services.forEach(function (s) {
        var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'svc';
        var left = document.createElement('span'); left.textContent = s.name;
        var meta = document.createElement('span'); meta.className = 'svc-meta'; meta.textContent = durLabel(s.duration_min) + ' · ' + priceLabel(s.price_cents);
        btn.appendChild(left); btn.appendChild(meta);
        btn.addEventListener('click', function () { selectService(s); });
        block.appendChild(btn);
      });
      wrap.appendChild(block);
    });
  }

  function selectService(s) {
    state.service = s; state.date = null; state.slot = null; state.monthOffset = 0;
    $('#sum-2').innerHTML = '<strong>' + esc(s.name) + '</strong> · ' + durLabel(s.duration_min) + ' · ' + priceLabel(s.price_cents);
    $('#bilan-note').innerHTML = s.requires_bilan
      ? '<div class="callout"><p>Un <strong>bilan/diagnostic est obligatoire avant la 1ère séance</strong> (offert pour tout achat de séance ou de cure).</p></div>' : '';
    $('#slots-wrap').innerHTML = '';
    renderCalendar(); setStep(2);
  }

  function renderCalendar() {
    var base = new Date(); base.setDate(1); base.setMonth(base.getMonth() + state.monthOffset);
    var year = base.getFullYear(), month = base.getMonth();
    $('#cal-label').textContent = MONTHS[month] + ' ' + year;
    $('#cal-prev').disabled = state.monthOffset <= 0; $('#cal-next').disabled = state.monthOffset >= 1;
    var grid = $('#cal-grid'); grid.innerHTML = '';
    DOW.forEach(function (d) { var c = document.createElement('div'); c.className = 'dow'; c.textContent = d; grid.appendChild(c); });
    var first = new Date(year, month, 1);
    var startCol = (first.getDay() + 6) % 7;
    var daysInMonth = new Date(year, month + 1, 0).getDate();
    var today = new Date(); today.setHours(0, 0, 0, 0);
    for (var i = 0; i < startCol; i++) { var e = document.createElement('div'); e.className = 'cal-day empty'; grid.appendChild(e); }
    for (var day = 1; day <= daysInMonth; day++) {
      var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'cal-day'; btn.textContent = day;
      var dd = new Date(year, month, day); dd.setHours(0, 0, 0, 0);
      var iso = year + '-' + String(month + 1).padStart(2, '0') + '-' + String(day).padStart(2, '0');
      if (dd < today) btn.disabled = true;
      else btn.addEventListener('click', (function (isoDate, el) { return function () {
        grid.querySelectorAll('.cal-day.sel').forEach(function (x) { x.classList.remove('sel'); });
        el.classList.add('sel'); state.date = isoDate; loadSlots(isoDate);
      }; })(iso, btn));
      grid.appendChild(btn);
    }
  }
  $('#cal-prev').addEventListener('click', function () { if (state.monthOffset > 0) { state.monthOffset--; renderCalendar(); } });
  $('#cal-next').addEventListener('click', function () { if (state.monthOffset < 1) { state.monthOffset++; renderCalendar(); } });

  function loadSlots(date) {
    var wrap = $('#slots-wrap'); wrap.innerHTML = '<p class="b-note">Recherche des créneaux…</p>';
    DS.availability(state.service.id, date).then(function (j) {
      var slots = j.slots || [];
      if (!slots.length) { wrap.innerHTML = '<p class="b-note">Aucun créneau disponible ce jour. Choisissez une autre date.</p>'; return; }
      wrap.innerHTML = '<p class="b-note">Créneaux du ' + new Date(date + 'T00:00:00').toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' }) + ' :</p>';
      var g = document.createElement('div'); g.className = 'slots';
      slots.forEach(function (hm) {
        var bt = document.createElement('button'); bt.type = 'button'; bt.className = 'slot'; bt.textContent = hm;
        bt.addEventListener('click', function () { selectSlot(hm); });
        g.appendChild(bt);
      });
      wrap.appendChild(g);
    }).catch(function () { wrap.innerHTML = '<p class="b-note">Erreur de chargement. Réessayez.</p>'; });
  }

  function selectSlot(hm) {
    state.slot = hm;
    var d = new Date(state.date + 'T00:00:00').toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
    $('#sum-3').innerHTML = '<strong>' + esc(state.service.name) + '</strong><br>' + d + ' à ' + hm;
    setStep(3);
  }

  $('#b-form').addEventListener('submit', function (e) {
    e.preventDefault(); clearError();
    var f = e.target;
    if (!f.consent.checked) { showError('Merci d\'accepter la politique de confidentialité.'); return; }
    var btn = $('#b-submit'); btn.disabled = true; btn.textContent = 'Envoi en cours…';
    var payload = { service_id: state.service.id, start: state.date + ' ' + state.slot,
      first: f.first.value.trim(), last: f.last.value.trim(), email: f.email.value.trim(),
      phone: f.phone.value.trim(), message: f.message.value.trim(), consent: true, website: f.website.value, csrf: state.csrf };
    DS.book(payload).then(function (res) {
      btn.disabled = false; btn.textContent = 'Confirmer le rendez-vous';
      if (res.code === 200 && res.j.ok) {
        $('#done-msg').innerHTML = esc(state.service.name) + '<br>le ' + esc(new Date(state.date + 'T00:00:00').toLocaleDateString('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' })) + ' à ' + esc(state.slot)
          + (res.j.demo ? '<br><span class="b-note">(démonstration — rien n\'a été enregistré)</span>' : '');
        setStep(4); return;
      }
      if (res.code === 409) { showError('Ce créneau vient d\'être réservé. Choisissez-en un autre.'); setStep(2); loadSlots(state.date); return; }
      showError(res.j.error || 'Une erreur est survenue. Réessayez.');
    }).catch(function () { btn.disabled = false; btn.textContent = 'Confirmer le rendez-vous'; showError('Erreur réseau. Réessayez ou appelez le 04 92 87 63 72.'); });
  });

  document.querySelectorAll('[data-goto]').forEach(function (b) { b.addEventListener('click', function () { setStep(+b.dataset.goto); }); });
})();
