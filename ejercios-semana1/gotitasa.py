cliente = input("ingrese tipo de cliente : residencial,industrial o comercial")
m3_consumidos = int(input("ingrse metros cubicos consumidos"))
iva = 0.21
costo_fijo = 7000
valor_m3 = 200
bonificacion = 0
recargo = 0

#Bonificaciones y recargos segun tipo de cliente

match cliente:
    case "residencial":
        if m3_consumidos < 30:
           bonificacion = 0.10
        elif m3_consumidos > 80:
             recargo = 0.15
        

    case "comercial":
        if m3_consumidos > 300:
            bonificacion = 0.12
        elif m3_consumidos > 150:
            bonificacion = 0.08
        elif m3_consumidos < 50:
            recargo = 0.05
    

    case "industrial":
        if m3_consumidos > 1000:
            bonificacion = 0.30
        elif m3_consumidos > 500:
            bonificacion = 0.20
        elif m3_consumidos < 200:
            recargo = 0.10
                   

subtotal =  valor_m3 * m3_consumidos

#caso especial
if cliente == "residencial" and subtotal < 35000:
    bonificacion += 0.05

#calculos
bonificacion_total = subtotal * bonificacion
recargo_total = subtotal * recargo
subtotal_byr = subtotal - bonificacion_total - recargo_total
iva_aplicado = subtotal_byr * iva
total_final = subtotal_byr + iva_aplicado + costo_fijo

#salida


print("el subtotal es : $",subtotal)
print("la bonificacion es : $",bonificacion_total)
print("el recargo es : $",recargo_total)
print("el subtotal con bonificaciones y recargos es: $",subtotal_byr)
print("el iva aplicado es : $",iva_aplicado)
print("el total a pagar es : $",total_final)
