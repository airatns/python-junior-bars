"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number = 3
        print(number)

    printer()
    print(number)


print_msg(9)

# 3
# 3
# В первый раз выведется 3 из функции printer()
# Во второй раз выведется 3, т.к. из функции printer() произошла подмена локальной переменной
# И возвращается 'number = 3', определенный внутри функции printer()
