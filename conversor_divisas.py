from unicodedata import decimal

def conversor(tipo_peso, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_peso + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + "USD")

menu = """
Bienvenido al conversor de monedas 💰

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3911)
elif opcion == 2:
    conversor("Argentinos", 107)
elif opcion == 3:
    conversor("Mexicanos", 20)
else:
    print("Ingresa una opción correcta por favor :)")