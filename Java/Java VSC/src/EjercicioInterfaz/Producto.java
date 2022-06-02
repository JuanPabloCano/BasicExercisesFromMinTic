package EjercicioInterfaz;


// Superclase
public abstract class Producto {
    
    // Atributos
    protected int codigo, precioCompra, precioVenta, cantidadBodega, cantidadMinimaRequerida, cantidadMaximaInventario;
    protected static double porcentajeDescuento= 0.01;
    protected String descripcion;

    // Constructor

    public Producto(int codigo, int precioCompra, int precioVenta, int cantidadBodega, int cantidadMinimaRequerida,int cantidadMaximaInventario, String descripcion) {
        this.codigo = codigo;
        this.precioCompra = precioCompra;
        this.precioVenta = precioVenta;
        this.cantidadBodega = cantidadBodega;
        this.cantidadMinimaRequerida = cantidadMinimaRequerida;
        this.cantidadMaximaInventario = cantidadMaximaInventario;
        this.descripcion = descripcion;
    }

    // Métodos

    public abstract boolean solicitarPedido();


    public abstract double calcularTotalPagar(double unidades);

    
    // Getters y Setters

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public int getPrecioCompra() {
        return precioCompra;
    }

    public void setPrecioCompra(int precioCompra) {
        this.precioCompra = precioCompra;
    }

    public int getPrecioVenta() {
        return precioVenta;
    }

    public void setPrecioVenta(int precioVenta) {
        this.precioVenta = precioVenta;
    }

    public int getCantidadBodega() {
        return cantidadBodega;
    }

    public void setCantidadBodega(int cantidadBodega) {
        this.cantidadBodega = cantidadBodega;
    }

    public int getCantidadMinimaRequerida() {
        return cantidadMinimaRequerida;
    }

    public void setCantidadMinimaRequerida(int cantidadMinimaRequerida) {
        this.cantidadMinimaRequerida = cantidadMinimaRequerida;
    }

    public int getCantidadMaximaInventario() {
        return cantidadMaximaInventario;
    }

    public void setCantidadMaximaInventario(int cantidadMaximaInventario) {
        this.cantidadMaximaInventario = cantidadMaximaInventario;
    }

    public static double getPorcentajeDescuento() {
        return porcentajeDescuento;
    }

    public static void setPorcentajeDescuento(double porcentajeDescuento) {
        Producto.porcentajeDescuento = porcentajeDescuento;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

}
