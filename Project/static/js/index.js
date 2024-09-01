//for the cards to scroll up and down animation

            document.addEventListener('DOMContentLoaded', function () {
            const cards = document.querySelectorAll('.fade-in');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        entry.target.classList.remove('hidden');
                    } else {
                        entry.target.classList.remove('visible');
                        entry.target.classList.add('hidden');
                    }
                });
            }, {
                threshold: 0.1
            });

            cards.forEach(card => {
                observer.observe(card);
            });
        });






//for the typewriter effect in the hero-section 

        document.addEventListener('DOMContentLoaded', function () {
        const words = ["Track","Search", "Filter","Manage"];
        let i = 0;
        const typewriterElement = document.querySelector('.typewriter');

        function typeEffect(word) {
            typewriterElement.textContent = '';
            let j = 0;
            const interval = setInterval(() => {
                typewriterElement.textContent += word[j];
                j++;
                if (j === word.length) {
                    clearInterval(interval);
                    setTimeout(() => {
                        eraseEffect();
                    }, 1500); // Pause before erasing
                }
            }, 150); // Typing speed
        }

        function eraseEffect() {
            let wordLength = typewriterElement.textContent.length;
            const interval = setInterval(() => {
                typewriterElement.textContent = typewriterElement.textContent.substring(0, wordLength - 1);
                wordLength--;
                if (wordLength === 0) {
                    clearInterval(interval);
                    i = (i + 1) % words.length;
                    typeEffect(words[i]);
                }
            }, 100); // Erasing speed
        }

        typeEffect(words[i]);
    });





//for the carousel scroll up and down in viewport
document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.carousel');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show-carousel');
            } else {
                entry.target.classList.remove('show-carousel');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(carousel);
});

