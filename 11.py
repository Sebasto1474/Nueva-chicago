def suma_hasta_negativo():
    total = 0
    while True:
        num = int(input("Ingresa un número (negativo para salir): "))
        if num < 0:
            break
        total += num
    print("Suma total:", total)


print(suma_hasta_negativo())