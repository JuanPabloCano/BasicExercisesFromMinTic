package PracticeExercises;

// Crear un programa que verifique una contraseña

import javax.swing.*;
public class Password {
    public static void main(String[] args) {
        String password_= "Name";
        String pass_= "";

        while (password_.equals(pass_)==false){
            pass_= JOptionPane.showInputDialog("Introduzca la contraseña, por favor");
            if (password_.equals(pass_)==false){
                JOptionPane.showMessageDialog(null, "Contraseña incorrecta", "ERROR", 3);
            }
        }
        JOptionPane.showMessageDialog(null, "Contraseña correcta", "ENHORABUENA!", 3);
    }
}
