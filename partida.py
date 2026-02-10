import msvcrt
import math
from printeadas import *
from juego import *

def pedirApuesta(juego):
    while True:
        try:
            apuesta = int(input())

            if 0 < apuesta <= juego.dinero:
                juego.apuestaJugador = apuesta
                juego.dinero -= apuesta
                break

        except ValueError:
            pass


def pedirInput(juego, opciones = "-q"): # e.g. opciones = "-qjkf"
    while True:
        opcion = msvcrt.getch().decode('utf-8', errors='ignore').lower()

        for o in opciones:
            if o == "-" and (opcion == '\r' or opcion == " "):
                return "-"
            elif o == opcion:
                return opcion


def partida(modo):
    juego = Juego(modo)

    opcion = ""
    ep = EP.INICIO
    es = ES.MEZCLAR

    while opcion != "q":
        match ep:

            case EP.INICIO:

                if len(juego.baraja.cartas) <= 80 or es == ES.MEZCLAR:
                    printTablero(juego, ES.MEZCLAR, "apuesta")
                    pedirApuesta(juego)
                    juego.mezclar()
                    juego.repartir()
                else:
                    printTablero(juego, ES.REPARTIR, "apuesta")
                    pedirApuesta(juego)
                    juego.repartir()

                # Blackjack Natural
                juego.cartasDealer[1].tipo = "MOSTRADA"
                juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                ## Blackjack Dealer
                if juego.puntuacionDealer == 21 and juego.puntuacionJugador != 21:
                    ep = EP.FIN
                    es = ES.DERROTA
                ## Blackjack Jugador
                elif juego.puntuacionDealer != 21 and juego.puntuacionJugador == 21:
                    ep = EP.FIN
                    es = ES.BLACKJACK
                ## Blackjack de ambos
                elif juego.puntuacionDealer == 21 and juego.puntuacionJugador == 21:
                    ep = EP.FIN
                    es = ES.EMPATE
                ## Sin Blackjack Natural
                else:
                    juego.cartasDealer[1].tipo = "TAPADA"
                    juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                    ep = EP.TURNO_JUGADOR
                    es = ES.MANO_1

            case EP.TURNO_JUGADOR:
                match es:

                    case ES.MANO_1:
                        opciones = "qjka"
                        if juego.split and juego.dinero >= juego.apuestaJugador and juego.cartasJugador[0].valor == juego.cartasJugador[1].valor:
                            opciones += "d"
                        if juego.double and juego.dinero >= juego.apuestaJugador:
                            opciones += "f"

                        printTablero(juego, ES.MANO_1, opciones)
                        opcion = pedirInput(juego, opciones)
                        juego.split = False
                        juego.double = False
                        
                        match opcion:
                            case "j": # HIT
                                juego.repartirJugador()

                                if juego.puntuacionJugador == 21:
                                    ep = EP.TURNO_DEALER
                                elif juego.puntuacionJugador > 21:
                                    if juego.haySplit:
                                        juego.double = True
                                        es = ES.MANO_2
                                    else:
                                        ep = EP.FIN
                                        es = ES.DERROTA

                            case "k": # STAND
                                if juego.haySplit:
                                    juego.double = True
                                    es = ES.MANO_2
                                else:
                                    ep = EP.TURNO_DEALER

                            case "f": # DOUBLE
                                juego.dinero -= juego.apuestaJugador
                                juego.apuestaJugador += juego.apuestaJugador

                                # Igual que HIT
                                juego.repartirJugador()

                                if juego.puntuacionJugador == 21:
                                    ep = EP.TURNO_DEALER
                                elif juego.puntuacionJugador > 21:
                                    if juego.haySplit:
                                        juego.double = True
                                        es = ES.MANO_2
                                    else:
                                        ep = EP.FIN
                                        es = ES.DERROTA
                                else:
                                    # Igual que STAND
                                    if juego.haySplit:
                                        juego.double = True
                                        es = ES.MANO_2
                                    else:
                                        ep = EP.TURNO_DEALER

                            case "d": # SPLIT ####################################
                                juego.haySplit = True
                                juego.double = True
                                # si con las dos has perdido directamente a derrota, si solo has perdido con una a dealer

                            case "a": # SURRENDER
                                juego.dinero += int(juego.apuestaJugador / 2)
                                juego.apuestaJugador = math.ceil(juego.apuestaJugador / 2)

                                if juego.haySplit:
                                    juego.double = True
                                    es = ES.MANO_2

                                else:
                                    ep = EP.FIN
                                    es = ES.DERROTA


                    case ES.MANO_2: # SE COMPRUEBA SI GANA O PIERDE, DE AHI APUESTASPLIT PASA TODA A JUGADOR PARA CALCULOS FACILES O SINO EN EP.FIN SE CLACULA CON UN IF HAYSPLIT
                        pass

            case EP.TURNO_DEALER:
                
                if juego.cartasDealer[1].tipo == "TAPADA":
                    printTablero(juego, ES.DEALER)
                    opcion = pedirInput(juego)

                    juego.cartasDealer[1].tipo = "MOSTRADA"
                    juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)
                else:
                    printTablero(juego, ES.DEALER)
                    opcion = pedirInput(juego)

                    juego.repartirDealer()

                if juego.puntuacionDealer > 21:
                    ep = EP.FIN
                    es = ES.VICTORIA
                    
                    if juego.haySplit:
                        pass ####################

                elif juego.modo == 17:
                    if juego.puntuacionDealer < 17:
                        pass
                    elif juego.haySplit: # a partir de estos elif se planta y comprueba quien gana
                        pass ##############################
                    elif juego.puntuacionJugador > juego.puntuacionDealer:
                        ep = EP.FIN
                        es = ES.VICTORIA
                    elif juego.puntuacionJugador < juego.puntuacionDealer:
                        ep = EP.FIN
                        es = ES.DERROTA
                    else:
                        ep = EP.FIN
                        es = ES.EMPATE

                else:
                    pass # hasta que supere jugador, da igual los puntos, si hay empate dealer hace stand

            case EP.FIN:
                match es:
                    case ES.BLACKJACK:
                        juego.cartasDealer[1].tipo = "MOSTRADA"
                        juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                        juego.dinero += int((juego.apuestaJugador + juego.apuestaSplit) * 3 / 2)

                        printTablero(juego, es)
                        opcion = pedirInput(juego) 

                    case ES.VICTORIA:
                        juego.dinero += (juego.apuestaJugador + juego.apuestaSplit) * 2
                        juego.victorias += 1
                        juego.marcador += 1

                        printTablero(juego, es)
                        opcion = pedirInput(juego)

                    case ES.EMPATE:
                        juego.dinero += juego.apuestaJugador + juego.apuestaSplit

                        printTablero(juego, es)
                        opcion = pedirInput(juego)

                    case ES.DERROTA:
                        juego.cartasDealer[1].tipo = "MOSTRADA"
                        juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)
                        juego.derrotas += 1
                        juego.marcador -= 1

                        printTablero(juego, es)
                        opcion = pedirInput(juego) 
                        if juego.dinero == 0: opcion = "q"

                # reiniciar todas variables
                juego.cartasDealer = []
                juego.cartasJugador = []
                juego.cartasSplit = []

                juego.puntuacionDealer = 0
                juego.puntuacionJugador = 0
                juego.puntuacionSplit = 0

                juego.apuestaJugador = 0
                juego.apuestaSplit = 0

                juego.haySplit = False
                juego.split = True
                juego.double = True

                ep = EP.INICIO
