from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationCases:

    def test_register_with_correct_inputs_success(self, url, generated_email, generated_password):
        self.name = 'Виктор Testov'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(self.name)
        driver.find_element(By.XPATH, "//fieldset[2]//input[@name = 'name']").send_keys(generated_email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(generated_password)
        driver.find_element(By.XPATH, "//button[text() = 'Зарегистрироваться']").click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[text() = 'Вход']")))

        assert 'login' in driver.current_url

        driver.quit()

    def test_register_password_length_less_than_6_symbols_false(self, url, generated_email):
        self.name = 'Пароль Некорректный'

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(self.name)
        driver.find_element(By.XPATH, "//fieldset[2]//input[@name = 'name']").send_keys(generated_email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys('abc12')
        driver.find_element(By.XPATH, "//button[text() = 'Зарегистрироваться']").click()

        assert driver.find_element(By.CSS_SELECTOR, ".input__error").text == 'Некорректный пароль'

        driver.quit()
