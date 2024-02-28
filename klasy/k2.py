class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, name, age, height, gender='k'):
        """
        Metoda inicjalizująca
        :param name:
        :param age:
        :param height:
        :param gender:
        """
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def get_age(self):
        print(f"I am {self.age} years old")

    def get_height(self):
        print(f"My height is {self.height} cm")

    def get_gender(self):
        print(f"I'm a {"woman" if self.gender == "k" else "men"}")

    def pet(self):
        if self.gender == "k":
            print("I have a cat")
        else:
            print("I have a dog")

    def __repr__(self):  # reprezentacja obiektu
        return f"I am {self.name}, {self.age} years old"


print("----------------")
print("Woman")
print("----------------")
cz1 = Human("Anna", 30, 168)
cz1.say_hello()
cz1.get_age()
cz1.get_height()
cz1.get_gender()
cz1.pet()
print("----------------")
print("Men")
print("----------------")
cz2 = Human("Alex", 50, 182, 'm')
cz2.say_hello()
cz2.get_age()
cz2.get_height()
cz2.get_gender()
cz2.pet()

lista = [cz1, cz2]
print(lista)

for i in lista:
    print(i.name)

print(lista)
