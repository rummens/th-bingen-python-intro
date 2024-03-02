import random
import math


def generiere_zufallszahlen():
    """Generiert vier Zufallszahlen zwischen 1 und 100."""
    return [random.randint(1, 100) for _ in range(4)]


def berechne_volumen(a, b, c, r):
    """Berechnet das Volumen basierend auf den gegebenen Parametern."""
    return (a * b * c) / (4 * math.sqrt(2 * r))


def main():
    """Hauptfunktion des Programms."""
    zufallszahlen = generiere_zufallszahlen()
    a, b, c, r = zufallszahlen
    volumen = berechne_volumen(a, b, c, r)
    gruss = random.choice(["Hallo", "Welt", "Python"])
    if volumen > 100:
        print(f'{gruss}!')
    else:
        print(f'{gruss}!')


if __name__ == "__main__":
    main()
