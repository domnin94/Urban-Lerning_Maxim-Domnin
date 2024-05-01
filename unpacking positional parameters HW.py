def print_params(a='Max ', b='строку ', c='написал'):
    print(a, b, c)
print_params()
print(print_params(b = 'книгу '))
print(print_params(c = ['Журнал', 'статью', 'стих']))

values_list = [1, 'B', 'ducs']
values_dict ={'a' : 5, 'b' : 'нет', 'c' : 'dog' }
print_params(*values_list)
print_params(**values_dict)

values_list2 = [89, 'cat']
print_params(*values_list2, 46)