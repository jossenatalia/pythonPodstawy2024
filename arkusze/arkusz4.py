import pandas as pd

from bazyDanych.baza4 import engine

lista = [[2, 5, 8, 9], [4, 6, 7, 10]]
slownik = {"Imie": ['Ania', 'Julia', 'Kevin'], 'wiek': [18, 25, 67]}
zbior = pd.DataFrame(lista)

zbior.columns = ["jeden", "dwa", "trzy", "cztery"]
sl = pd.DataFrame(slownik)
print(sl)
print(zbior)

zbior.to_csv('test1.csv')
sl.to_csv('test2.csv')