#Para este proyecto se pide realizar un programa que calcule las comiciones de empleados. El empleado introduce...
#Cuanto fue su venta del mes y su nombre y se da la leyenda de "Ok, {nombre} has comisionado ${comision} este mes"

nombre = input("Ingresa tu nombre\n:")
venta = int(input("Ingresa la venta del mes\n :$"))

comision = ((venta * 13)/100)

print(f"Ok, {nombre} has comisionado ${round(comision, 2)} este mes. Felicidades!!")