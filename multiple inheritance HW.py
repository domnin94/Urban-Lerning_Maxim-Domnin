class Vehicle:
    def __init__(self, vehicle_type = "none"):
        super().__init__()
        self.vehicle_type = vehicle_type
    def __str__(self):
        return '{} тип машины {}'.format(
            self.__class__.__name__, self.vehicle_type)
class Car:
    def __init__(self):
        self.price = 3000000
    def horse_powers(self):
        self.horse_powers = 400
    def __str__(self):
        return '{}, цена {}, лошадиные силы {}'.format(
            self.__class__.__name__, self.price, self.horse_powers)
class Nissan(Vehicle, Car):
    def __init__(self, vehicle_type = "гоночная"):
        self.price = 2400000
        self.vehicle_type =  vehicle_type
    def horse_powers(self):
        self.horse_powers = 350
    def __str__(self):
        return '{}, тип машины {}, цена {}, лошадиные силы {}'.format(
            self.__class__.__name__, self.vehicle_type, self.price, self.horse_powers)

type = Vehicle()
print(type)
car = Car()
car.horse_powers()
print(car)
nissan = Nissan()
nissan.horse_powers()
print(nissan)
print(nissan.price, nissan.vehicle_type)
