#Proyecto2.py

import random

import os # Para poder limpiar la consola

import sys # Para finalizar el programa

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

dinero = int(input("Cuanta plata vas a disponer para toda la partida?: \n"))

while True:

	inicio = True

	os.system('clear')

	print("Cuentas con: ", dinero)
	#--- Comienzo de la partida

	if dinero == 0:

			print("Te quedaste sin plata")

			break

	cartas = mazoNuevo() # Creo un mazo nuevo

	random.shuffle(cartas) #Barajeo las cartas

	print("Primera mano, se hacen apuestas\n")

	# --------- apuesta

	apuestaPlayer = int(input("Cuanto apuestas?: \n"))

	prueba = dinero-apuestaPlayer # Chequeo si tengo los fondos para doblar

	if prueba < 0:

		print("\nNo puedes apostar tanto\n")

		continue

	else:

		dinero = dinero - apuestaPlayer

	apuestaCasa = apuestaPlayer

	print("\nApuesta Jugador: ", apuestaPlayer, "\nApuesta Casa: ", apuestaCasa, "\n")

	print("No va más\n")

	# --------- Muestro mi apuesta



	cartasPlayer=[cartas.pop(0),cartas.pop(1)]

	cartasCasa = [cartas.pop(0)] # La casa comienza con una sola carta

	while True:

		print("Cartas del jugador:\n")
		print(cartasPlayer, "\n")
		print("Cartas de la casa:\n")
		print(cartasCasa, "\n")
		print("Apuesta en mesa: ",apuestaPlayer,"$\n")


		opcion = int(input("Que deseas hacer?\n1 Pedir carta \n2 Doblar \n3 Plantarse \n4 Separar\n5 Finalizar\n"))

		if opcion == 5:

			sys.exit(0)




		if opcion == 1:

			inicio = False

			os.system('clear')

			cartasPlayer.append(cartas.pop(0))

			print("Cartas del jugador:\n", cartasPlayer,"\n")

			#Chequeo la suma de la casa
			suma = 0

			for carta in cartasCasa: 

				try: 
					suma = suma + int(carta[0:2]) # 

				except:

					suma = suma + 10

			if suma < 17: #Si la casa tiene menos de 17, agarra carta

				print("\nLa casa pide carta\n")

				cartasCasa.append(cartas.pop(0))

			else:

				print("La casa se planta\n")

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


			print("Tus cartas suman: ", suma, "\n")

			if suma > 21:

				print("\nPerdiste la mano, gana la casa")

				print("\nCuentas con: ", dinero)

				op = input("\nQuires seguir jugando?  y  /  n\n")

				if op == "y":

					break

				else:
					
					sys.exit(0)

			# -----------Ahora para la casa
			suma = 0

			for carta in cartasCasa: 

				try: 
					suma = suma + int(carta[0:2]) # 

				except:

					suma = suma + 10

			print("La casa suma: ", suma, "\n")

			if suma < 17: #Si la casa tiene menos de 17, agarra carta

				print("\nLa casa pide carta\n")

				cartasCasa.append(cartas.pop(0))

			if suma > 21:

				print("\nPerdio la casa, gana el jugador")

				print("\nCuentas con: ", dinero)

				op = input("\nQuires seguir jugando?  y  /  n\n")

				if op == "y":

					break

				else:
					
					sys.exit(0)


		if opcion == 2:

			if inicio is False:

				print("\nNo puedes realizar esta accion\n")

			else:

				inicio = False

				os.system('clear')

				prueba = dinero-apuestaPlayer # Chequeo si tengo los fondos para doblar

				if prueba < 0:

					print("\nNo puedes apostar tanto\n")

				else:

					dinero = prueba

					apuestaPlayer = apuestaPlayer*2

					apuestaCasa = apuestaPlayer


					print("\nApuesta en mesa: ",apuestaPlayer,"\n" ) # Al doblar se te da otra carta


					cartasPlayer.append(cartas.pop(0))



					suma = 0

					for carta in cartasPlayer: # Utilizo try/except para lidiar con la posibilidad de que me rebote las letras J,Q,K y ahorrarme el IF statement

						try: 
							suma = suma + int(carta[0:2]) # 

						except:

							suma = suma + 10


					print("Tus cartas suman: ", suma)

					if suma > 21:

						print("\nPerdiste la mano, gana la casa")

						print("\nCuentas con: ", dinero)

						op = input("\nQuires seguir jugando?  y  /  n\n")

						if op == "y":

							break

						else:
							
							sys.exit(0)


		if opcion == 3:

			apuestaCasa = apuestaPlayer

			os.system('clear')

			print("\nEl jugador se planta\n")

			cut = False

			while True:		

				casaSuma = 0

				for carta in cartasCasa: 

					try: 
						casaSuma = casaSuma + int(carta[0:2]) # 

					except:

						casaSuma = casaSuma + 10

				if casaSuma < 17: #Si la casa tiene menos de 17, agarra carta

					print("\nLa casa pide carta\n")

					cartasCasa.append(cartas.pop(0))

				elif casaSuma > 21: #Si la casa tiene menas de 21 pierde

					dinero = dinero + apuestaPlayer + apuestaCasa

					print("\nLa casa pierde\n")

					op = input("\nQuires seguir jugando?  y  /  n\n")

					if op == "y":

						cut = True

						break

					else:

						sys.exit(0)	
				if cut:

					break

				else:

					print("La casa se planta\n")

					break

					op = input("\nQuires seguir jugando?  y  /  n\n")

					if op == "y":

						break

					else:

						sys.exit(0)		

				

				print("Cartas de la casa:\n", cartasCasa,"\n")

				print("Cartas del jugador:\n", cartasPlayer,"\n")

			# Ahora que termino  la casa comparo ambos resultados

			suma = 0

			for carta in cartasPlayer: # Utilizo try/except para lidiar con la posibilidad de que me rebote las letras J,Q,K y ahorrarme el IF statement

				try: 
					suma = suma + int(carta[0:2]) # 

				except:

					suma = suma + 10

			print("Cartas de la casa:\n", cartasCasa,"\n")

			print("Cartas del jugador:\n", cartasPlayer,"\n")

			if casaSuma > suma:

				print("Gana la casa\n")

				print("\nCuentas con: ", dinero)

				op = input("\nQuires seguir jugando?  y  /  n\n")

				if op == "y":

					break

				else:

					sys.exit(0)



			elif casaSuma == suma:

				print("Empate\n")

				dinero = dinero + apuestaPlayer	

				print("\nCuentas con: ", dinero)

				op = input("\nQuires seguir jugando?  y  /  n\n")

				if op == "y":

					break

				else:
					
					sys.exit(0)

				

			else: 

				print("Gana el jugador, felicidades\n")

				dinero = dinero + apuestaPlayer + apuestaCasa

				print("\nCuentas con: ", dinero)

				op = input("\nQuires seguir jugando?  y  /  n\n")

				if op == "y":

					os.system('clear')

					break

				else:
					
					sys.exit(0)














		# SEPARO LA OPCION 4 PORQUE SE ME ENREDO 

		if opcion == 4:

			if inicio is False:

				print("\nNo puedes realizar esta accion\n")

			else:

				prueba = dinero-apuestaPlayer # Chequeo si tengo los fondos para doblar

				if prueba < 0:

					print("\nNo puedes apostar tanto\n")

				else:

					suma = 0

					for carta in cartasPlayer: # Utilizo try/except para lidiar con la posibilidad de que me rebote las letras J,Q,K y ahorrarme el IF statement

						try: 
							suma = suma + int(carta[0:2])

						except:

							suma = suma + 10

					if suma < 20:

						os.system('clear')

						print("\nNo puedes realizar esta accion\n")

						continue


					else:

						inicio = False

						dinero = prueba

						apuestaPlayer = apuestaPlayer*2

						#Declaro las manos nuevas

						playerA = [cartasPlayer[0]]

						playerB = [cartasPlayer[1]]

						playerA.append(cartas.pop(0))

						playerB.append(cartas.pop(0))

						while True:

							print("\nCartas A Jugador: ", playerA,)

							print("\nCartas B Jugador: ", playerB,"\n")

							print("Cartas casa\n")

							print(cartasCasa, "\n")

							print("Apuesta en mesa: ",apuestaPlayer,"$\n")

							print 

							opt = int(input("Que desea hacer?\n1 Doblar\n2 plantarse\n3 Finalizar\n"))


							if opt ==1:

								os.system('clear')

								prueba = dinero-apuestaPlayer # Chequeo si tengo los fondos para doblar

								if prueba < 0:

									print("\nNo puedes apostar tanto\n")

								else:

									dinero = prueba

									apuestaPlayer = apuestaPlayer*2

									apuestaCasa = apuestaCasa*2


							if opt == 2:

								os.system('clear')

								print("\nEl jugador se planta\n")



								while True:		

									casaSuma = 0



									for carta in cartasCasa: 

										try: 
											casaSuma = casaSuma + int(carta[0:2]) # 

										except:

											casaSuma = casaSuma + 10



									if casaSuma < 17: #Si la casa tiene menos de 17, agarra carta

										print("\nLa casa pide carta\n")

										cartasCasa.append(cartas.pop(0))



									if casaSuma > 21: #Si la casa tiene menas de 21 pierde

										dinero = dinero + apuestaPlayer + apuestaCasa

										print("\nLa casa pierde\n")

										op = input("\nQuires seguir jugando?  y  /  n\n")

										if op == "y":

											break

										else:

											sys.exit(0)


									else:

										print("La casa se planta\n")

										break

									print("Cartas de la casa:\n", cartasCasa,"\n")

									print("\nCartas A Jugador: ", playerA,)

									print("\nCartas B Jugador: ", playerB,"\n")


								# Ahora que termino  la casa comparo ambos resultados


								sumaA = 0
								sumaB = 0

								for carta in playerA: # Utilizo try/except para lidiar con la posibilidad de que me rebote las letras J,Q,K y ahorrarme el IF statement

									try: 
										sumaA = sumaA + int(carta[0:2]) # 

									except:

										sumaA = sumaA + 10.

								for carta in playerB: # Utilizo try/except para lidiar con la posibilidad de que me rebote las letras J,Q,K y ahorrarme el IF statement

									try: 
										sumaB = sumaB + int(carta[0:2]) # 

									except:

										sumaB = sumaB + 10

								print("Cartas de la casa:\n", cartasCasa,"\n")

								print("\nCartas A Jugador: ", playerA,)

								print("\nCartas B Jugador: ", playerB,"\n")

								if casaSuma > sumaA and casaSuma > sumaB :

									print("Gana la casa\n")

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:

										sys.exit(0)

								if casaSuma < sumaA and casaSuma > sumaB :

									print("Gana la casa al mazoB y gana el mazoA a la casa\n")

									dinero = dinero + apuestaPlayer/2 + apuestaCasa/2

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:


										sys.exit(0)

								if casaSuma > sumaA and casaSuma < sumaB :

									print("Gana la casa al mazoA y gana el mazoB a la casa\n")

									dinero = dinero + apuestaPlayer/2 + apuestaCasa/2

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:

										sys.exit(0)


								elif casaSuma == sumaA and casaSuma ==sumaB:

									print("Empate\n")

									dinero = dinero + apuestaPlayer	

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:
										
										sys.exit(0)

								elif casaSuma > sumaA and casaSuma ==sumaB:

									print("Empate\n")

									dinero = dinero - apuestaPlayer/2	

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:
										
										sys.exit(0)

								elif casaSuma < sumaA and casaSuma ==sumaB:

									print("Empate\n")

									dinero = dinero + apuestaPlayer/2	

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:
										
										sys.exit(0)

								elif casaSuma == sumaA and casaSuma > sumaB:

									print("Empate\n")

									dinero = dinero - apuestaPlayer/2	

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:
										
										sys.exit(0)

								elif casaSuma == sumaA and casaSuma < sumaB:

									print("Empate\n")

									dinero = dinero + apuestaPlayer/2	

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										break

									else:
										
										sys.exit(0)

								else: 

									print("Gana el jugador, felicidades\n")

									dinero = dinero + apuestaPlayer + apuestaCasa

									print("\nCuentas con: ", dinero)

									op = input("\nQuires seguir jugando?  y  /  n\n")

									if op == "y":

										os.system('clear')

										break

									else:
										
										sys.exit(0)

			break


						