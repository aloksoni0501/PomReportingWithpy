class FacebookLogin():

    def __init__(self, driver):

        self.driver = driver

        driver.username_textbox_xpath = "//*[@id='email']"
        driver.password_textbox_xpath = "//*[@id='pass']"
        driver.click_login_btn_xpath = "//*[@id='u_0_a']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.driver.username_textbox_xpath).clear()

        self.driver.find_element_by_xpath(self.driver.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.driver.password_textbox_xpath).clear()

        self.driver.find_element_by_xpath(self.driver.password_textbox_xpath).send_keys(password)

    def username_next_btn(self):
        self.driver.find_element_by_xpath(self.driver.click_login_btn_xpath).click()