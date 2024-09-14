import numpy as np
from scipy.integrate import quad, odeint
import matplotlib.pyplot as plt


# Teil 1: Numerische Integration

# Komplexe mathematische Funktion (trigonometrische Funktion)
def f(x):
    return np.sin(x) / (x + 1)


# Berechnung des bestimmten Integrals der Funktion über dem Intervall [0, pi]
integral, _ = quad(f, 0, np.pi)

# Ausgabe des berechneten Integrals
print("Bestimmtes Integral von f(x) über [0, pi]:", integral)


# Teil 2: Lösung einer Differentialgleichung

# Definition der Differentialgleichung (nichtlineare Differentialgleichung zweiter Ordnung)
def difgleichung(y, t):
    # Index 0 entspricht y'(t), also dem Integral von -sin(y)
    # Index 1 entspricht y''(t), also -sin(y) aus der Aufgabe
    return [y[1], -np.sin(y[0])]


# Zeitpunkte für die Lösung der Differentialgleichung
t = np.linspace(0, 10, 100)

# Anfangsbedingungen für y und y'
y0 = [np.pi / 4, 0]

# Numerische Lösung der Differentialgleichung
y = odeint(difgleichung, y0, t)

# Visualisierung der Lösung der Differentialgleichung
plt.plot(t, y[:, 0], label='y(t)')
plt.plot(t, y[:, 1], label="y'(t)")
plt.title('Lösung einer nichtlinearen Differentialgleichung zweiter Ordnung')
plt.xlabel('Zeit t')
plt.ylabel('y(t), y\'(t)')
plt.legend()
plt.grid(True)
plt.show()
