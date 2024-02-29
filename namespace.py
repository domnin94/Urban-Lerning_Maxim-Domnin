def test():
    a = 2
    b = 4
    print('test:', a)
    print('test:', b)
test()

def test_2(x, y, z):
    print('Функцию вызвали с параметром', x)
    print('Функцию вызвали с параметром', y)
    print('Функцию вызвали с параметром', z)
result = test_2(x = 2, y = 3, z = 4)
print(result)
