from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators


class TestMoveToAccountPage:

    def test_move_to_account_page_unauthorized_login_page_opened(self, driver):

        driver.find_element(By.LINK_TEXT, locators.account_link).click()

        assert 'login' in driver.current_url

    def test_move_to_account_page_authorized_profile_page_opened(self, driver):

        driver.find_element(By.XPATH, locators.sign_in_button).click()
        driver.find_element(By.XPATH, locators.name_field).send_keys(data.login_data["email"])
        driver.find_element(By.XPATH, locators.password_field).send_keys(data.login_data["password"])
        driver.find_element(By.XPATH, locators.login_button).click()
        driver.find_element(By.LINK_TEXT, locators.account_link).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, locators.profile_link)))

        assert 'profile' in driver.current_url
