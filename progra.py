import os
import random


tableroJugador = []
tableroAtaqueJugador = []
tableroCPU = []
listaFilas = ["A","B","C","D","E","F","G","H","I","J"]
listaColumnas = ["0","1","2","3","4","5","6","7","8","9"]
listaPosicionesOcupadas = []
lista_archivos_cpu = ["tableroCPU.txt","tableroCPU1.txt","tableroCPU2.txt"]



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

def leer_archivo_CPU(nombre_archivo):
    fichero = open(nombre_archivo, 'r')
    filas = fichero.readlines()
    listaCPU = []
    listaPosiciones = []
    i=0
    for fila in filas:
        barco = ""
        i=0
        for item in fila:
            if item != ":":
                barco += item
                i+=1
            else:
                if item == ":":
                    listaCPU.append(barco)
                    barco = ""
                    barco += fila[i+1]
                    barco += fila[i+2]
                    listaPosiciones.append(barco)
                    listaCPU.append(barco)
    #print(listaPosiciones)
    #print(listaCPU)
    if len(listaPosiciones) != 15:
        print("El archivo de configuracion para el CPU no contiene suficientes barcos o contiene mas de los permitidos, recuerde que deben ser 5 portaviones, 4 battleship, 3 cruceros, 2 submarinos y 1 lancha")
        exit()
    else:
        ocurrenciasP = listaCPU.count("Portaviones")
        ocurrenciasB = listaCPU.count("Battleship")
        ocurrenciasC = listaCPU.count("Crucero")
        ocurrenciasS = listaCPU.count("Submarino")
        ocurrenciasL = listaCPU.count("Lancha")
        if ocurrenciasP != 5:
            print("Faltan o sobran posiciones para el portaviones")
            exit()
        elif ocurrenciasB != 4:
            print("Faltan o sobran posiciones para el battleship")
            exit()           
        elif ocurrenciasC != 3:
            print("Faltan o sobran posiciones para el crucero")
            exit()           
        elif ocurrenciasS != 2:
            print("Faltan o sobran posiciones para el submarino")
            exit()           
        elif ocurrenciasL != 1:
            print("Faltan o sobran posiciones para la lancha")
            exit()
    j = 0
    k = 0
    while(j < 15):
        fila = ord(listaPosiciones[j][0]) - 65 
        columna = int(listaPosiciones[j][1])
        if tableroCPU[fila][columna] == 0:
            tableroCPU[fila][columna] = "B"
            j+=1
        else:
            print("Error: El archivo de tablero para CPU contiene la misma posicion en el tablero para dos fichas, Abortando juego")
            exit()
    #imprimir_tablero(tableroCPU)

def pedir_portaviones():
    listaPortaviones = []
    portaviones = input("Ingrese la ubicacion del portaviones\n")
    posicion = ""
    item = 0
    while item < len(portaviones):
        if portaviones[item] in listaFilas or portaviones[item] in listaColumnas:
            posicion+= portaviones[item]
            item+=1
            if len(posicion)==2:
                listaPortaviones.append(posicion)
                posicion = ""
        else:
            item+=1

    if len(listaPortaviones) != 5:
        print("Error: El Portaviones debe constar de 5 fichas en el tablero\n")
        pedir_portaviones()
    
    for item in listaPortaviones:
        if item not in listaPosicionesOcupadas:
            listaPosicionesOcupadas.append(item)
        else:
            exit()

def pedir_battleship():
    listaBattleship = []
    battleship = input("Ingrese la ubicacion del battleship\n")
    posicion = ""
    item = 0
    while item < len(battleship):
        if battleship[item] in listaFilas or battleship[item] in listaColumnas:
            posicion+= battleship[item]
            item+=1
            if len(posicion)==2:
                listaBattleship.append(posicion)
                posicion = ""
        else:
            item+=1

    if len(listaBattleship) != 4:
        print("El Battleship debe constar de 4 fichas en el tablero\n")
        listaBattleship = []
        pedir_battleship()    
    
    for item in listaBattleship:
        if item in listaPosicionesOcupadas:
            print("Error: Se eligio una casilla que ya se encuentra ocupada")
            exit()
        else:
            listaPosicionesOcupadas.append(item)

def pedir_crucero():
    listaCrucero = []
    crucero = input("Ingrese la ubicacion del Crucero\n")
    posicion = ""
    item = 0
    while item < len(crucero):
        if crucero[item] in listaFilas or crucero[item] in listaColumnas:
            posicion+= crucero[item]
            item+=1
            if len(posicion)==2:
                listaCrucero.append(posicion)
                posicion = ""
        else:
            item+=1

    if len(listaCrucero) != 3:
        print("El Crucero debe constar de 3 fichas en el tablero\n")
        listaCrucero = []
        pedir_crucero()
    
    for item in listaCrucero:
        if item in listaPosicionesOcupadas:
            print("Error: Se eligio una casilla que ya se encuentra ocupada")
            exit()
        else:
            listaPosicionesOcupadas.append(item)

def pedir_submarino():
    listaSubmarino = []
    submarino = input("Ingrese la ubicacion del Submarino\n")
    posicion = ""
    item = 0
    while item < len(submarino):
        if submarino[item] in listaFilas or submarino[item] in listaColumnas:
            posicion+= submarino[item]
            item+=1
            if len(posicion)==2:
                listaSubmarino.append(posicion)
                posicion = ""
        else:
            item+=1

    if len(listaSubmarino) != 2:
        print("El Submarino debe constar de 2 fichas en el tablero\n")
        listaSubmarino = []
        pedir_submarino()
    
    for item in listaSubmarino:
        if item in listaPosicionesOcupadas:
            print("Error: Se eligio una casilla que ya se encuentra ocupada")
            exit()
        else:
            listaPosicionesOcupadas.append(item)

def pedir_lancha():
    listaLancha = []
    lancha = input("Ingrese la ubicacion de la Lancha\n")
    posicion = ""
    item = 0
    while item < len(lancha):
        if lancha[item] in listaFilas or lancha[item] in listaColumnas:
            posicion+= lancha[item]
            item+=1
            if len(posicion)==2:
                listaLancha.append(posicion)
                posicion = ""
        else:
            item+=1

    if len(listaLancha) != 1:
        print("La Lancha debe constar de 1 fichas en el tablero\n")
        listaLancha = []
        pedir_lancha()
    
    for item in listaLancha:
        if item in listaPosicionesOcupadas:
            print("Error: Se eligio una casilla que ya se encuentra ocupada")
            exit()
        else:
            listaPosicionesOcupadas.append(item)

def cargar_tablero_jugador():
    i = 0
    while i < len(listaPosicionesOcupadas):
        fila = ord(listaPosicionesOcupadas[i][0]) - 65 
        columna = int(listaPosicionesOcupadas[i][1])
        if i < 5:
            tableroJugador[fila][columna] = "P"
        if i >= 5 and i < 9:
            tableroJugador[fila][columna] = "B"
        if i >= 9 and i < 12:
            tableroJugador[fila][columna] = "C"
        if i >= 12 and i < 14:
            tableroJugador[fila][columna] = "S"
        if i >= 14:
            tableroJugador[fila][columna] = "L"
        i+=1
    #print(tableroJugador)        
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
			print("%5s " % (str(tablero[i][j])), end="")
		print()

def movimiento_pc():
	movimiento = []
	while movimiento == []:
		fila = random.randint(0, 9)
		columna = random.randint(0, 9)
		if tableroJugador[fila][columna] not in ["X", "A"]:
			movimiento = [fila,columna]
	
	print("PC ataca a " + listaFilas[fila] + listaColumnas[columna])
	
	if tableroJugador[movimiento[0]][movimiento[1]] in ["P","L","S","C","0","B"]:
		print("Acierto")
		tableroJugador[movimiento[0]][movimiento[1]] = "A"
	else:
		print("Fallo")
		tableroJugador[movimiento[0]][movimiento[1]] = "X"
		
	print()
	
def movimiento_jugador():
	movimiento = []
	while movimiento == []:
		jugada = input("Ingrese la coordenada a atacar: ")
		if len(jugada) != 2 or jugada[0] not in listaFilas or jugada[1] not in listaColumnas:
			print("Coordinada Invalida")
			continue
		# https://itsmycode.com/convert-letters-to-numbers-in-python/#:~:text=We%20can%20convert%20letters%20to%20numbers%20in%20Python%20using%20the,convert%20each%20letter%20into%20number.
		fila = ord(jugada[0]) - 65 
		columna = int(jugada[1])
		if tableroAtaqueJugador[fila][columna] not in ["X", "A"]:
			movimiento = [fila,columna]
		else:
			print("Esa casilla ya fue atacada")	
			
	if tableroCPU[movimiento[0]][movimiento[1]] in ["P","L","S","C","0","B"]:
		print("Acierto")
		tableroCPU[movimiento[0]][movimiento[1]] = "A"
		tableroAtaqueJugador[movimiento[0]][movimiento[1]] = "A"
	else:
		print("Fallo")
		tableroCPU[movimiento[0]][movimiento[1]] = "X"
		tableroAtaqueJugador[movimiento[0]][movimiento[1]] = "X"
		
	print()
	
def tablero_sin_barcos(tablero):
	for fila in tablero:
		for item in fila:
			if item in["P","L","S","C","0","B"]:
				return False
	return True

def jugar():
	llenar_tableros()
	aleatorio = random.randint(0,2)
	nombre_archivo = lista_archivos_cpu[aleatorio]
	print("Leyendo archivo: " + nombre_archivo)
	print("\nCargando tablero de CPU")
	leer_archivo_CPU(nombre_archivo)
	pedir_portaviones()
	print("Posiciones ocupadas: ")
	print(listaPosicionesOcupadas)	
	pedir_battleship()
	print("Posiciones ocupadas: ")
	print(listaPosicionesOcupadas)	
	pedir_crucero()
	print("Posiciones ocupadas: ")
	print(listaPosicionesOcupadas)
	pedir_submarino()
	print("Posiciones ocupadas: ")
	print(listaPosicionesOcupadas)
	pedir_lancha()
	cargar_tablero_jugador()
	
	jugador_gana = False
	CPU_gana = False
	
	orden = random.randint(0, 1)
	if orden == 0:
		print("*** Inicia el Jugador ***")
	else:
		print("*** Inicia la PC ***")
    
	while jugador_gana == False and CPU_gana == False:
		if orden == 0:
			movimiento_jugador()
			movimiento_pc()
		else:
			movimiento_pc()
			movimiento_jugador()
			
			
		print("Tablero defensivo Jugador")
		imprimir_tablero(tableroJugador)
		print()
		print()	
		print("Tablero de Ataque Jugador")
		imprimir_tablero(tableroAtaqueJugador)
		
		jugador_gana = tablero_sin_barcos(tableroCPU)
		CPU_gana = tablero_sin_barcos(tableroJugador)
		
	if jugador_gana and CPU_gana:
		print("Empate!")
	elif jugador_gana:
		print("Jugador gana!")
	elif CPU_gana:
		print("CPU gana!")

while(True):
	tableroJugador = []
	tableroAtaqueJugador = []
	tableroCPU = []
	listaPosicionesOcupadas = []

	jugar()
	seguir_jugando = input("Desea iniciar un juego nuevo? Digite la letra s para iniciar, cualquier otra letra para salir")
	if seguir_jugando == "s" or seguir_jugando == "S":
		continue
	else:
		exit()
