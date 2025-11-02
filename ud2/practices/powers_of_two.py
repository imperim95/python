"""Crea un programa que demane a l'usuari un nombre enter i mostre totes les potències de 2 fins a la potència indicada (inclosa)."""
numero=int(input("Dame un número: "))
resultado=0

for i in range (numero+1):
    resultado=2**i
    print(f"2^{i} =",resultado)