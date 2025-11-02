#Crea una programa que demane a l'usuari un nombre de persones i un nombre de galetes.



def repartir(persona,galletas):
    resultado=int(galletas%persona)

    if resultado == 0:
        print("A comer")
    else:
        print("A luchar")

a=int(input("Dime el numero de personas: "))
b=int(input("Dime el numero de galletas: "))

repartir(a,b)