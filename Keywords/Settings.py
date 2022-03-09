import time
from selenium.webdriver.common.by import By


class Settings_Administration:
    def __init__(self,driver):
        self.driver = driver

    '''1.Click on Settings>Administration>Academic Periods'''
    def academic_periods(self):
        menu = self.driver.find_element(By.XPATH, "//*[@role='presentation' and contains(text(),'Settings')]")
        # sub_menu = self.driver.find_element(By.XPATH,"/../../../following-sibling::div//span[contains(text(),'Stays')]")
        # child_menu =self.driver.find_element(By.XPATH,"/../../../following-sibling::div//a[contains(text(),'Stays')]")
        menu.click()
        time.sleep(2)
        sub_menu = menu.find_element(By.XPATH, "../../../following-sibling::div//span[contains(text(),'Administration')]")
        child_menu = sub_menu.find_element(By.XPATH, "../../../following-sibling::div//a[contains(text(),'Academic periods')]")
        sub_menu.click()
        time.sleep(2)
        child_menu.click()

    '''2.Click on New Academic Periods'''

