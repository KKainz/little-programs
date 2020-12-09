class Motor:
    def __init__(self):
        # das ist für andere teile des autos interessant
        # diese möchten darauf zugreifen können
        # deswegen machen wir es public
        self.umdrehungen_pro_minute = 0

        # es sollten keinen anderen teil des autos interessieren wie viel benzin eingespritzt qwird
        # deswegen --> private
        self.__einspritzmenge = 0

        # protected: immer dann wenn nzr wir als klasse und unsere subklassen darauf zugreifen sollen
        self._motor_modus = "sport"

        # es geht um daten die zuvor public waren
        # jetzt möchte ich den zugriff darauf nur über meine methoden erlauben
        # --> property mit einer private o. protected variable dahinter (üblich private)
        self.geschwindigkeit = 50

    @property
    def geschwindigkeit(self):
         # theoretisch müsste ich hier noch daten transformieren
        # zB geb.datum in alter umwandeln, falls gefragt
        print("getter Zugriff")
        return self.__geschwindigkeit # unbedingt mit __!!

    @geschwindigkeit.setter
    def geschwindigkeit(self, value):
        print("setter zugriff")
        if value >= 0 and value <= 250:
            self.__geschwindigkeit = value  # unbedingt mit __!!

    # geht auch mit methoden??:
    def __interne_fkt():
        print("hallo")



if __name__ == '__main__':
    m = Motor()

    print(m.umdrehungen_pro_minute)
    m.umdrehungen_pro_minute = 1000
    print(m.umdrehungen_pro_minute)

    # python benennt den namen um
    # achtung: sollte man nicht machen
    print(m._Motor__einspritzmenge)

    # keine umbenennung bei protected
    # trotzdem nicht machen ;)
    print(m._motor_modus)

    print(m.geschwindigkeit)




