import json
import os # Para comprobar si el archivo existe
from libro import Libro

class Biblioteca:
    def __init__(self, archivo="biblioteca.json"):
        self.libros = []
        self.archivo = archivo
        self.cargar_datos() # Esto hace que al crear la biblioteca, ya tenga los libros guardados

    def guardar_datos(self):
        """Convierte los libros a diccionarios y los guarda en el archivo JSON."""
        with open(self.archivo, "w", encoding="utf-8") as f:
            # Transformamos cada objeto Libro en un diccionario usando to_dict()
            lista_dicts = [libro.to_dict() for libro in self.libros]
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """Si el archivo existe, lee los datos y crea los objetos Libro."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    for d in datos:
                        # Reconstruimos el objeto Libro
                        libro = Libro(d['titulo'], d['autor'], d['anio'])
                        libro.disponible = d['disponible']
                        self.libros.append(libro)
            except Exception as e:
                print(f"Error al cargar los datos: {e}")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_datos()
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
                self.guardar_datos()
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

    def eliminar_libro(self, titulo):
        libro = self.buscar_libro(titulo).lower()

        if libro:
            self.libros.remove(libro)
            self.guardar_datos()  # Actualizamos el JSON
            return f"🗑 El libro '{libro.titulo}' ha sido eliminado del sistema."
        else:
            return " No se pudo eliminar: El libro no existe."
