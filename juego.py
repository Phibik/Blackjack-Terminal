from baraja import *

class Juego:

    def __init__(self, modo):
        self.modo = modo
        self.baraja = Baraja()
        self.baraja.mezclar()
        self.victorias = 0
        self.derrotas = 0
        self.marcador = 0

        self.cartasDealer = []
        self.cartasJugador = []
        self.cartasSplit = []

        self.puntuacionDealer = 0
        self.puntuacionJugador = 0
        self.puntuacionSplit = 0

        self.dinero = 1000
        self.apuestaJugador = 0
        self.apuestaSplit = 0

        self.haySplit = False
        self.split = True
        self.double = True

    def mezclar(self):
        self.baraja = Baraja()
        self.baraja.mezclar()

    def repartir(self):
        self.repartirJugador()
        self.repartirDealer()
        self.repartirJugador()
        self.repartirDealer()
        self.cartasDealer[1].tipo = "TAPADA"
        self.puntuacionDealer = self.calcularPuntuacion(self.cartasDealer)

    def repartirDealer(self):
        nuevaCarta = self.baraja.robar()
        self.cartasDealer.append(nuevaCarta)
        self.puntuacionDealer = self.calcularPuntuacion(self.cartasDealer)

    def repartirJugador(self):
        nuevaCarta = self.baraja.robar()
        self.cartasJugador.append(nuevaCarta)
        self.puntuacionJugador = self.calcularPuntuacion(self.cartasJugador)

    def repartirSplit(self):
        nuevaCarta = self.baraja.robar()
        self.cartasSplit.append(nuevaCarta)
        self.puntuacionSplit = self.calcularPuntuacion(self.cartasSplit)

    def calcularPuntuacion(self, cartas):
        puntos = 0
        nAses = 0
        for c in cartas:
            if c.tipo == "MOSTRADA":
                puntos += c.valor
                if c.simbolo == "A":
                    nAses += 1

        while puntos > 21:
            if nAses == 0:
                return puntos

            puntos -= 10
            nAses -= 1

        return puntos

