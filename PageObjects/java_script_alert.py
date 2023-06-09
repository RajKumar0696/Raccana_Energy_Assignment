from selenium.webdriver.common.by import By


class JavaScriptAlert:
    lin_js_alert_xpath = "//button[normalize-space()='Click for JS Alert']"
    lin_js_conform_xpath = "//button[normalize-space()='Click for JS Confirm']"
    lin_js_prompt_xpath = "//button[normalize-space()='Click for JS Prompt']"


    def __init__(self,driver):
        self.driver = driver

    def click_js_alert(self):
        self.driver.find_element(By.XPATH, self.lin_js_alert_xpath).click()

    def click_js_conform(self):
        self.driver.find_element(By.XPATH, self.lin_js_conform_xpath).click()

    def click_js_prompt(self):
        self.driver.find_element(By.XPATH, self.lin_js_prompt_xpath).click()




