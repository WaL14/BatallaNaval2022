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


def jugar():
    llenar_tableros()
    leer_archivo_CPU()
    #print(tableroCPU)

jugar()