edad = int(input("pasame tu edad, forro: "))

if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad <= 65:
    print("Adulto")
else:
    print("Mayor de edad")