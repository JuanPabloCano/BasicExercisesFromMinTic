package PracticeExercises;

import java.util.Scanner;

public class MissingNumber {

    //Encontrar el primer número faltante más pequeño de un Array

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el tamaño del Array");
        int size= sc.nextInt();
        int array[]= new int[size];
        System.out.println("Ingrese los valores");

        for (int i = 0; i < size; i++){
            array[i]= sc.nextInt();
        }
        int max= 0;

        for (int i=0; i < size; i++){
            for (int j = i+1; j < size; j++){
                
                if (array[i] < array[j]){
                    max= array[i];
                }
            }
        }

        int b[]= new int[max];
        int count= 0;

        for (int i=1; i < max; i++){
            b[count]= i;
            count++;
        }

        int fountNum= 0;
        boolean solution= false;

        for (int i=0; i < b.length; i++){
            for (int j=0; j < array.length; j++){
                if (b[i] == array[j]){
                    fountNum = 1;
                }
            }
            if (fountNum == 0){
                System.out.println("El primer número faltante más pequeño es: " + b[i]);
                solution= true;
                break;
            }
            fountNum= 0;
        }
        if (solution == false){
            System.out.println("No hay número faltante");
        }
        
        sc.close();
    }
}
