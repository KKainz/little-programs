class Hund: # Name in großge. CamelCase

    species = 'Canis lupus familiaris' # Klassenattri.

    def __init__(self, name, age): # Zum Initialisieren
        self.name = name # Instanzattribut
        self.age = age

if __name__ == '__main__':

    rex = Hund("Kommissar Rex", 14)
    lassie = Hund("Lassie", 10)

    print(rex.age) # Zugriff auf eine objekt- bzw. instanzvariable

    print(lassie.age)

    print(lassie.species) # geht theoretisch auch (aber bitte nicht schreibend darauf zugreifen)
    # lassie.species = "Abenteuerhuendin"
    # nicht machen, weil jetzt wuerde neues instanzattribut erzeugt werden
    # am beseten immer ueber klassenvariable zugreifen

    print(Hund.species)
    print(lassie.species)

    print(dir(lassie))
    # Variante um schön anzusehen
    # automatisch auch eigenschaften von klassen dabei

    print(lassie.__dict__) # zeigt alle werte auf die ich zugreifen kann
    # immer wenn ich mit "." zugreife, schuat python im __dict__ ob es das kennt,
    # falls nicht, wird im dict der Klasse nachgeschaut

    








