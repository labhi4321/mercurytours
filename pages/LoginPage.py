from testdata.data import *

class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.un_text_name="userName"
        self.pw_text_name="password"
        self.ln_bttn_name="login"

    def enter_username(self):
        self.driver.find_element_by_name(self.un_text_name).send_keys(UN)

    def enter_password(self):
        self.driver.find_element_by_name(self.pw_text_name).send_keys(PWD)

    def click_Login(self):
        self.driver.find_element_by_name(self.ln_bttn_name).click()
