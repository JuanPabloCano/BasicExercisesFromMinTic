import * as datos from "./form";

//Validar tipo y número de documento
var tipoD= document.forms["form-registro"]["tipoDocumento"].value;
var documento= document.forms["form-registro"]["n-documento"].value;
console.log(tipoD);
console.log(documento)
var validarTd= datos.checkNumDocumento(documento, tipoD);
console.log(validarTd);

//Validar Email
var email= document.forms["form-registro"]["correo"].value;
var validarCorreo= datos.checkCorreo(email);
console.log(validarCorreo);


//Validar contraseña
var contra= document.forms["form-registro"]["contrasena"].value;
var validarContra= datos.checkContrasena(contra);
console.log(validarContra);