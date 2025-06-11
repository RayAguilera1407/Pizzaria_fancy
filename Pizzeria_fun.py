#PIZZERIA................
import os, time

# Variables globales
pizza = ["Napolitana", "Vegetariana", "Peperoni", "Doble queso"]
cliente = []
masa = ("masa Napolitana", "masa Romana", "masa Americana", "masa sin gluten")
pizzas = 0
precio = 0
stock = 0
pedidos = []
menu_pizza = []

def mostrar_menu():
    menu = f"""\n{"="*20}MENÚ PIZZERIA{"="*20}
1. Registrar nuevas pizzas disponibles para la venta.
2. Ver catálogo de pizzas.
3. Realizar un pedido.
4. Ver los pedidos realizados.
5. Salir del sistema.
{"="*53}"""
    print(menu)

def limpiar_pantalla():
    os.system('cls')

def esperar_continuar():
    print("\nPresione Enter para continuar...")
    input()

def validar_entero():
    while True:
        try:
            valor = int(input())
            if valor < 0:
                print("Error! Debes ingresar un número entero positivo!")
            else:
                return valor
        except ValueError:
            print("Error!!! Debe ingresar un valor válido!")

def validar_texto():
    while True:
        texto = input().strip().title()
        if len(texto) < 3:
            print("Error!!! El texto debe tener más de 3 letras")
        else:
            return texto

def registrar_pizza():
    print("Ingrese el código de la pizza: ")
    codigo = validar_entero()
    
    print("Ingrese el nombre de la pizza: ")
    nombre = validar_texto()
    
    print("Ingrese la cantidad de pizzas: ")
    pizzas = validar_entero()
    
    print("Ingrese el tipo de masa: ")
    masa = validar_texto()
    
    print("Ingrese precio unitario de la pizza: ")
    precio = validar_entero()
    
    print("Ingrese stock disponible: ")
    stock = validar_entero()

    nueva_pizza = {
        'codigo': codigo,
        'nombre': nombre,
        'pizzas': pizzas,
        'masa': masa,
        'precio': precio,
        'stock': stock
    }
    menu_pizza.append(nueva_pizza)
    print("Pizza registrada con éxito!")
    time.sleep(3)

def ver_catalogo():
    print("Ver catalogo de pizzas.")
    if len(menu_pizza) == 0:
        print("No hay pizzas registradas.")
    else:
        print("\n--- VER CATALOGO ---\n")
        for p in menu_pizza:
            for key in p:
                print(key, "=>", p[key])
            print(f"="*30)

def realizar_pedido():
    print("Realizar pedido.")
    print("Ingrese el nombre del cliente: ")
    nombre_cliente = validar_texto()
    
    print("Ingrese nombre de la pizza seleccionada: ")
    pizza = validar_texto()
    
    print("Ingrese la cantidad de pizzas que va a llevar: ")
    cant = validar_entero()

    for p in menu_pizza:
        if p['nombre'] == pizza:
            if cant > p['stock']:
                print("Error! No hay stock de pizzas!")
                return
            total = p['precio'] * cant
            p['stock'] -= cant

            nuevo_pedido = {
                'nombre_cliente': nombre_cliente,
                'pizza': pizza,
                'cant': cant,
                'total': total
            }
            pedidos.append(nuevo_pedido)
            print(f"Pedido realizado con éxito!. El total es: ${total}")
            time.sleep(3)
            return
    print("Error! Pizza no encontrada en el menú")

def ver_pedidos():
    print("Ver pedidos")
    if not pedidos:
        print("No hay pedidos registrados")
    for n in pedidos:
        for key in n:
            print(key, "=>", n[key])
        print(f"="*30)

def menu_principal():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opc = input("Ingrese un opción (1-5): ")
        limpiar_pantalla()

        if opc == "1":
            registrar_pizza()
        elif opc == "2":
            ver_catalogo()
        elif opc == "3":
            realizar_pedido()
        elif opc == "4":
            ver_pedidos()
        elif opc == "5":
            print("Salir del sistema.")
            time.sleep(3)
            break
        else:
            print("Error!!! Ingrese una opción válida!")
        
        esperar_continuar()

if __name__ == "__main__":
    menu_principal()