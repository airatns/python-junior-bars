import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args):
        start = time.time()
        func(*args)
        duration = time.time() - start
        return f'Время выполнения функции: {duration} секунд'
    return wrapper


@time_execution
def calc_factorial(number):
    product = 1
    for element in range(1, number + 1):
        product *= element
    return product


print(calc_factorial(11))
