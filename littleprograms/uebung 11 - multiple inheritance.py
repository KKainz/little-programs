import abc

class Person:
    def __init__(self, vname, zname):
        self.vname = vname
        self.zname = zname

    def get_info(self):
        return f'{self.vname} {self.zname}'


class Human:
    def __init__(self, nickname):
        self.nickname = nickname

    def quack(self):
        print(f"{self.nickname}*awkward silence* *quack quack*")

    def fly(self):
        print("*ouch*")

# natürlich könnte man das auch ganz ohne diese beiden abstrakten klassen machen
class Swimmer(abc.ABC):
     @abc.abstractmethod
     def swim(self):
         pass

class Eater(abc.ABC):
     @abc.abstractmethod
     def eat(self):
         pass

# zwei oder mehr Elternteile:
class PersonInDuckSimulation(Human, Person, Swimmer, Eater):
    def __init__(self, vname, zname, nickname):
        # wenn wir nur ein init aufrufen wollen, könne wir super() verwenden
        # wenn wir mehrere aufrufen wollen, müssen wir es explizit machen
        Person.__init__(self, vname, zname)
        Human.__init__(self, nickname)

    def swim(self):
         print("swim")

    def eat(self):
         print("eat")





if __name__ == '__main__':
    p = PersonInDuckSimulation("Johann Ernst", "Hinterseer", "Hansi")

    p.fly()
    print(p.get_info())
    p.eat()
    p.swim()
    p.quack()
    print(PersonInDuckSimulation.mro()) # zeigt mir in welcher reihenfolge methoden gesucht werden