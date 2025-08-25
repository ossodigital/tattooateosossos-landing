
// Smooth scroll e highlight simples
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const id = a.getAttribute('href');
    if (id.length > 1) {
      e.preventDefault();
      document.querySelector(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      // fechar menu mobile
      navLinks.classList.remove('show');
    }
  });
});

// Navbar mobile
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');
navToggle?.addEventListener('click', () => navLinks.classList.toggle('show'));

// Atualiza ano do footer
document.getElementById('year').textContent = new Date().getFullYear();

// Validação básica do email no hero (extra – Netlify já valida também)
const emailHero = document.getElementById('emailHero');
emailHero?.addEventListener('invalid', () => {
  emailHero.setCustomValidity('Informe um e-mail válido');
});
emailHero?.addEventListener('input', () => emailHero.setCustomValidity(''));
