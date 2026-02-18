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


def pedirInput(opciones = "-q"): # e.g. opciones = "-qjkf"
    while True:
        opcion = msvcrt.getch().decode('utf-8', errors='ignore').lower()

        for o in opciones:
            if o == "-" and (opcion == '\r' or opcion == ' ' or opcion == 'j'):
                return "-"
            elif o == opcion:
                return opcion

def irMano2(juego):
    printTablero(juego, ES.MANO_2)
    opcion = pedirInput()

    juego.double = True
    juego.repartirSplit()

    if juego.puntuacionSplit == 21:
        return opcion, ES.MANO_2, EP.TURNO_DEALER
    else:
        return opcion, ES.MANO_2, EP.TURNO_JUGADOR

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

                    juego.cartasJugador = [Carta("A", "D"), Carta("A", "D")]################## PARA TESTEAR
                    juego.puntuacionJugador = juego.calcularPuntuacion(juego.cartasJugador)##################
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
                        opciones = "qjk"
                        if juego.split:
                            opciones += "a"
                        if juego.split and juego.dinero >= juego.apuestaJugador and juego.cartasJugador[0].valor == juego.cartasJugador[1].valor:
                            opciones += "d"
                        if juego.double and juego.dinero >= juego.apuestaJugador:
                            opciones += "f"

                        printTablero(juego, ES.MANO_1, opciones)
                        opcion = pedirInput(opciones)
                        juego.split = False
                        juego.double = False
                        
                        match opcion:
                            case "j": # HIT
                                juego.repartirJugador()

                                if juego.puntuacionJugador == 21:
                                    if juego.haySplit:
                                        opcion, es, ep = irMano2(juego)
                                    else:
                                        ep = EP.TURNO_DEALER
                                elif juego.puntuacionJugador > 21:
                                    if juego.haySplit:
                                        opcion, es, ep = irMano2(juego)
                                    else:
                                        ep = EP.FIN
                                        es = ES.DERROTA

                            case "k": # STAND
                                if juego.haySplit:
                                    opcion, es, ep = irMano2(juego)
                                else:
                                    ep = EP.TURNO_DEALER

                            case "f": # DOUBLE
                                juego.dinero -= juego.apuestaJugador
                                juego.apuestaJugador += juego.apuestaJugador

                                # Igual que HIT
                                juego.repartirJugador()

                                if juego.puntuacionJugador == 21:
                                    if juego.haySplit:
                                        opcion, es, ep = irMano2(juego)
                                    else:
                                        ep = EP.TURNO_DEALER
                                elif juego.puntuacionJugador > 21:
                                    if juego.haySplit:
                                        opcion, es, ep = irMano2(juego)
                                    else:
                                        ep = EP.FIN
                                        es = ES.DERROTA
                                else:
                                    # Igual que STAND
                                    if juego.haySplit:
                                        opcion, es, ep = irMano2(juego)
                                    else:
                                        ep = EP.TURNO_DEALER

                            case "d": # SPLIT
                                juego.haySplit = True
                                juego.double = True

                                juego.dinero -= juego.apuestaJugador
                                juego.apuestaSplit = juego.apuestaJugador

                                juego.cartasSplit.append(juego.cartasJugador.pop())
                                juego.puntuacionJugador = juego.calcularPuntuacion(juego.cartasJugador)
                                juego.puntuacionSplit = juego.calcularPuntuacion(juego.cartasSplit)

                                # Igual que HIT en caso haySplit con intermedio
                                printTablero(juego, ES.MANO_1)
                                opcion = pedirInput()

                                juego.repartirJugador()

                                if juego.puntuacionJugador == 21 and opcion != "q":
                                    opcion, es, ep = irMano2(juego)

                            case "a": # SURRENDER
                                juego.dinero += int(juego.apuestaJugador / 2)
                                juego.apuestaJugador = math.ceil(juego.apuestaJugador / 2)

                                if juego.haySplit:
                                    opcion, es, ep = irMano2(juego)
                                else:
                                    ep = EP.FIN
                                    es = ES.DERROTA


                    case ES.MANO_2:
                        opciones = "qjk"
                        if juego.double and juego.dinero >= juego.apuestaJugador:
                            opciones += "f"

                        printTablero(juego, ES.MANO_2, opciones)
                        opcion = pedirInput(opciones)
                        juego.double = False

                        match opcion:
                            case "j": # HIT
                                juego.repartirSplit()

                                if juego.puntuacionSplit == 21:
                                    ep = EP.TURNO_DEALER
                                elif juego.puntuacionSplit > 21:
                                    if juego.puntuacionJugador > 21:
                                        ep = EP.FIN
                                        es = ES.SPLIT
                                    else:
                                        ep = EP.TURNO_DEALER

                            case "k": # STAND
                                ep = EP.TURNO_DEALER

                            case "f": # DOUBLE
                                juego.dinero -= juego.apuestaSplit
                                juego.apuestaSplit += juego.apuestaSplit

                                # Igual que HIT
                                juego.repartirSplit()

                                if juego.puntuacionSplit == 21:
                                    ep = EP.TURNO_DEALER
                                elif juego.puntuacionSplit > 21:
                                    if juego.puntuacionJugador > 21:
                                        ep = EP.FIN
                                        es = ES.SPLIT
                                    else:
                                        ep = EP.TURNO_DEALER
                                else:
                                    # Igual que STAND
                                    ep = EP.TURNO_DEALER

            case EP.TURNO_DEALER:
                
                if juego.cartasDealer[1].tipo == "TAPADA":
                    printTablero(juego, ES.DEALER)
                    opcion = pedirInput()

                    juego.cartasDealer[1].tipo = "MOSTRADA"
                    juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)
                else:
                    printTablero(juego, ES.DEALER)
                    opcion = pedirInput()

                    juego.repartirDealer()

                if juego.puntuacionDealer > 21:
                    ep = EP.FIN
                    es = ES.VICTORIA
                    
                    if juego.haySplit:
                        ep = EP.FIN
                        es = ES.SPLIT

                elif juego.modo == 17:
                    if juego.puntuacionDealer < 17:
                        pass
                    elif juego.haySplit:
                        ep = EP.FIN
                        es = ES.SPLIT
                    elif juego.puntuacionJugador > juego.puntuacionDealer:
                        ep = EP.FIN
                        es = ES.VICTORIA
                    elif juego.puntuacionJugador < juego.puntuacionDealer:
                        ep = EP.FIN
                        es = ES.DERROTA
                    else:
                        ep = EP.FIN
                        es = ES.EMPATE

                else: # juego.modo = 21
                    if juego.haySplit:
                        if (juego.puntuacionDealer == juego.puntuacionJugador or juego.puntuacionDealer == juego.puntuacionSplit) and juego.puntuacionDealer >= 17:
                            ep = EP.FIN
                            es = ES.SPLIT
                        elif juego.puntuacionDealer > juego.puntuacionJugador or juego.puntuacionDealer > juego.puntuacionSplit:
                            ep = EP.FIN
                            es = ES.SPLIT
                        else:
                            pass

                    elif juego.puntuacionDealer < juego.puntuacionJugador:
                        pass
                    elif juego.puntuacionDealer > juego.puntuacionJugador:
                        ep = EP.FIN
                        es = ES.DERROTA
                    else:
                        ep = EP.FIN
                        es = ES.EMPATE

            case EP.FIN:
                ganancias = 0

                if es == ES.SPLIT:
                    resultado = 0

                    if juego.puntuacionJugador > 21: # DERROTA
                        resultado -= juego.apuestaJugador
                    elif juego.puntuacionDealer < juego.puntuacionJugador or juego.puntuacionDealer > 21: # VICTORIA
                        resultado += juego.apuestaJugador
                        ganancias += juego.apuestaJugador * 2
                    elif juego.puntuacionDealer > juego.puntuacionJugador: # DERROTA
                        resultado -= juego.apuestaJugador
                    else: # EMPATE
                        ganancias += juego.apuestaJugador

                    if juego.puntuacionSplit > 21: # DERROTA
                        resultado -= juego.apuestaSplit
                    elif juego.puntuacionDealer < juego.puntuacionSplit or juego.puntuacionDealer > 21: # VICTORIA
                        resultado += juego.apuestaSplit
                        ganancias += juego.apuestaSplit * 2
                    elif juego.puntuacionDealer > juego.puntuacionSplit: # DERROTA
                        resultado -= juego.apuestaSplit
                    else: # EMPATE
                        ganancias += juego.apuestaSplit

                    if resultado > 0:
                        es = ES.VICTORIA
                    elif resultado < 0:
                        es = ES.DERROTA
                    else:
                        es = ES.EMPATE

                match es:
                    case ES.BLACKJACK:
                        juego.cartasDealer[1].tipo = "MOSTRADA"
                        juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                        juego.dinero += math.ceil(juego.apuestaJugador * 5 / 2)

                        printTablero(juego, es)
                        opcion = pedirInput() 

                    case ES.VICTORIA:
                        if juego.haySplit:
                            juego.dinero += ganancias
                        else:
                            juego.dinero += juego.apuestaJugador * 2

                        juego.victorias += 1
                        juego.marcador += 1

                        printTablero(juego, es)
                        opcion = pedirInput()

                    case ES.EMPATE:
                        if juego.haySplit:
                            juego.dinero += ganancias
                        else:
                            juego.dinero += juego.apuestaJugador

                        printTablero(juego, es)
                        opcion = pedirInput()

                    case ES.DERROTA:
                        juego.cartasDealer[1].tipo = "MOSTRADA"
                        juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                        juego.dinero += ganancias
                        juego.derrotas += 1
                        juego.marcador -= 1

                        printTablero(juego, es)
                        opcion = pedirInput() 
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
