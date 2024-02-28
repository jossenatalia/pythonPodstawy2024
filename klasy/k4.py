# dziedziczenie
# mamy klasę

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczenie po klasie pojazd
    """
    Klasa samochód
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka: {self.marka}")


poj = Pojazd("zielony")
# poj.info()
sam = Samochod("czerwony", "Izera")
# sam.info()

lista = [poj, sam]
for i in lista:
    i.info()
    
# polimorfizm obiektych różnych klasa posiadaja wspólne cechy i funkcje, możemy te same operacje wykonywać
# dziedziczenie wspólne cechy dla obiektów i podklas, zachowanie cech polimorfizmu
