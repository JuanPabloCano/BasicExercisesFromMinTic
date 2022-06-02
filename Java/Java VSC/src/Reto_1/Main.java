package Reto_1;
import javax.swing.*;
public class Main {
    public static void main(String[] args) {
        
        Empleado x= new Empleado("Hugo", "hugo@gmail.com", "Termino fijo", 1200000, "Dermatología");
        x.setId(Integer.parseInt(JOptionPane.showInputDialog("Ingrese el número de identificación del empleado")));


        System.out.println("Identificación: "+ x.getId());
        System.out.println("Nombre: "+ x.getNombre());
        System.out.println("Correo: "+ x.getEmail());
        System.out.println("Tipo de contrato: "+ x.getTipoContrato());
        System.out.println("Salario: "+ x.getSalario());
        System.out.println("Especialidad médica: "+ x.getEspecialidad());
        System.out.println("Pago de seguridad social devengado: $ "+ x.liquidarSalud(x)+ " pesos");
    }
    
}
