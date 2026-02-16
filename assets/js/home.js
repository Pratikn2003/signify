function scrollHome() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}

const toggle = document.getElementById("themeToggle");

toggle.addEventListener("click", () => {
    document.documentElement.classList.toggle("dark");
    toggle.classList.toggle("ri-sun-line");
});

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-menu a");

window.addEventListener("scroll", () => {
    const navbar = document.querySelector("nav");

    if (window.scrollY > 10) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

    let current = "";

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 200;
        if (window.scrollY >= sectionTop) {
            current = section.id;
        }
    });

    navLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }
    });
});

const scrollUp = document.getElementById("scrollUp");

window.addEventListener("scroll", () => {
    if (window.scrollY > 400) {
        scrollUp.classList.add("show");
    } else {
        scrollUp.classList.remove("show");
    }
});

// ==========================================
// CONTACT FORM HANDLER
// ==========================================

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form');
    
    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Get input values
            const nameInput = this.querySelector('input[type="text"]');
            const emailInput = this.querySelector('input[type="email"]');
            const messageInput = this.querySelector('textarea');
            
            const name = nameInput.value.trim();
            const email = emailInput.value.trim();
            const message = messageInput.value.trim();
            
            // Validation
            if (!name || !email || !message) {
                alert('Please fill all fields');
                return;
            }
            
            // Get submit button
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Show loading
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Sending...';
            
            try {
                // Send to Python backend
                // Use environment variable or fallback to localhost for development
                const apiUrl = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
                    ? 'http://localhost:5000/api/contact'
                    : '/api/contact';
                
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        name: name,
                        email: email,
                        message: message
                    })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    alert('✅ Message sent successfully! We will reply soon.');
                    
                    // Clear form
                    nameInput.value = '';
                    emailInput.value = '';
                    messageInput.value = '';
                } else {
                    alert('❌ Error: ' + data.message);
                }
                
            } catch (error) {
                alert('❌ Network error. Please make sure Python backend is running!');
                console.error('Error:', error);
            } finally {
                // Re-enable button
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalText;
            }
        });
    }
});
