import msvcrt
from enum import IntEnum
from printeadas import *
from juego import *

class EP(IntEnum):
    INICIO = 1
    TURNO_JUGADOR = 2
    TURNO_SPLIT = 3
    TURNO_DEALER = 4
    FIN = 5

class ES(IntEnum):
    MEZCLAR = 0
    REPARTIR = 1
    MANO_1 = 2
    MANO_2 = 3
    DEALER = 4
    VICTORIA = 5
    DERROTA = 6
    EMPATE = 7
    MALA_APUESTA = 8
    MAL_INPUT = 9

def pedirApuesta(juego):
    while True:
        try:
            apuesta = int(input())

            if 0 < apuesta <= juego.dinero:
                break
        except ValueError:
            pass

        printTablero(juego, ES.MALA_APUESTA)



def pedirInput(juego, opciones): # e.g. opciones = "-qjkf"
    while True:
        opcion = msvcrt.getch().decode('utf-8', errors='ignore').lower()

        for o in opciones:
            if o == "-" and (opcion == '\r' or opcion == " "):
                return "-"
            elif o == opcion:
                return opcion

        printTablero(juego, ES.MAL_INPUT)


def partida(modo):
    juego = Juego(modo)

    opcion = ""
    ep = EP.INICIO
    es = ES.MEZCLAR
    
    while opcion != "q":
        match ep:

            case EP.INICIO:

                juego.nTurnos += 1
                if juego.nTurnos == 5:
                    juego.nTurnos = 0

                    printTablero(juego, ES.MEZCLAR)
                    pedirApuesta(juego)
                    juego.mezclar()
                    juego.repartir()
                else:
                    printTablero(juego, ES.REPARTIR)
                    pedirApuesta(juego)
                    juego.repartir()

                ep = EP.TURNO_JUGADOR
                es = ES.MANO_1

            case EP.TURNO_JUGADOR:
                match es:

                    case ES.MANO_1:
                        opciones = "qjka"
                        if juego.split and juego.cartasJugador[0].valor == juego.cartasJugador[1].valor: opciones += "d"
                        if juego.double: opciones += "f"
                        
                        printTablero(juego, ES.MANO_1)
                        opcion = pedirInput(juego, opciones)
                        
                        match opcion:
                            case "j": # HIT ####################################
                                juego.split = False
                                juego.double = False

                            case "k": # STAND ####################################
                                juego.split = False
                                juego.double = False

                            case "f": # DOUBLE ####################################
                                juego.split = False
                                juego.double = False

                            case "d": # SPLIT ####################################
                                juego.split = False

                            case "a": # SURRENDER ####################################
                                juego.split = False
                                juego.double = False

                    case ES.MANO_2:
                        pass
                        

            case EP.TURNO_SPLIT:
                opcion = pedirInput(juego, "-q")

            case EP.TURNO_DEALER:
                opcion = pedirInput(juego, "-q")

            case EP.FIN:
                opcion = pedirInput(juego, "-q")

# si derrota y juego.dinero == 0, opcion = "q"
