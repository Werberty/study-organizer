(() => {
    const forms = document.querySelectorAll('.form-delete');

    for (const form of forms) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const confirmed = confirm('Tem certeza?');

            if (confirmed) {
                form.submit();
            }
        })
    }
})();