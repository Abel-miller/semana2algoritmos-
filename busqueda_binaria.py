libros_biblioteca = {
    101: {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "genero": "Fábula"},
    102: {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "genero": "Realismo mágico"},
    103: {"titulo": "1984", "autor": "George Orwell", "genero": "Distopía"},
    104: {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "genero": "Romance"},
    105: {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "genero": "Fantasía"}
}

print("Lista de libros en la biblioteca:")
for codigo, libro in libros_biblioteca.items():
    print(f"Código: {codigo}, Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")

ordenar = input("¿Desea ordenar los libros por código? (1: Sí, 2: No): ")

if ordenar == "1":
    lista_libros_ordenados = sorted(libros_biblioteca.items())
    print("Lista de libros ordenada por código:")
    for codigo, libro in lista_libros_ordenados:
        print(f"Código: {codigo}, Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
elif ordenar == "2":
    pass
else:
    print("Opción inválida.")

buscar = input("¿Desea buscar un libro por código? (1: Sí, 2: No): ")

if buscar == "1":
    codigo_buscado = int(input("Ingrese el código del libro: "))
    if codigo_buscado in libros_biblioteca:
        libro = libros_biblioteca[codigo_buscado]
        print(f"Libro encontrado - Código: {codigo_buscado}, Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}")
    else:
        print("Libro no encontrado.")
elif buscar == "2":
    pass
else:
    print("Opción inválida.")
