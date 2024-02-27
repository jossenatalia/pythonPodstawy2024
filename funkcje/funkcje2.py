# funkcje zwracające wynik

def dodaj(a, b):
    return a + b  # zwróć wynik

def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(f"Zapłacisz {oblicz_vat(500)} vatu")
print(f"Zapłacisz {oblicz_vat(500, 40)} vatu")
print(f"Zapłacisz {oblicz_vat(vat=40, cena=500)} vatu")

zm = oblicz_vat(1000)
print(zm)
if zm == 1230:
    print("Hurra")

# dodaj(5, 2)
# print(dodaj(5, 2))
#
# wynik = dodaj(5, 2)
# print(f"Wynik działania funkcji {wynik}")
# print(wynik)
# print(dodaj(5, 2))
