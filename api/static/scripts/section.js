const sections = document.querySelectorAll('.content-section');

const fadeInOut = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
        } else {
            entry.target.classList.remove('fade-in');
        }
    });
};

const options = {
    root: null,
    rootMargin: '0px',
    threshold: 0.5
};

const observer = new IntersectionObserver(fadeInOut, options);

sections.forEach(section => {
    observer.observe(section);
});