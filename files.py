# pliki
# kontekst manager
# with
# aby obsłużyć bezpiecznie sytuacje krytyczne

"""
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    ========= ===============================================================
"""

with open('test.log', 'w') as fh:  # filehandler
    fh.write('Hello\n')
    fh.write('Kolejne\n')
    fh.write('Jeszcze jeden\n')

with open('test.log', 'w') as fh:
    fh.write("Skasowany\n")

with open('test.log', 'a') as f:
    f.write("Dodane\n")
    f.write("Kolejne dodane\n")

try:
    with open('test.log', "x") as t:
        t.write("Dodane\n")
except FileExistsError:
    print("Plik istnieje, użyj innej nazwy")

with open('test.log', 'a', encoding='utf-8') as f:
    f.write("Dodane\n")
    f.write("Kolejne dodane śś\n")

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)