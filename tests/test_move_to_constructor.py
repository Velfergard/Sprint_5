from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators


class TestMoveToConstructorPage:

    def test_from_unauthorized_account_page_move_to_constructor_page_success(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        driver.find_element(By.LINK_TEXT, locators.constructor_link).click()

        assert 'Соберите бургер' in driver.page_source

    def test_move_to_constructor_page_by_logo_success(self, driver):

        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, locators.profile_link)))
        driver.find_element(By.XPATH, locators.logo).click()

        assert 'Соберите бургер' in driver.page_source
