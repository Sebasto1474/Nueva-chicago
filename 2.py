lista_de_precios = [120, 50, 300, 20, 70]

#ejercicio 1
precio_total = sum(lista_de_precios)
print(f"Total: {precio_total}")

#ejercicio 2
mayores_100 = [n for n in lista_de_precios if n > 100]
print(f"Precios mayores a 100: {mayores_100}")

#ejercicio3
menores_500 = all([p for p in lista_de_precios if p < 500])
print(f"¿todos los precios son menores a 500? {menores_500}")