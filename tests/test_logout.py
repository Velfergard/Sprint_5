from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators


class TestLogOffAccount:

    def test_logoff_from_personal_account_success(self, driver):

        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.logout_button))).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.login_header)))

        assert 'login' in driver.current_url
