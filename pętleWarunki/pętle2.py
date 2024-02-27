dict = {'name': 'Radek', 'nazwisko': 'Kowalski'}

for key in dict:
    print(key)

for value in dict.values():
    print(value)

for i in dict.items():
    print(i)

for key, value in dict.items():
    print(key, "=>", value)

dict2 = {'name': 'imie', 'company': 'Company'}
print(dict2)

print({value: key for key, value in dict2.items()})

d2 = {}
for key, value in dict2.items():
    d2[value] = key
print(d2)
