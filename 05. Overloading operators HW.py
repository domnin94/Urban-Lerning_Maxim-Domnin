class Building:
    def __init__(self, numberOfFloors, buldingType):
        self.numberOfFloors = numberOfFloors
        self.buldingType = buldingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buldingType == other.buldingType


new_building = Building(numberOfFloors=678, buldingType='five')
old_building = Building(numberOfFloors=678, buldingType='five')

print(new_building == old_building)


