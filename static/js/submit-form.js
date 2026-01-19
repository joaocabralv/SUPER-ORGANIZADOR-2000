const form = document.getElementById('form-to-submit')

form.addEventListener('submit', function (e) {
    e.preventDefault()

    const formData = new FormData(form)

    fetch(form.action, {
        method: 'POST',
        body: formData,
        redirect: 'manual'
    })

    fetch(form.action, {
        method: 'POST',
        body: formData
    })
        .then(resp => resp.json())
        .then(data => {
            if (!data.ok) {
                alert(data.error)
                return
            }
            window.location.href = data.redirect
        })

})
