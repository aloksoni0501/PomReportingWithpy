
import unittest
from selenium import webdriver
class Assertion(unittest.TestCase):


    def chrom_valid(self):
        self.driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com")
        title = self.driver.title
        self.assertEqual("Google", title, "it will not come ")


if __name__ == "__main__":
    unittest.main()