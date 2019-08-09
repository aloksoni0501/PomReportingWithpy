from selenium import webdriver
import unittest
import HtmlTestRunner
from POMFile.Pages.facebook_login_page import FacebookLogin
from POMFile.Pages.logout_page import FacebookLogout

import time




class Facebook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("===================Start Testing=======================")
        cls.driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login_user_valid(self):
        driver = self.driver
        driver.get("https://www.facebook.com")

        login = FacebookLogin(driver)

        login.enter_username("6264001327")
        time.sleep(2)
        login.enter_password("9589965520")

        login.username_next_btn()
        logout = FacebookLogout(driver)
        logout.click_setting()
        logout.click_logout()
        # password1 = PassWord(driver)
        # password1.enter_password("alok@123")
        # time.sleep(2)
        # password1.password_next_btn()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("/n ===============================Test Completed==================================")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/Reports"))