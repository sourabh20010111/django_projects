const menuToggle = document.querySelector('.menu-toggle');
const links = document.querySelector('.links');

menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active'); // Animate hamburger to X
    links.classList.toggle('active');      // Show/hide menu
});

const messages = [
    "Sourabh Sonkar",
    "QA Enthusiast",
    "Manual & Automation Tester",
    "Passionate About Quality Software"
];

let i = 0;
let j = 0;
let currentMessage = '';
let isDeleting = false;
const dynamicText = document.getElementById('dynamicText');
const speed = 100; // typing speed

function type() {
    const fullText = messages[i];

    if (isDeleting) {
        currentMessage = fullText.substring(0, j--);
    } else {
        currentMessage = fullText.substring(0, j++);
    }

    dynamicText.textContent = currentMessage;

    if (!isDeleting && j === fullText.length + 1) {
        // Fade out and delete after delay
        setTimeout(() => {
            dynamicText.style.opacity = 0;
            setTimeout(() => {
                isDeleting = true;
                dynamicText.style.opacity = 1;
                type();
            }, 500); // fade duration
        }, 2000); // delay after typing complete (2 seconds)
    } else if (isDeleting && j === 0) {
        isDeleting = false;
        i = (i + 1) % messages.length;
        setTimeout(type, 1000); // delay before next message starts typing
    } else {
        setTimeout(type, speed);
    }
}

// Start typing
type();
