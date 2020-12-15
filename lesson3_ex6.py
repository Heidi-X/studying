# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(string: str):
    string = string.capitalize()
    return string

print(int_func('text'))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной
# строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
# ранее функцию int_func().

def int_func(string: str):
    list2 = string.split()
    list3 = []
    for i in list2:
        i = i.capitalize()
        list3.append(i)
    result = ' '.join(list3)
    return result

print(int_func('my favourite month is october'))