package Polimorfismo.Ejemplo;
public class Main {
    public static void main(String[] args) {
        

        Suma suma= new Suma();

        System.out.println("Datos para la suma: ");
        suma.pedirValor();
        suma.operacion();
        System.out.println("El resultado de la suma es: "+ suma.mostrarResultado());


        Resta resta= new Resta();
        System.out.println("Datos para la resta: ");
        resta.pedirValor();
        resta.operacion();
        System.out.println("El resultado de la resta es: "+ resta.mostrarResultado());





    }
}
