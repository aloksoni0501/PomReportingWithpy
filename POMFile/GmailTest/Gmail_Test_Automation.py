from selenium import webdriver
import unittest
import HtmlTestRunner
from POMFile.Pages.usernameLogin import UserLogin
from POMFile.Pages.passwordLogin import PassWord
import time




class GmailSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test_login_user_valid(self):
        driver = self.driver
        driver.get("https://accounts.google.com")

        login = UserLogin(driver)

        login.enter_username("9109643374")

        login.username_next_btn()

        password1 = PassWord(driver)
        password1.enter_password("alok@123")
        time.sleep(2)
        password1.password_next_btn()

        # self.driver.find_element_by_id("identifierId").send_keys("aloksoni0501@gmail.com")
        # self.driver.find_element_by_xpath("//span[@class='CwaK9']").click()
        #
        # self.driver.find_element_by_xpath("//input[@name='password']").send_keys("alok@123")
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//span[ text()='Next']").click()
    @classmethod
    def tearDownClass(cls):#("/Users/macbookpro/PycharmProjects/GmailProject/POMFile/Pages/reports")
        cls.driver.close()
        cls.driver.quit()
        print("===============================Test Completed==================================")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/Reports"))