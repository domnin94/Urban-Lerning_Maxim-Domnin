class Building:
    def __init__(self, name: str):
        self.building = name
    def __str__(self):
        return "Здание 1:" + self.building

    __repr__ = __str__

Buildings = [Building(f"Здание_{i+1}") for i in range(40)]
print(Buildings)


