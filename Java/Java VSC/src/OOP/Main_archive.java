package OOP;
import java.util.*;
import java.util.ArrayList;
import javax.swing.*;

public class Main_archive {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        
        // POO objoperacionConstructor= new POO("Juan cano", 3.5, 4.3, 3.9); // CONSTRUCTOR

        // POO objOperacion1= new POO(); // Creación del objeto o intancia de la clase
        // POO objOperacion2= new POO();



        // objOperacion1.a=5;   // Acá se llaman los objetos y asignando valor a los atributos
        // objOperacion1.b=12;
        // objOperacion1.sumar(); // Acá se llama al método del objeto

        // objOperacion2.a= 23;
        // objOperacion2.b= 45;
        // objOperacion2.sumar();

        //  // Otro objeto
        // int valor= objOperacion1.suma_con_retorno();
        // System.out.println("La suma con retorno es: "+ valor);



    // Archivo ENCAPSULAMIENTO


    // Encapsulamiento e1= new Encapsulamiento();
    // Encapsulamiento e2= new Encapsulamiento();

    // // Empleo de los Set, para ingresar datos a los atributos
    // System.out.println("Ingrese el nombre del estudiante: ");
    // e1.setNombre(sc.nextLine());

    // e1.setNota1(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la nota 1")));
    // e1.setNota2(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la nota 2")));
    // e1.setNota3(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la nota 3")));

    // // Empleo de los Get para poder mostrar los datos privados de los atributos

    // JOptionPane.showMessageDialog(null, "El nombre del estudiante es "+ e1.getNombre(), "Nombre", 1);
    // JOptionPane.showMessageDialog(null, "El Promedio del estudiante es "+ e1.prom(), "Promedio", 1);

    // // Objeto #2

    // System.out.println("Ingrese el nombre del estudiante: ");
    // e2.setNombre(sc.nextLine());

    // e2.setNota1(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la nota 1")));
    // e2.setNota2(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la nota 2")));
    // e2.setNota3(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la nota 3")));

    // JOptionPane.showMessageDialog(null, "El nombre del estudiante es "+ e2.getNombre(), "Nombre", 1);
    // JOptionPane.showMessageDialog(null, "El Promedio del estudiante es "+ e2.prom(), "Promedio", 1);





    // Archivo BODEGA


    // Bodega obj1 = new Bodega();

    // obj1.setCodigo(Integer.parseInt(JOptionPane.showInputDialog("Ingrese el código del producto")));

    // obj1.setPrecioCompra(Double.parseDouble(JOptionPane.showInputDialog("Ingrese el precio del producto")));

    // obj1.setCantidadBodega(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la cantidad en bodega del producto")));

    // obj1.setCantidadMinima(Double.parseDouble(JOptionPane.showInputDialog("Ingrese la cantidad mínima del producto")));


    // obj1.solicitarProducto();





    // Archivo PERSONA tipo ARRAY

    // ArrayList <Persona> Persona= new ArrayList <Persona>();

    // Persona p1= new Persona("Daniela", 1001, 14);
    // Persona p2= new Persona("Andrea", 1002, 10);
    // Persona p3= new Persona("María", 1003, 20);

    // // Se adicionan los objetos al Array

    // Persona.add(p1);
    // Persona.add(p2);
    // Persona.add(p3);

    // // Se imprime el Array y Size: Devuelve la cantidad de elementos agregados

    // // for (int i= 0; i < Persona.size(); i++){
    // //     System.out.println(Persona.get(i).toString()); // toString devuelve los valores de toda la lista
    // //     System.out.println(Persona.get(i).getNombre());
    // // }

    // for (Persona p: Persona){ // For Each

    //     System.out.println(p);
    //     System.out.println(p.getNombre());
    // }

    // // Método saludar
    // System.out.println();
    // for (Persona p: Persona){
    //     p.saludar();
    // }
    // System.out.println();

    // // Cambiar elemento de la lista
    // Persona.get(0).setNombre("Sofía");
    // for (Persona p: Persona){
    //     System.out.println(p.getNombre());
    // }
    
    // System.out.println();

    // // Remover elemento de la lista
    // Persona.remove(1);
    // System.out.println(Persona.size());




































    


    sc.close();
    }
}
