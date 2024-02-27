# csv - dane oddzielone znakiem podziału kropka, przecinek, spacja, tab
# Zenek, Marek, Anka, Tomek

import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'},
    {'name': 'anka', 'branch': 'dvf', 'year': '1', 'cgpa': '2'},
    {'name': 'daniel', 'branch': 'efg', 'year': '5', 'cgpa': '6'},
    {'name': 'olka', 'branch': 'tgh', 'year': '8', 'cgpa': '4'}
]
filename = 'dane.csv'
dict = dict(zip(fields, row))
print(dict)

with open(filename, 'w', newline='') as csvfile:
    # proste użycie, wiersz po wierszu
    # csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields, delimiter=';')
    csvwriter.writeheader()
    #zapisanie pojedynczego wiersza
    # csvwriter.writerow(dict)
    csvwriter.writerows(dict_list)
