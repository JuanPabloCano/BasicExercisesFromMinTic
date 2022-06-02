var permitido= "Usuario permitido";
var miFuncion= acceso => acceso;

//Objeto para ingresar en el Array
var persona={
    nombre:"Juan",
    miAutomovil: [
        pintura= {
            marca: "Pintuco",
            precio: 20000,
            color: "Negro"
        },
        vendedor= {
            nombre: "Juancho",
            edad: 22
        }
    ]
}

var myArray= ["Juan", "Cano", 2021, [34,"Saldarriaga", 45], miFuncion(permitido), persona];
console.log(myArray);
console.log(myArray[3][1]); // Se accede al array seleccionado dentro del Array padre y a su índice
console.log(myArray[4]);
console.log(myArray[5].nombre);
console.log(myArray[5].miAutomovil[0]);
console.log(myArray[5].miAutomovil[1]);
console.log(myArray[5].miAutomovil[0].color);
console.log(myArray[5].miAutomovil[1].edad);


