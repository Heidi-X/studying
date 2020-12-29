# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

from random import randint
list1 = []
f_1 = open('sum.txt', 'w')
i = 1
while i < 10:
        i += 1
        a = str(randint(1, 100))
        list1.append(int(a))
        f_1.write(a)
        f_1.write(' ')

sum1 = sum(list1)
print(sum1)
f_1.close()