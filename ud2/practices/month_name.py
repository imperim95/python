"""Crea un programa que demane a l'usuari un nombre enter entre 1 i 12 i mostre el nom del mes corresponent. Si l'usuari introdueix un nombre fora d'aquest rang, 
el programa ha de mostrar un missatge d'error i tonarà a demanar el nombre fins que l'usuari introduesca un valor vàlid.
Exemple d'entrada i eixida"""

numero=int(input("Dime un número del 1 al 12: "))

while not(numero >=1 and numero<=12):
    numero=int(input("Error. Tienes que introducir un número del 1 al 12. Vuelve a intentarlo: "))

match numero:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")


