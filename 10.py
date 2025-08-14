def programita_negativos():
    total = 0
    while True:
        numero = int(input("Selecciona un numero, (negativo para salir del programa): "))
        if numero < 0:
            break
        
        total+= numero
    print(f"La suma total es {total}")
    

print(programita_negativos())
    
    
    