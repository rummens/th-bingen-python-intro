import numpy as np
import matplotlib.pyplot as plt

# Generiere einen zufälligen Datensatz von ganzen Zahlen zwischen 1 und 100
datensatz = np.random.randint(1, 101, size=20)

# Berechne statistische Kennzahlen
mittelwert = np.mean(datensatz)
median = np.median(datensatz)
standardabweichung = np.std(datensatz)
varianz = np.var(datensatz)
minimum = np.min(datensatz)
maximum = np.max(datensatz)

# Ausgabe der statistischen Kennzahlen
print("Statistische Kennzahlen:")
print("Mittelwert:", mittelwert)
print("Median:", median)
print("Standardabweichung:", standardabweichung)
print("Varianz:", varianz)
print("Minimum:", minimum)
print("Maximum:", maximum)

# Visualisierung des Datensatzes mit einem Histogramm
plt.hist(datensatz, bins=10, edgecolor='black')
plt.title('Histogramm des Datensatzes')
plt.xlabel('Werte')
plt.ylabel('Häufigkeit')
plt.grid(True)
plt.show()
