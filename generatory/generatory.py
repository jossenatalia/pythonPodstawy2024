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




# kwadrat(5)
# kwa = kwadrat2(5)
# print(type(kwa))
# print(next(kwa))
# print(next(kwa))
# print(next(kwa))
# print(next(kwa))
# print(next(kwa))
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


# c = counter()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
#
# cd = counter_down(10)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))

def counter_2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break;
        n += 1


c3 = counter_2(10)
print(next(c3))
print(next(c3))  # None
print(next(c3))
print(next(c3))
c3.send('OK')
print(next(c3))
c3.send('q')
# print(next(c3)) StopIteration



