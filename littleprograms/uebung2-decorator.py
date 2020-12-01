def my_decorator(func): # Dekorator
    def text_around(para):
        print(f'Davor {func.__name__}')
        func(para) # Funktion wird aufgerufen
        print(f'Danach {func.__name__}')
    return text_around

# das ist die kurzversion der zuweisung hallo = my_decorator(hallo)
@my_decorator
def hallo(txt):     # zu dekorierendes Objekt
    print(f'Hallo {txt}')

if __name__ == '__main__':
    hallo("DAT")

    # wenn ich ab sofort hallo aufrufe, will ich, dass noch etwas anderes gemacht wird
    # und zwar, dass was in meinem decorator passiert

    # im python tutor anschauen was wann wohin zeigt (fuer besseres verstaendnis)

    # x = my_decorator(hallo)  # wird nur mitgegeben, nicht aufgerufen
    # x('DAT2')

    # hallo = my_decorator(hallo)
    hallo("DAT")


