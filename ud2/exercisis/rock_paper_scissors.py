#Crea un programa per jugar al joc Pedra, paper o tisores.
#El programa rebrà la jugada de 2 jugadors i indicarà quins dels dos jugadors guanyat.

def juego(a,b):
    if a == "piedra":
        if b == "piedra":
            print("empate")
        else:
            if b == "papel":
                print("El jugador 2 ha ganado")
            else:
                print("El jugador 1 ha ganado")

    if a == "papel":
        if b == "papel":
             print("empate")
        else:
            if b == "tijera":
                print("El jugador 2 ha ganado")
            else:
                print("El jugador 1 ha ganado")

    if a == "tijera":
        if b == "tijera":
             print("empate")
        else:
            if b == "piedra":
                print("El jugador 2 ha ganado")
            else:
                print("El jugador 1 ha ganado")
print("Piedra, papel o tijeras")
a=str(input("Jugador 1. Elige: "))
b=str(input("Jugador 2. Elige: "))

juego(a,b)
    
        
    