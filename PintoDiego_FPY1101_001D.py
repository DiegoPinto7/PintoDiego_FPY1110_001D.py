productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}


def stock_marca(marca):
    """
    Calcula y muestra el stock total de una marca específica.

    Args:
        marca (str): La marca de notebooks a consultar.
    """
    total_stock = 0
    for modelo, detalles in productos.items():
        if detalles[0].lower() == marca.lower():
            total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")


def busqueda_precio(p_min, p_max):
    """
    Busca y muestra los modelos de notebooks dentro de un rango de precios
    específico y que tienen stock.

    Args:
        p_min (int): El precio mínimo del rango.
        p_max (int): El precio máximo del rango.
    """
    found_notebooks = []
    for modelo, detalles_stock in stock.items():
        precio = detalles_stock[0]
        cantidad_stock = detalles_stock[1]
        if p_min <= precio <= p_max and cantidad_stock > 0:
            marca = productos[modelo][0]
            found_notebooks.append(f"{marca}--{modelo}")

    if found_notebooks:
        found_notebooks.sort()
        print(f"Los notebooks entre los precios consultas son: {found_notebooks}")
    else:
        print("No hay notebooks en ese rango de precios.")


def actualizar_precio(modelo, p_nuevo):
    """
    Actualiza el precio de un modelo de notebook en el diccionario 'stock'.

    Args:
        modelo (str): El modelo del notebook a actualizar.
        p_nuevo (int): El nuevo precio para el notebook.

    Returns:
        bool: True si el modelo existe y el precio fue actualizado, False en caso contrario.
    """
    if modelo in stock:
        stock[modelo][0] = p_nuevo
        return True
    return False


def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")


def main():
    """
    Función principal que gestiona el flujo del programa,
    mostrando el menú y manejando las opciones del usuario.
    """
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                marca_consulta = input("Ingrese marca a consultar: ")
                stock_marca(marca_consulta)
            elif opcion == 2:
                while True:
                    try:
                        precio_min = int(input("Ingrese precio mínimo: "))
                        precio_max = int(input("Ingrese precio máximo: "))
                        busqueda_precio(precio_min, precio_max)
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
            elif opcion == 3:
                while True:
                    modelo_actualizar = input("Ingrese modelo a actualizar: ")
                    while True:
                        try:
                            precio_nuevo = int(input("Ingrese precio nuevo: "))
                            break
                        except ValueError:
                            print("Debe ingresar valores enteros!!")

                    if actualizar_precio(modelo_actualizar, precio_nuevo):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")

                    respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
                    if respuesta != 'si':
                        break
            elif opcion == 4:
                print("Programa finalizado.")
                break
            else:
                print("Debe seleccionar una opción válida!!")
        except ValueError:
            print("Debe seleccionar una opción válida!!")


if __name__ == "__main__":
    main()