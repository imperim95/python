
numero=int(input("dame un numero: "))
pasos=0
for a in range(1,numero):

    if numero%2 != 1:
        numero=numero/2
    else:
        if numero%2 !=0:
            numero=numero*3+1
    print("n",a,": ",numero)
    pasos=a
print("passos: ",pasos)
