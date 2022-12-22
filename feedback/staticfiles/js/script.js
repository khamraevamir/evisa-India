let hidden_fields = document.querySelectorAll('.hidden_field')
for(let item of hidden_fields) {
    item.classList.add('is-hidden')
}
deactivate_radios = document.querySelectorAll('.deactivate_hidden')
activate_radios = document.querySelectorAll('.activate_hidden')

deactivate_radios.forEach(item => {
    item.addEventListener('click', (e)=> {
            let radio = e.target
            let parent = radio.parentElement.parentElement.parentElement
            let hidden_area = parent.querySelector('.hidden_field')
            for(let inp of hidden_area.querySelectorAll('input')){
                inp.setAttribute('required', '')
            }

            if (radio.checked) {
                hidden_area.classList.remove('is-hidden')
            }
        })
})

activate_radios.forEach(item => {
    item.addEventListener('click', (e)=> {
            let radio = e.target
            let parent = radio.parentElement.parentElement.parentElement
            let hidden_area = parent.querySelector('.hidden_field')

            for(let inp of hidden_area.querySelectorAll('input')){
                inp.removeAttribute('required')
                inp.value = ''
            }
            if (radio.checked) {
                hidden_area.classList.add('is-hidden')
            }
        })
})



