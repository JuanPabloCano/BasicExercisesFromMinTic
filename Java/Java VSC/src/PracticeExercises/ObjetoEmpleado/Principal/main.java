package PracticeExercises.ObjetoEmpleado.Principal;

import PracticeExercises.ObjetoEmpleado.Clases.Empleado;

public class main {

    public static void main(String[] args) {

        // Array de empleados

        Empleado [] empleados= new Empleado[3];
        empleados[0]=new Empleado("Juan", 50000);
        empleados[1]=new Empleado("María", 28000);
        empleados[2]=new Empleado("Jacob", 45000);
        
        for (Empleado empleado : empleados) {
            empleado.setSubeSueldo(5);
            System.out.println("Nombre: "+ empleado.getNombre()+ ". Salario: "+ empleado.getSueldo());
        }
    }
    
}
