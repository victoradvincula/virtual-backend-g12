from pyclbr import Function
from typing import Type


nombre = "Victor"
edad=30
print(nombre)
print(edad)

#variables de texto se define con ""
apellido = "Advincula"
print(nombre + " " +apellido)

#si queremos tener un texto que pueda contener saltos de linea utilizar """
descripcion2 = """hola amigos ¿Como estan?:
Muy bien"""
print(descripcion2)

num1 = 10
num2 = 20
print(num1+num2)    

#variables numericas
year = 2022

#type() mostrara tipo de variable
print(type(year))
print(type(descripcion2))

#python no se puede crear variable sin un contenido
#en python None = null | undefined
variable = None
print(type(variable))

#en Python  no hace validacion del tipo de dato primario (si la variable "nace" siendo string se puede cambiar su tipo de dato
# a otro)
# en Python no existen las constantes

dni = [12345679]
dni = "peruano"
dni = False

#id() brindara la ubicacion de esa variable en relacion a la memoria del dispositivo
print(id(dni))

#definicion de varias variables
mes, dia = "marzo", 1
print(mes,dia)

#del > elimina la variable de la memoria
#si queremos usar luego de eliminar esa variable no se podra utilizar por que ya se borro de la memoria
del dia
print(dia)