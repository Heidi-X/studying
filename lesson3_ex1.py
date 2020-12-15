# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
#их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*args):
    try:
        arg1 = float(input("Введите число 1:"))
        arg2 = float(input("Введите число 2:"))
        result = arg1 / arg2
    except ValueError:
        return 'Ошибка ввода, вводите ЧИСЛО'
    except ZeroDivisionError:
        return "Ошибка ввода, введите число отличное от 0"
    return result
print(division())