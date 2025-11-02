#Escriu un programa que mostre totes les fitxes del dominó existents, en el format indicat.

for a in range(0,7):
    print()
    for b in range(a,7):
        print(f"{a}|{b }"," ",end="")
