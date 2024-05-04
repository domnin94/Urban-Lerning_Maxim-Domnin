class House:

    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        if floors >= 0:
            print('numberOfFloors')

house = House()
house.setNewNumberOfFloors(0)
