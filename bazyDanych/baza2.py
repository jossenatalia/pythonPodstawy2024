# baza sql - relacyjna baza danych
import functools
import sqlite3

try:
    conn = sqlite3.connect("baza_sqlite.db")  # połączenie z bazą, jak pliku nie ma to zostanie stworzony
    # conn = sqlite3.connect(":memory:")  # baza w pamięci
    c = conn.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS sqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''
    print("Baza danych została podłączona")
    # c.execute(query)
    # conn.commit()
    with open("tables.sql", "r") as file:
        sql_script = file.read()

    c.executescript(sql_script)
    conn.commit()
except sqlite3.Error as e:
    print("Błąd połączenia z bazą danych: ", e)
finally:
    if conn:
        conn.close()
        print("Połączenie z bazą danych zostało zamknięte")
