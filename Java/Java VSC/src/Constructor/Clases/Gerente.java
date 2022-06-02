package Constructor.Clases;

// Subclase
public class Gerente extends Empleado{

    private String departamento;


    // Constructor
    public Gerente(String nombre, int sueldo, String departamento) {
        super(nombre, sueldo); // Super llama a los atributos del padre
        this.departamento= departamento;
    }

    public String getDepartamento(){
        return departamento;
    }

    public void setDepartamento(String departamento){
        this.departamento= departamento;
    }


    // Sobreescritura

    @Override
    public String detalles(){
        return super.detalles() + " \n Departamento: " + this.departamento;
    }
}
