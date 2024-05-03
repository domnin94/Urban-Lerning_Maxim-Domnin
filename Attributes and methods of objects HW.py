class House:
    def __init__(self):
        self.numberOfFloors = 10

    def floor(self):
        print('Спускаемся')
        self.current_floor = 8

my_home = House()

print('Всего этажей', my_home.numberOfFloors)
my_home.floor()
print('Текущий этаж', my_home.current_floor)

