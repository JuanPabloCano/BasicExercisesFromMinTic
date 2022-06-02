package Basics;

import java.util.*;
import javax.swing.JOptionPane;

public class Arrays {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        // Los arrays solo pueden almacenar elementos del mismo tipo
        // Por lo general se controlan con 1 sola variable
        // Tipo de dato- nombre del arreglo[] (int num[])

        // int arreglo[]= new int[2]; // Creación de un arreglo de 2 posiciones
        // arreglo[0]= 1; // Declaración de valores de los arreglos en las posiciones especificas
        // arreglo[1]= 2;
        // System.out.println(arreglo[1]);

        // int vect[]= {1,2,3,4,5,6,7,8,9,10}; // Valores predefinidos del arreglo

        // for (int i=0; i < vect.length; i++){
        //     System.out.println(vect[i]);
        // }
        // System.out.println(Arrays.toString(vect)); // Metodo para imprimir el arreglo

        // Arreglo unidimensional mediante un ciclo for

        // int suma= 0;
        // System.out.print("Tamaño del vector: ");
        // int arrSize= sc.nextInt();

        // int vector[]= new int[arrSize];

        // for(int i=0; i < vector.length; i++){
        //     System.out.println("Ingrese el valor " + (i+1) + ":");
        //     vector[i] = sc.nextInt();
        //     suma += vector[i];
        // }
        // System.out.println(Arrays.toString(vector));
        // System.out.println("La suma es: "+ suma);
        // sc.close();

        // Crear un programa que imprima un vector de n elementos ingresados por teclado y que muestre el mayor y su posición

        // System.out.print("Ingrese el tamaño del vector: ");
        // int vecSize= sc.nextInt();
        // int maxNum= 0, pos= 0;
        // int vect[]= new int[vecSize];

        // for(int i=0; i < vect.length; i++){
        //     System.out.println("Ingrese el número "+ (i+1)+ ":");
        //     vect[i]= sc.nextInt();
        //     if (vect[i] > maxNum){
        //         maxNum=vect[i];
        //         pos=i+1;
        //     }
        // }
        // System.out.printf("El número mayor es %d y se encuentra en la posición %d", maxNum,pos);
        // JOptionPane.showMessageDialog(null, "El número mayor es: "+maxNum+" y se encuentra en la posisicón: "+pos, "VECTOR", 0);




    sc.close();
    }
}
