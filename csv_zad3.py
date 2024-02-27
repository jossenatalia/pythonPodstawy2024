import pandas

data = pandas.read_csv('dane.csv', delimiter=";")

print(data)
print(data.columns)
print(data.values)
print(data.items)
