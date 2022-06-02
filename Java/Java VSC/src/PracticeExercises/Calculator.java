package PracticeExercises;


import javax.swing.*;

public class Calculator{
    public static void main(String[] args) {
        // Declaración de variables
        boolean exit= false; // Booleano para controlar el bucle While
        int menu_option, num1, num2, suma, resta, multiplicacion, division, residuo;

        while (!exit){

            try{ // Se utiliza Try para evitar error por ingreso de letras 
                menu_option=Integer.parseInt(JOptionPane.showInputDialog(null,"Seleccione una opción:\n1. Suma" +
                "\n2. Resta\n"+ 
                "3. Multiplicación\n"+ 
                "4. División\n"+
                "5. Residuo\n"+
                "6. Exit"));

                switch (menu_option) {
                    case 1:
                        num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer número"));
                        num2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo número"));
                        suma= (num1 + num2);
                        JOptionPane.showMessageDialog(null, "El resultado de la suma de los números ingresados es: "+ suma, "SUMA", 1);
                        break;
                    case 2:
                        num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer número"));
                        num2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo número"));
                        resta= (num1 - num2);
                        JOptionPane.showMessageDialog(null, "El resultado de la resta de los números ingresados es: "+ resta, "RESTA", 1);
                        break;
                    case 3:
                        num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer número"));
                        num2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo número"));
                        multiplicacion= (num1 * num2);
                        JOptionPane.showMessageDialog(null, "El resultado de la multiplicación de los números ingresados es: "+ multiplicacion, "MULTIPLICACIÓN", 1);
                        break;
                    case 4:
                        num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer número"));
                        num2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo número"));
                        division= (num1 / num2);
                        JOptionPane.showMessageDialog(null, "El resultado de la división de los números ingresados es: "+ division, "DIVISIÓN", 1);
                        break;
                    case 5:
                        num1=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el primer número"));
                        num2=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el segundo número"));
                        residuo= (num1 % num2);
                        JOptionPane.showMessageDialog(null, "El módulo de los números ingresados es: "+ residuo, "MÓDULO", 1);
                        break;
                    case 6:
                        exit=true;
                        JOptionPane.showMessageDialog(null, "Ha salido del sistema. ¡Feliz tarde!", "¡Hasta luego!", 1);
                        break;
                    default:
                        JOptionPane.showMessageDialog(null, "Ingrese un número entre 1 y 6", "¡ERROR!", 2);
                        break;
                    }
                }catch(Exception e){
                    JOptionPane.showMessageDialog(null, "No se aceptan caracteres, utiliza un número entre 1 y 6", "¡ERROR!", 2);
            }
        }
    }   
}