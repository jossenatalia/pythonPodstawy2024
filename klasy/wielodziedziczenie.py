# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # klasy po których dziedziczymy - B, A
    """
    Klasa C dziedziczy po klasie B i A
    """


class D(A, B):
    """
    Klasa D dziedziczy po klasie A i B
    """

    def method(self):
        super().method()  # dziedziczy po klasie A, B


class E(B, A):
    def method(self):
        print("Metoda z klasy E")


class G(A, B):
    def method(self):
        B.method(self)  # wyraźne wskazanie z której klasy wziąć metodę


class H(A, B):
    def method(self):
        super().method()
        A.method(self)
        print("Metoda z klasy H")


a = A()
a.method()  # Metoda z klasy A

b = B()
b.method()  # Metoda z klasy B

c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

c.method()  # Metoda z klasy B
d = D()
d.method()
print(D.__mro__)

e = E()
e.method()  # Metoda z klasy E

g = G()
g.method()  # Metoda z klasy B

h = H()
h.method()
# Metoda z klasy A
# Metoda z klasy A
# Metoda z klasy H
