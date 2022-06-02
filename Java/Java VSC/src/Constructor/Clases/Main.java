package Constructor.Clases;
public class Main {
    public static void main(String[] args) {
        

        Gerente gerente1= new Gerente("Mateo", 5000, "Sistemas");
        System.out.println("Gerente 1 \n"+ gerente1.detalles());

        Gerente gerente2= new Gerente("Gabriela", 2300, "Comunicaciones");
        System.out.println("Gerente 2: \n"+ gerente2.detalles());

        Gerente gerente3= new Gerente("Milagros", 2250, "Marketing");
        System.out.println("Gerente 2: \n"+ gerente3.detalles());
        
        Gerente gerente4= new Gerente("José", 1600, "Auxiliar administrativo");
        System.out.println("Gerente 2: \n"+ gerente4.detalles());


        Empleado empleado= new Empleado("Henry", 6000);
        //System.out.println("Empleado"+ empleado.detalles());
        imprimir(empleado); // Se hace el llamado al polimorfismo declarado en la línea de abajo
    }

    public static void imprimir(Empleado a){ // a es una variable de tipo clase (Empleado)
        System.out.println("Empleado "+ a.detalles());  // Polimorfismo
    }





}

