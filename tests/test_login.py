from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators


class TestLoginFromDifferentPages:

    def test_login_button_sign_in_account_success(self, driver):

        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, locators.profile_link)))

        assert 'profile' in driver.current_url

    def test_login_from_personal_account_success(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, locators.profile_link)))

        assert 'profile' in driver.current_url

    def test_login_from_ref_on_registration_form_success(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        driver.find_element(By.LINK_TEXT, locators.sign_up_link).click()
        driver.find_element(By.LINK_TEXT, locators.login_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, locators.profile_link)))

        assert 'profile' in driver.current_url

    def test_login_from_ref_on_reset_password_form_success(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        driver.find_element(By.LINK_TEXT, locators.reset_password_link).click()
        driver.find_element(By.LINK_TEXT, locators.login_link).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()

        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, locators.profile_link)))

        assert 'profile' in driver.current_url
