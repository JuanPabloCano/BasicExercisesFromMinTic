// Prueba de javascript
function multiplicar() {
    var s1= document.forms["form1"]["numero 1"].value;
    var s2= document.forms["form1"]["numero 2"].value;
    var result= parseInt(s1)*parseInt(s2);
    document.forms["form1"]["resultadoM"].value= result;
    //alert("La multiplicación es: "+ result);
}

function sumar() {
    var s1= document.forms["form1"]["numero 1"].value;
    var s2= document.forms["form1"]["numero 2"].value;
    var result= parseInt(s1) + parseInt(s2);
    document.forms["form1"]["resultadoS"].value= result;
}

function restar() {
    var s1= document.forms["form1"]["numero 1"].value;
    var s2= document.forms["form1"]["numero 2"].value;
    var result= parseInt(s1) - parseInt(s2);
    document.forms["form1"]["resultadoR"].value= result;
}

function dividir() {
    var s1= document.forms["form1"]["numero 1"].value;
    var s2= document.forms["form1"]["numero 2"].value;
    var result= parseInt(s1) / parseInt(s2);
    document.forms["form1"]["resultadoD"].value= result;
}