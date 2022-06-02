// console.log("Hello world") // Forma para imprimir en consola
// Var- variables globales
// Let- variables locales
// Const- variables inmutables

// var saludo= "Hola amigo"
// console.log(saludo)

// let nombre= "Juan"
// console.log(nombre)

// const PI= 3.14
// console.log(PI);

// Datos tipo string, enteros, decimales, booleanos, null, indefinido

// console.log(typeof nombre);


// Strings- algunos métodos

var nombre= "Juan"
var edad= 25
console.log(`Mi nombre es ${nombre} y tengo ${edad} años`)
console.log(nombre.toUpperCase())
console.log(nombre.toLowerCase())
console.log(nombre.length)

function name(){
    console.log(nombre);
}
// Operadores

// AND (&&), Or (||), XOR (^^), Distinto (!) Operadores lógicos
// +=, -=, *=, **=  Operadores artiméticos de asignación
// == Operador de comparación 
// === Operador de comparación de mismo valor y mismo tipo de variable
// != y !==

// Condicional ternario: condicion ? true : false
var edad= 16
var result= edad >= 18 ? console.log("Es mayor de edad") : console.log("Es menor de edad")

var a= "2"
var a1= 2
console.log(a == a)

var b= "2"
var b1= 2
console.log(b === b1)

console.log(a1 **= 3) 


// Funciones- Conjunto de instrucciones que realizan una tarea

function saludo() {
    console.log("Hola a todos")
}

function oper(a,b) {
    return a * b
}

saludo()
console.log(oper(4,6))


// Funciones de flecha Arrow

var acceso=true;
var nivel= "alto";

// var accesoU= function(a){
//     return a
// }

var accesoU= a => a  // Arrow function, es lo mismo que el comentario de arriba, retorna un valor
// Sintáxis:
// var accesoU () => "Valor a retornar". Los parentesis se usan cuando no hay parámetros o cuando hay más de 1

accesoU(acceso) == true
? console.log("Acceso permitido"): console.log("Usuario denegado"); //Condicional ternario

var accesoA= (le, n) => console.log(`Usuario ${n} nivel ${le}`) //Arrow function con más de 1 parámetro
accesoA(nivel, "Juan");


