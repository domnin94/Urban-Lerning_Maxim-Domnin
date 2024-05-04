class House:

    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        if floors > 0:
            self.numberOfFloors = floors
            print('numberOfFloors:', self.numberOfFloors)

house = House()
house.setNewNumberOfFloors(6)
