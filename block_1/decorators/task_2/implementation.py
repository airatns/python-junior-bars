class MyException(Exception):
    pass


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(number):
        if number is not None or isinstance(number, int) or number >= 0:
            return func(number)
        else:
            raise MyException
    return wrapper


def cache(func):
    """
    Обертка, которая кеширует результат.
    """
    memo_cache = {}
    def wraper(number):
        if number not in memo_cache:
            result = check_value(func)
            memo_cache[number] = result(number)
        return memo_cache[number]
    return wraper


