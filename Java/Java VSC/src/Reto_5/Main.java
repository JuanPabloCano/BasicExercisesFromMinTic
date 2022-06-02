package Reto_5;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        Doctor e[]= new Doctor[3];
        e[0]= new Doctor("Hugo", "Término fijo", 1200000, "Cardiología");
        e[1]= new Doctor("Martha", "Término indefinido", 1800000, "Dermatología");
        e[2]= new Doctor("Cristi", "Prestación de servicios", 1500000, "Fisiatria");

        // for (int i= 0; i < e.length; i++){
        //     System.out.println("Nombre del doctor: "+ e[i].getNombre() + "\n Tipo de contrato: "+ e[i].getTipoContrato()+
        //     "\n Salario: "+ e[i].getSalario()+ "\n Especialidad: "+ e[i].getEspecialidad());
        // }
        // for (int i= 0; i < e.length; i++){
        //     System.out.println("Este empleado de nombre "+ e[i].getNombre() + ", tiene un salario mensual de: "+Hospital.liquidarNominaEmpleado(e[i]));
        //     System.out.println(e[i].getNombre() + ", paga de salud: "+Hospital.liquidarSaludEmpleado(e[i])+ ", de prestaciones sociales: "+ Hospital.liquidarPrestacionesEmpleado(e[i])+ " y de parafiscales: "+ Hospital.liquidarParafiscalesEmpleado(e[i]));
        //     System.out.println(e[i].getNombre()+ " es especialista en "+ e[i].getEspecialidad()+ " y tiene un contrato de tipo "+ e[i].getTipoContrato());
        //     System.out.println("____________________________________________________________________________");
        // }

        ArrayList <Empleado> empleados = new ArrayList<>();
        empleados.add(e[0]);
        empleados.add(e[1]);
        empleados.add(e[2]);

        for (Empleado es : empleados) {
            System.err.println("Nombre: "+es.getNombre()+ ". Salario: "+es.getSalario() + ". Identificación: "+ es.getId()+ ". Tipo de contrato: "+es.getTipoContrato());
        }

        // Falta hacer los demás métodos de los contratos

    }
}
