"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...
"""
nota = int(input("ingrese su nota"))
condicion = ""
if nota >= 6:
    condicion = "promocion directa"
elif nota >= 4:
    condicion = "aprobado"
else:
    condicion = "desaprobado"

print(condicion, "la nota es: ", nota)