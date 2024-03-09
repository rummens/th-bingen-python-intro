class Tier:
    geraeusch_dict = {
        "hund": "wuff",
        "katze": "miau",
        "kuh": "muuh"
    }

    def __init__(self, name: str, alter: int, farbe: str, anzahl_beine: int, tier_art: str):
        self.name = name
        self.alter = alter
        self.farbe = farbe
        self.anzahl_beine = anzahl_beine
        self.tier_art = tier_art

    @staticmethod
    def gib_arten_info():
        return "Hmm, da haben wir noch nix."

    def gib_meine_info(self):
        return (f"Ich bin die {self.tier_art} {self.name} und bin {self.alter} Jahre alt. Mein Fell ist {self.farbe} "
                f"und ich habe {self.anzahl_beine} Beine.")

    def mach_geraeusch(self):
        # Wir müssen prüfen. dass die Tier Art bekannt ist. Ansonsten können wir später kein Geräusch ausgeben
        if self.tier_art.lower() not in Tier.geraeusch_dict:
            raise ValueError(f"Tier {self.tier_art} nicht bekannt! Kann kein Geeräusch erzeugen.")

        # Geräusch anhand von Tier Art ausgeben
        return Tier.geraeusch_dict[self.tier_art]

    def habe_geburtstag(self):
        # Alter um eins erhöhen
        self.alter += 1


if __name__ == '__main__':
    bello = Tier("Bello", alter=5, farbe="Schwarz", anzahl_beine=4, tier_art="hund")
    garfield = Tier("Garfield", alter=2, farbe="Orange", anzahl_beine=4, tier_art="katze")

    print(bello.gib_arten_info())
    print(garfield.gib_arten_info())
    print("-------------------------")
    print(bello.gib_meine_info())
    print(garfield.gib_meine_info())
    print("-------------------------")
    bello.habe_geburtstag()
    print(bello.gib_meine_info())
    print(garfield.gib_meine_info())
    print("-------------------------")
    print(bello.mach_geraeusch())
    print(garfield.mach_geraeusch())
    print("-------------------------")

