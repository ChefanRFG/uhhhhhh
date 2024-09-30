# Lista vacía para productos
Lista = []

def mostrar_menu():
    print("--- Opciones ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver productos")
    print("4. Salir")

def agregar_producto():
    prod = input("Escribe producto: ")
    total = input("Escribe total: ")
    Lista.append([prod, total])
    print(prod + " agregado.")

def eliminar_producto():
    prod = input("Escribe producto a eliminar: ")
    for elem in Lista:
        if elem[0] == prod:
            Lista.remove(elem)
            print(prod + " fue eliminado.")
            return
    print(prod + " no existe.")

def ver_lista():
    if len(Lista) > 0:
        print("--- Lista de productos ---")
        for elem in Lista:
            print("Producto: " + elem[0] + ", Total: " + elem[1])
    else:
        print("Lista vacía.")

# Programa
print("Bienvenido a la frutería Pozole")

while True:
    mostrar_menu()
    opcion = input("Elige algo: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        ver_lista()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
