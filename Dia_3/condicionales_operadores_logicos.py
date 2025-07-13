"""En este programa aprenderemos a usar condicionales en conjunto con operadores lógicos.
Los operadores lógicos son `and`, `or` y `not`. Estos operadores se utilizan para combinar o invertir condiciones"""
import os
os.system('cls')
# Ejemplo de uso de operadores lógicos
edad = int(input("Ingrese su edad: "))
if edad >= 18 and edad < 65:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un adulto mayor.")
elif edad < 18 and edad >= 13:
    print("Eres un adolescente.")
else:
    print("Eres un niño o niña.")
# Ejemplo de uso de operador lógico `or`
nombre = input("Ingrese su nombre: ")
if nombre == "Juan" or nombre == "Maria":
    print("Hola Juan o Maria")
else:
    print("Hola, no eres Juan ni Maria")
# Ejemplo de uso de operador lógico `not`
contraseña = input("Ingrese su contraseña: ")
validar_contraseña = "1234"
if not contraseña == validar_contraseña:
    print("Contraseña incorrecta")
else:
    print("Contraseña correcta")