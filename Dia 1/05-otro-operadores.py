# OPERADORES DE COMPARACION
num1, num2 = 10, 20
# igual que
print(num1 == num2)
# mayor que | mayor igual que
print(num1 > num2)
print(num1 >= num2)
# menor que | menor igual que
print(num1 < num2)
print(num1 <= num2)
# diferente
print(num1 != num2)

# operadores logicos
# sirve para varias condiciones
print((10 < 5) and (10 < 20))  # ambas tienen que ser verdadero
print((10 > 5) or (10 < 20))  # al menos uno tiene que ser verdadero

# operadores de identidad
# is
# is not
# sirve para ver si estan apuntando a la misma direccion de memoria

verduras = ["apio", "lechuga", "zapallo"]
verduras2 = verduras
verduras3 = ["apio", "lechuga", "zapallo"]

verduras2[0] = "perejil"
verduras[1] = "manzana"
# el metodo copy() genera una copia de la varaible en una nueva posicion en la memoria
verduras4 = verduras.copy()
verduras4[0] = "huacatay"
print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)

print("la posicion es", id(verduras))
print("la posicion es", id(verduras2))
print("la posicion es", id(verduras4))

# si hablamos de variables primitivas (str, int, float, boolean, date) entonces al hacer la copia compartira
# su contenido y posicion en la memoria PERO al hacer alguna modificacion a las variables que esten usando
# el mismo espacio python automaticamente les asignara una nueva posicion

nombre10 = "victor"
nombre2 = nombre10
print(nombre2 is nombre10)
print(id(nombre2))
print(id(nombre10))
nombre2 = 1
print(nombre10)
print(id(nombre2))
print(id(nombre10))


# validar si el nombre del usuario es eduardo y que sea peruano o colombiano

nombre = "eduardo"
nacionalidad = "peruano"

print((nombre == "eduardo") and (nacionalidad == "colombiano" or nacionalidad=="peruano"))
