inputs = document.querySelectorAll('input')
labels = document.querySelectorAll('label')
container = document.getElementsByClassName('container')[0]

container.classList.add('justify-content-center')

for (input of inputs){
    if (input.type == 'checkbox'){
        input.classList.add('form-check-input')
        continue
    }
    if (input.type == 'submit'){
        input.classList.add('btn', 'btn-primary')
        continue
    }       
    input.classList.add('form-control')
}



for (label of labels){
    label.classList.add('form-label')
}




