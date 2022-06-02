package Constructor.Clases;

// Super clase
public class Empleado {
    
    protected String nombre;
    protected int sueldo;


    // Constructor
    public Empleado(String nombre, int sueldo) {
        this.nombre = nombre;
        this.sueldo = sueldo;
    }


    // Método

    public String detalles(){
        return " Nombre: " + this.nombre + "\n Sueldo: " + this.sueldo;
    }
}
