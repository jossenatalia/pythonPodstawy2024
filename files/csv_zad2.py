import csv

filename = 'dane.csv'

fields = []
rows = []

with open(filename, 'r') as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    print(dialect.delimiter, dialect.quotechar, dialect.escapechar)
    file.seek(0) # ustawienia odczytu ponownie na początek pliku
    # csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)
    print(csvreader)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(fields)
print(row)
