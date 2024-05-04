class House:
    def __init__(self):
        self.numberOfFloors = 10

my_home = House()
for i in range(my_home.numberOfFloors):
    print('Текущий этаж', my_home.numberOfFloors)