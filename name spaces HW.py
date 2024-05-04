def test_fuction(x):
    def inner_function(x):
        if x > 0:
            print('Я в области видимости функции test_function')
    inner_function(x)
b = test_fuction(8)
print(b)
# inner_function() - не выводится вне функции test_function,
# так как она существует локально в объемлющей области видимости функции test_function
