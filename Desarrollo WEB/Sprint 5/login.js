let registros= [
    {
      correo: 'carlos@gmail.com',
      contrasena: 'SecurePassword123'
    }
  ];
function login(){
    console.log(registros);
    var emaillogin=document.getElementById('form-login').elements[0].value;
    var contrasenalogin=document.getElementById('form-login').elements[1].value;
    var captcha=element =document.getElementById('form-login').elements[2].value;
    console.log(contrasenalogin);
    console.log(emaillogin);
    console.log(captcha);
    var correos = registros.map(el => el.correo);
    console.log(correos);
    var booleano = correos.includes(emaillogin);
    console.log(booleano)
    var index = correos.indexOf(emaillogin);
    console.log(index)
    var contrasenas = registros.map(el => el.contrasena);
    console.log(contrasenas)
    var contrasenaaway = contrasenas[index];
    console.log(contrasenaaway)
    if (booleano==true)  {
        if(contrasenaaway==contrasenalogin){    
            let validar = validarCAPTCHA(captcha);
            if (validar == true) {
                console.log('True Validacion');
                return false;

            } else {
                console.log('False validacion');
                return true;

            }
        }else{
            console.log('False Correo');
            return true;  
        }
    }
    else {
        console.log('False correo');
        return true;
    }
}
function agregarRegistro(){
    var usuario, correo, contrasena;
    numdoc = document.getElementById('usuario');
    if (numdoc != null) {
        usuario = numdoc.value;
    } else {
        usuario = '';
    }
    email = document.getElementById('correo');
    if (email != null) {
        correo = email.value;
    } else {
        correo = '';
    }
    contra = document.getElementById('contrasena');
    if (contra != null) {
        contrasena = contra.value;

    } else {
        contrasena = '';
    }
    let user = [usuario, correo, contrasena];
    registros.push(user);
    
}
 function validarCAPTCHA(valor){
    if (valor == 15){
        return true;
    }
    return false;
 }

 module.exports = { registros, login, agregarRegistro, validarCAPTCHA };