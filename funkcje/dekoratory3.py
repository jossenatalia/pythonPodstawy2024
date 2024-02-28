import time
import numpy as np

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        print(f"Czas wykonania funkcji {func.__name__}: {exec_time}")
        return result

    return wrapper


@measure_time
def my_function():
    """Dokumentacja"""
    pass


@measure_time
def my_wait():
    time.sleep(2)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += 1
    print("Sum is: ", suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is: ", total)


@measure_time
def my_sum_with_sum():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is: ", total)


# print(my_function().__doc__)
# my_function()
# my_wait()
my_for_sum()
my_sum_without_for()
my_sum_with_sum()
