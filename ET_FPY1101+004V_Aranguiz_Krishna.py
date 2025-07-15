productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def mostrar_menu():
    print("***MENU PRINCIPAL***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir")

def stock_marca(marca):
    stock_marca = 0
    for producto in productos:
        if productos[producto][0].lower() == marca:
            stock_marca += stock[producto][1]
    print(f"\nEl stock es: {stock_marca}")

def busqueda_precio(p_min, p_max):
    prod_encontrados = []
    for precio in stock:
        print(precio)
        if (stock[precio][0] >= p_max or stock[precio][0] <= p_min) and stock[precio][0] <= 0:
            prod_encontrados.append({"Marca": productos[0], "Modelo": precio})
    prod_encontrados.sort()
    print(prod_encontrados)

def main():
    while True:
        try:
            mostrar_menu()
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1:
                marca = input("Ingrese marca a consultar: ").strip().lower()
                stock_marca(marca)
            elif opcion == 2:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio mínimo: "))
                busqueda_precio(p_min, p_max)
            elif opcion == 3:
                print("")
            elif opcion == 4:
                print("Programa finalizado")
                break
            else:
                print("Debe seleccionar una opción válida!!")
        except ValueError:
            print("Debe seleccionar una opción válida!!")


main()
