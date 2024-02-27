# słownik - typ danych para klucz - wartość
# {'user': "Radek, 'wiek': 38}
# odpowiednik jsona

dict = {}
print(dict)
print(type(dict))

# dodanie elementu do słownika
dict['name'] = 'Radek'
print(dict)
dict['wiek'] = 39
print(dict)
print(dict['wiek'])  # 39
print(dict.keys())    # dict_keys(['name', 'wiek'])
print(dict.values())  # dict_values(['Radek', 39])
print(dict.items())   # dict_items([('name', 'Radek'), ('wiek', 39)])

dict.update({'gender': 'male'})
print(dict)

dict2 = {'x': 2}
print(dict2)
dict2.update([('y', 3), ('z', 2)])
print(dict2)

#gdy brak klucza w słowniku
print(dict.get('wzrost'))
print(dict.get('wzrost', 'default'))

#napisać aplikację słownik
dict_translate = {'imie': 'name',
                  'kot': 'cat',
                  'pies': 'dog'}
print(dict_translate['pies'])

#input() pobiranie danych od usera
key = input("Podaj słowo do przetłumaczenie")
print(dict_translate[key])

