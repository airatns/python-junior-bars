"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

# Test message
# None
# В первый раз сработал print() внутри функции data_transmitter().
# А во второй раз вернулся None, т.к. возврата из функции не было.
