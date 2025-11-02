"""Crea una programa que demane a l'usuari un nombre enter i mostre per pantalla si el nombre introduït és una potència de 2 o no."""

numero=int(input("Dame un número: "))

while numero>2:
    numero=numero/2

if numero==2:
    print("True")
else:
    print("False")
