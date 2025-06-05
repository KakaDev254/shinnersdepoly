/*  scripts.js  |  loaded in base.html  */

/* ---------- 1.  AOS (Animate-On-Scroll) ---------- */
AOS.init({
  duration: 1000,   // animation length in ms
  once: true        // animate only the first time you scroll to an element
});

/* ---------- 2.  Back-to-Top button ---------- */
const backToTopBtn = document.getElementById('backToTopBtn');

window.addEventListener('scroll', () => {
  const scrolled = document.documentElement.scrollTop || document.body.scrollTop;
  backToTopBtn.style.display = scrolled > 200 ? 'block' : 'none';
});

backToTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

/* ---------- 3.  Navbar toggler icon  (hamburger ➜ X) ---------- */
const toggler = document.querySelector('.navbar-toggler');

toggler.addEventListener('click', function () {
  this.classList.toggle('collapsed');           // for your custom “no-border” CSS
  // Change icon to “X” by toggling a class on the inner <span>
  const icon = this.querySelector('.navbar-toggler-icon');
  icon.classList.toggle('bx');                  // give it boxicons’ base class
  icon.classList.toggle('bx-x');                // …and the “X” glyph
});

/* ---------- 4.  Auto-collapse navbar after link click (mobile) ---------- */
const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    const navbar = document.getElementById('navbarNav');
    if (window.getComputedStyle(toggler).display !== 'none' && navbar.classList.contains('show')) {
      toggler.click();   // programmatically close
    }
  });
});
