#Repaso Administrador de peliculas
'''
Instrucciones:
1- crear una lista que simulara una base de datos de peliculas con al menos 3 peliculas
2- Solicitar una accion: agregar, eliminar, mostrar o salir
3- Sentencias condicionales para cada accion
    - Agregar: Solicitar el nombre de la pelicula y agregarla a la lista
    - Eliminar: Solicitar el nombre de la pelicula y eliminarla de la lista si
        existe, si no, mostrar un mensaje de error
    - Mostrar: Mostrar todas las peliculas en la lista
    - Salir: Terminar el programa
    - Opcion no valida: Mostrar un mensaje de error
'''

movies = ['Interstellar', 'Ready player one', 'Juego de honor']

print('\nNota: Solo podras realizar una opcion a la vez, si deseas realizar otra, vuelve a iniciar el programa')
opcion = str(input('Ingresa la opcion que deseas realizar: agregar, eliminar, mostrar o salir:\n')).lower()

if opcion == 'agregar':
    new_movie = str(input('Ingresa el nuevo titulo que quieres agregar:\n')).title()
    movies.append(new_movie)
    print(f'Has agregado la pelicula: {new_movie}\nLista actualizada de peliculas: {movies}')
