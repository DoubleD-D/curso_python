#Conversion de tipos de datos, ya sea de Integer a Flotanteo viceversa
#Hay dos tipos: Implicitos y explicitos
#Implicitos: Los hace sin darnos cuenta el mismo python------ Explicitos: Los hacemos nosotros mediante codigo

#Ejemplo de cambio inplicito, al sumar los numeros se convirtio en un flotante
num1 = 20
num2 = 30.5

num1 += num2

print(num1)
print(type(num1))
#-------------------------------------
#Ejemplo de cambio explicito
n = 7.8
n2 = int(n)
print(n2)
print(type(n2))
#-------------------------
edad = int(input("Ingresa tu edad: "))
print(edad)
print(type(edad))

nueva_edad = 1
edad += nueva_edad
print(f"El siguiente anio cumpliras {edad}")
