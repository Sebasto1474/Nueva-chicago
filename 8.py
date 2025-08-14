import random

num = int(random.randint(1,100))

while num:
    seleccion_numero = int(input("che pedazo de forrazo, elegite un numero a ver si la pegas: "))
    if seleccion_numero > 100:
        resultado = "Numero invalido, sorete"
    elif seleccion_numero > num:
        resultado = "Casi, pero muy alto boludo"
    elif seleccion_numero ==0 :
        resultado = "Saliste del juego cagon"
        break
    elif seleccion_numero < num:
        resultado = "Te quedaste corto, mierda humana"
    elif seleccion_numero == num:
        resultado = "Bien excremento, le pegaste"
        continue
    print(resultado)


