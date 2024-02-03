const toggle_header = document.getElementById('toggle_header');
toggle_header.addEventListener('click', function() {
    
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.toggle('green');
    } else {
        header.classList.toggle('red');
    }
});
