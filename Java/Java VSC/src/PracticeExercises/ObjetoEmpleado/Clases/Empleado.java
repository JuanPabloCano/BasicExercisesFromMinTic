package PracticeExercises.ObjetoEmpleado.Clases;

public class Empleado {

    //Atributos
    private final String nombre; //Final se utiliza para que la variable no sea modificable, tipo constante
    private double sueldo;

    //This se utiliza para acceder a las variables globales/atributos, siempre y cuando tengan el mismo nombre de los parámetros de los métodos
    
    //Constructor

    public Empleado(String name, double salary){

        nombre= name;
        sueldo= salary;

    }
        //Setters y Getters


        public String getNombre() {
            return nombre;
        }
    
    
        public double getSueldo() {
            return sueldo;
        }
    
    
        public void setSueldo(double sueldo) {
            this.sueldo = sueldo;
        }
    
        public void setSubeSueldo(double porcentaje){ //Setter para aumentar el salario
            double aumento= (sueldo * porcentaje)/100;
            sueldo += aumento;
        }
}
