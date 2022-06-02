var user= "JuanPablo";
var persona= {
    nombre: "Juancho",
    sexo: "Masculino"
}

var myObjeto={
    //Clave:valor
    nombre:"Juan",
    edad:"25",
    texto: `Usuario ${user}`,
    miFuncion: (a,b) => a + b,
    otroObjeto: persona
}

console.log(persona.nombre);
console.log(myObjeto.edad);
console.log(myObjeto.miFuncion(13,19));
console.log(myObjeto.otroObjeto.sexo);

var otraFuncion= (text,{otroObjeto}) => {
    console.log(otroObjeto.sexo)
    console.log(text)
}
otraFuncion(myObjeto.texto, myObjeto);