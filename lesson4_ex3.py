# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание
# в одну строку.
# Подсказка: использовать функцию range() и генератор.

list1 = [el for el in list(range(20, 241)) if el % 20 == 0 or el % 21 == 0]
print(list1)