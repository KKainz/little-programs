from dataclasses import dataclass

@dataclass
class WeeklySmartphoneSales:
    smartphone: str
    week: int
    numbers_sold: int = 0

# rekursive funktion (ruft sich selbst auf, bis abbruchbedingung)
def fakultaet(n):
    if n == 1:
        print("yay ein ende ist bei 1 in sicht")
        return 1
    else:
        print(f"rufe gleich {n - 1} fakultaet auf")
        return n * fakultaet(n - 1)


if __name__ == '__main__':
    iphone_w40 = WeeklySmartphoneSales("iPhone 11", 40)

    iphone_w40.numbers_sold = 100000
    print(iphone_w40)

    # list comprehension
    l2 = [i ** 2 for i in range(10)]
    print(l2)

    # list comprehension mit bedingung
    # eintrag nur für geradzahlige i
    l3 = [i ** 2 for i in range(10) if (i % 2) == 0]
    print(l3)

    # liste mit listen generieren -> quasi so wie wenn wir 2 verschachtelte for schleifen hätten
    ll = [[i*j for j in range(10)] for i in range(10)]
    print(ll)

    # mit muss bewusst sein, dass eine hier (in __main__) definierte funktion auc nur hier verwendbar ist
    def plus_one(x):
        return x + 1

    # alternative:
    plus_one_two = lambda x: x + 1

    print(plus_one(2))
    print(plus_one_two(2))

    # anonyme funktionen definieren (funktion hat keinen namen)
    print((lambda x, y: x * y)(2,4))

    print(fakultaet(5))











