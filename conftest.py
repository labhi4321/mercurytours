import pytest
from selenium import webdriver
from testdata.data import *
import time



@pytest.fixture(scope="function")
def test_LaunchBrowser(request):
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/Abhijit/PycharmProjects/mercurytours/drivers/chromedriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    time.sleep(5)
    driver.quit()
