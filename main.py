import operaciones
import os

"""

*Hacer un programa que simule un cajero automaticocon un saldo
inicial de $1.000 y tendrá el siguiente menú de opciones:
    1.-ingresar dinero en la cuenta
    2.-retirar dinero de la cuenta
    3.-mostrar dinero disponible
    4.-salir
"""

def inicio():
    while True:
        print("\n********** Banco Cripto $$$ $$$ $$$ **********")
        print("Menu")
        print("""
            1.-Ingresar dinero en la cuenta
            2.-Retirar dinero de la cuenta
            3.-Mostrar dinero disponible
            4.-Limpiar consola
            5.-Salir""")
        print("")
        opcion = int(input("Ingrese la opcion:"))

        if opcion == 1:
            ope.ingresar_dinero()
            #os.system('cls')
        elif opcion == 2:
            ope.retirar_dinero()
        elif opcion == 3:
            ope.mostrar_dinero()
            #os.system('cls')
        elif opcion == 4:
            os.system('cls')
        elif opcion == 5:
            ope.salir()
#*******************************************************************
#Instanciar objeto
ope = operaciones.Operaciones()


resultado = ope.iniciar_sesion()

if resultado == True:
    inicio()
else:
    print("Usuario no encontrado o incorrecto")
