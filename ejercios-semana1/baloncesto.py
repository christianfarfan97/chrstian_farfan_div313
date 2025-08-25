
altura = int(input("ingrese altura de jugador"))
posicion = ""

if altura < 160:
    posicion = "base"
elif altura <= 179:
    posicion = "escolta"
elif altura  <= 199:
    posicion = "alero"
else:
    posicion ="ala_pivot o pivot"

print("el jugador debera jugar en la posicion de: ",posicion)

