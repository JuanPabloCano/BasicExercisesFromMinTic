package Polimorfismo.Ejemplo;
import java.util.*;
public abstract class Operaciones {
    
    protected int valorUno;
    protected int valorDos;
    protected int resultado;


    Scanner sc= new Scanner(System.in);

    // Método para pedir valores

    public void pedirValor(){
        System.out.println("Ingrese el primer valor");
        valorUno= Integer.parseInt(sc.nextLine());

        System.out.println("Ingrese el segundo valor");
        valorDos= Integer.parseInt(sc.nextLine());
    }

    // Método abstracto
    public abstract void operacion();



    // Método para mostrar el resultado
    public int mostrarResultado(){
        return resultado;
    }





}
