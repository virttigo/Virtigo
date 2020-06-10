const first_name = document.getElementById('first_name')
const last_name = document.getElementById('last_name')
const user_name = document.getElementById('user_name')
const email = document.getElementById('email')
const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')
const contactForm = document.getElementById('contactForm')
const errorElement = document.getElementById('error')
const errorElement1 = document.getElementById('error1')

contactForm.addEventListener('submit', (e) => {
    let messages = []
    if(first_name.value === '' || first_name.value == null) {
        messages.push('Name is required !!!')
    }
    if(password1.value.length <= 8) {
        messages.push('Secured password should be greater than 8 characters !!!')

    }
    if(password1.value !== password2.value) {
        messages.push('Passwords do not match !!!')
    }
    if (messages.length > 0)  {
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
   

})