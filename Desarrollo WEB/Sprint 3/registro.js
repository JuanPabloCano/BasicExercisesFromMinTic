registros=[];
class Persona {
    constructor(tipo_documento, numero_documento, correo, contrasena) {
        this.tipo_documento = tipo_documento;
        this.numero_documento = numero_documento;
        this.correo = correo;
        this.contrasena = contrasena;
    }
}
function agregarRegistro() {
    var tipo_documento,
    element = document.getElementById('tipo-documento');
    if (element != null) {
        tipo_documento = element.value;
    }
    else {
        tipo_documento = null;
    };
    var numero_documento,
    element = document.getElementById('numero-documento');
    if (element != null) {
        numero_documento = element.value;
    }
    else {
        numero_documento = null;
    };
    var correo,
    element = document.getElementById('correo');
    if (element != null) {
        correo = element.value;
    }
    else {
        correo = null;
    };
    var contrasena,
    element = document.getElementById('contrasena');
    if (element != null) {
        contrasena = element.value;
    }
    else {
        contrasena = null;
    };

    var usuario = new  Persona(tipo_documento, numero_documento, correo, contrasena);
    registros.push(usuario);
    console.log(registros);
    return registros;
}

function filtrarCorreo(arreglo) {
    let filtrarCorreo = arreglo.filter((value)=>{
        return value.correo.includes("email.com")
    });
    console.log(filtrarCorreo);
    return filtrarCorreo;

}
function obtenerRegPasaporte (arreglo) {
    let registroPasaporte = arreglo.filter((usuario)=>{
        return usuario.tipo_documento === "P"
    });
    console.table(registroPasaporte);
    return registroPasaporte;
}


function ordenarArreglo(arreglo){
    let ordenar=obtenerRegPasaporte(arreglo);
    ordenar.sort(function(a, b){
    let x = a.numero_documento;
    let y = b.numero_documento;
    if (x < y) {
        return 1;
    }else if (x > y) {
        return -1;
    }else{
        return 0;
    }
    });
    console.table(ordenar);
    return ordenar;
}

module.exports.registros=registros;
module.exports.filtrarCorreo=filtrarCorreo;
module.exports.obtenerRegPasaporte=obtenerRegPasaporte;
module.exports.ordenarArreglo=ordenarArreglo;
module.exports.agregarRegistro=agregarRegistro;
