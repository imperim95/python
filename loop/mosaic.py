
numero=int(input("Dime un número: "))
letra=""
for a in range(numero):
    print()
    for b in range(numero):
        if a == b:
            print("X ",end="")
        else:
            if b<a:
                print("D ",end="")
            else:
                print("U ",end="")

    

