from carta import *

def printCarta(carta):
    palo = carta.palo
    if carta.simbolo != "10":
        simbolo = carta.simbolo + " "
    else:
        simbolo = carta.simbolo

    if carta.tipo == "VACIO":
        return ["┌────┐", "|    |", "|    |", "└────┘"]
    elif carta.tipo == "TAPADO":
        return ["┌────┐", "|▒░▒░|", "|░▒░▒|", "└────┘"]
    else:
        return ["┌────┐", f"| {simbolo} |", f"| {palo}  |", "└────┘"]

def printEvento(evento):
    match evento:
        case ev.REPARTIR:
            pass
        case ev.BARAJAR_REPARTIR:
            pass
        case ev.MANO1:
            pass
        case ev.MANO2:
            pass
        case ev.DEALER:
            pass
        case ev.VICTORIA:
            pass
        case ev.DERROTA:
            pass
        case ev.EMPATE:
            pass
        case ev.SPLIT:
            pass
        case ev.SURRENDER:
            pass

def printDealer(cartas, puntos):
    if puntos < 10:
        puntos = str(puntos) + " "
    else:
        puntos = str(puntos)
    
    print("║ Dealer, Puntuación: " + puntos + "                             ║")

    pcartas = []
    for c in cartas:
        pcartas.append(printCarta(c))

    if len(pcartas) == 0:
        pcartas = [printCarta(Carta("0", "P", "VACIO")), printCarta(Carta("0", "P", "VACIO"))]
    elif len(pcartas) == 1:
        pcartas.append(printCarta(Carta("0", "P", "VACIO")))

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

def printMano1(cartas):
    pass

def printMano2(cartas):
    pass

def printMano(cartas1, cartas2):
    pass

def printDatos(dinero, estado1, estado2, puntuacionDealer, puntuacion1, puntuacion2):
    pass

def printTablero(dinero, estado1, estado2, puntuacionDealer, puntuacion1, puntuacion2, cartasDealer, cartas1, cartas2, evento):
    print("╔════════════════════════════════════════════════════╗")
    print("║ ┌────┐ ┌────┐   ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ║ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ")
