package SobrecargaConstructor.Clases;

// Subclase
public class Camioneta extends Vehiculo {

    private int sillasAdicionales;
    private boolean AA;


    // Constructor

    public Camioneta(String matricula, boolean AA){
        super(matricula);
        this.AA= AA;
    }

    // Setters y Getters

    public int getSillasAdicionales() {
        return sillasAdicionales;
    }

    public void setSillasAdicionales(int sillasAdicionales) {
        this.sillasAdicionales = sillasAdicionales;
    }

    public boolean isAA() {
        return AA;
    }

    public void setAA(boolean AA) {
        this.AA = AA;
    }


    // Sobreescritura

    @Override
    public int getNumSillas() {
        return super.getNumSillas() + sillasAdicionales;
    }


}
