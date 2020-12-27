# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

list = []
while True:
    user_input = input('Введите данные:')
    if user_input == '':
        break
    str = user_input + '\n'
    list.append(str)

out_f = open('out_file.txt', 'w')
out_f.writelines(list)
out_f.close()

