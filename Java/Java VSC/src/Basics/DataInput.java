package Basics;


import java.util.Scanner; // Se debe importar la clase Scanner para poder ingresar datos  por teclado

class DataInput{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Realizar un programa que tome un número por teclado e imprima los siguientes mensajes:
        //"Feliz día", si el número es mayor a cero.
        //"Vamos muy bien" si es igual a cero.
        //"Para atrás ni para coger impulso", si el número es menor a cero. 
    
        // Scanner sc= new Scanner(System.in);
        // System.out.print("Ingrese su número: ");
        // int number= sc.nextInt();
        
        // if (number > 0) System.out.println("Feliz día"); 
        // else if (number == 0) System.out.println("Vamos muy bien"); 
        // else System.out.println("Para atrás ni para coger impulso");
        
//         if (number > 0) {System.out.println("Feliz día"); 
//     }
//     else if (number == 0){System.out.println("Vamos muy bien"); 
// }
// else {System.out.println("Para atrás ni para coger impulso");
// }
// num.close(); // Siempre se debe de cerrar el Scanner

        // String name= "Juan";
        // int age= 25;
        // System.out.println("Hola " + name + ", es un placer conocerte."+ " Cuantos años tienes?: "+ age);
        // Scanner sc = new Scanner(System.in); // sc es el nombre de la variable más usado para llamar al scanner
        // System.out.print("Ingrese su nombre: ");
        // String nombre= sc.nextLine();
        // System.out.printf("Hola %s, que tengas un felíz día. ", nombre); // printf es un formato que imprime la variable luego de la ,
        // sc.close();

        //System.out.printf("%.2f", 12.4356);
        // El 2 es el número de decimales (Similar al método Round)
        // La f significa que el valor es tipo float o double

        // Comparar dos cadenas

        // String nombre1="", nombre2="";
        // System.out.print("Ingrese el primer nombre: ");
        // nombre1=sc.nextLine();
        // System.out.print("Ingrese el segundo nombre: ");
        // nombre2=sc.nextLine();
        // if (nombre1.equals(nombre2)) System.out.println("Los nombres son iguales");
        // else if (nombre1.equalsIgnoreCase(nombre2)) System.out.println("Los nombres son iguales sin importar la diferencia entre mayúscula y minúscula");
        // else System.out.println("Los nombres no son iguales");














    sc.close();
    }
}


