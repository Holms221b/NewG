from random import randint, choice, choices
import random
import re
from email_validator import validate_email, EmailSyntaxError

EMAIL_DOMAINS = ["mail.ru", "yandex.ru", "gmail.com", "outlook.com"]
LOCAL_PART_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.+-"


def generate_fake_email(name=None, surname=None):
    # Преобразуем в строки, если переданы другие типы данных
    if not isinstance(name, str):
        name = str(name)
    if not isinstance(surname, str):
        surname = str(surname)

    # Убираем лишние символы
    name = re.sub(r'[^a-zA-Z0-9]', '', name.lower())
    surname = re.sub(r'[^a-zA-Z0-9]', '', surname.lower())

    local_part = f"{name}.{surname}.{random.randint(1000, 9999)}"
    local_part = "".join(c for c in local_part if c in LOCAL_PART_CHARS)

    # Убираем точки в начале и конце локальной части
    local_part = local_part.strip(".")

    # Обрезаем, если длина превышает 64 символа
    local_part = local_part[:64]

    domain = random.choice(EMAIL_DOMAINS)
    email = f"{local_part}@{domain}"

    try:
        # validate_email(email)  # Проверяем валидность
        return email  # Гарантированно валидный email
    except EmailSyntaxError:
        return generate_fake_email(name, surname)


print(generate_fake_email("name", "name"))