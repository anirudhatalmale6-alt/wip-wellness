/* Work in Progress Wellness — interactions
   Vanilla JS, no dependencies. Safe to edit. */
(function () {
  'use strict';

  /* ---- Header: solid background once scrolled ------------------------- */
  var header = document.querySelector('.site-header');
  var menuOpen = function () { return document.body.classList.contains('menu-open'); };
  var onScroll = function () {
    if (!header) { return; }
    // While the menu is open the header always sits on the light panel, so it
    // must drop its over-image (dark) styling regardless of scroll position.
    header.classList.toggle('is-solid', menuOpen() || window.scrollY > 24);
  };
  if (header) {
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Mobile menu ----------------------------------------------------- */
  var burger = document.querySelector('.burger');
  if (burger) {
    var setMenu = function (open) {
      document.body.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
      onScroll();
    };
    burger.addEventListener('click', function () { setMenu(!menuOpen()); });
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menuOpen()) { setMenu(false); burger.focus(); }
    });
  }

  /* ---- Reveal on scroll ------------------------------------------------ */
  var targets = document.querySelectorAll('[data-reveal]');
  if (!('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (el) { io.observe(el); });
  }

  /* ---- Contact form ----------------------------------------------------
     No back end is wired up yet, so the form opens the visitor's mail app
     with everything pre-filled. Swap the handler for a real endpoint
     (Formspree, Hostinger PHP mail, etc.) when you're ready.          */
  var form = document.querySelector('[data-mailto-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input').value) { return; }  // honeypot

      var get = function (n) {
        var el = form.elements[n];
        return el ? el.value.trim() : '';
      };
      var to = form.getAttribute('data-mailto-form');
      var subject = 'Website enquiry — ' + (get('name') || 'New message');
      var body = [
        'Name: ' + get('name'),
        'Phone: ' + get('phone'),
        'Email: ' + get('email'),
        'Best way to reach me: ' + get('contact_pref'),
        'Interested in: ' + get('topic'),
        '',
        get('message')
      ].join('\n');

      window.location.href = 'mailto:' + to +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);

      var status = form.querySelector('[data-form-status]');
      if (status) {
        status.textContent =
          'Your email app should now be open with the message ready to send. ' +
          'If nothing happened, please email or call directly using the details above.';
      }
    });
  }

  /* ---- Current year in footer ------------------------------------------ */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
