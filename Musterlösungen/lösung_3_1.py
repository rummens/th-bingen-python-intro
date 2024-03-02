import random

# Zufällige Int zwischen 1 und 6
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)

# Ausgabe zur Kontrolle und für Nutzer
print("Gewürfelt wurde: %i %i %i" % (a, b, c))


if a == 1 and b == 1 and c == 1:
    # Super, Chicago. Das Spiel ist gewonnen, also könnten wir nach dem Print sofort aufhören.
    print("Chicago")
else:
    # Okay, kein Chicago. Schauen wir ob 1er oder 6er haben
    if a == 6:
        # Alles klar, eine 6. Wir belegen die Variable einfach mit dem neuen Wert neu
        a = 60
    if a == 1:
        # Alles klar, eine 1. Wir belegen die Variable einfach mit dem neuen Wert neu
        a = 100

    if b == 6:
        b = 60
    if b == 1:
        b = 100

    if c == 6:
        c = 60
    if c == 1:
        c = 100

    # Summe bilden
    summe = a + b + c

    # Wenn mindestens eine 6 oder 1 gewürfelt wurde, muss die Summe über 60 sein, ansonsten ist es ein Fisch
    if summe < 60:
        print("Fisch")
    else:
        print(a+b+c)
