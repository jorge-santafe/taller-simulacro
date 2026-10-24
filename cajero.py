"""
Variable saldo inicial = 1000
Funciones
- Mostrar menu
- Consultar saldo
- Depositar dinero
- Retirar dinero
- Usar el ciclo while para salir
"""

saldo_inicial = 1000


def consultar_saldo(saldo_inicial):
    return print(f"Su saldo es ${saldo_inicial}")


def depositar_dinero(saldo_inicial: int):
    deposito = int(input("Ingrese el valor a depositar: "))
    if deposito > 0:
        deposito += saldo_inicial
        consultar_saldo(deposito)
    else:
        print("Error el deposito no puede ser menor a cero")
    return saldo_inicial


def retirar_dinero(saldo_inicial: int):
    # 1.  Solicitar cuanto debe retirar
    # 2.  Validar si el valor del retiro es menor que el saldo inicial
    # 3.  Realizar retiro si se cumple la condicion
    retiro = int(input("Ingrese el valor a retirar: "))
    if retiro <= saldo_inicial:
        saldo_inicial -= retiro
        consultar_saldo(saldo_inicial)
    else:
        print("Saldo insuficiente")


def mostrar_menu(saldo_inicial):
    flag = True
    while flag:
        print("\n============ Menu Principal============\n")
        print("""
          1. Consultar saldo
          2. Depositar dinero
          3. Retirar dinero
          0. Salir
          """)
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                consultar_saldo(saldo_inicial)
            case 2:
                saldo_inicial = depositar_dinero(saldo_inicial)
            case 3:
                saldo_inicial = retirar_dinero(saldo_inicial)
            case _:
                print("Operación finalizada")
                flag = False


# Invocar funcion
mostrar_menu(saldo_inicial)
