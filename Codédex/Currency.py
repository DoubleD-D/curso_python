'''We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.'''

#Pesos colombianos a USD
CO = float(input('Ingresa el monto en pesos colombianos: '))
#Soles peruanos a USD
PE = float(input('Ingresa el monto en soles peruanos: '))
#Reales brazilenos a USD
BR = float(input('Ingresa el monto en reales: '))

#Operaciones para convertir los montos en USD
CO_to_USD = (CO * 0.0002736)
PE_to_USD = (PE * 0.2989)
BR_to_USD = (BR * 0.1929)

#Total de dolares
total = CO_to_USD + PE_to_USD + BR_to_USD
print(f'El monto total en USD es de: ${total:.2f}')
print(f'Esto obtenido de sumar {CO_to_USD:.2f} plus {PE_to_USD:.2f} y {BR_to_USD:.2f}')