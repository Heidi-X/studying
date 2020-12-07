# https://github.com/Heidi-X/studying/pull/1

# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Alice'
age = 16
age_in_20 = age + 20
result = f'Name: {name}, age: {age}, age in 20 years: {age_in_20}'
print(result)

name = input('Enter your name \n>>>')
age = input('Enter your age \n>>>')

while not age.isdigit():
    age = input('Wrong input, only numeric values allowed \nEnter your age \n>>>')

age = int(age)
age_in_30 = age + 30
result = f'Hello, {name}! In 30 years you will be {age_in_30} years old.'
print(result)


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк

time_sec = input('Enter time in seconds \n>>>')

while not time_sec.isdigit():
    time_sec = input('Wrong input, only numeric values allowed \nEnter time in seconds \n>>>')

time_sec = int(time_sec)
hour = int(time_sec / 3600)
min = int((time_sec % 3600) / 60)
sec = (time_sec % 3600) % 60
time = f'{hour}:{min}:{sec}'
print(time)


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = input('Enter a number \n>>>')

while not number.isdigit():
    number = input('Wrong input, only numeric values allowed \nEnter a number')

number2 = number + number
number3 = number + number2
sum = int(number) + int(number2) + int(number3)
result = f'{number} + {number2} + {number3} = {sum}'
print(result)


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

n = input('Enter a positive integer \n>>>')
while not n.isdigit():
    n = input("Wrong input, only numeric values allowed \nEnter a positive integer \n>>>")
n_int = int(n)

numbers = []

for i in n:
        numbers.append(int(i))

x = 0
largest = numbers[x]
while x < len(numbers):
  if numbers[x] > largest:
    largest = numbers[x]
  x = x+1
print(largest)


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток —
# издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с
# прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

rev = input("Your company's revenue \n>>>")
while not rev.isdigit():
    rev = input("Wrong input, only numeric values allowed \nEnter your company's revenue \n>>>")
rev = int(rev)

expenses = input("Your company's costs \n>>>")
while not expenses.isdigit():
    expenses = input("Wrong input, only numeric values allowed \nEnter your company's costs \n>>>")
expenses = int(expenses)

if rev > expenses:
    print('Your company has made a profit')
    profit_margin = ((rev - expenses) / rev) * 100
    print('Profit margin = ', profit_margin, '%')
    workers = input('Number of company employees \n>>>')
    while not workers.isdigit():
        workers = input("Wrong input, only numeric values allowed \nEnter the number of company employees \n>>>")
    workers = int(workers)
    profit_per_employee = profit_margin / workers
    print('Profit per employee = ', profit_per_employee, '%')
elif expenses > rev:
    print('Your company has made a loss')


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить
# номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = input('First run (km) \n>>>')
while not a.isdigit():
    a = input("Wrong input, only numeric values allowed \nEnter first run (km) \n>>>")
a = int(a)

b = input('Minimum distance required (km) \n>>>')
while not b.isdigit():
    b = input("Wrong input, only numeric values allowed \nEnter minimum distance (km) \n>>>")
b = int(b)

day = 1

while a < b:
    a = a + (a / 100 * 10)
    day += 1

result = f'The result (not less than {b} km) was achieved on the {day}th day'
print(result)










