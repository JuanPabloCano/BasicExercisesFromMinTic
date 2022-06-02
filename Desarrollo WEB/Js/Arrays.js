var array= ["Carro", "Moto", "Camión", "Bicicleta"];

for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}

array.forEach(function(elemento, indice){
    console.log(elemento, indice);
})

var llamado= require('./prueba_array');

llamado.add("casa", "hotel", "carro", "camión");
llamado.add2("Gato");
llamado.add2("Perro");

console.log("Arreglo: ", llamado.array);
console.log("Arreglo: ", llamado.array2);