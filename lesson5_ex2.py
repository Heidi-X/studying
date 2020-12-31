# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('kill.txt') as f_1:
    lines = 0
    words = 0
    for line in f_1:
        lines += line.count('\n')
        words = line.count(' ') + 1
        print(f'Number of words in the line: {words}')
print(f'Number of lines: {lines}')