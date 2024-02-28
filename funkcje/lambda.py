# skrócony zapis funkcji
# funkcja anonimowa
# możliwość deklaracji w miejscu wykonania funkcji
from functools import reduce


def odejmij2(a, b):
    return a - b


print(odejmij2(5, 6))

odejmij = lambda a,b: a - b  # return - lambda zwraca wynik, jeśli deklarujemy powinno używać się def a nie przypisywanie do zmiennej
print(odejmij(5, 6))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(18))
print(wiek(5))
print(wiek(16))



lista = [1, 2, 3, 4, 24, 45, 50, 100, 200]
# l = []
# for i in lista:
#     l.append(i * 2)


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(i)
print(l2)
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)
#filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 100 and x % 2 != 0, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x // 2 == 0, lista))}")

#reduce
lista_reduce = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, lista_reduce))
print(reduce(lambda x, y: x * y, lista_reduce))
print(reduce(lambda x, y: x % y, lista_reduce))

