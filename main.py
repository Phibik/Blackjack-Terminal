from menus import *
from partida import partida
from records import records

while True:
    menuPrincipal()
    opcion = input("Selecciona una opción: ").lower()
    while opcion != "a" and opcion != "s" and opcion != "d" and opcion != "f" and opcion != "h":
        menuPrincipalParaEstupidos()
        opcion = input("Selecciona una opción: ").lower()

    match opcion:
        case "a":
            partida(17)
        case "h":
            partida(21)
        case "s":
            records()
        case "d":
            reglas()
        case "f":
            break

