efectivo = 120000

leche = 1700
carne = 11000
coca = 2800

Pedido1 = leche * 2 + carne * 4 + coca * 6
Pedido2 = leche * 6 + carne * 2 + coca * 4
Pedido3 = leche * 2 + carne * 10 + coca * 1

if efectivo >= Pedido3:
    print("llevo pa los pibes")
elif efectivo >= Pedido1 and efectivo < Pedido3:
    print("llevo pedido1")
elif efectivo < Pedido1 and efectivo >= Pedido2:
    print("levo pedido2")
else: print("no llevo una mierda")