from selenium.webdriver.common.by import By
from Utilities.custom_logger import Logger
from PageObjects.java_script_alert import JavaScriptAlert
from Utilities.read_properties import ReadProperties


class Test_004_javaScriptAlert:
    url = ReadProperties.get_alert_url()
    logger = Logger()

    def test_java_script_alert(self, setup):
        self.logger.log_info("*** Test_004_javaScriptAlert ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.logger.log_info("*** Java script alerts tests start ***")
        self.logger.log_info("*** Js simple alert test start ***")
        self.alert = JavaScriptAlert(self.driver)
        self.alert.click_js_alert()
        my_alert = self.driver.switch_to.alert
        my_alert.accept()
        expected_result = "You successfully clicked an alert"
        actual_result = self.driver.find_element(By.ID, "result").text
        if actual_result == expected_result:
            assert True
        else:
            assert False
        self.logger.log_info("*** Js simple alert test end ***")

        self.logger.log_info("*** Js conform alert test start ***")
        self.alert.click_js_conform()
        my_alert.dismiss()
        expected_result = "You clicked: Cancel"
        actual_result = self.driver.find_element(By.ID, "result").text
        if actual_result == expected_result:
            assert True
        else:
            assert False
        self.logger.log_info("*** Js conform alert test end ***")

        self.logger.log_info("*** Js prompt test start ***")
        self.alert.click_js_prompt()
        my_alert.send_keys("Hey tester")
        my_alert.accept()
        expected_result = "You entered: Hey tester"
        actual_result = self.driver.find_element(By.ID, "result").text
        if actual_result == expected_result:
            assert True
        else:
            assert False
        self.logger.log_info("*** Js prompt test end ***")
        self.logger.log_info("*** Java script alerts tests end ***")
        self.driver.close()
