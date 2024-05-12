let radios = document.getElementsByName('type')

let textForm = document.getElementById('text-form')
let urlForm = document.getElementById('url-form')
let vcardForm = document.getElementById('vcard-form')
let labelForm = document.getElementById('label-form')

radios[0].addEventListener('click', () => {
    textForm.style.display = 'flex'
    urlForm.style.display = 'none'
    vcardForm.style.display = 'none'
    labelForm.style.display = 'none'
    currentForm = textForm
})
radios[1].addEventListener('click', () => {
    textForm.style.display = 'none'
    urlForm.style.display = 'flex'
    vcardForm.style.display = 'none'
    labelForm.style.display = 'none'
    currentForm = urlForm
})
radios[2].addEventListener('click', () => {
    textForm.style.display = 'none'
    urlForm.style.display = 'none'
    vcardForm.style.display = 'flex'
    labelForm.style.display = 'none'
    currentForm = vcardForm
})
radios[3].addEventListener('click', () => {
    textForm.style.display = 'none'
    urlForm.style.display = 'none'
    vcardForm.style.display = 'none'
    labelForm.style.display = 'flex'
    currentForm = labelForm
})
radios[0].click()

const qr_rectangle = document.getElementById('qr_rectangle')
const link = document.getElementById('link')

async function generateQr(){
    const formData = new FormData(currentForm);
    formData.append('id', currentForm.id)

    const options = {
        method: "POST",
        body: formData
    };

    const response = await fetch("/api", options);

    if (response.ok){
        const data = await response.json()
        if(data['success']){
            qr_rectangle.innerHTML = `<img src= ${data['qr_img']} ></img>`
            link.innerHTML = `<a href= ${data['qr_img']} download>Download your QR</a>`
        }else{
            alert(data['message'])
        }

    } else {
        alert('please fill all the required (*) fields')
    }
}

document.addEventListener('keydown', (event) => {
    if(event.key == 'Enter'){
        event.preventDefault()
        generateQr()
    }
})