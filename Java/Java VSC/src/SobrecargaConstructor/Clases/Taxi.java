package SobrecargaConstructor.Clases;


// Subclase
public class Taxi extends Vehiculo{

    private boolean AA;

    // Constructores

    public Taxi(boolean AA){
        super();
        this.AA=AA;
    }

    public Taxi(String matricula, boolean AA){
        super(matricula);
        this.AA= AA;
    }

    public Taxi(String matricula, int numSillas, boolean AA) {
        super(matricula, numSillas);
        this.AA = AA;
    }

    // Setters y Getters

    public boolean isAA() {
        return AA;
    }

    public void setAA(boolean AA) {
        this.AA = AA;
    }
}
