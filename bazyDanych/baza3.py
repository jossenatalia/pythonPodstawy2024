# baza sql - relacyjna baza danych
import sqlite3

try:
    conn = sqlite3.connect("baza_sqlite.db")  # połączenie z bazą, jak pliku nie ma to zostanie stworzony
    c = conn.cursor()
    print("Baza danych została podłączona")

    insert = """
    INSERT INTO software (id, name, price) VALUES (1, 'Python', 200);
    """

    insert2 = """
        INSERT INTO software (id, name, price) VALUES (?, ?, ?);
        """

    select_all = """
    SELECT * FROM software;
    """

    for row in c.execute(select_all):
        print(row)

    c.execute(select_all)
    for row in c.fetchall():
        print(row)

    c.execute(insert2, (2, 'Python', 200))
    for row in c.fetchall():
        print(row)


    # c.execute(insert)
    # conn.commit()
except sqlite3.Error as e:
    print("Błąd połączenia z bazą danych: ", e)
finally:
    if conn:
        conn.close()
        print("Połączenie z bazą danych zostało zamknięte")
