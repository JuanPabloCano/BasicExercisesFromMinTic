package PracticeExercises;

// Hacer un programa que identifique un número random y el usuario lo adivine
import javax.swing.*; 
public class RandomNum {
    public static void main(String[] args) {

        int aleatory= (int)(Math.random()*100);
        int num=0, tries=0;

        do{ // Se hace con el ciclo Do-While para que pida primero el número y luego entre a la condición para evitar que el programa arroje un cero y se cierre
            tries++;
            num= Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));

            if (aleatory < num){
                JOptionPane.showMessageDialog(null, "Más bajo", "¡TRY AGAIN!", 1);
            }
            else if (aleatory > num){
                JOptionPane.showMessageDialog(null, "Más alto", "¡TRY AGAIN!", 1);
            }
        }while (num != aleatory);
        JOptionPane.showMessageDialog(null, "Número correcto!! Lo has conseguido en "+ tries + " intentos", "¡CONGRATULATIONS!", 1);
    }
}
