package Basics;


import java.util.Scanner;

public class Fibonacci {

    // Iterativo

    public static void FibonacciIterativoFor() {

        Scanner sc= new Scanner(System.in);

        System.out.println("Ingrese el tamaño de la operación Fibonacci (For): ");
        int fib= sc.nextInt();
        System.out.println("******************************************");
        int num1= 0, num2= 1, result= 0;

        for (int i = 0; i < fib; i++) {
            if (i < fib-1){
            System.out.print(num1 + ", ");
            result= num1 + num2;
            num1=num2;
            num2= result;
            }
            else System.out.println(num1);
        }
        sc.close();
    }

    public static void FibonacciIterativoWhile() {

        Scanner sc= new Scanner(System.in);

        System.out.println("Ingrese el tamaño de la operación Fibonacci (While): ");
        int fib= sc.nextInt();
        System.out.println("******************************************");
        int i= 0, num1= 0, num2= 1, result= 0;

        while (i < fib){
            if (i < fib-1){
                System.out.print(num1 + ", ");
                result= num1 + num2;
                num1=num2;
                num2= result;
                }
                else System.out.println(num1);
            i++;
            }   
        sc.close();
    }

    public static void FibonacciIterativoDoWhile() {

        Scanner sc= new Scanner(System.in);
        System.out.println("Ingrese el tamaño de la operación Fibonacci (Do-While): ");
        int fib= sc.nextInt();
        System.out.println("******************************************");
        int i= 0, num1= 0, num2= 1, result= 0;

        do{
            if (i < fib-1){
                System.out.print(num1 + ", ");
                result= num1 + num2;
                num1=num2;
                num2= result;
                }
                else System.out.println(num1);
            i++;    
        }while (i < fib);
        sc.close();
    }

    // Recursivo

    public static int Rfibonnaci (int num){

        if (num > 1){
            return Rfibonnaci (num-1) + Rfibonnaci (num-2);
        } else if (num == 1){
            return 1;
        } else if (num == 0){
            return 0;
        }else{
            System.out.println("Ingrese un número mayor que cero");
            return -1;
        }

    }

    public static void main(String[] args) {
        
        // FibonacciIterativoFor();
        // System.out.println("***************************************");
        //FibonacciIterativoWhile();
        // System.out.println("***************************************");
        // FibonacciIterativoDoWhile();
        // System.out.println("******************************************");
        // System.out.println("Forma recursiva: "+ Rfibonnaci(10));
    }
}