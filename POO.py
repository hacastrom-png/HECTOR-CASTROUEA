#abstraccion
class Auto:
    def arrancar(self):
        print("El auto está arrancando...")

    def frenar(self):
        print("El auto está frenando...")
#encapsulacion
class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo
#herencia
class Animal:
    def comer(self):
        print("El animal está comiendo")

class Perro(Animal):
    def ladrar(self):
        print("Guau guau")
#polimorfismo
class Ave:
    def sonido(self):
        print("El ave hace un sonido")

class Loro(Ave):
    def sonido(self):
        print("El loro dice: Hola!")

class Aguila(Ave):
    def sonido(self):
        print("El águila grita: Screee!")