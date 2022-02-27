#Paquete de funciones
import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido > numero_aleatorio:
            print('El número es menor, elige otro')
        else:
            print('Elige un número más grande, elige otro')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste¡ Has adivinado el número')


if __name__ == '__main__':
    run()