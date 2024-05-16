def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError as exc:
        print('Складывать нельзя, потому-что', exc, 'но мы все равно сложим')
    finally:
        print('Cложили', str(a) + b)

print(add_everything_up(120, 'cars'))