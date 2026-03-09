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

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)

        if libro:
            if not libro.disponible:
                libro.disponible = True
                return f"Gracias. Has devuelto el libro {libro.titulo}"
            else:
                return f"El libro {libro.titulo} ya estaba en la biblioteca."
        else:
            return f"No se ha encontrado el libro en nuestro sistema"

    def obtener_estadisticas(self):
        total = len(self.libros)
        disponibles = len([l for l in self.libros if l.disponible])
        prestados = total - disponibles

        return {
            "total": total,
            "disponibles": disponibles,
            "prestados": prestados
        }