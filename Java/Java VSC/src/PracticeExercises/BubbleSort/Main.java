package PracticeExercises.BubbleSort;


public class Main {
    public static void main(String[] args) {
        
        int a[]= {35, 54, 65, 76, 21, 74, 98, 12, 43};

        //Intancia del objeto
        Bubble b1= new Bubble();

        System.out.println("Antes de ordenar el array: ");
        b1.print(a);
        b1.bubbleSort(a);
        System.out.println();
        System.out.println("Después de organizar el array: ");
        b1.print(a);
    }
}
