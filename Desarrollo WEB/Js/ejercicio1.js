function subtotalR() {
    var sub1= document.forms["formPro"]["valor"].value;
    var sub2= document.forms["formPro"]["cantidad"].value
    var subTo= parseInt(sub1) * parseInt(sub2);
    return subTo;
}

function ivaR(){
    var iva_P= document.forms["formPro"]["valor"].value;
    var res_iva= parseInt(iva_P) * 0.19;
    return res_iva;
}

function totalR() {
    var t1= subtotalR();
    var i1= ivaR();
    var result= t1 + i1;
    document.forms["formPro"]["iva"].value= i1;
    document.forms["formPro"]["subtotal"].value=t1;
    document.forms["formPro"]["total"].value=result;

}
