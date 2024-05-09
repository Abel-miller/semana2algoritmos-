busqueda_de_numeros_telefonico_de_mis_cotactos = [
    ("Juan", "0973431212"), ("María", "092321313"),
    ("Carlos", "09325232"), ("Laura", "032231223"),
    ("Ana", "0932656575")
]

def buscar_contacto_por_numero(numero):
    for nombre, telefono_contacto in busqueda_de_numeros_telefonico_de_mis_cotactos:
        if telefono_contacto == numero:
            return nombre
    return None

while True:
    print("¿Elige la opcion que desea realizar?")
    print("1. Buscar el nombre de un contacto a partir de su número telefónico")
    print("2. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == "1":
        numero_contacto = input("Ingrese el número de teléfono del contacto que desea buscar: ")
        nombre_encontrado = buscar_contacto_por_numero(numero_contacto)
        if nombre_encontrado:
            print(f"El número de teléfono {numero_contacto} pertenece al contacto {nombre_encontrado}.")
        else:
            print(f"El número de teléfono {numero_contacto} no está en la lista de contactos.")
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese 1 o 2.")
