### Pet Store Management System - Sistema de Gestión de Tienda de Mascotas

Este repositorio contiene un sistema de gestión para una tienda de mascotas programado en Python. Permite administrar mascotas, clientes, productos y ventas a través de una interfaz de línea de comandos.

### Archivos Incluidos

1. **Programa Principal** (`main.py`):
   - Contiene el menú principal y las funciones para registrar mascotas, clientes, productos y ventas, así como mostrar información y generar alertas de inventario.

2. **Clases** (ubicadas en la carpeta `clases`):
   - `mascota.py`: Define las clases `Perro` y `Gato` para registrar mascotas.
   - `cliente.py`: Define la clase `Cliente` para gestionar clientes.
   - `producto.py`: Define la clase `Producto` para administrar productos.
   - `inventario.py`: Define la clase `Inventario` para manejar el stock de productos.
   - `venta.py`: Define la clase `Venta` para registrar ventas.

### Cómo Usar

1. **Iniciar el Programa**:
   - Ejecute el archivo principal con: `python main.py`.

2. **Navegar por el Menú**:
   - Seleccione una opción del menú (1-9) para registrar mascotas, clientes, productos, ventas, mostrar información o generar alertas de inventario.

3. **Registrar Datos**:
   - Para mascotas: Ingrese tipo (perro/gato), nombre, edad, salud, precio y características específicas (raza, nivel de energía o independencia).
   - Para clientes: Ingrese nombre, dirección y teléfono.
   - Para productos: Ingrese nombre, categoría, precio y cantidad.
   - Para ventas: Ingrese el nombre del cliente y los productos a vender.

4. **Otras Funciones**:
   - Mostrar información de mascotas, clientes o productos.
   - Generar alertas de inventario ingresando un umbral mínimo de stock.
   - Salir del programa seleccionando la opción 9.

### Requisitos

- Python 3.x

---

### Pet Store Management System

This repository contains a pet store management system programmed in Python. It allows managing pets, clients, products, and sales through a command-line interface.

### Included Files

1. **Main Program** (`main.py`):
   - Contains the main menu and functions to register pets, clients, products, and sales, as well as display information and generate inventory alerts.

2. **Classes** (located in the `clases` folder):
   - `mascota.py`: Defines the `Perro` and `Gato` classes for registering pets.
   - `cliente.py`: Defines the `Cliente` class for managing clients.
   - `producto.py`: Defines the `Producto` class for managing products.
   - `inventario.py`: Defines the `Inventario` class for handling product stock.
   - `venta.py`: Defines the `Venta` class for recording sales.

### How to Use

1. **Start the Program**:
   - Run the main file with: `python main.py`.

2. **Navigate the Menu**:
   - Select an option from the menu (1-9) to register pets, clients, products, sales, display information, or generate inventory alerts.

3. **Register Data**:
   - For pets: Enter type (dog/cat), name, age, health, price, and specific characteristics (breed, energy level, or independence).
   - For clients: Enter name, address, and phone number.
   - For products: Enter name, category, price, and quantity.
   - For sales: Enter the client's name and the products to be sold.

4. **Other Functions**:
   - Display information about pets, clients, or products.
   - Generate inventory alerts by entering a minimum stock threshold.
   - Exit the program by selecting option 9.

### Requirements

- Python 3.x