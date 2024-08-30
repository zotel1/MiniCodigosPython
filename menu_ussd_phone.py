menu = """
############################- Bienvenido -############################
1- Consultar saldo
2- Recargar crédito
3- Salir
"""

saldo = 100

def consultar_saldo():
    print("Tu saldo es de ${saldo}")

def recargar_credito():
    monto = int(input("Ingresa el monto a recargar: "))
    print(f"Has recargado ${monto}")

def ussd_menu():
    while True:
        print(menu)
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            consultar_saldo()
        elif opcion == 2:
            recargar_credito()
        elif opcion == 3:
            print("Gracias por usar nuestro servicio.")
            break
        else:
            print("Opcion inválida. Intenta de nuevo.")

if __name__ == "__main":
    ussd_menu()