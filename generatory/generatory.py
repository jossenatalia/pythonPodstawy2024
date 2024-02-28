# generator - funkcja zwracająca wyniki
# nie przechowuje poprzednich wyników
# musi pobierać wyniki po kolei
# efektywne zarządzanie pamięcią - ograniczenie zużycia pamięci

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonuje operację, zwraca wynik, zapamiętuje ostatni element




kwadrat(5)
kwa = kwadrat2(5)
print(type(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
# print(next(kwa))  #StopIteration gdy koniec iteracji


def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


def counter_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

cd = counter_down(10)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))



