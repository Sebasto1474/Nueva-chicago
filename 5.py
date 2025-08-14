ingreso_anual = float(input("el ingreso anual es de : "))

if ingreso_anual < 0:
    raise ValueError("El ingreso no puede ser negativo")
elif    ingreso_anual < 10000:
    impuesto = 0
elif ingreso_anual >= 10000 and ingreso_anual < 50000:
    impuesto = 0.1
elif ingreso_anual >= 50000 and ingreso_anual < 100000:
    impuesto = 0.2
elif ingreso_anual >= 10000:
    impuesto = 0.3

impuesto_a_pagar = ingreso_anual * impuesto

print(f"El impuesto que debe pagar este sorete es de: {impuesto_a_pagar}")