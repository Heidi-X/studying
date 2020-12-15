#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов
def my_func(a, b, c):
    nums = []
    d = [a, b, c]
    nums.append(max(d))
    d.remove(max(d))
    nums.append(max(d))
    result = sum(nums)
    return result

print(my_func(3, 4, 5))
print(my_func(10, 100, 100.45))