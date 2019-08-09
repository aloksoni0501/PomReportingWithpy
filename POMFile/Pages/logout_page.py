class FacebookLogout():

    def __init__(self, driver):

        self.driver = driver


        driver.click_setting_btn_xpath = "///*[@id='userNavigationLabel']"
        driver.click.on.logout_xpath = "//*[@id='js_32']/div/div/ul/li[8]"

    def click_setting(self):
        self.driver.find_element_by_xpath(self.driver.click_setting_btn_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self. driver.click.on.logout_xpath).click()



