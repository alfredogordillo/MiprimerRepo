
from random import randint

def dar_carta(max_valor=10):
    return randint(1, max_valor)

def mostrar_estado(jugador, casa):
    print(f"Acumulado de cartas del jugador: {jugador}")
    print(f"Acumulado de cartas de la casa: {casa}")

def verificar_ganador(jugador, casa):
    if jugador > 21:
        print("EL JUGADOR SUMA MÁS DE 21. LA CASA GANA, FIN DEL JUEGO")
        return True
    elif jugador == 21:
        print("EL JUGADOR CONSIGUIÓ 21, BLACKJACK. EL JUGADOR GANA, FIN DEL JUEGO")
        return True
    elif casa > 21:
        print("LA CASA TIENE MÁS DE 21. EL JUGADOR GANA, FIN DEL JUEGO")
        return True
    elif casa == 21:
        print("LA CASA CONSIGUIÓ 21, BLACKJACK. LA CASA GANA, FIN DEL JUEGO")
        return True
    return False

def turno_casa(casa, jugador):
    while casa < 17:  
        carta_ca = dar_carta()
        casa += carta_ca
        print(f"Nueva carta para la casa: {carta_ca}")
        mostrar_estado(jugador, casa)
        if verificar_ganador(jugador, casa):
            return casa, True
    return casa, False

def determinar_ganador(jugador, casa):
    if jugador <= 21 and (jugador > casa or casa > 21):
        print("EL JUGADOR GANA, FIN DEL JUEGO")
    elif casa <= 21 and (casa > jugador or jugador > 21):
        print("LA CASA GANA, FIN DEL JUEGO")
    else:
        print("EMPATE, FIN DEL JUEGO")

jugador = 0
casa = 0
ganador = False
ronda = 1
## Commentario 1

while not ganador:
    print(f"\nRonda: {ronda}")
    if ronda == 1:
        print("Repartiendo cartas")
        carta_ju = dar_carta()
        jugador += carta_ju
        carta_ca = dar_carta()
        casa += carta_ca
        print(f"Nueva carta para el jugador: {carta_ju}")
        mostrar_estado(jugador, casa)
    else:
        opcion = input("¿Nueva carta? (s/n): ").lower()
        if opcion == "s":
            carta_ju = dar_carta()
            jugador += carta_ju
            print(f"Nueva carta para el jugador: {carta_ju}")
            mostrar_estado(jugador, casa)
            ganador = verificar_ganador(jugador, casa)
        elif opcion == "n":
            casa, ganador = turno_casa(casa, jugador)
            if not ganador:  # Solo determina el ganador si no ha terminado el juego
                determinar_ganador(jugador, casa)
                ganador = True
        else:
            print("Opción no válida.")
    ronda += 1
    #Comentario 2