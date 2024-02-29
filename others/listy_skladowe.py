numbers = [1, 2, 3, 4, 5]

# tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(f"Squared numbers: {squared}")

# filtrowanie listy
even_number = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_number}")

# modyfikacja w zależności od warunków
modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"Modified numbers: {modifed_numbers}")

# parzysta, nieparzysta
even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(f"Even odd numbers: {even_odd}")

# squared numbers
squared_numbers = [x ** 2 for x in range(1, 6)]
print(f"Squared numbers: {squared_numbers}")

# abs() wartość bezwzględna
numbers2 = [-1, -2, 7, -3, -4, -5, 6]
absolute = [abs(x) for x in numbers2]
print(f"Absolute numbers: {absolute}")

# rozbicie na literki
word = 'Python'
letters = [letter for letter in word]
print(f"Letters: {letters}")
print(list(word))  # rozpakowanie sekwencji

lista1 = [word]
print(lista1)


