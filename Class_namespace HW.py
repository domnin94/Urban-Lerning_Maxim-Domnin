class Building:
    total = 0
    def __init__(self):
        Building.total += 1

district = []
district_size = 40
while len(district) < district_size:
    new_build = Building()
    district.append(new_build)
print(Building.total)

