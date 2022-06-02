package Basics;


import java.util.Scanner;
public class Conditionals {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        // Condicional(Condicion){
            //Cuerpo
        //}
        // Condicional(Condición) Acción

        // Dependiendo de o según (Switch)

        System.out.print("Ingrese un valor: ");
        int x= sc.nextInt();
        if (x<0) System.out.printf("%d es negativo %n", x);
        else if (x==0) System.out.printf("Es cero %n", x);
        else System.out.printf("%d es positivo %n", x);













    sc.close();
    }
}
