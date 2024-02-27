# napisać funkcję, która oblicza średnią ocen

def liczby(*cyfry):
    print(cyfry)
    suma = sum(cyfry)
    count = len(cyfry)
    avg = suma / count
    print(f"Średnia to {avg}")


liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
