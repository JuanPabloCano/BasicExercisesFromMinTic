package Reto_3;

public class Main {
    public static void main(String[] args) {

    Doctor e= new Doctor("Hugo", "Termino fijo", 1200000, "Dermatología");
    
    // Liquidar nómina y salud empleado
    
    System.out.println("Nombre: "+ e.getNombre());
    System.out.println("Tipo de contrato: "+ e.getTipoContrato());
    System.out.println("Salario: "+ e.getSalario());
    System.out.println("Especialidad: "+ e.getEspecialidad());

    System.out.println("Liquidación de nómina: "+ Hospital.liquidarNominaEmpleado(e));
    System.out.println("Liquidación de salud: "+ Hospital.liquidarSaludEmpleado(e));
    System.out.println("Liquidación de prestaciones sociales: "+ Hospital.liquidarPrestacionesEmpleado(e));
    System.out.println("Liquidación de aportes parafiscales: "+ Hospital.liquidarParafiscalesEmpleado(e));

    }
}
