import os

tableroJugador = []
tableroAtaqueJugador = []
tableroCPU = []
listaFilas = ["A","B","C","D","E","F","G","H","I","J"]
listaColumnas = ["0","1","2","3","4","5","6","7","8","9"]
listaPosicionesOcupadas = []



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
        print(fila)
        print(columna)
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
    #imprimir_tablero(tableroJugador)
    #print(tableroCPU)

jugar()
       
