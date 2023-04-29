import time

class MyException(Exception):
    pass

def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
                if result:
                    return result
                else:
                    time.sleep(delay)
            raise MyException
        return wrapper
    return func_decorator
