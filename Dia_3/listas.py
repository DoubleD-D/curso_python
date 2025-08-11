#Las listas en python son colecciones ordenadas y mutables de elementos, que pueden ser de diferentes tipos.
mi_lista = ['a', 'b', 'c']
print(type(mi_lista))  # Imprime el tipo de la variable mi_lista

print('--'*10 + 'Lista con diferentes valores' + '--'*10 + "\n")  # Imprime una línea de separación
my_list = ['hola', 1, 2.3, True, None]  # Lista con diferentes tipos de datos
print(my_list)  # Imprime la lista con diferentes tipos de datos
print(type(my_list))  # Imprime el tipo de la variable my_list

print('--'*10 + 'Buscar un elemento de la lista' + '--'*10 + "\n")  # Imprime una línea de separación
#En las listas también puedes buscar elementos por el índice, que comienza en 0.
print(mi_lista[0])  # Imprime el primer elemento de la lista mi_lista
print(my_list[1])  # Imprime el segundo elemento de la lista my_list
print(my_list[0:3])  # Imprime los primeros tres elementos de la lista my_list

#Concatenación de listas
print('--'*10 + 'Concatenación de listas' + '--'*10 + "\n")  # Imprime una línea de separación
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2  # Concatenación de dos listas
print(lista_concatenada)  # Imprime la lista concatenada

#Remplazamiento de elementos en una lista
print('--'*10 + 'Remplazamiento de elementos en una lista' + '--'*10 + "\n")  # Imprime una línea de separación
lista = [1, 2, 3, 4, 5]
print('Lista original:', lista)  # Imprime la lista original
lista[0] = 10  # Reemplaza el primer elemento de la lista por 10
print('Lista modificada:', lista)

#Añadir y eliminar elementos de una lista
print('--'*10 + 'Añadir y eliminar elementos de una lista' + '--'*10 + "\n")  # Imprime una línea de separación
lista = [1, 2, 3]
print('Lista original:', lista)
lista.append(4)  # Añade el elemento 4 al final de la lista
print('Lista después de añadir 4:', lista)  # Imprime la lista después de añadir el elemento 4
lista.pop(1)  # Elimina el elemento en el índice 1 de la lista
print('Lista después de eliminar el elemento en el índice 1:', lista)  # Imprime la lista después de eliminar el elemento en el índice 1

#Ordenar una lista
print('--'*10 + 'Ordenar una lista' + '--'*10 + "\n")  # Imprime una línea de separación
lista = [10,4,3,2,6,11,12,1,5,7,3,3,3]
lista.sort()
print(lista)  # Imprime la lista ordenada
#Método más rápido para ordenar una lista
print(sorted([10,4,3,2,6,11,12,1,5,7,3,3,3]))#El defecto de este es que debes de agregar la lista a ordenar como argumento, y no modifica la lista original