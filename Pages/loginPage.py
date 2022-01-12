from selenium.webdriver.common.by import By
from Locators.locators import Locators
class LoginPage():

    def __init__(self,driver):
        self.driver=driver

        self.username_textbox_id=Locators.username_textbox_id
        self.passord_textbox_id=Locators.passord_textbox_id
        self.login_button_id=Locators.login_button_id
        self.msg=Locators.msg_xpath

    def enter_username(self,username):
        self.driver.find_element(By.ID,self. username_textbox_id).send_keys('Admin')


    def enter_password(self,password):
        self.driver.find_element(By.ID, self.passord_textbox_id).send_keys('admin123')

    def login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def neg_loign(self):
        return self.driver.find_element(By.XPATH(self.msg))



