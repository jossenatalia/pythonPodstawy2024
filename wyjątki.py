# wyjątki
# przerywają działanie programu

# print(2 / 0)
# print("Dalsza część programu")

# try except [else, finally]

# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("Nie dziel przez zero")
#
# print("Dalsza część programu")


# aplikacja kalkulator
# daje do wyboru działania
# pobrać liczby
# wyświetlić wynik działania 1 + 3 = 4

print('''
1. Dodawanie
2. Odejmnowanie
3. Mnożenie
4. Dzielenie
''')

try:
    a = int(input("Podaj liczbę a"))
    b = int(input("Podaj liczbę b"))
    operacja = int(input(f"Wybierz działanie matematyczne"))

    match operacja:
        case 1:
            print(f"Wynik działania: {a + b}")
        case 2:
            print(f"Wynik działania: {a - b}")
        case 3:
            print(f"Wynik działania: {a * b}")
        case 4:
            try:
                print(f"Wynik działania: {a / b}")
            except ZeroDivisionError:
                print("Nie dziel przez 0")
        case _:
            print("Nie znam takiego działania")
except ValueError as e:
    print("Błąd wartości", e)
except TypeError as e:
    print("Błąd typu", e)
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)
except Exception as e:
    print("Błąd", e)
