class Hund:  # Name in großge. CamelCase
    """ Hundeklasee

        Attribute:
        -------------
        name: str
        Name des Hundes

        age: int
        Alter des Hundes"""

    species = 'Canis lupus familiaris'  # Klassenattri.
    zaehler = 0  # soll mitzählen wieviele Objekte gerade leben

    @classmethod
    def get_anzahl_hunde(cls):
        return cls.zaehler

    def __init__(self, name, age):  # Zum Initialisieren
        self.__name = name  # Instanzattribut
        self.age = age
        self._gefuettert = False        # protected attribut
        self.__gassi_gegangen = False   # private attribut
        Hund.zaehler += 1

    @property           # mit props
    def age(self):
        print("age getter aufgerufen")
        return self.__age

    @age.setter
    def age(self, value):
        print("age setter aufgerufen")
        self.__age = value

    @property               # wenn nur prop muss __name in class so geändert werden --> nur getter, kein setter
    def name(self):
        return self.__name


    def __repr__(self):
        """returns 'Hund (name), (age)'"""
        return f'Hund(name={self.name}, age={self.age})'

    def __str__(self):
        return f'{self.name} ist ein Hund und ist {self.age} Jahre alt.'

    def __del__(self):
            Hund.zaehler -= 1

    def gib_laut(self):
        """hund gibt laut"""
        print(f'{self.name} bellt')
        if self.__gassi_gegangen:
            print("wedelt mit Schwanz weil sich Hund freut")


if __name__ == '__main__':
    rex = Hund("Kommissar Rex", 14)
    lassie = Hund("Lassie", 10)

    rex.gib_laut()
    print(rex._gefuettert)  # nicht machen, weil protected
    # print(rex.__gassi_gegangen)  --> geht nicht wg. name mageling
    print(rex._Hund__gassi_gegangen)  # funktioniert, aber nicht machen
    print(rex._Hund__age)   # so kann man noch direkt auf age zugreifen
    print(rex.age)          # greift jetzt auf getter zu

    print(lassie.name)
    # rex.name = "Scooby Doo"  --> Name kann nicht mehr geändert werden


# Parameter mit default werten NIE verändern














