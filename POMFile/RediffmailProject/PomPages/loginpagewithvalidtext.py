class LoginWithValidText():

    def __init__(self, driver):
        self.driver = driver
        driver.sign_in_link_link_text = "Sign in"
        driver.username_textbox_xpath = "//*[@id='login1']"
        driver.password_textbox_xpath = "//*[@id='password']"
        driver.click_on_login_xpath = "//input[@title='Sign in']"
        driver.logout_click_xpath = "//a[text()='Logout']"

    def sign_in_link(self):
        self.driver.find_element_by_link_text(self.driver.sign_in_link_link_text).click()

    def valid_username(self, username):
        self.driver.driver.find_element_by_xpath(self.driver.username_textbox_xpath).clear()
        self.driver.driver.find_element_by_xpath(self.driver.login_click_xpath).sen_keys(username)

    def valid_password(self, password):
        self.driver.driver.find_element_by_xpath(self.driver.password_textbox_xpath).clear()
        self.driver.driver.find_element_by_xpath(self.driver.login_click_xpath).sendkeys(password)

    def click_on_login_btn(self):
        self.driver.driver.find_element_by_xpath(self.driver.click_on_login_xpath).click()

    def click_on_logout_btn(self):
        self.driver.ind_element_by_xpath(self.driver.logout_click_xpath ).click()

