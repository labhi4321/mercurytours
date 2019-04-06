from selenium import webdriver
import time
import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import homepage
from testdata.data import *

@pytest.mark.usefixtures("test_LaunchBrowser")
class TestLogin:

    def test_Login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.enter_username()
        lp.enter_password()
        lp.click_Login()

        hp = homepage(driver)
        hp.click_SignOff()

        # driver.find_element_by_name("userName").send_keys("mercury")
        # driver.find_element_by_name("password").send_keys("mercury")
        # driver.find_element_by_name("login").click()

    def test_Logout(self):
        driver = self.driver

        # driver.find_element_by_link_text("SIGN-OFF").click()
        #driver.quit()

    # test_LaunchBrowser()
    # test_Login()
    # test_Logout()



