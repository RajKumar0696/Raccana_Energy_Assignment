from selenium.webdriver.common.by import By


class DropDown:
    txt_menu_id = "dropdown"

    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        self.driver.find_element(By.ID, self.txt_menu_id)
