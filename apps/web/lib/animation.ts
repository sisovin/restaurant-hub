// Utility functions for animations and interactions

// Counter animation function
export function animateCounters() {
  const counters = document.querySelectorAll('[data-toggle="counter-up"]');
  if (!counters) return;

  counters.forEach(counter => {
    const target = parseInt(counter.textContent || '0', 10);
    const duration = 2000; // 2 seconds
    const increment = Math.ceil(target / (duration / 15)); // Update every 15ms
    let current = 0;

    const updateCount = () => {
      current += increment;
      if (current >= target) {
        counter.textContent = target.toString();
      } else {
        counter.textContent = current.toString();
        requestAnimationFrame(updateCount);
      }
    };

    updateCount();
  });
}

// Handle sticky navigation
export function handleStickyNav() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      navbar.classList.add('sticky-top');
      navbar.style.backgroundColor = 'rgba(17, 17, 17, 0.95)';
      navbar.style.transition = 'all 0.3s ease-in-out';
    } else {
      navbar.classList.remove('sticky-top');
      navbar.style.backgroundColor = '#111111';
    }
  });
}

// Handle back to top button
export function handleBackToTop() {
  const backToTop = document.querySelector('.back-to-top');
  if (!backToTop) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      backToTop.classList.add('show');
    } else {
      backToTop.classList.remove('show');
    }
  });

  backToTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// Handle team member hover effects
export function handleTeamHover() {
  const teamItems = document.querySelectorAll('.team-item');
  if (!teamItems.length) return;

  teamItems.forEach(item => {
    const overlay = item.querySelector('.team-overlay');
    if (!overlay) return;

    item.addEventListener('mouseenter', () => {
      overlay.style.opacity = '1';
      overlay.style.transition = 'all 0.5s ease';
    });

    item.addEventListener('mouseleave', () => {
      overlay.style.opacity = '0';
    });
  });
}
