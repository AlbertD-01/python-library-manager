from libro import Libro
from biblioteca import Biblioteca

mi_biblioteca = Biblioteca()

Libro1 = Libro("Sangre y fuego", "John McKenzy", 2002)
Libro2 = Libro("Tierra santa", "Ronnie Coleman", 2009)
Libro3 = Libro("Nobleza", "Mike Mentzer", 1989)

mi_biblioteca.agregar_libro(Libro1)
mi_biblioteca.agregar_libro(Libro2)
mi_biblioteca.agregar_libro(Libro3)

print("Catálogo de la biblioteca")
for libro in mi_biblioteca.libros:
    print(libro)