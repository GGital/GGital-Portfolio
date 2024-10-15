// Typing Animation
const texts = ['a Web Developer.', 'a Designer.', 'a Creative Thinker.'];
let count = 0;
let index = 0;
let currentText = '';
let letter = '';

document.addEventListener('DOMContentLoaded', () => {
  const animateElements = document.querySelectorAll('.animate-element');
  let lastScrollTop = window.pageYOffset || document.documentElement.scrollTop;
  let staggerDelay = 100; // Delay between each element's animation
  
  const observerCallback = (entries, observer) => {
      let delay = 0;
      const currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;
      const isScrollingDown = currentScrollTop > lastScrollTop;
      lastScrollTop = currentScrollTop;
      
      entries.forEach(entry => {
          const element = entry.target;
          
          if (entry.isIntersecting) {
              // Remove both classes and add the appropriate one
              element.classList.remove('slide-up', 'slide-down');
              element.classList.add(isScrollingDown ? 'slide-down' : 'slide-up');
              
              setTimeout(() => {
                  element.classList.add('visible');
              }, delay);
              delay += staggerDelay;
          } else {
              // Reset the element when it's out of view
              element.classList.remove('visible');
          }
      });
  };

  const observer = new IntersectionObserver(observerCallback, {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
  });

  animateElements.forEach(element => {
      observer.observe(element);
  });
});

// Bubble animation code
function createBubble() {
  const bubble = document.createElement('img');
  bubble.src = "/static/moodeng.png"; // Using placeholder as per instructions
  bubble.classList.add('bubble');
  document.body.appendChild(bubble);

  // Random starting position
  const startX = Math.random() * window.innerWidth;
  const startY = window.innerHeight + 100; // Start below the viewport

  // Random movement parameters
  const floatDuration = 5000 + Math.random() * 5000; // 5-10 seconds
  const horizontalMovement = Math.random() * 100 - 50; // -50 to 50 pixels

  // Set initial position
  bubble.style.left = `${startX}px`;
  bubble.style.top = `${startY}px`;

  // Animate the bubble
  const startTime = Date.now();
  
  function animateBubble() {
      const elapsed = Date.now() - startTime;
      const progress = elapsed / floatDuration;

      if (progress >= 1) {
          bubble.style.opacity = '0';
          setTimeout(() => {
              document.body.removeChild(bubble);
          }, 500);
          return;
      }

      const currentY = startY - (window.innerHeight + 200) * progress;
      const currentX = startX + Math.sin(progress * 4 * Math.PI) * horizontalMovement;

      bubble.style.transform = `translate(${currentX - startX}px, ${currentY - startY}px)`;

      requestAnimationFrame(animateBubble);
  }

  requestAnimationFrame(animateBubble);
}

// Create new bubbles periodically
setInterval(createBubble, 1000);

(function type() {
  if (count === texts.length) {
    count = 0;
  }
  currentText = texts[count];
  letter = currentText.slice(0, ++index);

  document.querySelector('.typed-text').textContent = letter;
  if (letter.length === currentText.length) {
    count++;
    index = 0;
    setTimeout(type, 2000); // Pause before typing next text
  } else {
    setTimeout(type, 100);
  }
})();
