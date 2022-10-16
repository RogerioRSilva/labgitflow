import datetime

nome = input('Digite seu nome: ')

print(nome)

def get_date_from_day_number_of_year(day_number_of_year, year):
    return datetime.date(year, 1, 1) + datetime.timedelta(day_number_of_year - 1)

day_number = int(input('Digite o dia do ano: '))
year = int(input('Digite o ano: '))

print(get_date_from_day_number_of_year(day_number, year))