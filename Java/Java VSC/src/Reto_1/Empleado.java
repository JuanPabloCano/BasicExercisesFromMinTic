package Reto_1;

public class Empleado {

    // Atributos
    private int id, salario;
    private String nombre, email, tipoContrato, especialidad;


    // Constructor

    public Empleado(String nombre, String email, String tipoContrato, int salario, String especialidad){
        this.nombre= nombre;
        this.email= email;
        this.tipoContrato= tipoContrato;
        this.salario= salario;
        this.especialidad= especialidad;
    }

    // Métodos

    public double liquidarSalud(Empleado empleado){
        double salud= (salario * 8.5)/100;
        double pension= (salario * 12)/100;
        double arl= (salario * 0.522)/100;
        double segSoc= salud + pension + arl;
        return segSoc;
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

public String getEmail() {
    return email;
}

public void setEmail(String email) {
    this.email = email;
}

public String getTipoContrato() {
    return tipoContrato;
}

public void setTipoContrato(String tipoContrato) {
    this.tipoContrato = tipoContrato;
}

public String getEspecialidad() {
    return especialidad;
}

public void setEspecialidad(String especialidad) {
    this.especialidad = especialidad;
}




}
