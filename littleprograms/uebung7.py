class Hund:  # Name in großge. CamelCase

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
        return f'Hund(name={self.name}, age={self.age})'

    def __str__(self):
        return f'{self.name} ist ein Hund und ist {self.age} Jahre alt.'

    def __del__(self):
            Hund.zaehler -= 1

    def gib_laut(self):
        print(f'{self.name} bellt')
        if self.__gassi_gegangen:
            print("wedelt mit Schwanz weil sich Hund freut")

class Corgi(Hund):
    # es wird standardmäßig nur ein init aufgerufen
    # wenn wir hier keines hätten, dann das von den eltern

    def __init__(self, name, age, iq):
        # wir müssen hier explizit init unserer eltern aufrufen
        super().__init__(name, age) # super() -> Funktion von Basisklasse aufrufen
        # Alternative zu super(): Hund.__init__(self, name, age)
        self.iq = iq
    # wenn kein zusätzliche methode gebraucht wird, muss man super().__init__ + self. nicht angeben!

    def gib_laut(self):
        # override von eltern
        print(f'{self.name} bellt ganz intelligent')
        # wenn ich die implementation der basisklasse brauchen würde, könnte ich super verwenden
        super().gib_laut()

class Mensch:
    def gib_laut(self):
        print("Mensch macht wuff wuff")

class Kind:
    def gib_laut(self):
        print("Kind schreit")



if __name__ == '__main__':
    cheddar = Corgi("Cheddar", 14, 100)
    m = Mensch()
    k = Kind()

    print(cheddar.iq)
    print(cheddar.name)

    cheddar.gib_laut()

    k.gib_laut()

    l = [cheddar, m, k]
    # duck typing
    for laut_geber in l:
        laut_geber.gib_laut()

    l = [k, cheddar]
    for schreihals in l:
        schreihals.gib_laut()

if type(cheddar) == Corgi:
    print("ja ist er")

if type(cheddar) == Hund:
    print("liest niemand")

if isinstance(cheddar, Hund):
    print("is er wieder")