age = 47  # int
year = 2023  # int
temp = 36.6  # float
age2 = 37.5  # float

print(age // year)  # dzielenie calkowite bez reszty
print(age % year)  # modulo
print(age ** year)  # potęgowanie
print(len(str(age ** year)))

# przy float jest błąd zaokrąglenia
print(0.2 + 0.7)  # 0.8999999999999999
sum = 0.2 + 0.7
print(f"{sum: .1f}")

do_you_know_python = True
print(do_you_know_python)
print(type(do_you_know_python))  # bool
print(int(do_you_know_python))

print(bool(50 > 100))
# porównanie bitowe
print(True & False)
print(True & True)
print(True | True)
print(True | False)
print(False | False)
print(False & False)

# normalne porównanie
print(True and False)
print(True and True)
print(True or True)
print(True or False)
print(False or False)
print(False and False)

a = 14
b = 3
print(f"Wynik porównania {a} > {b}", a > b)
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)
print(f"Wynik porównania {a} != {b}", a != b)

print(not True)
print(not False)

