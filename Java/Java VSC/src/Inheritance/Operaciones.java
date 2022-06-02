package Inheritance;

import java.util.Scanner;

// Super clase
public class Operaciones {

    // Atributos

    protected int valorUno;
    protected int valorDos;
    protected int resultado;


    Scanner sc= new Scanner(System.in);

    // Métodos para pedir valores

    public void pedirDatos(){
        System.out.println("Ingrese el primer valor: ");
        valorUno= Integer.parseInt(sc.nextLine());

        System.out.println("Ingrese el segundo valor: ");
        valorDos= Integer.parseInt(sc.nextLine());
    }

    // Método para mostrar resultado

    public int mostrarResultado(){
        return resultado;
    }
}
