#Proyecto1.py

import os # Importo System de OS para poder limpiar la pantalla os.system("clear")

dinero = 100

while True:

	print("\nBienvenido/a al banco XXXX introduzca el número de la operación desea realizar")

	opcion = int(input("1 Consulta de saldo\n2 Retiro\n3 Deposito\n4 Transferencia\n5 Salida\n"))

	if opcion == 1:

		while True:

			print("Su saldo actual es de: ", dinero, "$")

			clear = int(input("0 para continuar"))

			if clear == 0:

				os.system('clear')

				break

	if opcion == 2:

		while True:

			print("Su saldo actual es de: ", dinero, "$")

			retiro = int(input("\nCuanto desea retirar?:\n"))

			if retiro > dinero :

				print("\nSus fondos no son suficientes pra realizar esta operacion, por favor ingrese un monto menor\n")

				continue # Para que comience el ciclo desde el principio

			else:

				dinero = dinero - retiro

				print("Su saldo actual es de ", dinero, "\n")

			clear = int(input("0 para continuar\n"))

			if clear == 0:

				os.system('clear')

				break

	if opcion == 3:

		while True:

			print("Su saldo actual es de: ", dinero, "$")

			deposito = int(input("\nIngrese monto de deposito:\n"))

			dinero = dinero + deposito

			print("Su saldo actual es de ", dinero, "\n")

			clear = int(input("0 para continuar\n"))

			if clear == 0:

				os.system('clear')

				break

	if opcion == 4:

		while True:

			print("Su saldo actual es de: ", dinero, "$")

			nombre = input("Nombre del receptor de la transferencia:\n")

			retiro = int(input("\nCuanto desea Transferir?:\n"))

			if retiro > dinero :

				print("\nSus fondos no son suficientes pra realizar esta operacion, por favor ingrese un monto menor\n")

				continue # Para que comience el ciclo desde el principio

			else:

				print("Transferencia realizada con exito a,", nombre, "\n")

				dinero = dinero - retiro

				print("Su saldo actual es de ", dinero, "\n")

			clear = int(input("0 para continuar\n"))

			if clear == 0:

				os.system('clear')

				break



	if opcion == 5:

		break

print("Muchas gracias por utilizar nuestros servicios")