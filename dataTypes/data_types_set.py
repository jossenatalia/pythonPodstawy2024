# przechowuje niepowtarzające się elementy (unikalne)
# nie zachowuje kolejności
# nie ma indeksu

list = [1, 5, 1, 17, 78.85, 5, 1, 17, 758]
print(list)

zbior = set(list)
print(zbior)  # {1, 5, 78.85, 17, 758}

zb2 = set()  # pusty zbiór
print(type(zb2))  # <class 'set'>
print(zb2)  # set()


zbior.add(33)
zbior.add(183)
zbior.add(33)
zbior.add(337)
zbior.add(337)

print(zbior)

print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior)

zbior.remove(758)
print(zbior)

zb2 = {667, 15, 758, 15, 785, 96.45, 745, 17}
print(zb2)

print(zbior | zb2)  # suma zbiorów
print(zbior & zb2)  # część wspólna
print(zbior - zb2)  # różnica wspólna
print(zbior.difference(zb2))  # różnica wspólna
print(zbior.union(zb2))  # suma, zwraca nowy zbiór, nie zmienia zbioru

print("Update")  # zbiory się nadpisują!!!
zbior.update(zb2)
print(zbior)
print(zb2)

