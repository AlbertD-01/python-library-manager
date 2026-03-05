class Libro:
    def __init__(self, titulo, autor, anio, disponible):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def rep_texto(self):
        estado = "Disponible" if self.disponible else "Prestado"

        return f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio} | Estado: {estado}"

