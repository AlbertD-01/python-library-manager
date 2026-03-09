# python-library-manager
Desarrollo incremental de una aplicación Python con Git y GitHub

# 📚 Gestor de Biblioteca en Python

Un sistema de gestión de biblioteca desarrollado en Python para administrar un catálogo de libros con persistencia de datos en JSON.

## 📝 Qué hace el programa
El **Gestor de Biblioteca** permite administrar un catálogo digital. Actúa como una base de datos local donde se pueden registrar obras, gestionar préstamos y devoluciones, y mantener un control del inventario con estadísticas en tiempo real. Los datos se guardan permanentemente en un archivo local.

## 🛠️ Funcionalidades incluidas
* **Gestión de Catálogo:** Añadir libros (título, autor, año) y eliminarlos definitivamente.
* **Sistema de Préstamos:** Buscar libros, marcarlos como prestados o devolverlos.
* **Estadísticas:** Resumen total de libros disponibles y prestados.
* **Persistencia:** Guardado y carga automática mediante un archivo `biblioteca.json`.

## 🚀 Cómo ejecutar el programa
1. **Clona el repositorio:** `git clone https://github.com/AlbertD-01/python-library-manager.git`
2. **Entra en la carpeta:** `cd python-library-manager`
3. **Ejecuta el menú:** `python3 biblioteca/menu.py`

## 📂 Estructura
* `bibliotecaGestor.py`: Lógica de la Biblioteca.
* `libro.py`: Modelo del objeto Libro.
* `menu.py`: Interfaz de usuario.