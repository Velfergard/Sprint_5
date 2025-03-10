from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMoveToAccountPage:

    def test_move_to_account_page_unauthorized_login_page_opened(self, url):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        assert 'login' in driver.current_url

        driver.quit()

    def test_move_to_account_page_authorized_profile_page_opened(self, url, email, password):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.XPATH, "//button[text() = 'Войти в аккаунт']").click()
        driver.find_element(By.XPATH, "//input[@name = 'name']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name = 'Пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button[text() = 'Войти']").click()
        driver.find_element(By.XPATH, "//p[text() = 'Личный Кабинет']").click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Профиль")))

        assert 'profile' in driver.current_url

        driver.quit()
