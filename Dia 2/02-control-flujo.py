#IF ELSE

from ast import If

edad=int(input("ingresa tu edad"))
#asi convertimos el str a int
if (edad>18):   
    print("la persona es mayor de edad")
elif (edad>15):
    print("la persona es adolescente")
elif (edad>10):
    print("la persona es una niño")
else:   
    print("la persona es menor de edad")

print("finalizo el programa")

#Validar si un numero (ingresos de una persona) ingresado por teclado es :
# * mayor a 500: indicar que no recibe el bono yanapay 
# * entre 500 y 250: indicar que si recibe el bono 
# * es menor que 250: indicar que recibe el bono y un balon de gas 
# RESOLUCION DEL EJERCICIO

ingreso =int(input("ingrese monto: "))

if (ingreso>500):
    print("no recibes el bono")
elif (ingreso >= 250 and ingreso <= 500):
    print("recibes bono yanapay")
else:
    print("recibe el bono y su balon de gas")