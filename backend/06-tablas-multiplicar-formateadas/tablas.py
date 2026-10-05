def mostrar_tabla(num):
    for i in range(1,13):
        print(f"{num:2d} x {i:2d} = {num * i:3d}")

print("Hola, con este programa puedes visualizar cualquier tabla de multipliacion")

while True:
    try:
        tabla = int(input("Ingresa que tabla deseas visualizar: "))
        mostrar_tabla(tabla)
        break
    except ValueError:
        print("Debe ser un numero enterooojiji")
    

