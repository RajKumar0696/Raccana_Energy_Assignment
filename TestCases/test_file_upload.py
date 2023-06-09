from selenium.webdriver.common.by import By
from Utilities.custom_logger import Logger
from Utilities.read_properties import ReadProperties
from PageObjects.file_upload import FileUpload


class Test_002_FileUpload:
    url = ReadProperties.get_file_upload_url()
    expected_result_xpath = "//*[@id='content']/div/h3"
    logger = Logger()
    logger.log_info("***Test_002_FileUpload test***")
    try:
        def test_file_upload(self, setup):
            self.driver = setup
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.file_upload = FileUpload(self.driver)
            self.file_upload.click_file_upload()
            self.logger.log_info("***File upload test start***")

            expected_result = "File Uploaded!"
            actual_result = self.driver.find_element(By.XPATH, self.expected_result_xpath).text

            if expected_result == actual_result:
                print("File uploaded successfully")
                self.driver.save_screenshot(".\\ScreenShots\\" + "file_uploaded.png")
                assert True
            else:
                print("Please select proper file")
                assert False
    except:
        print("Please provide your correct file path")
    logger.log_info("***File uploaded test completed***")
