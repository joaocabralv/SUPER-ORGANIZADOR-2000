// Adicionando novas tarefas de forma dinâmica.

let count = 0

document.getElementById('button-new').addEventListener('click', function () {
    count++;

    // Criar o elemento form e atribuir à variável form.
    const form = document.createElement('form');
    form.id = 'form-checkbox-' + count;
    form.action = '/principal'
    form.method = 'POST'

    // Criar o elemento input e atribuir à variável check.
    const check = document.createElement('input')
    check.id = 'checkbox-' + count
    check.classList.add('checkbox')
    check.name = 'checkbox-' + count
    check.type = 'checkbox'
    check.checked = false

    // Criar o elemento div e atribuir à variável checkBoxWrapper.
    const checkBoxWrapper = document.createElement('div')
    checkBoxWrapper.classList.add('check-box-wrapper')

    // Criar o elemento span e atribuir à variável mark
    const mark = document.createElement('span')
    mark.classList.add('check-box-mark')

    checkBoxWrapper.append(check, mark)

    // Criar o elemento textarea e atribuir à variável textArea.
    const textArea = document.createElement('textarea')
    textArea.id = 'text-note-' + count
    textArea.name = 'text-note-' + count
    textArea.classList.add('text-note')
    textArea.placeholder = '...'
    textArea.setAttribute('required', true)

    // Criar o elemento button e atribuir à variável confirmButton.
    const confirmButton = document.createElement('button')
    confirmButton.id = 'confirm-button-' + count
    confirmButton.name = 'confirm-button-' + count
    confirmButton.classList.add('confirm-button')
    confirmButton.type = 'submit'
    confirmButton.textContent = 'SALVAR'

    // Criar o elemento div e atribuir à variável divRow.
    const divRow = document.createElement('div')
    divRow.classList.add('check-row')
    divRow.appendChild(checkBoxWrapper)
    divRow.appendChild(textArea)
    divRow.appendChild(confirmButton)

    form.appendChild(divRow)

    // Criar o elemento div e atribuir à variável checkDiv.
    const checkDiv = document.createElement('div')
    checkDiv.classList.add('check-div')
    checkDiv.appendChild(form)

    document.getElementById('check-flex').appendChild(checkDiv)

    // Salvar a página sem recarregar para manter múltiplas tarefas anotadas.
    form.addEventListener('submit', function (e) {
        e.preventDefault()

        const formData = new FormData(form)

        fetch('/principal', {
            method: 'POST',
            body: formData
        })

            .then(resp => resp.text())

    })
})
