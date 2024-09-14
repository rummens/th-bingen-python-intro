import matplotlib.pyplot as plt
import numpy as np

# Generiere fiktive Temperaturdaten für eine Woche
tage = np.arange(1, 8)
temperaturen = np.random.randint(10, 30, size=7)

# Berechne den Durchschnitt
durchschnittstemperatur = np.mean(temperaturen)

# Erstelle das Liniendiagramm
plt.plot(tage, temperaturen, marker='o', label='Temperatur')
plt.axhline(y=durchschnittstemperatur, color='r', linestyle='--', label='Durchschnittstemperatur')

# Beschriftung und Titel hinzufügen
plt.xlabel('Tag')
plt.ylabel('Temperatur (°C)')
plt.title('Temperaturverlauf über eine Woche')
plt.legend()

# Anzeigen des Diagramms
plt.grid(True)
plt.tight_layout()
plt.show()
