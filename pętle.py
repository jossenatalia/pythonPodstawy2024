# wielokrotnie powtarzany kod
from itertools import zip_longest

for i in range(10):  # 0 - 9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # nie ma zmiennej
    pass


for i in range(10):
    print((i * 20))

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

for c in lista3:
    if c == 2:
        c += 1
    print(c)

ludzie = ['Radek', 'Zenek', 'Asia', 'Tomek', 'Jarek']
wiek = [47, 67, 34, 32]

# for i in range(len(ludzie)):
#     print(ludzie[i], wiek[i])
#
# for i in range(len(ludzie)):
#     print(ludzie.index(ludzie[i]), ludzie[i], wiek[i])
#
# for o, w in zip(ludzie, wiek):
#     print(o, w)
#
# for o in enumerate(zip(ludzie, wiek)):
#     print(o)

# a, b = (3, ('Tomek', 32))
# print(a, b)
# c, d = b
# print(a, c, d)
# for i, (o, w) in enumerate(zip(ludzie, wiek)):
#     print(i, o, w)

zipped = zip_longest(ludzie, wiek, fillvalue='NaN')
for item in zipped:
    print(item)

for i in range(0, 10, 2):  # start, stop, step (krok)
    print(i)

for i in range(-10, 10, 2):
    print(i)

for i in range(10, 0, -1):  # pętla do tyłu
    print(i)
