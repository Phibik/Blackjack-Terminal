import sys
sys.stdout.reconfigure(encoding='utf-8')

import random
from carta import *

class Baraja:

    def __init__(self):
        palos = ["C", "D", "T", "P"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cartas = [Carta(v, p) for _ in range(6) for p in palos for v in valores]

    def mezclar(self):
        random.shuffle(self.cartas)

    def robar(self):
        return self.cartas.pop()
