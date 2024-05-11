from pprint import pprint


file_name = '07. File opening modes HW.txt'
file = open(file_name, mode='rb')
file_content = file.read()
file.close()
pprint(file_content)