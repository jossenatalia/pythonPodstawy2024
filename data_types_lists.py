# lista kolekcja do przechowywania danych
# zachowuje kolejnośc przy dodawaniu danych

list = []  # deklaracja pustej listy
print(type(list))

list.append("Natalia")
list.append("Maciej")
list.append("Jerzy")
list.append("Tadek")
list.append("Anna")
# listy są mutowalne, dokunujemy operacji na bazowej kolekcji

print(list)
print(list[0])
print(list[1])
print(list[2])

print(list[-1])
print(list[len(list) - 1])

print(list[-3])
print(list[-0])  # -0 = 0

# slicowanie
print(list[0:3])  # ['Natalia', 'Maciej', 'Jerzy']
print(list[3:10])  # wypisze ile może ['Tadek', 'Anna']
print(list[9:10])  # []

list[2] = "Katarzyna"
print(list)

# dodanie elementu na zadanym miejscu (indeksie)
list.insert(1, "Olaf")
print(list)

list.remove("Natalia")
print(list)

list.remove(list[0])
print(list)

list.pop(0)
print(list)

print(list)
list.append("Tadek")

print(list)
list.remove("Tadek")

print(list)

list2 = list
print(list)
print(list2)


list3 = list.copy()
print(list)
print(list3)

list.clear()
print(list)
print(list3)

print("Tadek" in list)
print("Anna" in list3)
numbers = [1, 6, 74, 12, 15]
print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers)
numbers.sort(reverse=True)
print(numbers)

krotka = tuple(numbers)
print(krotka)  # (74, 15, 12, 6, 1)
print(type(krotka))  # <class 'tuple'>

