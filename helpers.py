# Файл со вспомогательными методами

import random
import string


def generated_email():  # Метод для генерации Email
    mail_domains = ['yandex.ru', 'gmail.com', 'mail.ru']
    group_num = '19'
    email_base = ''.join(random.choices(string.ascii_letters, k=10))
    email = f"{email_base}{group_num}{random.randint(100, 999)}@{random.choice(mail_domains)}"

    return email


def generated_password():  # Метод для генерации паролей
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 10)))

    return password
