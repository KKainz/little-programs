import abc

class Things:
    def __init__(self):
        self.var = 12  # private
        self._prot_var = 11  # protected
        self.__prot_vars = 33  # private

class Dog(Things):

    def __init__(self):
        super().__init__()
        self._prot_var
        self.__prov_vars = 55


    def make_noise(self):
        print("wuff")

class Human:
    def make_noise(self):
        print("Hello")

    def make_hello(self):
        print("hellooooo")

class Car:

    def make_noise(self):
        print("Brummm")

# abkstrakte Klassen ermöglichen ein gemeinsames Interface oder Schnittstellte zu definireren
# gibt vor welche Methoden/Eigenschaften alle davon abgeleiteten Klassen haben müssen
# man kann keine Instanzen von abstrakten Klassen anlegen

class Konto(abc.ABC):

    def __init__(self):
        self.balance = 0

    def set_to_zero(self):
        self.balance = 0

    @abc.abstractmethod
    def calc_interest(self):
        pass

    @abc.abstractmethod
    def deposit(self):
        pass

class Sparkonto(Konto):

    def calc_interest(self):
        pass

    def deposit(self):
        pass


if __name__ == '__main__':
    # k = Konto() -> geht nicht weil abstrakte klasse
    k = Sparkonto()
    h = Human()
    d = Dog()
    c = Car()

    # jeder macht ein Geräusch
    d.make_noise()
    h.make_noise()
    c.make_noise()
    # > umständlich, geht einfacher
    # möglichkeit über liste
    l = [d, h, c]
    for objekt in l:
        objekt.make_noise()

