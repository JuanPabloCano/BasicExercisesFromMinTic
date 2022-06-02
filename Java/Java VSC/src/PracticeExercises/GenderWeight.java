package PracticeExercises;

import javax.swing.*;
public class GenderWeight {
    public static void main(String[] args) {

        String sex="";

        do{
            sex=JOptionPane.showInputDialog("Ingrese su sexo (M/F)");

        }while (sex.equalsIgnoreCase("M")==false && sex.equalsIgnoreCase("F")== false);

        int height=Integer.parseInt(JOptionPane.showInputDialog("Ingrese su altura en CM"));
        int weight=0;

        if(sex.equalsIgnoreCase("M")){
            weight= height - 110;
        }
        else if(sex.equalsIgnoreCase("F")){
            weight= height - 120;
        }
        JOptionPane.showMessageDialog(null, "Tu peso ideal es "+ weight + " Kg", "HEALTH", 1);



















    }
}
