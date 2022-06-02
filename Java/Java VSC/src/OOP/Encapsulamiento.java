package OOP;

public class Encapsulamiento {

    // Atributos

    private String nombre;
    private double nota1, nota2, nota3;

    // Método

    public double prom(){
        return (nota1 + nota2 + nota3)/3;
    }


    // Métodos Set y Get

    public String getNombre(){
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


    public double getNota1() {
        return nota1;
    }


    public void setNota1(double nota1) {
        this.nota1 = nota1;
    }


    public double getNota2() {
        return nota2;
    }


    public void setNota2(double nota2) {
        this.nota2 = nota2;
    }


    public double getNota3() {
        return nota3;
    }


    public void setNota3(double nota3) {
        this.nota3 = nota3;
    }



}
