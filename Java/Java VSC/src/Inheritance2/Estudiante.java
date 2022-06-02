package Inheritance2;

// Subclase
public class Estudiante extends Person{

    // Atributos
    private double nota1, nota2, nota3;
    private String codigo;

    // Métodos
    public void imprimirPadre(){
        System.out.println("El estudiante: "+ nombre + " " + apellido);
    }
    
    public double prome(){
        return (nota1 + nota2 + nota3)/3;
    }

    // Setters y Getters
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

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
}
