class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente al catálogo.")

    def buscar_libro(self, titulo_buscado):
        for libro in self.libros:
            if libro.titulo.lower() == titulo_buscado.lower():
                return libro
        return None

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)

        if libro:
            if libro.disponible:
                libro.disponible = False
                return f"Has tomado prestado: {libro.titulo}"
            else:
                return f"El libro '{libro.titulo}' ya está prestado."
        else:
            return f"No se ha encontrado ningún libro con ese título."
