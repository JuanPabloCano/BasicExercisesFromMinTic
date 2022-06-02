package PracticeExercises;

import java.util.*;
public class ArrayEmpresa {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        System.out.println("Ingrese el número de productos: ");
        int products= Integer.parseInt(sc.nextLine());


        int [] product_code= new int[products];
        int [] product_quantity= new int[products];
        int [] minimum_requiered_quantity= new int[products];

        
        for (int i=0; i < products; i++){
            System.out.println("Digite el código del producto: "+ (i+1));
            product_code[i]= sc.nextInt();
            System.out.println("Digite la cantidad en bodega del producto: "+ (i+1));
            product_quantity[i]= sc.nextInt();
            System.out.println("Digite la cantidad mínima requerida del producto: "+ (i+1));
            minimum_requiered_quantity[i]= sc.nextInt();
        }

        System.out.println("Códigos de productos que son necesarios solicitar: ");
        int max= -1, cMax= 0, min= 1000000, cMin= 0;

        for (int i = 0; i < products; i++){
            // Código de los productos que requieren pedido
            if (product_quantity[i] < minimum_requiered_quantity[i]){
                System.out.println(product_code[i]);
            }
            // Menor
            else if (product_quantity[i] < min){
                min = minimum_requiered_quantity[i];
                cMin= product_code[i];
            }
            // Mayor
            else if (product_quantity[i] > max){
                max= minimum_requiered_quantity[i];
                cMax= product_code[i];
            }
        }

        System.out.println("Código con mayor número de unidades en bodega: "+ cMax);
        System.out.println("Código con mayor número de unidades en bodega: "+ cMin);
        sc.close();
    }
}
