#Crea un programa que demane a l'usuari un enter i mostre per pantalla la seua taula de multiplicar del 1 al 9.

numero=int(input("Dime un numero: "))

for i in range(1,11):
    resultado=i*numero
    print(i," * ",numero," = ",resultado)