# klasy - element programowania obiektowego
# szablon, przepis na obiekt (stempelek)
# posiada cechy - pola
# funkcje - funkcje możliwe do wykonania na obiekcie
# obiekt - stworzony według przepisu (odcisk stempla) - instancja klasy
# Paradygmaty: abstrakcja, hermetyzacja (enkapsulacja), dziedziczenie, polimorfizm

# deklaracja klasy = tu siię nie nie wykonuje, adres obiektu
class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """
    name = ''
    age = None
    gender = 'k'

    def print_name(self):  # musi mieć parametr self
        print(f"My name is {self.name}")

    def print_age(self):
        print(f"I'm {self.age} years old")


print(Human.__doc__)
cz1 = Human()  # tworzenie obiektu, moment uruchomienia klasy
# print(cz1)
print(cz1.name)
print(cz1.age)
print(cz1.gender)

cz1.name = 'Anna'
cz1.age = 38

print(cz1.name)
print(cz1.age)
print(cz1.gender)

cz1.print_name()

# stworzyć inny obiekt odmiennej płci
cz2 = Human()
cz2.name = 'Andrzej'
cz2.age = 42
cz2.gender = 'm'

cz1.print_name()
cz1.print_age()
cz2.print_name()
cz2.print_age()
