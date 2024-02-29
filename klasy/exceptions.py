class MyException(Exception):  # dziedziczenie po klasie Exception, tworzymy własny wyjątek
    def __init__(self, message):
        super().__init__(message)



try:
    # print(5/0)
    raise ZeroDivisionError("Nie dziel przez zero")  # rzucanie wyjątku
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)


list = [1, 0, 2, 3]
for i in list:
    try:
        if i == 0:
            raise MyException("i nie może być 0")
        print(f"Wartość : {i}")
    except MyException as e:
        print("i nie może być 0", e)
