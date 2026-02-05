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
        print("╠════════════════════════════════════════════════════╣")
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

def printEvento():
    print("╠════════════════════════════════════════════════════╣")
    print("║                                                    ║")
    print("╚════════════════════════════════════════════════════╝")

def printTablero(juego, evento):
    print("╔════════════════════════════════════════════════════╗")
    print("║                 BLACKJACK " + juego.modo + ", 3:2                  ║")
    printDealer(juego.cartasDealer, juego.puntuacionDealer)
    printMano(1, juego.cartasJugador, juego.puntuacionJugador, juego.apuestaJugador)
    printMano(2, juego.cartasSplit, juego.puntuacionSplit, juego.apuestaSplit)
    printEvento()
