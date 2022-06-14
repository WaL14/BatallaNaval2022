import os

tableroJugador = []
tableroAtaqueJugador = []
tableroCPU = []



def llenar_tableros():
    for i in range(10):
        tableroJugador.append([])
        tableroAtaqueJugador.append([])
        tableroCPU.append([])
        for j in range(10):
            tableroJugador[i].append(0)
            tableroAtaqueJugador[i].append(0)
            tableroCPU[i].append(0)
    #print(tableroJugador)
    #print(tableroAtaqueJugador)
    #print(tableroCPU)

def leer_archivo_CPU():
    fichero = open('tablero1.txt', 'r')
    filas = fichero.readlines()
    i=0
    j=0
    for fila in filas:
        for item in fila:
            if item not in["P","L","S","C","0","B"]:
                continue
            else:
                if item == "0":
                    j+=1
                    continue
                else:
                    tableroCPU[i][j] = item
                    j+=1
        j=0        
        i+=1
        
def imprimir_tablero(tablero):
	print("     ", end="")
	for j in range(len(tablero[0])):
		print("%5d " % j, end="")
	print()
	print("     ", end="")
	for j in range(len(tablero[0])):
		print("------", end="")
	print()

	letras = ["A","B","C","D","E","F","G","H","I","J"]
	for i in range(len(tablero)):
		print("%3s |" % (letras[i]), end="") # Row nums
		for j in range(len(tablero[0])):
			print("%5d " % (tablero[i][j]), end="")
		print()

def movimiento_pc(tablero_enemigo):
	movimiento = []
	while movimiento == []:
		fila = randint(0, 9)
		columna = randint(0, 9)
		if tablero[fila][columna] != "X":
			movimiento = [fila,columna]
	return movimiento
	
def movimiento_jugador(tablero_enemigo):
	movimiento = []
	while movimiento == []:
		jugada = input("Ingrese la coordenada a atacar: ")
		# https://itsmycode.com/convert-letters-to-numbers-in-python/#:~:text=We%20can%20convert%20letters%20to%20numbers%20in%20Python%20using%20the,convert%20each%20letter%20into%20number.
		fila = ord(jugada[0]) - 65 
		columna = int(jugada[1])
		if tablero[fila][columna] != "X":
			movimiento = [fila,columna]
		else:
			print("Esa casilla ya fue atacada")	
	return movimiento
	

def jugar():
    llenar_tableros()
    leer_archivo_CPU()
    #print(tableroCPU)

jugar()
       
