package Inheritance2;

import java.util.Scanner;

// Sueperclase
public class Person {

    // Atributos

    protected String nombre;
    protected String apellido;

    Scanner sc= new Scanner(System.in);

    public void pedirDatos(){
        System.out.println("Ingrese su nombre: ");
        nombre= sc.nextLine();

        System.out.println("Ingrese su apellido: ");
        apellido= sc.nextLine();
    }
    
}
