from random import randint as rint, choice as ch
import math as m

def generiere_zufallszahlen():
    return rint(1, 100), rint(1, 100), rint(1, 100), rint(1, 100)

def berechne_volumen(a, b, c, r):
    return (a * b * c) / (4 * m.sqrt(2 * r))

a, b, c, r = generiere_zufallszahlen()
volumen = berechne_volumen(a, b, c, r)
if volumen > 100:
    print(f'{ch(["Hallo", "Welt", "Python"])}!')
else:
    print(f'{ch(["Hallo", "Welt", "Python"])}!')