import msvcrt
from enum import IntEnum
from printeadas import *
from juego import *

class EP(IntEnum):
    MAL_INPUT = 0
    INICIO = 1
    TURNO_JUGADOR = 2
    TURNO_SPLIT = 3
    TURNO_DEALER = 4
    FIN = 5

class ES(IntEnum):
    MEZCLAR = 0
    REPARTIR = 1

def pedirInput(juego, opciones): # e.g. opciones = "-rhsd"
    while True:
        opcion = msvcrt.getch().decode().lower()

        for o in opciones:
            if o == "-" and (opcion == "" or opcion == " "):
                return "-"
            elif o == opcion:
                return opcion

        printTablero(juego, EP.MAL_INPUT)


def partida(modo):
    juego = Juego(modo)

    opcion = ""
    ep = EP.INICIO
    es = ES.MEZCLAR
    
    while opcion != "r":
        match ep:

            case INICIO:

                juego.nTurnos++
                if juego.nTurnos == 5:
                    juego.nTurnos = 0

                    printTablero(juego, ES.MEZCLAR)
                    juego.mezclar()
                    juego.repartir()
                    opcion = pedirInput(juego, "-r")
                else:
                    printTablero(juego, ES.REPARTIR)
                    juego.repartir()
                    opcion = pedirInput(juego, "-r")                    

                ep = EP.TURNO_JUGADOR

            case TURNO_JUGADOR:
                opcion = pedirInput(juego, "-r")

            case TURNO_SPLIT:
                opcion = pedirInput(juego, "-r")

            case TURNO_DEALER:
                opcion = pedirInput(juego, "-r")

            case FIN:
                opcion = pedirInput(juego, "-r")

