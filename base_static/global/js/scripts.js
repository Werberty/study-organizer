(() => {
    const forms = document.querySelectorAll('.form-delete');

    for (const form of forms) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const confirmed = confirm('Quer deletar mesmo?');

            if (confirmed) {
                form.submit();
            }
        })
    }
})();

(() => {
    let userDropdown = document.querySelector('.user-dropdown');
    let navbarNav = document.querySelector('.navbar-nav');

    userDropdown.onclick = function(){
        navbarNav.classList.toggle('active')
    }
})();

$(document).ready(function() {
    // Abrir a modal e fechar
    loading();

    function loading() {
        setTimeout(function() {
            $('.message').fadeOut(500);
        }, 3000);
    };
})

