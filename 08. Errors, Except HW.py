def add_everything_up(a, b):
    try:
        result = a + b
        print(result)
    except TypeError as exc:
        print('Складывать нельзя, потому-что', exc, 'но мы все равно сложим')
        return str(a)+str(b)


print(add_everything_up(120, 'cars'))