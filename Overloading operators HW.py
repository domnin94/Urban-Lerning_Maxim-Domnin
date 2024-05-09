class Building:
    def __init__(self):
        self.numberOfFloors = 678
        self.buldingType = 'fives'
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buldingType == other.buldingType


new_building = Building()
old_building = Building()

if Building.__eq__(self=new_building, other=old_building):
    print('Thrue')
else:
    print('False')

