package Inheritance.Main_class;

import Inheritance.*;

public class Main {
    public static void main(String[] args) {
        
        Suma sum = new Suma();


        System.out.println("Datos para la suma: ");
        sum.pedirDatos();  // Superclase
        sum.Sumar(); // Subclase
        System.out.println("El resultado de la suma es: "+ sum.mostrarResultado());
        System.out.println();

        Resta res= new Resta();
        res.pedirDatos();
        res.restar();
        System.out.println("El resultado de la resta es: "+ res.mostrarResultado());

        







    }
}
