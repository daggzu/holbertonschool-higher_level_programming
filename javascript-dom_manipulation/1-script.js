
const red_header = document.getElementById('red_header');

// Liaten to click 
red_header.addEventListener('click', function() {
    // Change the header's text color to red.
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
    });
