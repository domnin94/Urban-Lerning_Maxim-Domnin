class Building:
    def __init__(self):
        self.numberOfFloors = 678
        self.buldingType = 'fives'
    def __eq__(self, other):
        return self.numberOfFloors and other.buldingType


new_building = Building()
old_building = Building()

if new_building == old_building:
    print('Perfect')
else:
    print('Loser')