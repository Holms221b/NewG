import datetime
from random import randint
from faker import Faker

fake_ru = Faker('ru_RU')

# Генерируем дату рождения
birth_date = fake_ru.date_of_birth(minimum_age=21, maximum_age=65)

# Форматируем дату рождения в строку
formatted_birth_date = birth_date.strftime("%Y-%m-%d")

# Генерируем дату выдачи паспорта (18+ лет)
issue_date = birth_date + datetime.timedelta(days=randint(6570, 7000))

# Форматируем дату выдачи в строку
formatted_issue_date = issue_date.strftime("%Y-%m-%d")

# Результаты
print(f"Дата рождения: {formatted_birth_date}")
print(f"Дата выдачи: {formatted_issue_date}")