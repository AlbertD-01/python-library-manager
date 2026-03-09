from bibliotecaGestor import Biblioteca
from libro import Libro

mi_biblioteca = Biblioteca()

while True:
    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Ver catálogo")
    print("2. Añadir libro")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Estadísticas")
    print("7. ELIMINAR LIBRO 🗑️")
    print("8. Salir")

    opcion = input("Escribe una opción: ")

    if opcion == "1":
        if not mi_biblioteca.libros:
            print("La biblioteca está vacía.")
        for libro in mi_biblioteca.libros:
            print(libro)

    elif opcion == "2":
        titulo = input("Título: ")
        autor = input("Autor: ")
        try:
            anio = int(input("Año: "))
            nuevo_libro = Libro(titulo, autor, anio)
            mi_biblioteca.agregar_libro(nuevo_libro)
        except ValueError:
            print("Error: El año debe ser un número.")

    elif opcion == "7":
        titulo_borrar = input("¿Qué libro quieres eliminar para siempre?: ")
        confirmar = input(f"¿Seguro que quieres borrar '{titulo_borrar}'? (s/n): ")
        if confirmar.lower() == 's':
            print(mi_biblioteca.eliminar_libro(titulo_borrar))
        else:
            print("Operación cancelada.")

    elif opcion == "8":
        print("Saliendo... ¡Hasta pronto!")
        break
    
    # ... (el resto de opciones 3, 4, 5, 6 se quedan como las tenías)
