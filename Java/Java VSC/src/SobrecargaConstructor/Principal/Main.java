package SobrecargaConstructor.Principal;

import java.util.Scanner;

import SobrecargaConstructor.Clases.*;

public class Main {

    public static void main(String[] args) {

        // Definición de variables
        char resp;
        boolean aa;
        String matricula;
        int numSillas, sillasAdicionales;

        Scanner sc = new Scanner(System.in);
        
        // Creación de objetos Vehículo

        Vehiculo v1= new Vehiculo();
        System.out.println("El vehículo con placa "+ v1.getMatricula()+ " tiene "+ v1.getNumSillas()+ " sillas");

        Vehiculo v2= new Vehiculo("BHW123");
        System.out.println("El vehículo con placa "+ v2.getMatricula()+ " tiene "+ v2.getNumSillas()+ " sillas");

        Vehiculo v3= new Vehiculo("AZX234", 6);
        System.out.println("El vehículo con placa "+ v3.getMatricula()+ " tiene "+ v3.getNumSillas()+ " sillas");


        // Creación de objetos instaciando la subclase Taxi

        // Primer objeto Taxi

        System.out.println("Primer taxi: Tiene aire acondicionado?(S/N): ");
        resp=sc.next().charAt(0);  // Leer 1 caracter
        aa = resp == 'S' || resp== 's'; // Prueba de operador || booleano

        Taxi t1= new Taxi(aa);
        System.out.printf("El primer taxi con matrícula %s tiene %d sillas y %s%n", t1.getMatricula(), t1.getNumSillas(), (t1.isAA()?"tiene AA":"No tiene AA"));


        // Segundo objeto Taxi

        System.out.println("Segundo taxi: Número de matricula: ");
        matricula = sc.next();
        System.out.println("Segundo taxi: Tiene aire acondicionado?(S/N): ");
        resp=sc.next().charAt(0);  // Leer 1 caracter
        aa = resp == 'S' || resp== 's'; // Prueba de operador || booleano

        Taxi t2= new Taxi(matricula, aa);
        System.out.printf("El segundo taxi con matrícula %s tiene %d sillas y %s%n", t2.getMatricula(), t2.getNumSillas(), (t2.isAA()?"tiene AA":"No tiene AA"));



        // Tercer objeto Taxi

        System.out.println("Tercer taxi: Número de matricula: ");
        matricula = sc.next();
        System.out.println("Tercer taxi: Número de sillas: ");
        numSillas= sc.nextInt();
        System.out.println("Tercer  taxi: Tiene aire acondicionado?(S/N): ");
        resp=sc.next().charAt(0);  // Leer 1 caracter
        aa = resp == 'S' || resp== 's'; // Prueba de operador || booleano

        Taxi t3= new Taxi(matricula, numSillas, aa);
        System.out.printf("El tercer taxi con matrícula %s tiene %d sillas y %s%n", t3.getMatricula(), t3.getNumSillas(), (t3.isAA()?"tiene AA":"No tiene AA"));



        // Creación de objetos c con la subclase Camioneta

        System.out.println("Camioneta: Número de matrícula: ");
        matricula= sc.next();
        System.out.println("Camioneta: Sillas adicionales: ");
        sillasAdicionales= sc.nextInt();
        System.out.println("Camioneta: Tiene aire acondicionado?(S/N): ");
        resp=sc.next().charAt(0); 
        aa = resp == 'S' || resp== 's'; 

        Camioneta c1= new Camioneta(matricula, aa);
        c1.setSillasAdicionales(sillasAdicionales); // Aumento de número de sillas

        System.out.printf("La camioneta con matrícula %s tiene %d sillas y %s%n", c1.getMatricula(), c1.getNumSillas(), (c1.isAA()?"tiene AA":"No tiene AA"));


        sc.close();
    // Encapsulación - Herencia- Sobrecarga de constructores- Sobreescritura- Palabra reservada Super
    }
}
