flag_mas_joven =True
heroe_joven=0
edad_heroe=0
heroe_mayor=0
flag_heroe_mayor=0
edad_heroe_mayor=0
contador_heroinas=0
cantidad_heroinas=0
acumulador_edades_heroinas=0
promedio_heroes=0
cantidad_heroes=0
acumulador_edades_heroes=0

while True:
    nombre=input("Ingrese el nombre de Heroína/Héroe\n")

    edad=input("Ingrese su edad\n")
    edad=int(edad)
    while (edad<19):
        edad=input("Ingrese nuevamente la edad(debe ser mayor de 18)\n")
        edad=int(edad)
    
    sexo=input("Ingrese el sexo('f','m' o 'nb')\n")
    while (sexo!='m' and sexo!='f' and sexo!='nb'):
        sexo=input("Ingrese correctamente el sexo\n")
    
    habilidad=input("Ingrese la habilidad('fuerza','magia' o 'inteligencia)\n")
    while (habilidad!='fuerza' and habilidad!='magia' and habilidad!='inteligencia'):
        habilidad=input("Ingrese correctamente la habilidad\n")

    if(habilidad=='fuerza'):
        if(sexo=='m'):
            cantidad_heroes=cantidad_heroes+1
            acumulador_edades_heroes=acumulador_edades_heroes+edad           
        if(flag_mas_joven):
            edad_heroe=edad
            heroe_joven=nombre
            flag_mas_joven=False
        elif (edad_heroe>edad):
            edad_heroe=edad
            heroe_joven=nombre

    if flag_heroe_mayor:
        edad_heroe_mayor=edad
        heroe_mayor=nombre
        flag_heroe_mayor =False
    elif(edad_heroe_mayor<edad):
        edad_heroe_mayor=edad
        heroe_mayor=nombre

    if(sexo=='f'):
        cantidad_heroinas=cantidad_heroinas+1
        acumulador_edades_heroinas=acumulador_edades_heroinas+edad
        if(habilidad=='magia' or habilidad=='fuerza'):
            contador_heroinas=contador_heroinas+1
            

    rta = input("Para salir pulse (s)")
    if(rta == 's'):
        break

promedio_heroinas=acumulador_edades_heroinas/cantidad_heroinas
promedio_heroes=acumulador_edades_heroes/cantidad_heroes

print("El Heroe/Heroina mas joven de 'fuerza' es: ",heroe_joven,"con ",edad_heroe," años \n")
print("El Heroe/Heroina mayor es: ",heroe_mayor,"con ",edad_heroe_mayor," años\n")
print("La cantidad de Heroinas con 'magia' o 'fuerza' son: ",contador_heroinas,"\n")
print("El promedio de edad de las Heroinas es: ",promedio_heroinas,"\n")
print("El promedio de edad de los Heroes de 'fuerza' es: ",promedio_heroes,"\n")