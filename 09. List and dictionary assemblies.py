
def car(x):
    return x ** 2


def car_2(x):
    return x % 2


my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(car, filter(car_2, my_list))
print(list(result))
