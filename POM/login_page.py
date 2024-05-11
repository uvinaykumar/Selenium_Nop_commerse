from selenium.webdriver.common.by import By


class login:
    text_box_username_name="Email"
    text_box_password_id="Password"
    button_login_xpath= "//button[@type='submit']"
    logout_linktext= "/logout"

    def __init__(self,driver):
        self.driver = driver
    def setUsername(self,username):
        self.driver.find_element(by=By.NAME, value= self.text_box_username_name).clear()
        self.driver.find_element(By.NAME, value=self.text_box_username_name).send_keys(username)
    def setpassword(self,password):
        self.driver.find_element(by=By.NAME, value=self.text_box_password_id).clear()
        self.driver.find_element(by=By.ID, value=self.text_box_password_id).send_keys(password)
    def clickLoginButton(self):
        self.driver.find_element(by=By.XPATH, value=self.button_login_xpath).click()

    def clickLogoutButton(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.logout_linktext).click()