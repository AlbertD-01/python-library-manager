from biblioteca.biblioteca import Biblioteca
from biblioteca.libro import Libro

mi_biblioteca = Biblioteca()

while True:
    print("1. Ver catálogo")
    print("2. Añadir libro")
    print("3. Salir")

    opcion = input("Escribe una opcion: ")

    if opcion == "1":
        for libro in mi_biblioteca.libros:
            print(libro)

    elif opcion == "2":
        titulo = input("Escribe el titulo: ")
        autor = input("Escribe el autor: ")
        anio = input("Escribe el año: ")

        nuevo_libro = Libro(titulo, autor, anio)

        mi_biblioteca.agregar_libro(nuevo_libro)

        print(f"{titulo} añadido con éxito")


    elif opcion == "3":
        print("Saliendo")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
