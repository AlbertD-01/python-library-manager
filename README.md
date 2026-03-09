# python-library-manager
Desarrollo incremental de una aplicación Python con Git y GitHub

# 📚 Gestor de Biblioteca en Python

Un sistema de gestión de biblioteca sencillo pero potente, desarrollado en Python, que permite administrar un catálogo de libros con persistencia de datos en formato JSON.

## 🚀 Características
Este proyecto fue desarrollado siguiendo un proceso de aprendizaje por fases:

* **Gestión de Libros:** Añadir, buscar, prestar y devolver libros.
* **Validación de Datos:** Control de errores en la entrada de años y gestión de disponibilidad.
* **Estadísticas:** Informe en tiempo real del estado del catálogo.
* **Persistencia:** Guardado automático en un archivo `biblioteca.json`.
* **Control de Versiones:** Desarrollado íntegramente usando Git y flujo de trabajo de ramas (Git Flow).

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Formato de datos:** JSON
* **Control de Versiones:** Git & GitHub

## 📂 Estructura del Proyecto
```text
python-library-manager/
├── biblioteca/
│   ├── gestor.py        # Lógica de la clase Biblioteca
│   ├── libro.py         # Definición de la clase Libro
│   └── menu.py          # Interfaz de usuario por consola
├── biblioteca.json      # Base de datos (generada automáticamente)
└── README.md            # Documentación

## 🖥️ Vista previa
Así se ve el menú principal al ejecutar el sistema:

```text
1. Ver catálogo
2. Añadir libro
3. Buscar libro
...
Escribe una opción: _

## 🚀 Próximos pasos
- [ ] Implementar búsqueda por autor.
- [ ] Añadir una interfaz gráfica (GUI).
- [ ] Generar reportes en PDF de los libros prestados.
