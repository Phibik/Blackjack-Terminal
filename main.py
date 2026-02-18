from menus import *
from partida import partida
from records import records

"""
TAREAS:
    - Arreglar menus (más bonitos)
    - Hacer puntuacion en un .txt
    - Hacer modo 99 (dealer hace mejor jugada estadisticamente)
    - Arreglar codigo (hacerlo bonito, clase mano y más funciones en partida.py)
"""

opcion = ""
while opcion != "q":

    menuPrincipal()
    opcion = input("Selecciona una opción: ").lower()
    while opcion != "j" and opcion != "f" and opcion != "d" and opcion != "k" and opcion != "a" and opcion != "q":
        menuPrincipalParaEstupidos()
        opcion = input("Selecciona una opción: ").lower()

    match opcion:
        case "j":
            partida(17)
        case "f":
            partida(21)
        case "d":
            partida(99)
        case "k":
            records()
        case "a":
            reglas()

