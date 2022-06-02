package Reto_2;
public class Doctor extends Empleado {

    // Atributos
    private String especialidad;

    // Constructor

    public Doctor(String nombre, String tipoContrato, int salario, String especialidad){
        super(nombre, tipoContrato, salario); // Super llama a los atributos del padre
        this.especialidad= especialidad;
    }


    // Getters y Setters

    public String getEspecialidad() {
        return especialidad;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }
    


}
