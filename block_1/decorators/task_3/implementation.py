def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    result = [0]
    def wrapper():
        result[0] += 1
        return result[0]
    return wrapper
