class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        """
        Parametry pracownika
        :param imie:
        :param nazwisko:
        :param pensja:
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    """
    Klasa Manager
    """
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Anna", "Kowalska", 2000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: wynagrodzenie {wyn_prac}")

manager = Manager("Joanna", "Nowak", 3000, 1000)
manager.przedstaw_sie()
wynagrodzenie = manager.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {manager.imie} {manager.nazwisko}: wynagrodzenie {wynagrodzenie}")
