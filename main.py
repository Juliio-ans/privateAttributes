from classVenta import Venta


def main():
    venta = Venta()
    venta.set_id_venta(1)
    venta.set_fecha("2024-10-17")
    venta.set_cliente("julio")

    productos = [
        "Producto A",
        "Producto B",
        "Producto C"
    ]

    for producto in productos:
        print(f"\nAgregando {producto}...")

        try:
            cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
            precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
            venta.agregar_producto(producto, cantidad, precio_unitario)
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números para cantidad y precio.")
            continue  # Continúa con el siguiente producto

    # Mostrar detalles de la venta
    venta.mostrar_detalle()


if __name__ == "__main__":
    main()
