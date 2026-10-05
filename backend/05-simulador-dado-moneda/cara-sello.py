import random

def lanzar_moneda():
    lista = ['cara', 'sello']
    return random.choice(lista)

def lanzar_dado():
    return random.randint(1,6)

print("1. Lanzar dado")
print("2. Lanzar modeda")
opc = input("Elige una opcion (1-2): ")

if opc == "1": 
    print(f"resutado del dado: {lanzar_dado()}")
elif opc == "2": 
    print(f"resutado de la moneda: {lanzar_moneda()}")
else:
    print("no seas gafo y pon una opcion bn")

