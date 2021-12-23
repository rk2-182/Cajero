
from time import sleep, time
import os
from datetime import datetime

class Operaciones():

    #Constructor
    def __init__(self):
        #self.dinero =0
        self.monto_total = 0
        self.fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
        self.usuarios = ['ricardo','gabriela','mateo','esteban']
        self.usuario_session = ''


    def iniciar_sesion(self):
        print("\n********** Banco Cripto $$$ $$$ $$$ **********")
        usuario = input("Ingrese nombre de usuario: ")

        resultado = usuario in self.usuarios

        if resultado == True:
            print("Iniciando sesion...")
            self.usuario_session = usuario #asignar usuario
            sleep(2)
            return resultado
        else:
            #print("Usuario no encontrado...")
            return resultado

    def ingresar_dinero(self):
        print("Fecha: {0}".format(self.fecha))
        print("********** Banco Cripto $$$ $$$ $$$ **********")
        print("")
        dinero = float(input("Ingrese el monto: $"))

        if dinero >0:
            print("El usuario {0} a ingresado un monto de {1} con exito!".format(self.usuario_session,dinero))
            sleep(1)
            self.monto_total = dinero + self.monto_total


        return self.monto_total


    def retirar_dinero(self):
        print("********** Banco Cripto $$$ $$$ $$$ **********")
        print("")
        dinero_retiro = float(input("Ingrese el monto a retirar: $"))
        
        if dinero_retiro > 0 and self.monto_total > dinero_retiro:
            self.monto_total = self.monto_total - dinero_retiro
            print("Dinero retirado con exito! acaba de retirar {0}".format(dinero_retiro))
            sleep(1)
        else:
            sleep(1)
            print("Monto insuficiente, el monto actual es {0} con fecha: {1}".format(self.monto_total,self.fecha))

        return self.monto_total

    def mostrar_dinero(self):
        os.system('cls')
        print("********** Banco Cripto $$$ $$$ $$$ **********","Fecha: ",datetime.today().strftime('%Y-%m-%d %H:%M'))
        print("")
        print("#################################################################")
        print("\tEl dinero actual de la cuenta es: ${0}".format(self.monto_total))
        print("#################################################################")
        sleep(2)
    
    def salir(self):
        print("Hasta pronto {0} ".format(self.usuario_session))
        sleep(1)
        exit()

