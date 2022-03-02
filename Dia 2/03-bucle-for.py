numeros =[10,20,16,8,6,1]

print (numeros)

#en cada iteracion de la lista notas tendremos su valor y los almacenaremos en una variable llamada nota
#el mismo funcionamiento se da para cualquier coleccion de datos
#(lista, tupla, diccionario, conjunto)
# for numero in numeros:
#     print (numero)

for numero in range (10):
    print (numero)
#RANGE crea una clase que se detiene en el numero <10
for numero in range (5,10):
    print (numero)
#si colocamos 2 parametros el primero significara el numero incial y el segundo el tope
for numero in range (5,20,2):
    print (numero)
#el terce parametro significa en cuanto hara el incremento o decremento
#empezara en 5 hasta <20 y en se incrementara en 2 unidades
for numero in numeros[0:3]:
    print(numero) #[10, 20, 16]
