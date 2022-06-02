package EjercicioInterfaz;

// Subclase
public class PrendaVestir extends Producto implements Vista {

    private String talla;
    private boolean planchado;


    // Constructor
    public PrendaVestir(int codigo, int precioCompra, int precioVenta, int cantidadBodega, int cantidadMinimaRequerida, int cantidadMaximaInventario, String descripcion, boolean planchado) {
    super(codigo, precioCompra, precioVenta, cantidadBodega, cantidadMinimaRequerida, cantidadMaximaInventario,
            descripcion);
}


@Override
public void mostrarTodo() {
    System.out.println(getCodigo()+ " - "+ getPorcentajeDescuento()+ " - "+ getPrecioCompra()+ " - "+ getPrecioVenta()+ " - "+ getCantidadBodega() + " - "+ getCantidadMinimaRequerida()+ " - "+ getCantidadMaximaInventario()+ " - "+ talla+ " - "+ planchado);
}

@Override
public void mostrarLite1() {
    System.out.println((getCodigo()+ " - "+ getPorcentajeDescuento()));
}

@Override
public void mostrarLite2() {
    System.out.println(getCodigo()+ " - "+ getPorcentajeDescuento()+ " - "+ " - "+ getPrecioCompra()+ " - "+ getPrecioVenta());
}

@Override
public boolean solicitarPedido() {
    if (cantidadBodega < cantidadMinimaRequerida){
        return true;
    }
    else return false;
}

@Override
public double calcularTotalPagar(double unidades) {
    return (unidades * precioCompra);
}

// Setters y Getters

public String getTalla() {
    return talla;
}


public void setTalla(String talla) {
    this.talla = talla;
}

public boolean isPlanchado() {
    return planchado;
}


public void setPlanchado(boolean planchado) {
    this.planchado = planchado;
}



}
