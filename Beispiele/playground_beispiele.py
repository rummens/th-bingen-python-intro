## Ignoriert diese zwei Zeilen. Das ist die "Magie" die Apple im Hintergrund macht
def moveForward():
    pass

# Beispiel wie man eine Funktion aufruft:
# Also Name der Funktion (Schreibweise beachten) und die Klammern nicht vergessen:
moveForward()

# Beispiel für Schleifen:
for i in range(1, 5):
    print(i)

# Wir definieren zwei Variablen (integer um genau zu sein)
a = 3
b = 10

# Man könnte es auch so schreiben um den Typ der Variabel zu markieren:
# a: int = 2
# b: int = 10

# Beispiel für eine if-elif-else Struktur:
# Achtet auf den Doppelpunkt und die Einrückung danach:
if a > 3:
    print("a ist größer als 3")
elif a < 3:
    print("a ist kleiner als 3")
elif a == 3 and b == 10:
    print("a ist gleich 3 und b ist gleich 10")
elif a == 3 or b == 3:
    print("a ist gleich 3 oder b ist gleich 3")
else:
    print("a ist gleich 3")

# Beispiel einer Funktion mit zwei Parameter:
# Alternativ könnte man den Typ der Parameter und die Rückgabe auch so markieren:
# def add_two_numbers(number1: int, number2: int) -> int:
def add_two_numbers(number1, number2):
    return number1 + number2

# Funktionen aufrufen genau wie die Funktion moveForward() oben:
added_number = add_two_numbers(a, b)
# Das Ergebnis der Funktion wird in der Variabel added_number gespeichert und dann ausgegeben:
print(added_number)