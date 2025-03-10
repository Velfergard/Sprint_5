from selenium import webdriver
from selenium.webdriver.common.by import By


class TestConstructorSectionChoice:

    def test_move_to_souses_section(self, url):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        element = driver.find_element(By.XPATH, "//span[text() = 'Соусы']")
        element.click()

        assert driver.find_element(By.XPATH, "//span[text() = 'Соусы']/parent::*[contains(@class, 'current')]")

        driver.quit()

    def test_move_to_toppings_section(self, url):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        element = driver.find_element(By.XPATH, "//span[text() = 'Начинки']")
        element.click()

        assert driver.find_element(By.XPATH, "//span[text() = 'Начинки']/parent::*[contains(@class, 'current')]")

        driver.quit()

    def test_move_to_buns_section(self, url):
        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(url)
        driver.find_element(By.XPATH, "//span[text() = 'Начинки']").click()
        element = driver.find_element(By.XPATH, "//span[text() = 'Булки']")
        element.click()

        assert driver.find_element(By.XPATH, "//span[text() = 'Булки']/parent::*[contains(@class, 'current')]")

        driver.quit()
