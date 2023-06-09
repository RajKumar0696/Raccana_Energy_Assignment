import logging

from selenium.webdriver.common.by import By
import requests

from Utilities.read_properties import ReadProperties
from Utilities.custom_logger import Logger


class Test_001_BrokenImage:
    url = ReadProperties.get_broken_link_url()

    logger = Logger()
    logger.log_info("*** Test_001_BrokenImage***")

    def test_broken_image(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.logger.log_info("***Broken image test start***")
        for image in images:
            image_source = requests.head(image.get_attribute('src'))
            if image_source.status_code != 200:
                print("This is Broken image", image_source.status_code)
            else:
                print("This is not broken image", image_source.status_code)
        self.logger.log_info("***Broken image test end***")

