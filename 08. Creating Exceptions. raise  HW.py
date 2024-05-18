# class BadName(Exception):
#     pass
#
#
# def h(a, b):
#     if b == '':
#         raise BadName("Имя не задано")
#     return a + b
#
#
# print(h('Город', ' Грехов'))
# print(h('Город', ''))
#

class InvalidDataException(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info

def k(login, pasword):
    if pasword != 'Food':
        raise InvalidDataException('Данные не верны', 'Попробуйте снова')
    return login + pasword

try:
    result = k('Orange', 'car')
    print(result)
except InvalidDataException as e:
    print(f'Сообщение об ошибке: {e.message}')
    print(e.extra_info)

print(k)