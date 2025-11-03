"""Crea un programa que indique si una llis
ta d'enters és cap i cua, és a dir, que si llegim la llista des del principi o
 des del final, donarà el mateix resultat."""

numero=[]
limite=0
texto=0
limite=int(input("Introduce un limite: "))

for i in range (limite):
    texto=input("Introduce un número: ")
    numero.append(texto)

for a in range(int(limite/2)):
    if not(numero[a] == numero[-a-1]):
        print("no")
        exit()


print("Es cap i cua")