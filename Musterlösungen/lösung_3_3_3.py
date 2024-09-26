import random
import statistics
from typing import List, Dict

alters_liste: List[int] = [25, 27, 30, 35, 40]

summe = 0

for alter in alters_liste:
    summe += alter

mittelwert = summe / len(alters_liste)
print(f"Die Summe der Altersliste beträgt:{summe}")
print(f"Der Mittelwert der Altersliste beträgt: {mittelwert:.2f}")
print(f"Der Median der Altersliste beträgt:{statistics.median(alters_liste)}")

if mittelwert > 30:
    raise Exception("Der Mittelwert ist größer als 30")
else:
    exit(0)
