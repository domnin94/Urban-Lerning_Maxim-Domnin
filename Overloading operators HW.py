class Building:
    def __init__(self):
        self.numberOfFloors = 5
        self.buldingType = 'fives'
    def __eq__(self, other):
        return self.numberOfFloors == len(self.buldingType)

new_building = Building()
old_building = Building()

if Building.__eq__(self = new_building, other=old_building ):
    print('Perfect')
else:
    print('Loser')