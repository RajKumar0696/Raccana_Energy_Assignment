from selenium.webdriver.common.by import By


class FormAuthentication:
    txt_username_id = "username"
    txt_password_id = "password"
    btn_login_xpath = "//*[@id='login']/button/i"
    btn_logout_xpath = " //*[@id='content']/div/a/i"

    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        self.driver.find_element(By.ID, self.txt_username_id).clear()
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

