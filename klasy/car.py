class Car:
    """
    Klasa opisująca samochód w Pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole jest prywatne

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmień bieg")


car1 = Car('Saab', '2024')
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car1.__predkosc)
car1.__predkosc = 0  # nadajemy pole publiczne o tej samej nazwie, lepiej tego nie robić
car1.licznik()
car1.hamuj()
car1.licznik()
