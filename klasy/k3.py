# klasa dom
# metraż, kolor, liczba_okien
# pola mają być prywatne
# wystawić metody do odczytu i zapisu tych pól
# dodać metodę prywatną farba

class Dom:
    """
       Klasa opisująca dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        """
        Parametry domu
        :param metraz:
        :param kolor:
        :param liczba_okien:
        """
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def get_metraz(self):
        print(f"Metraz {self.__metraz}")

    def get_kolor(self):
        return self.__farba()

    def get_liczba_okien(self):
        print(f"Liczba okien {self.__liczba_okien}")

    def __farba(self):
        print(f"Kolor farby {self.__kolor}")

    def zmien_metraz(self):
        self.__metraz += 10


dom = Dom(100, "czerwony", 5)
dom.get_metraz()
dom.get_kolor()
dom.get_liczba_okien()
dom.zmien_metraz()
dom.get_metraz()
