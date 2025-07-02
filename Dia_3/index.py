"""Práctica Método Index() 1
Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"""""
#cuando se habla de Index se refiere a la posición de un elemento dentro de una lista, cadena de texto, etc.
palabra = "ordenador"

buscar = palabra[4]# El índice comienza en 0, por lo que la quinta posición es el índice 4

print(buscar)
#---------------------------------------------
"""Práctica Método Index() 2
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."""""

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
buscar = frase.index("práctica")  # Encuentra el índice de la primera aparición de "práctica"
print(buscar)  # Imprime el índice de la primera aparición de "práctica"
#---------------------------------------------
"""Práctica Método Index() 3
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."""""
buscar = frase.rindex("práctica")  # Encuentra el índice de la última aparición de "práctica"
print(buscar)  # Imprime el índice de la última aparición de "práctica"
#---------------------------------------------
#final de las prácticas del método index, exitosanente