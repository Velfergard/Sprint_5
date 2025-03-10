from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMoveToConstructorPage:

    def test_from_unauthorized_account_page_move_to_constructor_page_success(self, url):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.XPATH, "//p[text() = 'Конструктор']").click()

        assert driver.current_url == url

        driver.quit()

    def test_move_to_constructor_page_by_logo_success(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))
        driver.find_element(By.XPATH, "//div[contains(@class, 'header__logo')]").click()

        assert driver.current_url == url

        driver.quit()
