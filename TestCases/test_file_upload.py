from selenium.webdriver.common.by import By
from Utilities.custom_logger import Logger
from Utilities.read_properties import ReadProperties
from PageObjects.file_upload import FileUpload


class Test_002_FileUpload:
    url = ReadProperties.get_file_upload_url()
    expected_result_xpath = "//*[@id='content']/div/h3"
    logger = Logger()

    def test_file_upload(self, setup):
        self.logger.log_info("*** Test_002_FileUpload test ***")
        try:
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            self.logger.log_info("*** File upload test start ***")
            self.file_upload = FileUpload(self.driver)
            self.file_upload.click_file_upload()

            expected_result = "File Uploaded!"
            actual_result = self.driver.find_element(By.XPATH, self.expected_result_xpath).text

            if expected_result == actual_result:
                self.logger.log_info("File uploaded successfully")
                self.driver.save_screenshot(".\\ScreenShots\\" + "file_uploaded.png")
                assert True
            else:
                self.logger.log_info("Please select valid file path")
                assert False
            self.logger.log_info("*** File uploaded test end ***")

        except:
            self.logger.log_info("Oops, invalid file path")
        self.driver.close()
