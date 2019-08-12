from selenium import webdriver
import  time
import unittest
import HtmlTestRunner
from POMFile.RediffmailProject.PomPages.pageLogin import LoginWithInvalidText
from POMFile.RediffmailProject.PomPages.loginpagewithvalidtext import LoginWithValidText

class RediffTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        cls.driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    def test_Homepage_Title(self):


        driver = self.driver

        self.driver.get("https://mail.rediff.com")
        self.assertEqual("Rediff.com: News | Rediffmail | Stock Quotes | Shopping", self.driver.title, "web page title not maching")
        login1 = LoginWithInvalidText(driver)
        login1.login()
        login2 = LoginWithValidText(driver)
        login2.sign_in_link()
        login2.valid_username("aloksoni0501")
        login2.valid_password("alok@123")
        login2.click_on_login_btn()
        login2.click_on_logout_btn()

    # def test_login_without_username_and_password(self, driver):
    #
    #     login1 = LoginWithInvalidText(driver)
    #     login1.login()
    #     # self.driver.find_element_by_xpath("//a[text()='Sign in']").click()
    #     # self.driver.find_element_by_xpath("//input[@name='proceed']").click()
    #     # self.driver.switch_to_alert().accept()
    #
    # def test_sign_in_with_valid_username_and_password(self):
    #
    #     self.driver.back()
    #     self.driver.find_element_by_link_text("Sign in").click()
    #
    #     self.driver.find_element_by_xpath("//*[@id='login1']").send_keys("aloksoni0501")
    #
    #     self.driver.find_element_by_xpath("//*[@id='password']").send_keys("alok@123")
    #
    #     self.driver.find_element_by_xpath("//input[@title='Sign in']").click()
    #
    #     self.driver.find_element_by_xpath("//a[text()='Logout']").click()
    #
    # def test_valid_username_and_invalid_password(self):
    #
    #     self.driver.find_element_by_link_text("Rediff Home").click()
    #     self.driver.find_element_by_link_text("Sign in").click()
    #     self.driver.find_element_by_xpath("//*[@id='login1']").send_keys("aloksoni0501")
    #     self.driver.find_element_by_name("passwd").send_keys("alok@12")
    #     self.driver.find_element_by_xpath("//input[@name='proceed']").click()
    #    # self.driver.assertEqual("", self.driver., "title is not matching")
    #     #self.driver.find_element_by_xpath("//a[text()='Logout']").click()
    #
    # # def test_invalid_username_and_password(self):
    # #     self.driver.back()
    # #     self.driver.find_element_by_xpath("//*[@id='login1']").send_keys("aloksoni")
    # #     self.driver.find_element_by_name("passwd").send_keys("alok@12")
    # #     self.driver.find_element_by_xpath("//input[@name='proceed']").click()
    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        #cls.driver.quit()
        print("=====================SuccessFully logged in====================")
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/RediffmailProject/reportfile"))


