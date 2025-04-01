import datetime
from random import randint
from faker import  Faker
from faker.contrib.pytest.plugin import faker
import random
from utils.email import generate_fake_email

#Инициализируем русскую и англ локали для данных

fake_ru = Faker('ru_RU')
fake_en = Faker('en_US')

def add_passport_visitor_dto():
    passport_series = randint(1000,9999)
    passport_number = randint(100000,999999)

#Генерируем дату рождения
    birth_date = fake_ru.date_of_birth(minimum_age=21, maximum_age=65)

# Форматируем дату рождения в строку
    formatted_birth_date = birth_date.strftime("%m-%d-%Y")

# Генерируем дату выдачи паспорта (18+ лет)
    issue_date = birth_date + datetime.timedelta(days=randint(3570, 7000))

# Форматируем дату выдачи в строку
    formatted_issue_date = issue_date.strftime("%m-%d-%Y")

    gender = random.choice(["Мужской","Женский"])
    if gender == "Мужской":
        first_name = fake_ru.first_name_male(),
        last_name = fake_ru.last_name_male(),
        middle_name = fake_ru.middle_name_male()
    else:
        first_name = fake_ru.first_name_female(),
        last_name = fake_ru.last_name_female(),
        middle_name = fake_ru.middle_name_female()

    email = generate_fake_email(first_name, last_name)

    dto = {
    # Основа без паспорта
    "first_name":first_name,
    "last_name":last_name,
    "middle_name":middle_name,
    "username":f"user_{fake_en.first_name()}",
    "password":fake_ru.password(),#f"{randint(100000,999999)}",
    "email": email,
    "phone":f"8985{randint(1000000,9999999)}",
    "fixed_line_phone": f"+7(351){randint(1000000,9999999)}",
    "company_name": f"OOO {fake_ru.middle_name().upper()}",
    "office":"Ilona",
    "department":"Колумба",
    "cabinet": f"{randint(100,999)}",
    # Паспорт
    "passport.series":passport_series,
    "passport.number":passport_number,
    "passport.division_code": f"{randint(100,999)}-{randint(100,999)}",
    "passport.registration": fake_ru.address(),
    "passport.date_of_birth": formatted_birth_date,
    "passport.place_of_birth":fake_ru.city(),
    "passport.place_of_issue": f"ОУФМС {fake_ru.city()}",
    "gender":gender,
    "passport.date_of_issue":formatted_issue_date,
    "passport.residential_address": fake_ru.address()
    }

    return dto





