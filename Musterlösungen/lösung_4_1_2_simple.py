import random
import sys

""" 
Leichtere Lösung der Schere Stein Papier Aufgabe, welche innerhalb der Vorlesung zusammen mit den Studenten 
entwickelt wurde.
"""


def gewinner_bestimmen(mensch, computer):
    if (mensch == "Schere" and computer == "Papier")\
            or (mensch == "Stein" and computer == "Schere")\
            or (mensch == "Papier" and computer == "Stein"):
        return "Mensch"

    elif (computer == "Schere" and mensch == "Papier")\
            or (computer == "Stein" and mensch == "Schere")\
            or (computer == "Papier" and mensch == "Stein"):
        return "Computer"
    else:
        return "Niemand"


if __name__ == '__main__':
    nutzer_wahl = input("Bitte gib Schere, Stein oder Papier ein:").strip()
    print(f"Ihre Wahl: {nutzer_wahl}")

    if nutzer_wahl == "Schere" or nutzer_wahl == "Stein" or nutzer_wahl == "Papier":
        computer_optionen = ["Schere", "Stein", "Papier"]
        computer_wahl = random.choice(computer_optionen)
        print(f"Die Wahl des Computers: {computer_wahl}")

        # Funktion aufrufen
        gewinner = gewinner_bestimmen(nutzer_wahl, computer_wahl)
        print(f"Der Gewinner ist {gewinner}")
    else:
        # file=sys.stderr lässt den Text in Rot erscheinen, kann also auch optional entfernt werden.
        print(f"Die Wahl {nutzer_wahl} ist nicht Schere, Stein oder Papier", file=sys.stderr)
