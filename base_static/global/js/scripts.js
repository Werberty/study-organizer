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