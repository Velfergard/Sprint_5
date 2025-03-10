from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginFromDifferentPages:

    def test_login_button_sign_in_account_success(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))

        assert 'profile' in driver.current_url

        driver.quit()

    def test_login_from_personal_account_success(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))

        assert 'profile' in driver.current_url

        driver.quit()

    def test_login_from_ref_on_registration_form_success(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.LINK_TEXT, "Войти").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))

        assert 'profile' in driver.current_url

        driver.quit()

    def test_login_from_ref_on_reset_password_form_success(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        driver.find_element(By.LINK_TEXT, "Войти").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))

        assert 'profile' in driver.current_url

        driver.quit()
