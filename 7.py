#ejercicio del sebasto
lista_enteros = [4,7,9,6,2,22,94,65,21,41]
suma_pares = 0

for x in lista_enteros:
    if x%2 == 0:
        suma_pares = suma_pares + x
    else: continue
print(f"la sumatoria de los numeros pares de la lista es: {suma_pares}")

#ejercicio optimo del loco grock
numeros = [3, 8, 12, 5, 7, 14, 9, 2, 16, 1]
suma_pares = 0
for num in numeros:
    if num % 2 == 0:
        suma_pares += num
print(f"La suma de los números pares es: {suma_pares}")




