package Interfaces.Main_class;

import Interfaces.Interfaces_class.Gps;
import Interfaces.Interfaces_class.Inalambrico;
import Interfaces.Interfaces_class.Iphone;
import Interfaces.Interfaces_class.Samsung;
import Interfaces.Interfaces_class.Telefono;

public class Main {
    /*
    Es una colección de métodos abstractos y constantes
    No se puede instanciar
    Debe implementar los métodos declaradados en dicha interfaz

    Sintaxis:

    public interface nombreInterfaz{
        static final tipo Constante= valor;
        tipoDevuelto nombreMetodo (listaParam);
    }

    Las constantes y los métodos deben de ser públicos

    Herencia múltiple
    Las interfaces pueden heredar de otras interfaces, creando una nueva interfaz

    Palabra reservada Implements


    Instanceof se utiliza para conocer si un objeto es de algún tipo determinado (clase o interfaz).

    */

    public static void main(String[] args) {

    // Creación de vector Telefono

    Telefono tel[]= new Telefono[4];

    tel[0]= new Iphone("Apple", "Iphone 7", "VNRA456", "3194567835");

    tel[1]= new Samsung("Samsung", "Galaxy 10");

    tel[2]= new Inalambrico("VTEX", "10.2", "YT45", "5988767");

    tel[3]= new Iphone("Apple", "Iphone 2", "VNTR567", "3207187654");


    for (int i=0; i < tel.length; i++){
        System.out.println("________________________________");
        System.out.println("Marca: "+ tel[i].getMarca() + " Modelo: "+ tel[i].getModelo());

        // Instanceof
        if (tel[i] instanceof Iphone){
            Iphone p= (Iphone) tel[i];  // Cast, convertir un vector a una variable objeto de Iphone
            p.obtenerCoordenadas();
            p.imprimirVelocidadLuz();
        }

        else if (tel[i] instanceof Samsung){
            Samsung s= (Samsung) tel[i];
            s.obtenerCoordenadas();
            s.imprimirVelocidadLuz();
            s.apagarFlash();
            s.prenderFlash();
        }

        else System.out.println("No es instancia de Iphone o Samsung");

    }

    System.out.println("__________________________");
    System.out.println("Velocidad de la luz: "+ Gps.velocidadLuz);






    }
}
