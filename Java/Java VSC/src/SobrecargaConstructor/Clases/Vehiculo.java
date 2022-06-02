package SobrecargaConstructor.Clases;

    // Superclase

public class Vehiculo {

    protected String matricula;
    protected int numSillas;

    // Constructores (3)

    public Vehiculo(){
        this("BDZ123", 3); //Método para pasar parámetros a otro constructor, es lo mismo que tener this.matricula="BDZ123". De esta forma el sistema reconoce el número de parámetros y hace el llamado a ese constructor, en este caso el constructor Vehiculo(matricula, numSillas)
    }

    public Vehiculo(String matricula){
        this(matricula, 4); 
    }

    public Vehiculo(String matricula, int numSillas) {
        this.matricula = matricula;
        this.numSillas = numSillas;
    }


    // Getters y Setters

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public int getNumSillas() {
        return numSillas;
    }

    public void setNumSillas(int numSillas) {
        this.numSillas = numSillas;
    }

}
