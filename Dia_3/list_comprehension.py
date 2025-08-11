"""List comprehension en Python permite crear listas de manera concisa y eficiente.
Se utiliza una sintaxis compacta que combina la creación de listas con un bucle for y
una condición opcional."""

"""Dado los enteros x, y, z y n, quieres construir una lista de todas las coordenadas posibles (i, j, k) 
con 0 ≤ i ≤ x, 0 ≤ j ≤ y y 0 ≤ k ≤ z, excepto aquellas cuya suma i + j + k sea igual a n.
La salida debe estar en orden lexicográfico, i.e., como lo genera el list comprehension."""

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
z = int(input("Ingrese el valor de z: "))
n = int(input("Ingrese el valor de n: "))

# Generar la lista de coordenadas utilizando list comprehension
result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]
print(result)