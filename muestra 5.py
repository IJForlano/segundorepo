import os


def crear_tabla(numero):
    contenido = ""
    for i in range(1, 11):
        resultado = numero * i
        contenido += f"{numero}*{i}= {resultado}.\n"
    nombre_archivo = f"tabla-{numero}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    print("Se creo la tabla.")


def mostrar_tabla(numero):
    nombre_archivo = f"tabla-{numero}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(f"La tabla de {numero}: \n es{contenido}")
    except FileNotFoundError:
        print("no existe la tabla.")


def mostrar_menu():
    print("1- Crear tabla.")
    print("2- Mostrar tabla.")
    print("1- Salir.")


def validar_opcion(opcion):
    return opcion in ("1", "2", "3")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion.")
        if validar_opcion(opcion):
            if opcion == "1":
                numero = int(input("Ingrese el numero a mostrar la tabla."))
                crear_tabla(numero)
            elif opcion == "2":
                numero = int(input("Ingrese el numero a mostrar la tabla."))
                mostrar_tabla(numero)
            else:
                print("Chau")
                break
        else:
            print("ingrese una opcion valida.")


if __name__ == "__main__":
    main()
