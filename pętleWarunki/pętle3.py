# while  pętla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("Komunikat!!!!")
    if licznik > 10:
        break

print(licznik)  # 11

licznik2 = 0
while licznik2 < 10:
    print("Komunikat 2")
    licznik2 += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))
print(lista)
print(lista2)
