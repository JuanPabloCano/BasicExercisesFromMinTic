package OOP;

public class POO {
    /* Paradigma de programación que busca descomponer el código en fragmentos simples y fáciles de codificar
    // Clase, objeto, instancia, atributo, método

    Clase avión= comercial, guerra, carga- La clase es como un molde, formato, plantilla que tiene atributos y forman un objeto
    Objeto= es una entidad que posee identidad (nombre), caracteristicas(atributos) y comportamientos(métodos)
    Instancia= es una ocurrencia de la clase, ejemplo. Placas de los vehiculos (hijos)

    El método constructor se encarga de asignar valores iniciales a los parámetros privados de la clase, solo se utiliza 1 vez y se modifica usando método Set()

    El nombre del constructor siempre es el mismo nombre de la clase

    Los atributos son representados como variables

    Encapsulamiento: Proceso para ocultar los atributos y métodos de una clase para proteger los datos de modificaciones incontroladas. El comportamiento y los atributos de un objeto no deben de ser alterados.
    Para hacer esto, se definen los atributos y métodos como privados, con Set y Get

    Set: Se establecen o asignan valores a los atributos encapsulados en una clase
    Get: Obtiene o retorna el valor de un atributo encapsulado. No recibe parámetros

    CONSTRUCTOR:

    Es un método especial dentro de la clase
    Se encarga de asignar valores iniciales a los parámetros privados de la clase

    Visibilidad nombreConstructor(Parémetro){
        atributoPrivado = Parámetro
    }

El nombre del constructor debe de ser el mismo nombre de la clase


La palabra Super sirve para acceder a los constructores de una superclase


    */



// Ejemplo

// Atributos

public int a;
public int b;


// Constructor

// public POO(int a, int b){  // El constructor puede o no llevar parámetros
//     this.a= a;
//     this.b= b;
// }


// Método

public void sumar(){
    int result = a + b;
    System.out.println("La suma es: "+ result);
}

public int suma_con_retorno(){
    int result = a + b;
    return result;
}










}
