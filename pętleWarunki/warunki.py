# instrukcje warunkowe
# instrukcje sterowania przepływem programu

# if warunek:
#     instrukcja

odp = False

if odp:
    print("Brawo")

print("Dalsza część programu")

if odp:
    print("Brawo")
else:  # domyślne działanie
    print("Musisz uczyć się dalej")

# Oblicz podatek
# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
#
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek} zł")

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabacik}")

# lista_bledow = []
# alert_system = input("Podaj źródło alertu")
# error = 'medium' if alert_system == 'email' else 'critical'
#
# error_message = 'Stało się coś strasznego'
# if alert_system == 'console':
#     print(error_message)
# elif alert_system == 'email':
#     print("Sytem email")
#     if error == 'medium':
#         lista_bledow.append("ostrzezenie")
#     elif error == 'critical':
#         lista_bledow.append("krytyczny")
#     else:
#         lista_bledow.append("inny błąd")
# else:
#     print("Nie znam takiego systemu")
#
# print(lista_bledow)

odpowiedz = int(input("W którym roku odbyła się bitwa pod grunwaldem?"))

if odpowiedz == 1410:
    print("Dobra odpowiedź!")
else:
    print("Zła odpowiedź. Spróbuj ponownie.")



