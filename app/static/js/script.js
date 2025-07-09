// app/static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Cek jika sidebar state tersimpan di localStorage
        if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
            document.body.querySelector('#wrapper').classList.add('toggled');
        }

        sidebarToggle.addEventListener('click', function(event) {
            event.preventDefault();
            const wrapper = document.body.querySelector('#wrapper');
            wrapper.classList.toggle('toggled');
            
            // Simpan state sidebar ke localStorage
            localStorage.setItem('sb|sidebar-toggle', wrapper.classList.contains('toggled'));
        });
    }
});
