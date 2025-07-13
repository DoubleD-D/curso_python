"""Lo metodos de cadena de texto son funciones que permiten
 manipular y transformar cadenas de texto en Python."""
# Ejemplos usados en el curso:
text = "Este es mi texto de ejemplo"
mostrar = text #Mostrar solo el texto original
print(mostrar)

mostrar = text.upper()  # Convierte todo el texto a mayúsculas
print(mostrar)

mostrar = text.lower()  # Convierte todo el texto a minúsculas
print(mostrar)

mostrar = text.title()  # Convierte la primera letra de cada palabra a mayúscula
print(mostrar)

#Split
mostrar = text.split()  # Divide el texto en palabras y las convierte en una lista
print(mostrar)
#Si le pasamos un argumento, divide el texto por ese argumento, ejeplo:
mostar = text.split('e')#divide el texto por la letra 'e', sin tomar la E mayúscula
print(mostar)

#Join
a = 'Join'
b = 'junta'
c = 'elementos'
mostrar = ' '.join([a, b, c])  # Une los elementos de la lista con un espacio
print(mostrar)

#Find
text_find = "Find buscara un caracter o subcadena en una cadena de texto"
mostrar = text_find.find('subcadena')  # Busca la primera aparición de 'mi' y devuelve su índice
print(mostrar)

#Replace
text_replace = "Replace reemplaza un caracter o subcadena por otro"
mostrar = text_replace.replace('e', 'x')  # Reemplaza la primera 'e' por 'x'
print(mostrar)

#Práctica Métodos de String 1
"""Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:"""
frase = "Especialmente en las comunicaciones electronicas, la escritura enteramente en mayusculas equivale a gritar."
mostrar = frase.upper()  # Convierte todo el texto a mayúsculas
print(mostrar)

#Práctica Métodos de String 2
"""Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado."""
lista_palabras = ["La","legibilidad","cuenta."]
print(' '.join(lista_palabras))  # Une los elementos de la lista con un espacio

#Práctica Métodos de String 3
"""Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:
"difícil" --> "fácil"
"mala" --> "buena"
y muestra en pantalla la frase con ambas palabras modificadas."""
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
mostrar = frase.replace("difícil", "fácil").replace("mala", "buena")  # Reemplaza las palabras
print(mostrar)