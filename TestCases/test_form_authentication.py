from selenium.webdriver.common.by import By
from PageObjects.form_authentication import FormAuthentication
from Utilities.read_properties import ReadProperties
from Utilities.custom_logger import Logger

class Test_003_FormAuthentication:
    url = ReadProperties.get_auth_url()
    username = "tomsmith"
    password = "SuperSecretPassword!"
    logger = Logger()

    def test_login(self,setup):
        self.logger.log_info("*** Test_003_FormAuthentication ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.logger.log_info("*** Form authentication login test start ***")
        self.login = FormAuthentication(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.click_login()

        expected_result = "You logged into a secure area!"
        actual = self.driver.find_element(By.XPATH, "//div[@id='flash']").text
        actual_res = actual.strip("×")
        actual_result = actual_res.strip()

        if actual_result == expected_result:
            self.logger.log_info("Login test passed")
            assert True
        else:
            self.logger.log_info("Login test filed")
            assert False
        self.logger.log_info("*** Form authentication login test end ***")

        self.logger.log_info("*** Form authentication logout test start ***")
        self.login.click_logout()
        expected_result = "You logged out of the secure area!"
        actual = self.driver.find_element(By.XPATH, "//div[@id='flash']").text
        actual_res = actual.strip("×")
        actual_result = actual_res.strip()

        if actual_result == expected_result:
            self.logger.log_info("Logout test passed")
            assert True
        else:
            self.logger.log_info("Logout test failed")
            assert False
        self.logger.log_info("*** Form authentication logout test end ***")
        self.driver.close()