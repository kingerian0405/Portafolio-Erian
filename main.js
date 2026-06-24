document.addEventListener('DOMContentLoaded', () => {

    // ──────────────────────────────────────────────
    // 1. Custom Cursor Glow
    // ──────────────────────────────────────────────
    const cursor = document.querySelector('.cursor-glow');
    if (cursor) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top  = e.clientY + 'px';
        });
    }

    // ──────────────────────────────────────────────
    // 2. Scroll Reveal — aplica a TODAS las tarjetas
    // ──────────────────────────────────────────────
    // Solo tarjetas de proyecto y skills — NO timeline (son demasiado altas)
    const revealSelectors = [
        '.project-card',
        '.skill-card',
    ];

    const revealElements = document.querySelectorAll(revealSelectors.join(', '));

    revealElements.forEach((el, i) => {
        el.style.opacity    = '0';
        el.style.transform  = 'translateY(28px)';
        el.style.transition = `opacity 0.6s ease ${i * 0.1}s, transform 0.6s ease ${i * 0.1}s`;
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity   = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0, rootMargin: '0px 0px -30px 0px' });

    revealElements.forEach(el => observer.observe(el));

    // Timeline items: animación CSS simple via clase, no JS opacity blocker
    document.querySelectorAll('.timeline-item').forEach((el, i) => {
        el.style.animation = `fadeInUp 0.6s ease ${0.1 + i * 0.15}s both`;
    });

    // ──────────────────────────────────────────────
    // 3. Smooth scroll para nav links
    // ──────────────────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
            }
        });
    });

    // ──────────────────────────────────────────────
    // 4. Navbar compacta al hacer scroll
    // ──────────────────────────────────────────────
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.style.padding    = '1rem 0';
                navbar.style.background = 'rgba(5, 7, 10, 0.97)';
            } else {
                navbar.style.padding    = '1.5rem 0';
                navbar.style.background = 'rgba(5, 7, 10, 0.8)';
            }
        }, { passive: true });
    }

});
