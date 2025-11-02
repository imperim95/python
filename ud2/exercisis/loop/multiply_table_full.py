primero=int(input("Dime el primer número: "))
segundo=int(input("Dime el segundo número: "))

for i in range(primero,segundo+1):
    print("TABLA DEL ",i)
    for k in range(1,11):
        resultado=k*i
        print(k," * ",i," = ",resultado)
    print("\n")
