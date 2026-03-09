from bibliotecaGestor import Biblioteca
from libro import Libro

mi_biblioteca = Biblioteca()

while True:
    print("1. Ver catálogo")
    print("2. Añadir libro")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Estadisticas")
    print("7. Eliminar libro")
    print("8. Salir")

    try:
        opcion = input("Escribe una opcion: ")
    except ValueError:
        print("Error: Por favor, introduce un número del menú.")
        continue

    if opcion == "1":
        for libro in mi_biblioteca.libros:
            print(libro)

    elif opcion == "2":
        titulo = input("Escribe el titulo: ")
        autor = input("Escribe el autor: ")

        try:
            anio = int(input("Escribe el año: "))

            nuevo_libro = Libro(titulo, autor, anio)

            mi_biblioteca.agregar_libro(nuevo_libro)

            print(f"{titulo} añadido con éxito")
        except ValueError:
            print("El año debe ser un número entero")

    elif opcion == "3":
        busqueda = input("Escribe el titulo del libro: ")
        resultado = mi_biblioteca.buscar_libro(busqueda)

        if resultado:
            print("Se ha encontrado el libro")
            print(resultado)

        else:
            print(f"Lo sentimos, no se ha encontrado el libro {busqueda}")

    elif opcion == "4":
        titulo_prestamo = input("¿Qué libro quieres llevarte?: ")
        mensaje = mi_biblioteca.prestar_libro(titulo_prestamo)
        print(mensaje)

    elif opcion == "5":

        titulo = input("¿Qué libro deseas devolver")
        mensaje = mi_biblioteca.devolver_libro(titulo)
        print(mensaje)

    elif opcion == "6":

        stats = mi_biblioteca.obtener_estadisticas()
        print(f"Total: {stats['total']}")
        print(f"Disponibles: {stats['disponibles']}")
        print(f"Prestados: {stats['prestados']}")


    elif opcion == "7":

        titulo = input("¿Qué libro deseas eliminar DEFINITIVAMENTE?: ")

        confirmar = input(f"¿Estás seguro de que quieres borrar '{titulo}'? (s/n): ")

        if confirmar.lower() == "s":

            mensaje = mi_biblioteca.eliminar_libro(titulo)

            print(mensaje)

        else:

            print("Operación cancelada.")


    elif opcion == "8":
        print("Saliendo")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
