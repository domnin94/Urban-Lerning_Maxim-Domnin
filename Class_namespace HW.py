class Building:
    total = 0
    def __init__(self):
        while self.total < 40:
            self.total += 1
            print('Object', self.total)
build = Building()
print(build)
