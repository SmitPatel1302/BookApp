// Javascript to make navbar stickey on scroll at top
document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            document.getElementById('base_navbar').classList.add('fixed-top');
            document.getElementById('base_navbar').classList.add('bg-dark');
            document.getElementById('base_navbar').classList.remove('navbar_fix_top');

            // add padding top to show content behind navbar
            navbar_height = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';

        } else if (window.scrollY < 50) {
            document.getElementById('base_navbar').classList.remove('fixed-top');
            document.getElementById('base_navbar').classList.remove('bg-dark');
            document.getElementById('base_navbar').classList.add('navbar_fix_top');

            document.body.style.paddingTop = '0'
        } else {
            document.getElementById('base_navbar').classList.remove('fixed-top');
            // remove padding top from body
            document.body.style.paddingTop = '0';
        }
    });
});