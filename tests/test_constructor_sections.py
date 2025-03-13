from selenium.webdriver.common.by import By
import locators


class TestConstructorSectionChoice:

    def test_move_to_souses_section(self, driver):

        element = driver.find_element(By.XPATH, locators.souses_section)
        element.click()

        assert driver.find_element(By.XPATH, locators.souses_is_current)

    def test_move_to_toppings_section(self, driver):

        element = driver.find_element(By.XPATH, locators.toppings_section)
        element.click()

        assert driver.find_element(By.XPATH, locators.toppings_is_current)

    def test_move_to_buns_section(self, driver):

        driver.find_element(By.XPATH, locators.toppings_section).click()
        element = driver.find_element(By.XPATH, locators.buns_section)
        element.click()

        assert driver.find_element(By.XPATH, locators.buns_is_current)
