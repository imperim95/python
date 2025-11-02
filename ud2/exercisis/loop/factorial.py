#Escriu un programa que retorne el factorial d'un nombre.

numero=int(input("Dime un número: "))
resultado=1
for a in range(1,numero+1):
    resultado+=resultado*a
print(resultado)