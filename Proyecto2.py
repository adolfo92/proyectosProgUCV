#Proyecto2.py

import random

import os

def mazoNuevo(): # Creo una función de mazo nuevo

	cartas=[]

	palos = ["trebol", "espadas", "corazones", "diamantes"]

	for i in range(10) :

		n = str(i+1)

		cartas.append(n + " trebol")
		cartas.append(n + " corazones") 
		cartas.append(n + " diamantes") 
		cartas.append(n + " espadas")


	for palo in palos:

		cartas.append("J " + palo)
		cartas.append("Q " + palo)
		cartas.append("K " + palo)

	return cartas


#--- Comienzo de la partida

cartas = mazoNuevo() # Creo un mazo nuevo

random.shuffle(cartas) #Barajeo las cartas

print("Primera mano, de hacen apuestas\n")

# --------- apuesta

apuestaPlayer = int(input("Cuanto apuestas?: \n"))

apuestaCasa = apuestaPlayer

print("\nApuesta Jugador: ", apuestaPlayer, "\nApuesta Casa: ", apuestaCasa, "\n")

print("No va más\n")

# --------- Muestro mi apuesta



cartasPlayer=[cartas.pop(0),cartas.pop(1)]




cartasCasa = [cartas.pop(0)] # La casa comienza con una sola carta

print(cartasCasa, "\n")

while True:
	print("Cartas del jugador:\n")
	print(cartasPlayer, "\n")
	print("Cartas de la casa:\n")
	print(cartasCasa, "\n")
	print("Apuesta en mesa: ",apuestaPlayer,"$\n")


	opcion = int(input("Que deseas hacer?\n1 Pedir carta \n2 Doblar \n3 Plantarse \n4 Separar\n"))

	if opcion == 1:

		cartasPlayer.append(cartas.pop(0))

		print("Cartas del jugador:\n", cartasPlayer,"\n")

		#Chequeo la suma de la casa
		suma = 0

		for carta in cartasCasa: 

			try: 
				suma = suma + int(carta[0:2]) # 

			except:

				suma = suma + 10

		if suma < 17: #Si la cas tiene menos de 17, agarra carta

			cartasCasa.append(cartas.pop(0))

		else:

			print("La casa de planta\n")

		print("Cartas de la casa:\n", cartasCasa,"\n")

		#Acá declaro las sumas de los valores en las cartas

		

		# Como una cadena de caracteres en una lista es una lista dentro de otra lista, voy a buscar el primer termino de la lista en cada elemento de la lista superior
		# y cconvertirlo en int para mostrar la suma de los valores de cartas en mano.
		suma = 0

		for carta in cartasPlayer: # Utilizo try/except para lidiar con la posibilidad de que me rebote las letras J,Q,K y ahorrarme el IF statement

			try: 
				suma = suma + int(carta[0:2]) # 

			except:

				suma = suma + 10


		print("Tus cartas suman: ", suma)

		if suma > 21:

			print("Perdiste la mano, gana la casa")

			break

		# -----------Ahora para la casa
		suma = 0

		for carta in cartasCasa: 

			try: 
				suma = suma + int(carta[0:2]) # 

			except:

				suma = suma + 10

		print("La casa suma: ", suma)

		if suma > 21:

			print("Perdio la casa, gana el jugador")

			break


	if opcion == 2:

		apuestaPlayer = apuestaPlayer*2

		apuestaCasa = apuestaCasa*2


	#if opcion == 3:

	#if opcion == 4:



"\n"
