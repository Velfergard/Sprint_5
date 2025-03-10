import pytest
import random
import string


# Фикстура для возврата адреса сайта
@pytest.fixture
def url():
    url = 'https://stellarburgers.nomoreparties.site/'

    return url


# Фикстура для генерации email'а
@pytest.fixture
def generated_email():
    mail_domains = ['yandex.ru', 'gmail.com', 'mail.ru']
    group_num = '19'
    email_base = ''.join(random.choices(string.ascii_letters, k=10))
    email = f"{email_base}{group_num}{random.randint(100, 999)}@{random.choice(mail_domains)}"

    return email


# Фикстура для генерации корректного пароля
@pytest.fixture
def generated_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 10)))

    return password


# Фикстура для возврата предопределенного Email
@pytest.fixture
def email():
    email = 'testartyom19023@mail.ru'

    return email


# Фикстура для возврата предопределенного Пароля
@pytest.fixture
def password():
    password = 'qaz123'

    return password
