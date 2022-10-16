import datetime
from telnetlib import STATUS

nome = input('Digite seu nome: ')

print('123456789')

print(nome)

print('Hoje é dia', datetime.datetime.now().day, 'de', datetime.datetime.now().month, 'de', datetime.datetime.now().year)

def get_date_from_day_number_of_year(day_number_of_year, year):
    return datetime.date(year, 1, 1) + datetime.timedelta(day_number_of_year - 1)

day_number = int(input('Por favor, digite o dia do ano: '))
year = int(input('Digite o ano: '))

print(get_date_from_day_number_of_year(day_number, year))

print('amanha é dia', datetime.datetime.now().day + 1, 'de', datetime.datetime.now().month, 'de', datetime.datetime.now().year)
