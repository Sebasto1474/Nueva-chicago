numero1 = float(input("elegi un numero forrazo: "))
numero2 = float(input("dame otro sorete mal cagado: "))

print(numero1 + numero2)
print(numero1 * numero2)   
print(numero1 - numero2)
if numero2 == 0 or numero1 == 0:
    print("No se puede dividir por 0")
else:
    print(numero1 / numero2)