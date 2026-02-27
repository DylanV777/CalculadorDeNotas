#Calculador de notas

suma = 0
cantidad = 0 

while True:
    entrada = input("Ingrese una nota, para finalizar digite ok: ")

    if entrada.lower() == "ok": 
        break
    
    try:
        notas = float(entrada)
        if notas < 0:
            print("No puedes ingresar valores negativos, intentalo nuevamente")
            continue
        suma += notas
        cantidad += 1
    
    except ValueError:
        print("Ingresaste un valor incorrecto, intentalo nuevamente")

if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio es de: ", promedio)

else:
    print("No ingresaste notas")

if promedio >= 3:
    print("Felicidades, aprobaste!")
else:
    print("Reprobaste, esfuerzate más!")