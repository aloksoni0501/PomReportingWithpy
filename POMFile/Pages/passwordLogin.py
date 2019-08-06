class PassWord():
    def __init__(self, driver):
        self.driver = driver
        driver.password_textbox_xpath = "//input[@name='password']"
        driver.password_login_next_btn_xpath = "//span/span[text()='Next']"

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.driver.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.driver.password_textbox_xpath).send_keys(password)

    def password_next_btn(self):
        self.driver.find_element_by_xpath(self.driver.password_login_next_btn_xpath).click()


