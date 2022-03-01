nombre = "victor"

print(nombre)
#concatenar 
print("El nombre es:",nombre,"del usuario")

estacivil= "soltero"

#si queremos usar el metodo format tenemos que usar la misma cantidad de variables que las {}
#en la declaracion
print("La persona {} es {}".format(nombre,estacivil))

#ademas se puede agregar la posicion de la variable que queremos imprimir dentro de las llaves
print("{1} es una persona {0}".format(estacivil,nombre))