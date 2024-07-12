from datetime import datetime, timedelta

def mostrar_menu():
    print("Bienvenido al menú telefónico USSD")
    print("1. Ver saldo")
    print("2. Consultar fecha de vencimiento del saldo")
    print("3. Comprar paquete de datos")
    print("4. Consultar el consumo de datos, minutos o mensajes.")
    print("5. Salir")

saldo = 100  # Initial balance
megas = 200

def ver_saldo():
    print(f"Tu saldo actual es: {saldo}")

def consultar_fecha():
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Calcular la fecha 7 días adelante
    fecha_futura = fecha_actual + timedelta(days=7)
    # Formatear la fecha para que sea más legible
    fecha_futura_formateada = fecha_futura.strftime("%Y-%m-%d")
    print("La fecha de vencimiento es:", fecha_futura_formateada)

def comprar_paquete_datos():
    print("Opciones de paquetes de datos:")
    print("1. Paquete 1GB")
    print("2. Paquete 2GB")
    opcion = int(input("Selecciona el paquete que deseas comprar: "))
    if opcion == 1:
        print("Has comprado el paquete de 1GB de datos.")
    elif opcion == 2:
        print("Has comprado el paquete de 2GB de datos.")
    else:
        print("Opción inválida.")


def consultar_consumo():
    print(f"{megas}MB Disponibles")

mostrando_menu = True
while mostrando_menu:
    mostrar_menu()
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        ver_saldo()
    elif opcion == 2:
        consultar_fecha()
    elif opcion == 3:
        comprar_paquete_datos()
    elif opcion == 4:
        consultar_consumo()
    elif opcion == 5:
        print("Gracias por utilizar nuestro servicio. Hasta luego.")
        mostrando_menu = False
    else:
        print("Opción inválida. Por favor selecciona una opción válida.")
