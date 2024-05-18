def create_operation(operation):
    if operation == "multiplier":
        def multiplier(x, y):
            return x * y

        return multiplier
    elif operation == "division":
        def division(x, y):
            return x / y

        return division


my_func_add = create_operation("multiplier")
print(my_func_add(1, 2))
my_func_add = create_operation("division")
print(my_func_add(1, 2))


home = lambda x, y: x-y
print(home(10, 3))


def home_1(a, b):
    return a - b

print(home_1(20, 12))


class Home:
    def __init__(self, a):
        self.a = a


    def __call__(self, b):
        print(f'Стороны: {self.a} и {b}')
        return self.a * b


result = Home(a=3)
result1 = result(b=7)

print(f'Площадь: {result1}')