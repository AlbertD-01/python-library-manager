class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def rep_texto(self):
        estado = "Disponible" if self.disponible else "Prestado"

        return f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio} | Estado: {estado}"

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f" {self.titulo} - {self.autor} ({self.anio}) [{estado}]"

    def to_dict(self):
        """Convierte el objeto Libro en un diccionario para JSON."""
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio": self.anio,
            "disponible": self.disponible
        }

