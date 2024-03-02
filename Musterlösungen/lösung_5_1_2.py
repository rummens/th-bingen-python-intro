from lösung_5_1_1 import Tier


class Hund(Tier):

    def __init__(self, name: str, alter: int, farbe: str):
        super().__init__(name=name, alter=alter, farbe=farbe, anzahl_beine=4, tier_art="hund")

    @staticmethod
    def gib_arten_info():
        # https://de.wikipedia.org/wiki/Hunde
        return ("Die Hunde (Canidae) sind eine Familie innerhalb der Überfamilie der Hundeartigen (Canoidea). Zu "
                "dieser Familie gehören verschiedene als „Fuchs“ und „Schakal“ bezeichnete Arten, Kojoten sowie die "
                "Wölfe, deren domestizierte Unterart (der Haushund) als Namensgeber der Gruppe dient.")

    def mach_geraeusch(self):
        # Wir wissen, dass es ein Hund ist. Also kann er nur "wuff" machen
        return "wuff"


class Katze(Tier):

    def __init__(self, name: str, alter: int, farbe: str, ist_lieb: bool):
        super().__init__(name=name, alter=alter, farbe=farbe, anzahl_beine=4, tier_art="katze")

        self.ist_lieb = ist_lieb

    @staticmethod
    def gib_arten_info():
        # https://de.wikipedia.org/wiki/Katzen
        return ("Die Katzen (Felidae) sind eine Familie aus der Ordnung der Raubtiere (Carnivora) innerhalb der "
                "Überfamilie der Katzenartigen (Feloidea). Sie sind auf allen Kontinenten außer in den Polarregionen "
                "und Australasien und Ozeanien verbreitet, wobei die domestizierte Hauskatze durch den Menschen auch "
                "in diese Regionen vorgedrungen ist. ")

    def mach_geraeusch(self):
        # Wir wissen, dass es eine Katze ist aber abhänig ob diese lieb ist oder nicht, kann ein anderes Geräusch
        # gemacht werden
        if self.ist_lieb:
            return "miau"
        else:
            return "Fauch"


if __name__ == '__main__':
    bello = Hund("Bello", alter=5, farbe="Schwarz")
    garfield = Katze("Garfield", alter=2, farbe="Orange", ist_lieb=True)

    print(bello.gib_arten_info())
    print(garfield.gib_arten_info())
    print("-------------------------")
    print(bello.gib_meine_info())
    print(garfield.gib_meine_info())
    print("-------------------------")
    bello.habe_geburtstag()
    garfield.ist_lieb = False
    print(bello.gib_meine_info())
    print(garfield.gib_meine_info())
    print("-------------------------")
    print(bello.mach_geraeusch())
    print(garfield.mach_geraeusch())
    print("-------------------------")
