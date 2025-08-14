def funcion_pares_cuadrados(lista):
    lista_de_pares_cuadrados = []
    for p in lista:
        if p%2 == 0:
            resultado = p**2
            lista_de_pares_cuadrados.append(resultado)
    return lista_de_pares_cuadrados

liston = [10,55,60,33,21,20,6,8,47,96]
print(funcion_pares_cuadrados(liston))
