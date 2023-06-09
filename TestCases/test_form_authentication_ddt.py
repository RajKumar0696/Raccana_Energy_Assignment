from selenium.webdriver.common.by import By
from PageObjects.form_authentication import FormAuthentication
from Utilities.read_properties import ReadProperties
from Utilities import excel_utils
from Utilities.custom_logger import Logger


class Test_003_FormAuthentication_DDT:
    url = ReadProperties.get_auth_url()
    path = r"TestData/form_authentication/authData.xlsx"
    logger = Logger()

    def test_login(self, setup):
        self.logger.log_info("*** Test_003_FormmAuthentication_DDT ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.login = FormAuthentication(self.driver)
        self.logger.log_info("*** Form authentication DDT test start ***")

        self.rows = excel_utils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = excel_utils.readData(self.path, 'Sheet1', r, 1)
            self.password = excel_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp = excel_utils.readData(self.path, 'Sheet1', r, 3)

            self.login.set_username(self.user)
            self.login.set_password(self.password)
            self.login.click_login()

            expected_result = "You logged into a secure area!"
            actual = self.driver.find_element(By.XPATH, "//div[@id='flash']").text
            actual_res = actual.strip("×")
            actual_result = actual_res.strip()

            if actual_result == expected_result:
                if self.exp == "Pass":
                    self.login.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    lst_status.append("Fail")
            elif actual_result != expected_result:
                if self.exp == "Pass":
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            assert True
        else:
            assert False

        self.logger.log_info("*** Form authentication DDT test end ***")
        self.driver.close()
