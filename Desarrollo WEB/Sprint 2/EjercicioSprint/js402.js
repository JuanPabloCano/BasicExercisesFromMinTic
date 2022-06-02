//Forma sencilla de hacer los importes
// import { info } from "./js402form.js";
// console.log(info());

// import { info2} from "./js402form.js";
// console.log(info2());

// import { info3 } from "./js402form.js";
// console.log(info3());

//Forma simplificada
// import {info,info2,info3} from "./js402form.js";
// console.log(info());
// console.log(info2());
// console.log(info3());

//Forma de traer todos los datos
import * as datos from "./js402form.js";
import * as formulario from "./form.js";
console.log(datos.info());
console.log(datos.info2());
console.log(datos.info3());

document.forms['formulario']['usuario'].value= datos.info3();

document.forms['formulario']['usuario'].value= datos.nombres();

var tipod= "CC";
var docu= document.forms['formulario']['documento'].value;

var respuesta= formulario.checkNumDocumento(docu, tipod);
console.log(respuesta);