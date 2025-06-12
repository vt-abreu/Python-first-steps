#Create a program to ask the quantity of km of a car.
#The quantity of days this car was rented.
#And calculate the price to be paid by rental.
#Note: each day costs 60€ and each km costs 0.15€.
#Example: p = (km * 0.15) + d * 60.

km = float(input('Digite quantos quilometros foram rodados: '))
d = int(input('Digite quantos dias foram utilizados '))

print('\nO valor a ser pago é de: €{:.2f}'.format((km * 0.15) + d * 60))