document.addEventListener("DOMContentLoaded", () => {
    let radios = document.getElementsByName('type')

    let textForm = document.getElementById('text-form')
    let urlForm = document.getElementById('url-form')
    let vcardForm = document.getElementById('vcard-form')

    radios[0].addEventListener('click', () => {
        radios[1].checked = 'false'
        radios[2].checked = 'false'
        radios[0].checked = 'true'
        textForm.style.display = 'flex'
        urlForm.style.display = 'none'
        vcardForm.style.display = 'none'
    })
    radios[1].addEventListener('click', () => {
        radios[0].checked = 'false'
        radios[2].checked = 'false'
        radios[1].checked = 'true'
        textForm.style.display = 'none'
        urlForm.style.display = 'flex'
        vcardForm.style.display = 'none'
    })
    radios[2].addEventListener('click', () => {
        radios[0].checked = 'false'
        radios[1].checked = 'false'
        radios[2].checked = 'true'
        textForm.style.display = 'none'
        urlForm.style.display = 'none'
        vcardForm.style.display = 'flex'
    })
    radios[0].click()
})