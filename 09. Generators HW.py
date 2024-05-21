# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.

def all_variants(text):
    for i in range(len(text)):
        yield text[i]
    iterator = iter(text)
    a = next(iterator, None)
    for b in text:
        yield a + b
        a = b
    yield text

k = all_variants("abc")

for i in k:
    print(i)
