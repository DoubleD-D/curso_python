#Para este proyecto se pide realizar un programa que calcule las comiciones de empleados. El empleado introduce...
#Cuanto fue su venta del mes y su nombre y se da la leyenda de "Ok, {nombre} has comisionado ${comision} este mes"
"""Nota: python es de tipado fuerte, por lo que si se introduce un número con decimales...
# este se debe convertir a float o int"""


nombre = input("Ingresa tu nombre\n:")
venta = input("Ingresa el monto de tu venta del mes\n: $")

comision = 0.13 * float(venta)  # Convertimos la venta a float para poder calcular la comisión

print(f"Ok, {nombre} has comisionado ${round(comision, 2)} este mes. Felicidades!!")

print("---- Fin del programa ----")
print("Gracias por usar este programa :)")
print("Recuerda que la comision es 13% de tu venta mensual")
print("Hasta la proxima")
print()
print("Si quieres volver a calcular, vuelve a iniciar el programa")

"""Intento de crear un bucle para que el usuario pueda calcular su comisión varias veces sin reiniciar el programa,
aun en proceso de aterrizar la lógica"""

"""while True:
    opcion = int(input("¿Quieres calcular tu comisión? (1: Sí, 2: No)\n: "))
    if opcion == 1:
        try:
            venta = float(venta)
            comision = venta * 0.13
            print(f"Ok, {nombre} has comisionado ${round(comision, 2)} este mes. Felicidades!!")
        except ValueError:
            print("Por favor, introduce un número válido para la venta.")
    elif opcion == 2:
        print("---- Fin del programa ----")
        print("Gracias por usar este programa :)")
        print("Recuerda que la comision es 13% de tu venta mensual")
        print("Hasta la proxima")
        break
    else:
        print("Opción no válida, por favor elige 1 o 2.")"""