import pandas as pd
import numpy as np

# Warnung bei Typ konvertierung aktivieren, um FutureWarning zu umgehen.
# Taucht bei ansonsten bei letzter Aufgabe auf, kann aber aktuell noch ignoriert werden.
# ref. https://stackoverflow.com/questions/77900971/pandas-futurewarning-downcasting-object-dtype-arrays-on-fillna-ffill-bfill
pd.set_option('future.no_silent_downcasting', True)

# 1. DataFrame erstellen
data = {
    "Name": ["Anna", "Ben", "Carla", "David", "Eva"],
    "Alter": [28, 34, 45, 23, 31],
    "Stadt": ["Berlin", "Hamburg", "München", "Köln", "Stuttgart"],
    "Gehalt": [45000, 52000, 62000, 38000, 48000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Daten filtern
# Personen älter als 30
df_ueber_30 = df[df["Alter"] > 30]
print("\nPersonen älter als 30:")
print(df_ueber_30)

# Personen, die in Berlin oder München wohnen
df_staedte = df[df["Stadt"].isin(["Berlin", "München"])]
print("\nPersonen aus Berlin oder München:")
print(df_staedte)

# 3. Spaltenauswahl: "Name" und "Stadt"
df_name_stadt = df[["Name", "Stadt"]]
print("\nNur Name und Stadt:")
print(df_name_stadt)


# 4. Neue Spalte "Steuerklasse" basierend auf dem Alter
def steuerklasse(alter):
    if alter < 30:
        return 1
    elif 30 <= alter <= 40:
        return 2
    else:
        return 3


df["Steuerklasse"] = df["Alter"].apply(steuerklasse)
print("\nDataFrame mit Steuerklasse:")
print(df)

# 5. Durchschnittliches Gehalt pro Stadt
durchschnitt_gehalt = df.groupby("Stadt")["Gehalt"].mean()
print("\nDurchschnittliches Gehalt pro Stadt:")
print(durchschnitt_gehalt)

# 6. Sortieren nach Alter (absteigend)
df_sorted = df.sort_values(by="Alter", ascending=False)
print("\nDataFrame nach Alter sortiert (absteigend):")
print(df_sorted)

# 7a Fehlende Werte behandeln
# Neue Person hinzufügen
neue_person = pd.DataFrame([{"Name": "Florian", "Alter": None, "Stadt": "Frankfurt", "Gehalt": 56000}])
df = pd.concat([df, neue_person], ignore_index=True)
print("\nDataFrame mit fehlendem Wert im Alter:")
print(df)

# 7b Fehlenden Wert im Alter durch Durchschnittsalter ersetzen
durchschnittsalter = df["Alter"].mean(skipna=True)  # Durchschnittsalter berechnen
df = df.fillna({"Alter": durchschnittsalter})  # Fehlenden Wert ersetzen
df["Steuerklasse"] = df["Alter"].apply(steuerklasse)  # Steuerklasse neu berechnen
print("\nDataFrame nach Ersetzen des fehlenden Alterswertes:")
print(df)
