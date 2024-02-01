def print_params(x, y):
    print('Функцию вызвали с параметром', x, y)
    power = x * y
    return power

for x in range(2):
    result = print_params(x=6, y=4)
    print(result)



