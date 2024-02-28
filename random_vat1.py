import random  # liczby pseudolosowe

# help(random)

print(random.random())  # int 1 ... 100
print(random.randint(1, 100))  # float
print(random.random() * 10)  # float
print(random.randrange(7))  # int 0 .. 6
print(random.randrange(1, 100))  # int 1 .. 99

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(lista))

lista_kula = list(range(1, 50))  # 1 -49

for i in range(6):
    wynik = random.choice(lista_kula)
    lista_kula.remove(wynik)
    print(wynik)

print(random.choices(lista_kula, k=6))  # losuje z powtórzeniami
print(random.sample(lista_kula, k=6))  # losuje bez powtórzeń
print(random.sample(lista_kula, 6))  # losuje bez powtórzeń
