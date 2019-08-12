
from selenium import webdriver
import pytest



def chrom_valid():
    driver = webdriver.Chrome(executable_path="/Users/macbookpro/PycharmProjects/GmailProject/POMFile/driver/chromedriver 2")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    title_of_webpage = driver.title
    driver.assertEqual(title_of_webpage == "Google")
    driver.find_element_by_xpath("//*[@id='fakebox-input']").send_keys("facebook")
    driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/button").click()


