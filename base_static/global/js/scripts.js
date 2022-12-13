(() => {
    const forms = document.querySelectorAll('.form-delete');

    for (const form of forms) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const confirmed = confirm('Deseja deletar?');

            if (confirmed) {
                form.submit();
            }
        })
    }
})();

(() => {
    let userDropdown = document.querySelector('.user-dropdown');
    let navbar = document.querySelector('.navbar');
    let arrowDropDown = document.querySelector('.arrow_drop_down'); 

    userDropdown.onclick = function(){
        navbar.classList.toggle('active')
        arrowDropDown.classList.toggle('active')
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

