def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        d = 2
        while d <= n - 1:
            if n % d == 0:
                break
            else:
                d += 1
        if n == 1 or d == n:
            return 'Простое', n

        else:
            return 'Составное', n

    return wrapper


@is_prime
def sum_three(*args):
    f = 0

    for k in args:
        f += k
    return f


r = sum_three(5, 6, 6)
print(r)
