from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogOffAccount:

    def test_logoff_from_personal_account_success(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[text() = 'Выход']"))).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h2[text() = 'Вход']")))

        assert 'login' in driver.current_url

        driver.quit()
