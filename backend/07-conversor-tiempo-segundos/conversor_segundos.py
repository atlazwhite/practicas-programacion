cantidad_seg_totales = int(input("Ingrese la cantidad de segundos: "))
cantidad_hrs = cantidad_seg_totales // 3600
cantidad_min =  (cantidad_seg_totales % 3600) // 60
cantidad_seg =  cantidad_seg_totales % 60 

print(f"horas:{cantidad_hrs}, minutos:{cantidad_min}, segundos:{cantidad_seg} ")