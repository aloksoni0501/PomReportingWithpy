class UserLogin():

    def __init__(self, driver):

        self.driver = driver

        driver.username_textbox_xpath = "//input[@name='identifier']"
        driver.user_login_next_btn_xpath = "//span[@class='CwaK9']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.driver.username_textbox_xpath).clear()

        self.driver.find_element_by_xpath(self.driver.username_textbox_xpath).send_keys(username)

    def username_next_btn(self):
        self.driver.find_element_by_xpath(self.driver.user_login_next_btn_xpath).click()

