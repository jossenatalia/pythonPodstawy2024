from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Dokumentacja opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko, Ko, Ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("Kier kieeeer kir")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa w Pythonie
    """
    def wydaj_odglos(self):
        print("Uhu uhuu uhhuuu")


# or1 = Ptak("Orzeł Bielik", 45)
# or1.latam()  # Tu Orzeł Bielik Lecę z szybkością 45
# or1.wydaj_odglos()

# kur1 = Ptak("Kura", 0)
# kur1.latam()
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()
kur2.wydaj_odglos()
kur2.dziobanie()

orzel = Orzel("Orzel Bielik", 50)
orzel.wydaj_odglos()
orzel.poluj()

sowa = Sowa("Sowa", 30)
sowa.wydaj_odglos()
