from selenium.webdriver.common.by import By
from Locators.locators import Locators

class HomePage:

    def __init__(self,driver):
        self.driver=driver
        self.welcome_link_text=Locators.welcome_link_text
        self.logout_link_text=Locators.logout_link_text

    def click_Welcome(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.welcome_link_text).click()

    def click_Logout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.logout_link_text).click()