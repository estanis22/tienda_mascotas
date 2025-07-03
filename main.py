from clases.mascota import Perro
from clases.mascota import Gato
from clases.cliente import Cliente
from clases.venta import Venta
from clases.inventario import Inventario
from clases.producto import Producto

def registrar_mascota():

    tipo = input("Ingrese tipo de mascota (perro/gato): ").strip().lower()
    nombre = input("Nombre: ").strip().lower()
    edad = int(input("Edad: "))
    salud = input("Estado de salud: ")
    precio = float(input("Precio de atencion: "))

    if tipo == "perro":
        raza = input("Ingrese la raza: ")
        energia = input("Nivel de energia: ")
        mascota = Perro(nombre, edad, salud, precio, raza, energia)
    elif tipo == "gato":
        raza = input("Ingrese la raza: ")
        independencia = input("Nivel de independencia: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocida")
        return
    return mascota


def registrar_cliente():
    nombre = input("Nombre: ").strip().lower()
    direccion = input("Direccion: ")
    telefono = input("Telefono: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad de producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return
    
    productos = []

    while True:
        nombre_producto = input("Nombre del producto (deje vacio para finalizar): ")
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado")

    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("La venta fue registrada exitosamente")
    else:
        print("No se han registrado productos para la venta")


def mostrar_menu():
    print("\n --- Menu de gestion de Tienda de Mascotas ---")
    print("1. Registar mascota")
    print("2. Registar cliente")
    print("3. Registar producto")
    print("4. Registar venta")
    print("5. Mostrar informacion de mascotas")
    print("6. Mostrar informacion de clientes")
    print("7. Mostrar informacion de productos")
    print("8. Generar alerta de inventario ")
    print("9. Salir")

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota) 
                print("Mascota registrada con exito") 
        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)  
                print("Cliente registrado con exito.")
        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado con exito.")
        elif opcion == "4":
            registrar_venta(clientes, inventario)
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_info())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_info())
        elif opcion == "7":        
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_info())
        elif opcion == "8":
            umbral_minimo = int(input("Ingrese el umbral minimo del inventario: "))
            print(inventario.generar_alerta(umbral_minimo))
        elif opcion == "9":
            print("Saliendo del sistema, gracias")
            break
        else:
            print("Opcion no valida, intente nuevamente. ")

if __name__ == "__main__":
    main()
 