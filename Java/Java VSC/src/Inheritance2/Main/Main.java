package Inheritance2.Main;

import java.util.Scanner;

import Inheritance2.Estudiante;

public class Main {
    public static void main(String[] args) {
        

        Scanner sc= new Scanner(System.in);
        
        Estudiante est= new Estudiante();

        est.pedirDatos();

        System.out.println("Ingrese código de estudiante: ");
        est.setCodigo(sc.nextLine());

        System.out.println("Ingrese primera nota: ");
        est.setNota1(Double.parseDouble(sc.nextLine()));

        System.out.println("Ingrese segunda nota: ");
        est.setNota2(Double.parseDouble(sc.nextLine()));

        System.out.println("Ingrese tercera nota: ");
        est.setNota3(Double.parseDouble(sc.nextLine()));


        est.imprimirPadre();
        System.out.println("Con código "+ est.getCodigo());
        System.out.println("Obtuvo un promedio de: "+ est.prome());


        sc.close();
    }
}
