# krotka - niezmienna kolekcja, niemutowalna
# krotka może mieć 0 elementów, jeden element, nieskończenie wiele elementów

tuple1 = ("Radek",)
print(len(tuple1))
print(tuple1)
print(type(tuple1))

tuple2 = ("Anna", "Mariusz", "Olaf", "Grzegorz")
print(tuple2)
print(type(tuple2))

tuple3 = (2.3, 1, 18, 6.7, 100)
print(tuple3)
print(type(tuple3))

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

tp = 1, 2, 3
print(type(tp))
# a, b = tp rozpakowanie tupli, to nie zadziała
a, *b = tp
print(a)
print(b)  # a = 1 b = [2, 3]

tuple5 = 'Radek', 'Asia', 'Zbyszek', 'Tomek'
print(len(tuple5))
print(tuple5)
*name1, name2, name3 = tuple5
print(name1, name2, name3)
name1, *name2, name3 = tuple5
print(name1, name2, name3)
name1, name2, *name3 = tuple5
print(name1, name2, name3)

list1 = list(tuple5)
print(list1)
print(type(list1))

