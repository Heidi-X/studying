#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def descr(name, surname, year, city, email, phone):
    return str(f'Name: {name}, surname: {surname}, year: {year}, city: {city}, email: {email}, phone: {phone}')

print(descr(name='Emma', surname='Porridge', year='1995', city='Kirov', email='vetka@gmail.com',
              phone='8-999-999-99-99'))