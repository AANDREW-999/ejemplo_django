// Animación de aparición al hacer scroll
const revealElements = () => {
	const items = document.querySelectorAll('.reveal');
	const trigger = window.innerHeight * 0.85;
	items.forEach(el => {
		const top = el.getBoundingClientRect().top;
		if (top < trigger) {
			el.classList.add('reveal-visible');
		}
	});
};

window.addEventListener('scroll', revealElements);
window.addEventListener('load', revealElements);

// Botón volver arriba
const backToTop = document.getElementById('backToTop');
if (backToTop) {
	window.addEventListener('scroll', () => {
		if (window.scrollY > 400) backToTop.classList.add('show');
		else backToTop.classList.remove('show');
	});
	backToTop.addEventListener('click', () => {
		window.scrollTo({ top: 0, behavior: 'smooth' });
	});
}

// Focus visible polyfill simple
document.body.addEventListener('keydown', (e) => {
	if (e.key === 'Tab') document.documentElement.classList.add('user-tabbing');
});

// Realce de navegación activa según scroll
const navLinks = document.querySelectorAll('.navbar .nav-link[href^="#"]');
const sections = Array.from(navLinks).map(l => document.querySelector(l.getAttribute('href'))).filter(Boolean);

const setActiveLink = () => {
	const scrollPos = window.scrollY + 120; // offset navbar
	let currentId = null;
	sections.forEach(sec => {
		if (sec.offsetTop <= scrollPos) currentId = sec.id;
	});
	navLinks.forEach(a => {
		a.classList.toggle('active', a.getAttribute('href') === '#' + currentId);
	});
};
window.addEventListener('scroll', setActiveLink);
window.addEventListener('load', setActiveLink);

// Micro-animación al pasar sobre tarjetas
document.addEventListener('pointermove', (e) => {
	document.querySelectorAll('.neon-card').forEach(card => {
		const r = card.getBoundingClientRect();
		const x = e.clientX - r.left;
		const y = e.clientY - r.top;
		if (x > 0 && y > 0 && x < r.width && y < r.height) {
			card.style.setProperty('--mx', (x / r.width * 100).toFixed(2));
			card.style.setProperty('--my', (y / r.height * 100).toFixed(2));
			card.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(33,230,117,0.18), rgba(15,25,22,0.9) 60%)`;
		} else {
			card.style.background = '';
		}
	});
});

// Accesibilidad: añadir skip link dinámico si no existe
if (!document.getElementById('skipLink')) {
	const skip = document.createElement('a');
	skip.id = 'skipLink';
	skip.href = '#que-es';
	skip.textContent = 'Saltar al contenido';
	skip.style.position = 'fixed';
	skip.style.top = '-40px';
	skip.style.left = '1rem';
	skip.style.padding = '8px 14px';
	skip.style.background = 'var(--neon)';
	skip.style.color = '#00160a';
	skip.style.fontWeight = '600';
	skip.style.borderRadius = '6px';
	skip.style.transition = 'top .25s';
	skip.addEventListener('focus', () => skip.style.top = '10px');
	skip.addEventListener('blur', () => skip.style.top = '-40px');
	document.body.appendChild(skip);
}

