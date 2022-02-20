import time

from selenium.webdriver.common.by import By


class Mobility:
    def __init__(self,driver):
        self.driver = driver

    def mobility(self):
        menu = self.driver.find_element(By.XPATH,"//*[@role='presentation' and contains(text(),'Mobility')]")
        # sub_menu = self.driver.find_element(By.XPATH,"/../../../following-sibling::div//span[contains(text(),'Stays')]")
        # child_menu =self.driver.find_element(By.XPATH,"/../../../following-sibling::div//a[contains(text(),'Stays')]")


        menu.click()
        time.sleep(2)
        sub_menu = menu.find_element(By.XPATH, "../../../following-sibling::div//span[contains(text(),'Stays')]")
        child_menu = sub_menu.find_element(By.XPATH,"../../../following-sibling::div//a[contains(text(),'Stays')]")
        sub_menu.click()
        time.sleep(2)
        child_menu.click()
        # (menu+sub_menu).click()
        # (menu+sub_menu+child_menu).click()
        self.driver.find_element(By.XPATH,"(//tr[@class='jqgrow ui-row-ltr ui-widget-content'])[1]/td/input[@type='checkbox']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//*[@title='Actions']//parent::span[contains(@class,'dijitDownArrowButton')]").click()
        # self.driver.find_element(By.XPATH,"(//input[@class='edit'])[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//td[text()='Open selection']").click()