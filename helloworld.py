import datetime

nome = input('Digite seu nome: ')

print('123456789')

'''
4645465 4654 654 4  4654654


gjdfogjdfjgdkfjglkdfgdf
gd
g
df
df
gd
'''


print(nome)

print('Hoje é dia', datetime.datetime.now().day, 'de', datetime.datetime.now().month, 'de', datetime.datetime.now().year)

def get_date_from_day_number_of_year(day_number_of_year, year):
    return datetime.date(year, 1, 1) + datetime.timedelta(day_number_of_year - 1)

day_number = int(input('Digite o dia do ano: '))
year = int(input('Digite o ano: '))

print(get_date_from_day_number_of_year(day_number, year))

# Fazendo testes