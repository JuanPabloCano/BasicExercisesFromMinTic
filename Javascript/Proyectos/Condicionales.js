var variable= true;

if (variable){
    console.log("Es verdadero")
} else{
    console.log("Es falso")
}

var edad= 18;

if (edad >= 18 && edad <= 30){
    console.log("Joven adulto")
}else if (edad < 18){
    console.log("Niño o adolescente")
}else if (edad > 30 && edad <= 55){
    console.log("Adulto")
}else if (edad > 55){
    console.log("Anciano")
}else{
    console.log("Indefinido")
}

// Switch

var opcion= 1

switch (opcion) {
    case 1:
        console.log("Menú de usuario")
        break;
    case 2:
        console.log("Menú administrativo")
    default:
        console.log("Configuración")
        break;
}