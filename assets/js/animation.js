// ==========================================
// SIGNATURE & MAGNIFIER ANIMATION
// ==========================================

document.addEventListener('DOMContentLoaded', function() {
    const magnifier = document.getElementById('magnifier');
    const signature = document.getElementById('signature');
    
    if (magnifier && signature) {
        // Animate magnifier position
        let position = 0;
        let direction = 1;
        
        function animateMagnifier() {
            position += direction * 0.5;
            
            // Reverse direction at boundaries
            if (position > 20 || position < -20) {
                direction *= -1;
            }
            
            magnifier.style.transform = `translate(${position}px, ${position * 0.5}px)`;
            requestAnimationFrame(animateMagnifier);
        }
        
        // Start animation
        animateMagnifier();
        
        // Add hover effect to signature
        signature.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        signature.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    }
});
