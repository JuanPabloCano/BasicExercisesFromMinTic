package Reto_5;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
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

    public static double costoDoctorPorContratoIndefinido(Empleado empleado){
        double liquiSalud = empleado.getSalario()*(4.0/100);
        double liquiPension= empleado.getSalario()*(4.0/100);
        double salud= empleado.getSalario()*(0.085);
        double pension= empleado.getSalario()*(0.12);
        double arl= empleado.getSalario()*(0.00522);
        double prima= empleado.getSalario()*(0.0833);
        double cesantia= empleado.getSalario()*(0.0833);
        double interesesCes= cesantia*(0.12);
        double vacaciones= empleado.getSalario()*(0.0416);
        double cajaCo= empleado.getSalario()*(4)/100;
        double icbf= empleado.getSalario()*(3)/100;
        double sena= empleado.getSalario()*(2)/100;
        double totalServicios= salud+pension+arl+prima+cesantia+interesesCes+vacaciones+cajaCo+icbf+sena;
        double totalLiqui= liquiSalud + liquiPension;
        return (empleado.getSalario() - totalLiqui)+ totalServicios;
    }
    public static double costoDoctorPorContratoFijo(Empleado empleado, String ingreso, String retiro){
        // Calculo de fecha
        LocalDate ing= LocalDate.parse(ingreso);
        LocalDate ret= LocalDate.parse(retiro);
        double diasTrab= ChronoUnit.DAYS.between(ing, ret);

        // Seguridad social
        double pension= ((empleado.getSalario()/ 30*diasTrab)*12)/100;
        double salud= ((empleado.getSalario()/ 30*diasTrab)*8.5)/100;
        double arl= ((empleado.getSalario()/ 30*diasTrab)*0.522)/100;
        double segSocial= pension + salud + arl;

        // Parafiscales
        double cajaComp= ((empleado.getSalario()/ 30*diasTrab)*4)/100;
        double icbf= ((empleado.getSalario()/ 30* diasTrab)*3)/100;
        double sena= ((empleado.getSalario()/ 30*diasTrab)*2)/100;
        double paraF= cajaComp + sena + icbf;

        // Prestaciones sociales
        double prima= (empleado.getSalario()* diasTrab)/360;
        double cesantias= (empleado.getSalario()* diasTrab)/360;
        double interesesCesan= (((cesantias*360)*12/100)/360);
        double vacac= (empleado.getSalario()* diasTrab)/720;
        double prestSocial= prima + cesantias + interesesCesan + vacac;

        double salary= empleado.getSalario()/ 30*diasTrab;
        double costoTotal= paraF + prestSocial + segSocial + salary;

        return costoTotal;
    }

    public static double costoDoctorPorContratoPorPrestaciones(Empleado empleado){
        return empleado.getSalario();
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
