class MyException(Exception):
    pass


class Value:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        try:
            result = self.number + other
        except:
            raise MyException
        else:
            return result

    def __sub__(self, other):
        try:
            result = self.number - other
        except:
            raise MyException
        else:
            return result

    def __mul__(self, other):
        try:
            result = self.number * other
        except:
            raise MyException
        else:
            return result

    def __truediv__(self, other):
        if other != 0 and isinstance((self.number, other), int):
            result = self.number / other
            return result
        else:
            raise MyException
