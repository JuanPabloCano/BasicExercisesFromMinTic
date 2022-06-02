package PracticeExercises;

import java.util.Scanner;

import PracticeExercises.ObjetoEmpleado.Principal.main;

public class ReverseString {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String cadena, invertida;

        invertida = "";

        System.out.println("Ingrese una palabra");
        cadena = sc.nextLine();
        System.out.println("Original: "+ cadena);

        StringBuilder strb = new StringBuilder(cadena); // Se utiliza la clase StringBuilder y sus métodos
        cadena = strb.reverse().toString();
        System.out.println("Invertida con StringBuilder: "+ cadena);


        for (int i = cadena.length() - 1; i >= 0; i--) {
            invertida += cadena.charAt(i);
        }
        System.out.println("Cadena invertida usando For: "+ invertida);

    }
}
