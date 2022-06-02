const login = require('./login.js');
let usuario1 = {
    tipodocumento: 'CC',
    numerodocumento: '10121212',
    correo: 'u1@u.com',
    contrasena: 'scdwcd5657'
}
let usuario2 = {
    tipodocumento: 'CE',
    numerodocumento: '12121212',
    correo: 'u2@u.com',
    contrasena: 'scdwcd5658'
}

login.registros = [ // se lleno el arreglo con 2 usuarios
    usuario1, usuario2
]
login.Login();