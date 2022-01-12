from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
from Pages.loginPage import *
from Pages.homePage import *
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ser = Service('C:/Users/sunakuma/Documents/POM-Demo/driver/chromedriver.exe')
        # driver=webdriver.Chrome(executable_path="C:/Users/sunakuma/Documents/POM-Demo/driver/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.ser)
        cls.driver.get('https://opensource-demo.orangehrmlive.com/')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test01_login_valid(self):
        driver=self.driver
        loginobj=LoginPage(driver)
        loginobj.enter_username('Admin')
        loginobj.enter_password('admin123')
        loginobj.login()

        homeobj=HomePage(driver)
        homeobj.click_Welcome()
        homeobj.click_Logout()
        time.sleep(5)

    def test02_login_invalid(self):
        driver=self.driver
        loginobj=LoginPage(driver)
        self.msg=loginobj.neg_loign()
        assert self.msg


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__=="__main__":
    try:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sunakuma/Documents/POM-Demo/Report'))
    except Exception as e:
        print('Exception==============',e)

