import json
import os
from libro import Libro

class Biblioteca:
    def __init__(self, archivo="biblioteca.json"):
        self.libros = []
        self.archivo = archivo
        self.cargar_datos() # Carga los libros al iniciar

    def guardar_datos(self):
        """Guarda la lista de libros en el archivo JSON"""
        with open(self.archivo, "w", encoding="utf-8") as f:
            lista_dicts = [libro.to_dict() for libro in self.libros]
            json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """Lee el archivo JSON y reconstruye los objetos Libro"""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                    for d in datos:
                        libro = Libro(d['titulo'], d['autor'], d['anio'])
                        libro.disponible = d['disponible']
                        self.libros.append(libro)
            except Exception as e:
                print(f"Error al cargar datos: {e}")

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_datos() # Guardar cambio
        print(f"Libro '{libro.titulo}' agregado correctamente.")

    def eliminar_libro(self, titulo_buscado):
        """Busca y elimina un libro por su título"""
        libro = self.buscar_libro(titulo_buscado)
        if libro:
            self.libros.remove(libro)
            self.guardar_datos() # Guardar cambio tras borrar
            return f"El libro '{libro.titulo}' ha sido eliminado."
        return "No se encontró el libro para eliminar."

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
            return f"El libro '{libro.titulo}' ya está prestado."
        return "No se ha encontrado el libro."

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if not libro.disponible:
                libro.disponible = True
                self.guardar_datos()
                return f"Gracias. Has devuelto {libro.titulo}"
            return f"El libro {libro.titulo} ya estaba aquí."
        return "No se ha encontrado el libro."

    def obtener_estadisticas(self):
        total = len(self.libros)
        disponibles = len([l for l in self.libros if l.disponible])
        return {"total": total, "disponibles": disponibles, "prestados": total - disponibles}
