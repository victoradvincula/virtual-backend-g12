# Tuplas //
# muy similar a la lista PERO NO SE PUEDE CAMBIAR LOS VALORES

cursos = ("backend", "frontend", 1, True)

print(cursos)
print(cursos[0])
print(cursos[0:1])
# desde la posicion de 0 hasta pa posicion <1

# en la tupla no podemos alterar los valores dpertenecientes a ella
# Pero si dentro de esta hay listas u otra coleccion de datos podemos modificarla sin problemas
variada = (1, 2, 3, [4, 5, 6])
variada[3][0] = "hola"
# posicion 3 y dentro de este lista posicion 0

print(variada)

print(2 in variada)
variada2 = list(variada)
# creamos una nueva lista a partir de una Tupla llamando a la clase list
# esta clase crea una nueva lista con los valores de la tupla
print(variada2)

print(list((1, 2, 3)))  # [],2,3]

# para ver la cantidad de elementos que conforman una tupla o una lista
# NOTA: la longitud siempre sera la cantidad de elementos y esta siempre empezara en 1
# Mientas posicion siempre empezara en 0. es por eso que siempre la longitud  = posicion+1

print(len(variada))


# CONJUNTOS //
# coleccion de datos DESORDENADA, una vez que se crea ya no se accede a las posiciones de sus elementos
estaciones = {"verano","otono","primavera","invierno"}
#una vez que se crea se agina una posicion aletoria
print(estaciones)
estaciones.add("otro")
print(estaciones)

#pop() > quita el ultimo elemento de la coleccion de datos (list,tuplas,set(conjuntos))
estacion = estaciones.pop()
print(estacion)

#DICCIONARIOS
#una coleccion de datos DESORDENADA  pero cada elemento obedece a una llave definida

persona={
    "nombre":"eduardo",
    "apellido":"de rivero",
    "correo":"victor@adv.com.pe"
}

print(persona["correo"])
print(persona.keys())
#devuelve todas las llaves de mi diccionario
print(persona.values())
#me devuelte todo el contenido del diccionario
print(persona.get("apellidos","No Existe"))
#el metodo get busca la llave si no lo encuentra no retonara un Error
print(persona.items())
#items devuelve todas las llaves y su contenido en forma de tuplas dentro de una lista
persona["edad"]=28
#si definimos una llave que no existe , la creara, caso contrario modificara su valor
persona["nombre"]= "Marco"
print(persona)
# eliminar una llave de una diccionario
persona.pop("apellido")
print(persona)