from enum import IntEnum

class EP(IntEnum):
    INICIO = 1
    TURNO_JUGADOR = 2
    TURNO_DEALER = 3
    FIN = 4

class ES(IntEnum):
    MEZCLAR = 0
    REPARTIR = 1
    MANO_1 = 2
    MANO_2 = 3
    DEALER = 4
    BLACKJACK = 5
    VICTORIA = 6
    DERROTA = 7
    EMPATE = 8
    SPLIT = 9

class Carta:

    def __init__(self, v = "0", p = "x", t = "MOSTRADA"):
        self.simbolo = v
        self.tipo = t
        match v:
            case "A":
                self.valor = 11
            case "J":
                self.valor = 10
            case "Q":
                self.valor = 10
            case "K":
                self.valor = 10
            case _:
                self.valor = int(v)
        match p:
            case "C":
                self.palo = "♥"
            case "D":
                self.palo = "♦"
            case "T":
                self.palo = "♣"
            case "P":
                self.palo = "♠"
            case _:
                self.palo = p

