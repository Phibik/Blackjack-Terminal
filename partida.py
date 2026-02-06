import msvcrt
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

                if len(juego.baraja.cartas) <= 80:
                    printTablero(juego, ES.MEZCLAR, "apuesta")
                    pedirApuesta(juego)
                    juego.mezclar()
                    juego.repartir()
                else:
                    printTablero(juego, ES.REPARTIR, "apuesta")
                    pedirApuesta(juego)
                    juego.repartir()

                        # CASO DEALER BLACKJACK NATURAL ##############
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
                        
                        # CASO DEALER NO BLACJACK Y JUGADOR SÍ
                        # CASO 1 BLACKJACK TRAS SPLIT Y 2 BLACKJACKS TRAS SPLIT (lol)

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

                            case "f": # DOUBLE #################################### usar multJugador/Split
                                pass

                            case "d": # SPLIT ####################################
                                juego.haySplit = True
                                juego.double = True
                                # si con las dos has perdido directamente a derrota, si solo has perdido con una a dealer

                            case "a": # SURRENDER ####################################
                                if juego.haySplit:
                                    pass


                    case ES.MANO_2:
                        pass

            case EP.TURNO_DEALER:
                
                if juego.cartasDealer[1].tipo == "TAPADA":
                    juego.cartasDealer[1].tipo = "MOSTRADA"
                    juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                printTablero(juego, ES.DEALER) ########################################### EL DEALER NO DEBERIA ROBAR CARTA SI TIENES 2 CARTAS CON >= 17
                opcion = pedirInput(juego)

                juego.repartirDealer()
                
                if juego.puntuacionDealer > 21:
                    ep = EP.FIN
                    es = ES.VICTORIA
                    
                    if juego.haySplit:
                        pass ####################

                elif juego.modo == 17:
                    if juego.puntuacionDealer < 17:
                        juego.repartirDealer()
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

                        juego.dinero += (juego.apuestaJugador + juego.apuestaSplit) * 2

                        printTablero(juego, es)
                        opcion = pedirInput(juego) 

                    case ES.VICTORIA:
                        juego.dinero += (juego.apuestaJugador + juego.apuestaSplit) * 2

                        printTablero(juego, es)
                        opcion = pedirInput(juego) 

                    case ES.EMPATE:
                        pass

                    case ES.DERROTA:
                        juego.cartasDealer[1].tipo = "MOSTRADA"
                        juego.puntuacionDealer = juego.calcularPuntuacion(juego.cartasDealer)

                        printTablero(juego, es)
                        opcion = pedirInput(juego) 
                        if juego.dinero == 0: opcion = "q"

# reiniciar todas variables #########################################
