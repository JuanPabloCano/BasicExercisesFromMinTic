package PracticeExercises.BubbleSort;

//Superclase

public class Bubble_Sort{

    //Método de intercambio de array
    
    public void bubbleSort(int a[]){
        
        int n = a.length;
        int i, j, temp;

        for (i=0; i < n; i++){
            for (j=i + 1; j < n; j++){
                if (a[j] < a[i]){
                    temp= a[i];
                    a[i]= a[j];
                    a[j]= temp;
                }
            }
        }
    }
    
}
