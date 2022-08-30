#La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
#El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.

# Se debe informar lo siguiente:
#Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#Del ítem con más unidades, el fabricante.
#Cuántas unidades de jabones hay en total

flag_barbijo_caro = True
cantidad_barbijos = 0
cantidad_alcohol = 0
cantidad_jabon = 0
acumulador_jabones = 0

for i in range(5):
    producto = input("Ingrese el producto 'barbijo' , 'jabon' o 'alcohol' \n ")
    while(producto != 'barbijo'and producto != 'jabon' and producto != 'alcohol'):
        producto = input("Ingrese el producto 'barbijo' , 'jabon' o 'alcohol' \n ")

    precio=input("Ingrese el precio \n")
    precio=int(precio)

    while( precio < 100 or precio > 300 ):
        precio=input("Ingrese el precio entre 100 y 300 \n ")
  
    unidades=input("Ingrese la cantidad de unidades \n")
    unidades=int(unidades)
    

    while( unidades < 0 or unidades > 1000 ):
        unidades=input("Ingrese el unidades entre 1 y 1000 ")

    marca=input("Ingrese la marca  \n")
    fabricante=input("Ingrese el fabricante  \n")

    if(producto=='jabon'):
        cantidad_jabon= cantidad_jabon + unidades
        acumulador_jabones += unidades

    if(producto=='alcohol'):
        cantidad_alcohol=cantidad_alcohol + unidades 

    if(producto =='barbijo'):
        cantidad_barbijos = cantidad_barbijos + unidades

        if(flag_barbijo_caro):
        
            barbijo_caro = precio
            unidades_barbijo_caro = unidades
            fabricante_barbijo_caro = fabricante
            flag_barbijo_caro = False
        elif(barbijo_caro < precio):
            barbijo_caro = precio
            unidades_barbijo_caro = unidades
            fabricante_barbijo_caro = fabricante 

    if(cantidad_alcohol>cantidad_barbijos and cantidad_alcohol>cantidad_jabon):
        fabricante_mas_unidades = fabricante
        item_mas_unidades = producto
    elif(cantidad_barbijos>cantidad_alcohol and cantidad_barbijos>cantidad_jabon):
        fabricante_mas_unidades = fabricante
        item_mas_unidades = producto
    else:
        fabricante_mas_unidades = fabricante
        item_mas_unidades = producto


print("El  fabricante del barbijo mas caro es:",fabricante_barbijo_caro,"\n")
print("Hay ",unidades_barbijo_caro," unidades del barbijo mas caro \n")
print("El item con mas unidades es: ",item_mas_unidades," y su fabricante es: ",fabricante_mas_unidades,"\n")
print("La cantidad de jabones en total es:",acumulador_jabones)