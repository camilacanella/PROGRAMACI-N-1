
acumulador_kilos=0
descuento_cien_kilos=0.85 #0.85 seria el porcentaje a pagar con el 15% de descuento
descuento_trecientos_kilos=0.75 #0.75 seria el porcentaje que queda a pagar con el 25% de descuento
acumulador_precios_brutos=0
flag_alimento_caro=True
acumulador_precio_porkilo=0
contador_preciokilo=0

while True:
    peso=input("Ingrese el peso(entre 10 y 100 kilos)\n")
    peso=int(peso)
    while peso<10 or peso>100:
        peso=input("Ingrese correctamente el peso(entre 10 y 100 kilos)\n")
        peso=int(peso)    
    
    precio_por_kilo=input("Ingrese el precio por kilo\n")
    precio_por_kilo=int(precio_por_kilo)
    while precio_por_kilo<1:
        precio_por_kilo=input("El precio debe ser mayor a 0 \n")
        precio_por_kilo=int(precio_por_kilo)

    tipo=input("Ingrese el tipo ('v' para vegetal,'a' para animal o 'm' para mezcla)\n")
    while tipo!='v' and tipo!='a' and tipo!='m':
        tipo=input("Ingrese correctamente el tipo('v','m' o 'a')\n")

    acumulador_kilos=acumulador_kilos+peso
    precio_bruto=peso*precio_por_kilo
    acumulador_precios_brutos=acumulador_precios_brutos+precio_bruto
    acumulador_precio_porkilo=acumulador_precio_porkilo+precio_por_kilo
    contador_preciokilo=contador_preciokilo+1
    
    if flag_alimento_caro:
        tipo_alimento_caro=tipo
        precio_alimento_caro=precio_por_kilo
        flag_alimento_caro=False
    elif precio_alimento_caro<precio_por_kilo:
        tipo_alimento_caro=tipo
        precio_alimento_caro=precio_por_kilo       


    rta = input("Para salir pulse (s)")
    if(rta == 's'):
        break

if acumulador_kilos>300:
    precio_con_descuento=acumulador_precios_brutos*descuento_trecientos_kilos
elif acumulador_kilos>100:
    precio_con_descuento=acumulador_precios_brutos*descuento_cien_kilos
else:
    precio_con_descuento="No le corresponde ningun descuento"

promedio_precio_kilo=acumulador_precio_porkilo/contador_preciokilo

print("El precio bruto a pagar es: ",acumulador_precios_brutos,"\n")
print("El precio a pagar con descuento es: ",precio_con_descuento,"\n")
print("El tipo de alimento mas caro es: ",tipo_alimento_caro,"\n")
print("El promedio de precio por kilo es: ",promedio_precio_kilo)


