package OOP;
public class ArrayList {
    public static void main(String[] args) {

    /* Permite tener un control de los datos haciendo el trabajo de un vector de objetos.

    ArrayList (nombre_clase) objeto= new ArrayList (nombre_clase) ();

    Método

    Add= Agrega elemento al final
    Clear= Elimina todos los elementos
    Get= Devuelve el elemento de la posición índicada

    */


    //EJemplo

    ArrayList lista= new ArrayList();

    lista.add(10);
    lista.add(11);
    lista.add(23);

    for (int i=0; i < lista.size(); i++){
        System.out.println("Que contiene mi lista "+ lista.get(i));
    }

    }

    private int size() {
        return 0;
    }

    private String get(int i) {
        return null;
    }

    private void add(int i) {
    }
    
}
