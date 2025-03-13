from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import helpers
import locators


class TestRegistrationCases:

    def test_register_with_correct_inputs_success(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        driver.find_element(By.LINK_TEXT, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.name_success)
        driver.find_element(By.XPATH, locators.email_field).send_keys(helpers.generated_email())
        driver.find_element(By.XPATH, locators.password_field).send_keys(helpers.generated_password())
        driver.find_element(By.XPATH, locators.sign_up_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.login_header)))

        assert 'login' in driver.current_url

    def test_register_password_length_less_than_6_symbols_false(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        driver.find_element(By.LINK_TEXT, locators.sign_up_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.name_fail)
        driver.find_element(By.XPATH, locators.email_field).send_keys(helpers.generated_email())
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.password_fail)
        driver.find_element(By.XPATH, locators.sign_up_button).click()

        assert driver.find_element(By.CSS_SELECTOR, locators.error_msg).text == 'Некорректный пароль'
