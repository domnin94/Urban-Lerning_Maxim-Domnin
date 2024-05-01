def test(*values):
    print(values)
test(1, 2, 3, 4, 5)

def test(**dict):
    print(dict)
test(a = 1, b = 2, c = 3,d = 4)

def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

print(sum(10))