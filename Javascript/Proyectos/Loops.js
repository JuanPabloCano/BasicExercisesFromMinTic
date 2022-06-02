//For

for (i=0; i < 10; i++){
    if (i == 1){
        console.log("Hola " + i+" vez")
    }else{
        console.log("Hola "+i+" veces")
    }
}

var myArray= ["Hola", 2020, "Adiós"]

for (let j = 0; j < myArray.length; j++) {
    const element = myArray[j];
    console.log(element);
}

//For con objetos

var miObjeto1={
    nombre: "Juan",
    edad: 25
}
var miObjeto2={
    nombre: "Carlos",
    edad: 26
}
var miObjeto3={
    nombre: "Andrea",
    edad: 35
}

var personas= [miObjeto1, miObjeto2, miObjeto3];

for (let z = 0; z < personas.length; z++) {
    const element = personas[z].nombre;
    console.log(element);
}

// ForEach
personas.forEach(element => console.log(element.edad));

// ForEach con segundo parámetro para identificar el índex del elemento
myArray.forEach((element,k) => {
    console.log(k);
    console.log(element);
})

// Hallar el número mayor de un arreglo
var array= [1,3,6,11,56,32,76,78,34,87];
var num;

for (i = 0; i < array.length; i++){
    if (array[i] < array[i+1]){
        num= array[i+1];
    }
}
console.log("El número mayor es: "+ num);

