package Basics;

import java.util.Scanner;

public class Funciones {
        // Programación modular

        // Variables locales y globales
        // VOID significa vacío, no devuelve valor alguno a quien lo invoque
        
        // Void nombreMetodo(){
            //Declaración variables locales
            //Cuerpo metodo
            // Retorno
        //}


        public static void Saludar(){
            System.out.println("Buenas, saludos!");
        }


        public static  String nombre(String nombre, String apellido){
            return "Mi nombre es: "+ nombre +" "+  apellido;
        }

        public static int sumar(int num1, int num2){
            int prome= (num1 + num2)/2;
            System.out.println("Promedio: ");
            return prome;
        }

        public static void main(String[] args) {
            
            // Las funciones dentro de la misma clase se llaman por obligación dentro del método MAIN
            Scanner sc = new Scanner(System.in);

            
            Saludar();
            System.out.println(nombre("Juan","Cano"));

            System.out.println("Primer número: ");
            int num1 = sc.nextInt();
            System.out.println("Segundo número: ");
            int num2 = sc.nextInt();

            System.out.println(sumar(num1, num2));
            sc.close();
        }
}
