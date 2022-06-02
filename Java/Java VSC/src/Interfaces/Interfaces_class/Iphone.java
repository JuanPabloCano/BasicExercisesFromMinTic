package Interfaces.Interfaces_class;

// Subclase
public class Iphone extends Telefono implements Gps, Camara {

    // Constructor

    public Iphone(String marca, String modelo, String serial, String numTelefonico) {
        super(marca, modelo, serial, numTelefonico);
    }

    // Sobreescritura

    @Override
    public void obtenerCoordenadas(){
        System.out.println("Implementación del método obtenerCoordenadas dentro de la clase Iphone");
    }

    @Override
    public void buscarDireccion(){
        System.out.println("Implementación del método buscarDireccion dentro de la clase Iphone");
    }
    @Override
    public void prenderFlash(){
        System.out.println("Implementación del método prenderFlash dentro de la clase Iphone");
    }
    @Override
    public void apagarFlash(){
        System.out.println("Implementación del método apagarFlash dentro de la clase Iphone");
    }
    @Override
    public void seleccionarVista(){
        System.out.println("Implementación del método seleccionarVista dentro de la clase Iphone");
    }


    // Método

    public void imprimirVelocidadLuz(){
        System.out.println("Velocidad de la luz "+ velocidadLuz);
    }




}
