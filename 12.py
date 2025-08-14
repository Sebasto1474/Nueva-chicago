def palabra_mas_caracteres(lista):
    palabra_mas_larga = max(lista, key=len)

    return palabra_mas_larga
    
lista = ["caravajal", "carnal", "federico", "pantorrilla","otorrinonaringologo","hola"]

print(palabra_mas_caracteres(lista))
    