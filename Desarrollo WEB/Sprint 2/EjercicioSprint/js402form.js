export function info(){
    return "Pepito"
}

export function info2(){
    return "Juanita"
}

export function info3(){
    var apellido= info4();
    return "Juan " + apellido;
}

function info4() {
    var ape="Cano";
    return ape;
}

export let nombres= "Juan Cano";

//Forma para exportar
export {info3,info,info2};