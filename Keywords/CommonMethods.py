from selenium.webdriver.common.by import By


class Common:

    def __init__(self,driver):
        self.driver = driver

    @staticmethod
    def new(self):
        self.driver.find_element(By.XPATH,"//ul[@id='actionsToolbar']//a[contains(text(),'New')]").click()

    @staticmethod
    def close(self):
        self.driver.find_element(By.XPATH,"//span[@class='dijitTabCloseText']//parent::span[@title='Close']").click()

