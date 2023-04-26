def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    result = list(filter(lambda i: (i % 7 == 0 and i % 5 != 0), range(1000, 2000)))
    return result
