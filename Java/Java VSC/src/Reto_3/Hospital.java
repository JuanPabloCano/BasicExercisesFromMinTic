package Reto_3;
import java.util.ArrayList;

public class Hospital{

    // Atributos
    private String nombre;
    ArrayList <Empleado> empleados = new ArrayList<>();

    // Métodos

    public static double liquidarNominaEmpleado(Empleado empleado){   
        double liquiSalud = empleado.getSalario()*(4.0/100);
        double liquiPension= empleado.getSalario()*(4.0/100);
        return ((empleado.getSalario()- (liquiSalud + liquiPension)));
    }

    public static double liquidarSaludEmpleado(Empleado empleado){
        double salud= empleado.getSalario()*(0.085);
        double pension= empleado.getSalario()*(0.12);
        double arl= empleado.getSalario()*(0.00522);
        return (salud + pension + arl);
        }

    public static double liquidarPrestacionesEmpleado(Empleado empleado){
        double prima= empleado.getSalario()*(0.0833);
        double cesantia= empleado.getSalario()*(0.0833);
        double interesesCes= cesantia*(0.12);
        double vacaciones= empleado.getSalario()*(0.0416);
        return (prima + cesantia + interesesCes + vacaciones);
    }

    public static double liquidarParafiscalesEmpleado(Empleado empleado){
        return (empleado.getSalario()*(4)/100) + (empleado.getSalario()*(3)/100) + (empleado.getSalario()*(2)/100);
    }


    // Getters y Setters

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }



}
