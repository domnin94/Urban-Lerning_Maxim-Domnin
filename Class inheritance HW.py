class Car:
    def __init__(self):
        self.price = 1000000
    def horse_power(self):
        self.horse_power = 150
    def __str__(self):
        return '{} цена {} лошадиные силы {}'.format(
            self.__class__.__name__, self.price, self.horse_power)
class Nissan(Car):
    def horse_power(self):
        self.horse_power = 100

class Kia(Car):
    def horse_power(self):
        self.horse_power = 145

car = Car()
car.horse_power()
print(car)
nissan = Nissan()
nissan.horse_power()
print(nissan)
kia = Kia()
kia.horse_power()
print(kia)
