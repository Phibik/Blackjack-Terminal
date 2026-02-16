from carta import *

def printCarta(carta = Carta("0", "P", "VACIA")):
    palo = carta.palo
    if carta.simbolo != "10":
        simbolo = carta.simbolo + " "
    else:
        simbolo = carta.simbolo

    if carta.tipo == "VACIA":
        return ["┌────┐", "│    │", "│    │", "└────┘"]
    elif carta.tipo == "TAPADA":
        return ["┌────┐", "│▒░▒░│", "│░▒░▒│", "└────┘"]
    else:
        return ["┌────┐", f"│ {simbolo} │", f"│ {palo}  │", "└────┘"]

def printDealer(cartas = [], puntos = 0):
    if puntos < 10:
        puntos = str(puntos) + " "
    else:
        puntos = str(puntos)
    
    print("╠════════════════════════════════════════════════════╣")
    print("║ Dealer, Puntuación: " + puntos + "                             ║")

    pcartas = []
    for c in cartas:
        pcartas.append(printCarta(c))

    if len(pcartas) == 0:
        pcartas = [printCarta(), printCarta()]
    elif len(pcartas) == 1:
        pcartas.append(printCarta())

    linea = [[pcartas[0][0], pcartas[1][0], " ", "      ", "      ", "      ", "      ", "      ", "║"],
             [pcartas[0][1], pcartas[1][1], " ", "      ", "      ", "      ", "      ", "      ", "║"],
             [pcartas[0][2], pcartas[1][2], " ", "      ", "      ", "      ", "      ", "      ", "║"],
             [pcartas[0][3], pcartas[1][3], " ", "      ", "      ", "      ", "      ", "      ", "║"]]

    if len(pcartas) >= 3:
        for i in range(3, len(pcartas) + 1):
            if i <= 7:
                for j in range(4):
                    linea[j][i] = pcartas[i - 1][j]
            else:
                for j in range(4):
                    linea[j].append(pcartas[i - 1][j])

    for fila in linea:
        print("║ " + " ".join(fila))

def printMano(mano, cartas = [], puntos = 0, apuesta = 0):
    espacioExtra = ""
    if puntos < 10:
        espacioExtra = " "

    if apuesta < 10:
        apuesta = str(apuesta) + "€" + " "*6
    elif apuesta < 100:
        apuesta = str(apuesta) + "€" + " "*5
    elif apuesta < 1000:
        apuesta = str(apuesta) + "€" + " "*4
    elif apuesta < 10000:
        apuesta = str(apuesta) + "€" + " "*3
    elif apuesta < 100000:
        apuesta = str(apuesta) + "€" + " "*2
    elif apuesta < 1000000:
        apuesta = str(apuesta) + "€" + " "*1
    elif apuesta < 10000000:
        apuesta = str(apuesta) + "€"
    else:
        apuesta = str(apuesta)
    
    if mano == 1:
        print("╟────────────────────────────────────────────────────╢")
    else:
        print("║                                                    ║")
    print("║ Mano " + str(mano) + ", Puntuación: " + str(puntos) + ", Apuesta: " + apuesta + espacioExtra + "          ║")

    pcartas = []
    for c in cartas:
        pcartas.append(printCarta(c))

    if len(pcartas) == 0:
        pcartas = [printCarta(), printCarta()]
    elif len(pcartas) == 1:
        pcartas.append(printCarta())

    linea = [[pcartas[0][0], pcartas[1][0], " ", "      ", "      ", "      ", "      ", "      ", "║"],
             [pcartas[0][1], pcartas[1][1], " ", "      ", "      ", "      ", "      ", "      ", "║"],
             [pcartas[0][2], pcartas[1][2], " ", "      ", "      ", "      ", "      ", "      ", "║"],
             [pcartas[0][3], pcartas[1][3], " ", "      ", "      ", "      ", "      ", "      ", "║"]]

    if len(pcartas) >= 3:
        for i in range(3, len(pcartas) + 1):
            if i <= 7:
                for j in range(4):
                    linea[j][i] = pcartas[i - 1][j]
            else:
                for j in range(4):
                    linea[j].append(pcartas[i - 1][j])

    for fila in linea:
        print("║ " + " ".join(fila))

def printDatos(evento, opciones, dinero, marcador, victorias, derrotas, nCartas):

    print("╠════════════════════════════════════════════════════╣")

    match evento:
        case ES.MEZCLAR:
            print("║         Mezclando y repartiendo la baraja          ║")

        case ES.REPARTIR:
            porcienCartas = round(nCartas / 312 * 100)
            lineaBaraja = "("

            if porcienCartas < 10:
                lineaBaraja += str(porcienCartas) + "%)  "
            else:
                lineaBaraja += str(porcienCartas) + "%) "

            print("║            Repartiendo la baraja " + lineaBaraja + "            ║")

        case ES.MANO_1:
            print("║                 Tu turno (mano 1)                  ║")

        case ES.MANO_2:
            print("║                 Tu turno (mano 2)                  ║")

        case ES.DEALER:
            print("║                  Turno del Dealer                  ║")

        case ES.BLACKJACK:
            print("║                     Blackjack!                     ║")

        case ES.VICTORIA:
            print("║                      Victoria                      ║")

        case ES.DERROTA:
            print("║                      Derrota                       ║")

        case ES.EMPATE:
            print("║                       Empate                       ║")

        case _:
            print("║                                                    ║")

    print("╟──────────────────────────────┬─────────────────────╢")
    
    lineaDinero = "Dinero: "
    lineaMarcador = "Marcador:   "
    lineaVictorias = "Victorias:    "

    nVictorias = 0
    if victorias + derrotas != 0:
        nVictorias = round(victorias / (victorias + derrotas) * 100)

    if nVictorias == 100:
        lineaVictorias += str(nVictorias)
    elif nVictorias < 10:
        lineaVictorias += "  " + str(nVictorias)
    else:
        lineaVictorias += " " + str(nVictorias)

    marcadorStr = str(marcador)
    if abs(marcador) >= 1000:
        pass
    elif abs(marcador) >= 100:
        lineaMarcador += " "
    elif abs(marcador) >= 10:
        lineaMarcador += "  "
    else:
        lineaMarcador += "   "

    if marcador < 0:
        lineaMarcador += marcadorStr
    else:
        lineaMarcador += " " + marcadorStr

    if dinero >= 100_000_000:
        pass
    elif dinero >= 10_000_000:
        lineaDinero += " "
    elif dinero >= 1_000_000:
        lineaDinero += "  "
    elif dinero >= 100_000:
        lineaDinero += "   "
    elif dinero >= 10_000:
        lineaDinero += "    "
    elif dinero >= 1_000:
        lineaDinero += "     "
    elif dinero >= 100:
        lineaDinero += "      "
    elif dinero >= 10:
        lineaDinero += "       "
    else:
        lineaDinero += "        "

    lineaDinero += str(dinero)

    if opciones == "apuesta":
        print(f"║                              │  {lineaDinero}€ ║")
        print(f"║  Escribe tu apuesta (sin €)  │  {lineaMarcador}  ║")
        print(f"║                              │  {lineaVictorias}% ║")

    elif opciones == "":
        print(f"║                              │  {lineaDinero}€ ║")
        print(f"║  (j) Continuar   (q) Salir   │  {lineaMarcador}  ║")
        print(f"║                              │  {lineaVictorias}% ║")

    else:
        lineaDouble = ""
        lineaSplit = ""

        if "f" in opciones: lineaDouble = "(f) Double"
        else: lineaDouble = "          "

        if "d" in opciones: lineaSplit = "(d) Split "
        else: lineaSplit = "          "

        print(f"║  (j) Hit         {lineaDouble}  │  {lineaDinero}€ ║")
        print(f"║  (k) Stand       {lineaSplit}  │  {lineaMarcador}  ║")
        print(f"║  (a) Surrender   (q) Salir   │  {lineaVictorias}% ║") ######################################## FALTA QUITAR SURRENDER TRAS PRIMERA JUGADA, LOGICA SIMILAR AL SPLIT

    print("╚══════════════════════════════╧═════════════════════╝")

def printTablero(juego, evento = "", opciones = ""):
    print("\n\n\n\n")
    print("╔════════════════════════════════════════════════════╗")
    print("║                 BLACKJACK " + str(juego.modo) + ", 3:2                  ║")
    printDealer(juego.cartasDealer, juego.puntuacionDealer)
    printMano(1, juego.cartasJugador, juego.puntuacionJugador, juego.apuestaJugador)
    printMano(2, juego.cartasSplit, juego.puntuacionSplit, juego.apuestaSplit)
    printDatos(evento, opciones, juego.dinero, juego.marcador, juego.victorias, juego.derrotas, len(juego.baraja.cartas))

