
class LoginWithInvalidText():

    def __init__(self, driver):
        self.driver = driver
        driver.sign_in_click_xpath = "//a[text()='Sign in']"

    def login(self):
        self.driver.driver.find_element_by_xpath(self.driver.sign_in_click_xpath).click()
