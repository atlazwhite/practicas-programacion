import random

opciones = ["dado 1/6", "cara o cruz", "salir"]
caida = ["cara", "cruz"]

while True:
    print("\nelija que jugar")
    for posicion, lugar in enumerate(opciones, start=1):
        print(posicion, lugar)
    select = input("> ")

    if select == "1":
        while True:
            user = input("hacer predict de dado? (si/no): ").lower()
            if user == "si":
                try:
                    predict = int(input("elija un numero del 1 al 6: "))
                except:
                    print("invalido, tiene que ser numero")
                    continue
                
                gpu = random.randint(1, 6)
                if predict < 1 or predict > 6:
                    print("invalido")
                elif predict == gpu:
                    print("GANASTE")
                    break
                else:
                    print(f"perdiste, habias elegido: {predict} y salio: {gpu}")
                    break

            elif user == "no":
                gpu2 = random.randint(1, 6)
                input("Enter para tirar dado")
                print(f"salio {gpu2}")
                break
            else:
                print("invalido")

    elif select == "2":
        intentos = 3
        moneda = random.choice(caida)
        while intentos > 0:
            op = input("elija cara o cruz: ").lower()
            
            if op not in caida:
                print("ingrese una opcion valida (cara o cruz)")
                continue

            if op == moneda:
                print(f"ganaste, la moneda cayo en {moneda}")
                break
            else:
                intentos -= 1
                print(f"perdiste, la moneda cayo en {moneda}")
                print(f"te queda {intentos} intentos")
                if intentos == 0:
                    print("te quedaste sin intentos")
                    break
                moneda = random.choice(caida) 

    elif select == "3":
        break
    else:
        print("opcion invalida")
