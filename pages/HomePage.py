class homepage():

    def __init__(self, driver):
        self.driver = driver
        self.link_signoff = "SIGN-OFF"

    def click_SignOff(self):
        self.driver.find_element_by_link_text(self.link_signoff).click()
