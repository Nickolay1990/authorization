let post_button = document.querySelector('.button-for-post');
let input_name = document.querySelector('#id_name');
let password_button = document.querySelector('.password-show-button');
let input_password = document.querySelector('#id_password');
let input_password1 = document.querySelector('#id_password1');
let input_password2 = document.querySelector('#id_password2');
let password_inputs = []
password_inputs.push(input_password)
password_inputs.push(input_password1)
password_inputs.push(input_password2)

password_button.addEventListener('click', function(){
    for(let i of password_inputs){
        if(i){
            if(i.type == 'password'){
                i.type = 'text';
                }
            else if(i.type == 'text'){
                i.type = 'password';
            }}}});

post_button.addEventListener('click', function(){
    input_name.value = input_name.value.trim()
});