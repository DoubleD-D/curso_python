#Variables que guardan un dato (Cadena de caracteres) ingresada por el usuario
from traceback import print_tb

nombre = input("Ingresa tu nombre: ")

print("Tu nombre es: "+nombre)

#Para números no se agregan las comillas
edad = input("Ingresa tu edad: ")

print("Tu edad es: " + edad)

#Concatenar variables dentro de otra variable
nombre = "Hola "
nombre2 = "Como estas?"
frase = nombre + nombre2

print(frase)

#Integers y floats
mi_numero = 1
print(mi_numero)
print(type(mi_numero))#"type" muy útil para saber de que tipo de variable hablamos