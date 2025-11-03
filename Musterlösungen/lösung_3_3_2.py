from typing import List
import statistics

# 1. Liste mit Altersangaben erstellen
alters_liste: List[int] = [25, 27, 30, 35, 40]

# Errechen Sie mithilfe einer For Schleife die Summe und den Mittelwert Ihrer Liste/Alterswerte.
summe = 0
for alter in alters_liste:
    print(alter)
    summe = summe + alter # ist identisch zu summe += alter

mittelwert = summe / len(alters_liste)

# Errechnen Sie den Median mit Hilfe des statistics Moduls.
median = statistics.median(alters_liste)

# Printen Sie alle drei Kennzahlen.
print(f'Median: {median}')
print(f"Summe: {summe}")
print(f"Mittelwert: {mittelwert}")
