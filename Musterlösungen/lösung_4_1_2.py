import random
import sys

""" 
Sehr simple Implementierung des Spieles "Schere, Stein, Papier".
Alle Vergleiche werden zur Veranschaulichung mit String gemacht, dies ist ineffizient und sollte eigentlich über 
Zahlen geschehen. Dies ist weniger fehleranfällig und schneller im rechnen.
Das Program wurde bewusst einfach und nicht optimiert gehalten.
"""

# Eingabe Optionen und mapping definieren
# Dies sind globale Variable, deswegen müssen diese groß geschrieben werden
EINGABE_OPTIONEN = ["schere", "stein", "papier"]
ZUFALLS_MAPPING = {
    0: "schere",
    1: "stein",
    2: "papier"
}


def nutzer_abfragen() -> str:
    # Nutzer Prompt erstellen
    nutzer_eingabe = input("Bitte geben Sie ihre Wahl ein (Schere, Stein, Papier)")

    # Unnötige Whitespaces (Leerzeichen, Tabs etc.) entfernen. Das macht den Vergleich stabiler.
    nutzer_eingabe = nutzer_eingabe.strip()

    # Prüfen ob Nutzer Eingabe valide ist (besser mit lower versehen, um kleine Tippfehler abzufangen)
    if nutzer_eingabe.lower() not in EINGABE_OPTIONEN:
        # Falls die Eingabe nicht okay ist, müssen wir eine Exception erzeugen damit das die überliegende Funktion den
        # Fehler mitbekommt und behandeln kann.
        raise ValueError("Unbekannte Eingabe %s. Bitte nur die folgenden Optionen nutzen: %s"
                         % (nutzer_eingabe, EINGABE_OPTIONEN))

    return nutzer_eingabe.lower()


def computer_zug() -> str:
    # zufällige Zahl zwischen 0 und 2 erzeugen
    zug = random.randint(0, 2)
    # Zahl in String übersetzen (besser für Lesbarkeit)
    return ZUFALLS_MAPPING[zug]


def gewinner_feststellen(zug_mensch: str, zug_computer: str):
    # Bei keinem Unterschied gewinnt keiner
    if zug_mensch == zug_computer:
        return "Unentschieden"

    # Gewinn Kombinationen Computer
    if zug_mensch == "schere" and zug_computer == "stein":
        return "Computer gewinnt"
    if zug_mensch == "papier" and zug_computer == "schere":
        return "Computer gewinnt"
    if zug_mensch == "stein" and zug_computer == "papier":
        return "Computer gewinnt"

    # Gewinn Kombinationen Mensch
    if zug_mensch == "stein" and zug_computer == "schere":
        return "Sie gewinnen"
    if zug_mensch == "schere" and zug_computer == "papier":
        return "Sie gewinnen"
    if zug_mensch == "papier" and zug_computer == "stein":
        return "Sie gewinnen"

    raise Exception("Hier sollten wir eigentlich nicht ankommen.")


if __name__ == '__main__':
    # Erst fragen wir den Nutzer nach einem Wert
    try:
        zug_nutzer = nutzer_abfragen()
    # Dies kann eine ValueError Exception hervorrufen. Diese sollten wir abfangen und dem Nutzer zeigen
    except ValueError as e:
        print(str(e), file=sys.stderr)  # Dies printed auf STDERR statt STDOUT und sollte somit in Rot erscheinen

        # Ein Fehler ist aufgetreten. Wir sollten das Program mit einem End-Code größer 0 beenden. Dies signaler
        # zusätzlich einen Fehler.
        sys.exit(1)

    # Dann lassen wir den Computer ziehen
    zufalls_zug = computer_zug()

    # Zur Sichtbarkeit printen wir dies aus
    print("Zug Nutzer: %s, Zug Computer: %s" % (zug_nutzer, zufalls_zug))

    # Gewinner ermitteln
    gewinner = gewinner_feststellen(zug_mensch=zug_nutzer, zug_computer=zufalls_zug)

    # Gewinner printen
    print(gewinner)

