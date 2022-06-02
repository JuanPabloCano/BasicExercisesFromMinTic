package OOP;
import javax.swing.*;
public class Bodega {
    // Atributos

    private int codigo;
    private double precioCompra,cantidadBodega,cantidadMinima;

    // Métodos

    public boolean solicitarProducto() {
        boolean solicitud = false;
        if (cantidadBodega < cantidadMinima){
            solicitud = true;
            JOptionPane.showMessageDialog(null, "Se necesita hacer pedido del producto con código "+ codigo, "WARNING!", 3);
        }
        else if (cantidadBodega == cantidadMinima){
            JOptionPane.showMessageDialog(null, "Cuidado, la cantidad mínima del producto con código " +codigo+ " es igual a la cantidad en bodega, se requiere control de unidades", "WARNING!", 3);
        }
        else {
            JOptionPane.showMessageDialog(null, "El producto con código "+codigo+ " no necesita hacer pedido por el", "WARNING!", 3);
        }
        return true;
    }


    // GETTERS y SETTERS

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public double getPrecioCompra() {
        return precioCompra;
    }

    public void setPrecioCompra(double precioCompra) {
        this.precioCompra = precioCompra;
    }

    public double getCantidadBodega() {
        return cantidadBodega;
    }

    public void setCantidadBodega(double cantidadBodega) {
        this.cantidadBodega = cantidadBodega;
    }

    public double getCantidadMinima() {
        return cantidadMinima;
    }

    public void setCantidadMinima(double cantidadMinima) {
        this.cantidadMinima = cantidadMinima;
    }















}
