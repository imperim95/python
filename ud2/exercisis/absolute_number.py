#Crea un programa que retorne el valor absolut del nombre que introduisca l'usuari.
# Demana un nombre a l'usuari
numero = float(input("Introdueix un nombre: "))

# Calcula el valor absolut manualment
if numero < 0:
    valor_absolut = -numero
else:
    valor_absolut = numero

# Mostra el resultat
print("El valor absolut és:", valor_absolut)
    