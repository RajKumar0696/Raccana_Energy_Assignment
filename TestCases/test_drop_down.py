from selenium.webdriver.common.by import By

from Utilities.read_properties import ReadProperties
from PageObjects.drop_down import DropDown
from selenium.webdriver.support.ui import Select
from Utilities.custom_logger import Logger


class Test_005_DropDown:
    url = ReadProperties.get_drop_down_url()
    logger = Logger()
    logger.log_info("***Test_005_DropDown test***")

    def test_drop_down(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.drop_down = DropDown(self.driver)
        self.drop_down.click_menu()
        self.logger.log_info("***Drop down test start***")

        element = self.driver.find_element(By.ID, "dropdown")
        drop_down = Select(element)
        self.logger.log_info("***Drop down selected by visible text***")
        # drop_down.select_by_visible_text("Option 1")
        self.logger.log_info("***Down drop selected by index***")
        # drop_down.select_by_index(2)
        self.logger.log_info("***Down drop selected by value***")
        drop_down.select_by_value("1")
        self.logger.log_info("***Down drop test end***")
