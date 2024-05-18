class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration()
        else:
            if self.start % 2 == 0:
                result = self.start
            else:
                result = self.start + 1
            self.start += 2
            return result

en = EvenNumbers(start=10, end=25)
print(en)
for i in en:
    print(i)
