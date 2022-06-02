package Interfaces.Interfaces_class;

// Subclase
public class Samsung extends Telefono implements Gps, Camara {


    // Constructor

    public Samsung(String marca, String modelo) {
        super(marca, modelo);
    }

    // Sobreescritura


    @Override
    public void obtenerCoordenadas(){
        System.out.println("Implementación del método obtenerCoordenadas dentro de la clase Samsung");
    }

    @Override
    public void buscarDireccion(){
        System.out.println("Implementación del método buscarDireccion dentro de la clase Samsung");
    }
    @Override
    public void prenderFlash(){
        System.out.println("Implementación del método prenderFlash dentro de la clase Samsung");
    }
    @Override
    public void apagarFlash(){
        System.out.println("Implementación del método apagarFlash dentro de la clase Samsung");
    }
    @Override
    public void seleccionarVista(){
        System.out.println("Implementación del método seleccionarVista dentro de la clase Samsung");
    }


    // Método

    public void imprimirVelocidadLuz(){
        System.out.println("Velocidad de la luz "+ velocidadLuz);
    }



}
