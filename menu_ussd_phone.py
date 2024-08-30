menu = """
############################- Bienvenido -############################ \n
1- Consultar saldo \n
2- Recargar crédito \n
3- Salir \n
"""

saldo = 100
limite_recarga = 1000  # Límite de recarga por transacción

def mostrar_menu():
    print(menu)

def obtener_opcion():
    try:
        return int(input("Selecciona una opción: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número.")
        return None

def consultar_saldo():
    print("\n"  + f"Tu saldo es de ${saldo}")

def recargar_credito():
    global saldo
    try:
        monto = int(input(f"Ingresa el monto a recargar (Máximo ${limite_recarga}): "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
        elif monto > limite_recarga:
            print(f"El monto excede el límite de recarga de ${limite_recarga}.")
        else:
            saldo += monto
            print(f"Has recargado ${monto}. Tu nuevo saldo es ${saldo}.")
    except ValueError:
        print("\n" + "Monto no válido. Por favor, ingresa un número.")

def salir():
    print("\n" + "Gracias por usar nuestro servicio.")

def ussd_menu():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        if opcion == 1:
            consultar_saldo()
        elif opcion == 2:
            recargar_credito()
        elif opcion == 3:
            salir()
            break
        elif opcion is None:
            continue
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    ussd_menu()
