package EjercicioInterfaz;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);

        System.out.println("Digite la cantidad de prendas de vestir: ");
        int numPrendas= Integer.parseInt(sc.nextLine());

        // Array para las prendas
        PrendaVestir productoP[]= new PrendaVestir[numPrendas];

        for (int i = 0; i < numPrendas; i++){
            System.out.println("Digite el código del producto: ");
            int cod= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la descripción del producto: ");
            String descr=sc.nextLine();
            System.out.println("Digite el precio de venta del producto: ");
            int preVenta= Integer.parseInt(sc.nextLine());
            System.out.println("Digite el precio de compra del producto: ");
            int preCompra= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la cantidad en bodega del producto: ");
            int cBodega= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la cantidad mínima requerida del producto: ");
            int cMinRe= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la cantidad máxima de inventario permitida del producto: ");
            int cMaxPro= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la talla del producto: ");
            String talla= sc.nextLine();
            System.out.println("Digite: -1, si se puede planchar del producto | 0- No se puede planchar. ");
            String planchado= sc.nextLine();
            
            // Llenado de Array
            if (planchado.equalsIgnoreCase("1")){
                productoP[i]= new PrendaVestir(cod, preCompra, preVenta, cBodega, cMinRe, cMaxPro, descr, true);
            }
            else{
                productoP[i]= new PrendaVestir(cod, preCompra, preVenta, cBodega, cMinRe, cMaxPro, descr, false);
            }
        }

        System.out.println("Digite la cantidad de producto calzado: ");
        int numCalzado= Integer.parseInt(sc.nextLine());

        // Array para el calzado
        Calzado productoC[]= new Calzado[numCalzado];

        for (int i = 0; i < numCalzado; i++){
            System.out.println("Digite el código del producto: ");
            int cod= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la descripción del producto: ");
            String descr=sc.nextLine();
            System.out.println("Digite el precio de venta del producto: ");
            int preVenta= Integer.parseInt(sc.nextLine());
            System.out.println("Digite el precio de compra del producto: ");
            int preCompra= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la cantidad en bodega del producto: ");
            int cBodega= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la cantidad mínima requerida del producto: ");
            int cMinRe= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la cantidad máxima de inventario permitida del producto: ");
            int cMaxPro= Integer.parseInt(sc.nextLine());
            System.out.println("Digite la talla del producto: ");
            String talla= sc.nextLine();

            // Llenado de Array
            productoC[i]= new Calzado(cod, preCompra, preVenta, cBodega, cMinRe, cMaxPro, descr);
        }
    
    
        // Menú principal

        System.out.println();
        boolean exit= false;

        do{
            System.out.println(" MENU DE OPCIONES ");
            System.out.println("1. Consultar productos ");
            System.out.println("2. Verificar productos a pedir de calzado y prendas");
            System.out.println("3. Calzado con mayor cantidad de unidades");
            System.out.println("4. Prendas con mayor cantidad de unidades");
            System.out.println("5. Modificar cantidad mínima requerida en bodega");
            System.out.println("6. Vender producto");
            System.out.println("7. Salir");
            System.out.println("Ingrese la opción deseada......: ");

            int op= sc.nextInt();
            sc.nextLine();
            int cp, cv;
            String tp;
            boolean sw;

            switch (op) {
                case 1:
                    System.out.println("1. Consultar productos");
                    System.out.println("Digite el código del producto");
                    cp= Integer.parseInt(sc.nextLine());
                    System.out.println("Digite el tipo de producto: (P- prenda | C- calzado ");
                    tp= sc.nextLine();
                    sw= true;
                    System.out.println();
                    if (tp.equalsIgnoreCase("p")){
                        for (int i=0; i < numPrendas; i++){
                            if (productoP[i].getCodigo()==cp){
                                productoP[i].mostrarTodo();
                                sw= false;
                                break;
                            }
                        }
                        if (sw){
                            System.out.println("Código no encontrado");
                        }
                    }
                    else{
                        for (int i=0; i < numCalzado; i++){
                            if (productoC[i].getCodigo()==cp){
                                productoC[i].mostrarTodo();
                                sw= false;
                                System.out.println();
                                break;
                            }
                    }
                    if(sw){
                        System.out.println("Código no encontrado");
                    }
                }
                case 2:
                    for (int i=0; i < numPrendas; i++){
                        if (productoP[i].solicitarPedido()){
                        System.out.println("se debe solictar producto "+ productoP[i].getCodigo());
                        }
                        else{ System.out.println("No se debe realizar pedido del producto " + productoP[i].getCodigo());
                        }
                    }
                    for (int i=0; i < numPrendas; i++){
                        if (productoC[i].solicitarPedido()){
                        System.out.println("se debe solictar producto "+ productoC[i].getCodigo());
                        }
                        else{
                        System.out.println("No se debe realizar pedido del producto " + productoC[i].getCodigo());
                        }
                    } 
                    System.out.println();
                    break;

                case 3:
                    continue;

                case 4:
                    continue;
                case 5:
                    continue;
                case 6:
                    continue;

                default:
                    break;
            }

        }while (!exit);
        sc.close();
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    }
    
}
