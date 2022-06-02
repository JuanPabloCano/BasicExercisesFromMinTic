package OOP;

public class Persona {
    
    private String nombre;
    private int id, edad;

    // Constructor
    public Persona( String nombre, int id, int edad){
        this.nombre= nombre;
        this.id=id;
        this.edad= edad;
    }

    public Persona(){

    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }


    // El método toString permite mostrar la información completa de un objeto, es decir el valor de sus atributos

    @Override  // Anotación
    public String toString() {
    
        String mensaje= "El alumno se llama "  + nombre + ", con número de id= " + id + ", y tiene " + edad + " años";
        return mensaje;
    }

    public void saludar(){
        System.out.println("Hola soy "+ nombre);
    }












}
