#Para redondear los números que tengan demásiados números decimales se útiliza "round"
#A continuación la sintaxis
#Nota, redondea al número más cercano, si es .5 redondea al número par más cercano, ojo número par más cercano

x = 7
y = 90

print(round(y/x,1))
#--------------------------------------------

redondeoPar = 3.5
redondeoNoPar = 2.5

print(round(redondeoPar))  # Redondea a 4, el número par más cercano
print(round(redondeoNoPar)) # Redondea a 2, el número par más cercano