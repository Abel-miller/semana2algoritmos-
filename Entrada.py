import array

def buscar_electrodomestico(electrodomesticos, nombre):
    return f"El electrodoméstico '{nombre}' {'está' if nombre in electrodomesticos else 'no está'} en la lista de compras."

arr_electrodomesticos = array.array('u', [input(f"Ingrese el electrodoméstico {i+1}: ") for i in range(5)])
electrodomestico_a_buscar = input("Ingrese el electrodoméstico a buscar en la lista: ")

print(buscar_electrodomestico(arr_electrodomesticos, electrodomestico_a_buscar))