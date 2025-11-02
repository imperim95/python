# Programa per a gestionar un torneig de Go

ganador = ""
nombre = ""
numero1 = 0
nombre=input("Dime tu nombre: ")
while nombre != "END":

    numero2=int(input())

    if numero2>numero1:
        numero1=numero2
        ganador=nombre
    nombre=input("Dime tu nombre: ")

print ("El ganador es ",ganador,"con el número ",numero1)


