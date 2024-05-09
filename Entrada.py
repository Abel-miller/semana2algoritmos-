lista_de_electrodomesticos = [
    'lavadora', 'nevera', 'televisor', 'microondas', 'licuadora', 'cafetera', 'ventilador', 
    'aspiradora', 'plancha', 'batidora', 'secadora', 'horno electrico', 'maquina para hacer helados', 
    'maquina de pan', 'tostadora', 'exprimidor de jugos', 'batidora de mano', 'parrilla electrica', 
    'lava platos', 'Deshidratador de alimentos'
]

while True:
    print("Bienvenido a la tienda de electrodomésticos. ¿Qué deseas hacer?")
    print("1. Buscar un electrodoméstico")
    print("2. Mostrar lista de electrodomésticos disponibles")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        electrodomestico_a_buscar = input("Ingrese el nombre del electrodoméstico a buscar: ")
        if electrodomestico_a_buscar in lista_de_electrodomesticos:
            print(f"El electrodoméstico '{electrodomestico_a_buscar}' está disponible en la tienda.")
        else:
            print(f"El electrodoméstico '{electrodomestico_a_buscar}' no está disponible en la tienda.")

    elif opcion == "2":
        print("Lista actual de electrodomésticos disponibles:")
        for i in range(0, len(lista_de_electrodomesticos), 3):
            print("   ".join(lista_de_electrodomesticos[i:i+3]))

    elif opcion == "3":
        print("¡Gracias por visitar la tienda de electrodomésticos!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")