# Crea un programa que demane a l'usuari la seua edat i mostre el següents missatge en cas que siga major d'edat o no.



def adulto(edad):
    if edad>=18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

a=int(input("Dime tu edad: "))

adulto(a)