"""El slicing es una técnica en Python que permite acceder a una porción de una secuencia (como una lista,
cadena de texto, etc.) especificando un rango de índices. Se utiliza la sintaxis `secuencia[inicio:fin]`,
donde `inicio` es el índice del primer elemento que se quiere incluir y `fin` es el índice del primer...
elemento que no se quiere incluir."""
#Ejemplos usados en el curso:
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Cadena de texto organizada alfabéticamente para facilitar la comprensión
fragment = text[2:4] #Obtención de una porcion de la cadena de texto desde el índice 2 hasta el 4 (sin incluir el 4)
print(fragment)

#Práctica Sub-Strings 1
"""Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
"Controlar la complejidad es la esencia de la programación"
Pista: "Controlar" tiene un largo de 9 caracteres."""
phrase = "Controlar la complejidad es la esencia de la programación"
fragment2 = phrase[0:9] # Extrae la primera palabra "Controlar"
print(fragment2)

#Práctica Sub-Strings 2
"""Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
'Nunca confíes en un ordenador que no puedas lanzar por una ventana'"""
phrase2 = 'Nunca confíes en un ordenador que no puedas lanzar por una ventana'
fragment3 = phrase2[8::3]  # Toma cada tercer caracter desde el noveno hasta el final
print(fragment3)

#Práctica Sub-Strings 3
"""Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.

'Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza'"""
phrase4 = 'Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza'
fragment4 = phrase4[::-1]  # Invierte la cadena de texto
print(fragment4)