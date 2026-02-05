def separador():
    print('')
    print("------------------------------------------------------------------------------------")
    print('')

def menuPrincipal():
    print("\n\n\n\n\n\n\n")
    print("==========================")
    print("        BLACKJACK")
    print("==========================")
    print('')
    print("(a) Blackjack 17, 3:2")
    print("(j) Blackjack 21, 3:2")
    print("(s) Récords")
    print("(d) Reglas")
    print("(f) Salir")
    
    separador()

def menuPrincipalParaEstupidos():
    separador()
    print("==========================")
    print("        BLACKJACK")
    print("==========================")
    print('\n')
    print("(a) Blackjack 17, 3:2")
    print("(j) Blackjack 21, 3:2")
    print("(s) Récords")
    print("(d) Reglas")
    print("(f) Salir")
    
    print("\nSelecciona una de las opciones disponibles por favor")
    separador()

def reglas():
    separador()
    print("=== Puntación ===")
    print("- Empiezas con 100 puntos, sólo puedes apostar lo que tienes en esa partida")
    print("- En la puntuación histórica se tendrán en cuenta las ganancias/perdidas respecto a los 100 iniciales de cada partida")
    print('')
    print("=== Reglas ===")
    print("- Objetivo: llegar a 21 sin pasarse")
    print("- Valores:")
    print("    - 2,...,10: Su mismo valor")
    print("    - J, Q, K:  10")
    print("    - A:        1 u 11 según convenga")
    print("- Acciones:")
    print("    - Hit: Pedir una carta")
    print("    - Stand: Plantarse")
    print("    - Double Down: Sólo antes de hit, duplicas apuesta, hit y stand")
    print("    - Split: Sólo en la primera acción y si las cartas tienen el mismo valor, las separas en dos manos, recibes nueva carta por mano y las juegas por separado")
    print("    - Surrender: Sólo en la primera acción, te rindes y pierdes la mitad de la apuesta")
    print("- Apuestas:")
    print("    - Flujo: En Blackjack 17 se planta a partir de 17. El Dealer muestra una carta y la otra la oculta. Reparte 2 cartas por jugador. Haces tus acciones, luego el Dealer.")
    print("    - Blackjack: Ganas 3:2 de tu apuesta")
    print("    - Victoria: Ganas 1:1 de tu apuesta")
    print("    - Empate: No pierdes nada")
    
    separador()
    input("Pulsa cualquier tecla para volver al menú")
















