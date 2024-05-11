file_name = '07. File opening modes HW.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
print(file.closed)

# оператор with автоматически закрывает файл после прочтения,
# а без него файл не закроется если не прописать file.closed()