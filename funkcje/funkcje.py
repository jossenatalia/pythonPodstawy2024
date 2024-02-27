# funkcja - blok kodu
# możliwość wywoływania w dowolnej chwili
# możliwośc uruchamiania wielokrotnie
# funkcja jest deklarowana, wykonuje się w miejscu wywołania funkcji

a = 4
b = 8


def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # argumenty pozycyjne, brane do funkcji według pozycji
    print(a + b)


def dodaj3(a, b, c=0):
    print(a + b + c)


def odejmij(a, b, c=0):
    print(a - b - c)


dodaj()
dodaj2(5, 6)
dodaj3(1, 2)
dodaj3(1, 2, 4)

# parametry nazwane, brane według nazwy argumentu
odejmij(c=3, a=1, b=2)
odejmij(1, 2, 3)
odejmij(7, c=8, b=9) # mieszany, pozycji musi byc przed nazwanymi
odejmij(7, c=8, b=9) # mieszany, pozycji musi byc przed nazwanymi
