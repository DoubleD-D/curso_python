#Repaso de lo anterior visto para poder seguir con el curso

#Calculadora de viajes - Repaso
'''Intrucciones:
1- Pedirle al usuario que ingrese su nombre
2- preguntarle al usuario la distancia del viaje en kilometros (Entero)
3- Preguntarle el costo de la gasolina por litro (Decimal)
4- Pedirle el rendimiento del vehiculo en kilometros por litro (Decimal)
5- Calcular el costo total de la gasolina para el viaje (Regla de 3)
6- Pedirle al usuario que ingrese el numero de personas que van a viajar
7- Calcular el costo por persona del viaje (solo de la gas)
8- Al final, muestra un resumen completo usando f-strings. El resultado debe mostrar:
    El nombre del usuario, usando la primera letra en mayúscula y el resto en minúscula.
    La distancia total del viaje.
    El costo total del viaje, redondeado a dos decimales.
    El costo por persona, también redondeado a dos decimales.
    El resultado debe ser similar a: Hola Sebastián, el costo total para tu viaje de 500 km es de $500.50. El costo por persona es de $125.13.'''

name = input('Ingrese su nombre: ').title()
distance = int(input('Ingrese la distancia del viaje en kilometros: '))
gasoline = float(input('Ingrese el costo de la gasolina por litro: '))
rendimiento_vehiculo = float(input('Ingrese el rendimiento del vehiculo: '))

costo_total_gasolina = float(((gasoline * distance) / rendimiento_vehiculo))

personas = int(input('Ingrese la personas que van a viajar: '))
costo_por_persona = (costo_total_gasolina / personas)

print(f'Hola {name}, el viaje que desea realizar de: {distance}km \ncostara un total de ${round(costo_total_gasolina,2)} debido al precio de la gasolina.\n Viajaran {personas} personas en este viaje, por lo que cada persona debera aportar ${round(costo_por_persona,2)} de la gasolina.')