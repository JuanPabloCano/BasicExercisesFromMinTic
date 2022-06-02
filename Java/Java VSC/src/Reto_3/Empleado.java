package Reto_3;
// Superclase
public class Empleado {

    // Atributos
    private int id, salario;
    private String nombre, tipoContrato;


    // Constructor

    public Empleado(String nombre,  String tipoContrato, int salario){
        this.nombre= nombre;
        this.tipoContrato= tipoContrato;
        this.salario= salario;
    }


// SETTERS y GETTERS

public int getId() {
    return id;
}

public void setId(int id) {
    this.id = id;
}

public int getSalario() {
    return salario;
}

public void setSalario(int salario) {
    this.salario = salario;
}

public String getNombre() {
    return nombre;
}

public void setNombre(String nombre) {
    this.nombre = nombre;
}


public String getTipoContrato() {
    return tipoContrato;
}

public void setTipoContrato(String tipoContrato) {
    this.tipoContrato = tipoContrato;
}

}
