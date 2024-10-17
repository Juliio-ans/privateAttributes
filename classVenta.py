class Venta:
    def __init__(self):
        self.__id_venta = None
        self.__fecha = None
        self.__cliente = None
        self.__productos = {}  # Diccionario de productos vendidos
        self.__total = 0.0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def agregar_producto(self, producto, cantidad, precio_unitario):
        # Verifica que el producto sea uno de los permitidos
        if producto in ['Producto A', 'Producto B', 'Producto C']:
            if producto not in self.__productos:
                self.__productos[producto] = {'cantidad': 0, 'precio_unitario': precio_unitario}
            self.__productos[producto]['cantidad'] += cantidad
            self.__total += cantidad * precio_unitario
        else:
            print("Producto no permitido.")

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")
        for producto, info in self.__productos.items():
            print(f"  {producto}: Cantidad: {info['cantidad']}, Precio Unitario: ${info['precio_unitario']:.2f}")
        print(f"Total: ${self.__total:.2f}")
