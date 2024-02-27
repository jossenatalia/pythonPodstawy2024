a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 6
    b = 8
    print(a + b)


print("Zmienna a z góry (globalna)", a)
# funkcja ma lokalne zmienne, wykona działanie, ale nie zmieni wartości globalnie
dodaj()
print("Zmienna a z góry (globalna)", a)
dodaj2()

dodaj3()
print("Zmienna a z góry (globalna)", a)
