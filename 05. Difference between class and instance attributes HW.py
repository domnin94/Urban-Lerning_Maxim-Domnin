class Building:
    total = 0
    def __init__(self):
        Building.total += 1
    def __str__(self):
        return "Объект:" + str(Building.total + i)

build = Building()
for i in range(40):
    print(build)