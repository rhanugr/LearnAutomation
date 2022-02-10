import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateFunding():
    def __init__(self,driver):
        self.driver = driver

    def test_funding(self):
        self.driver.find_element(By.ID,"sideBarFunding_button").click()
        self.driver.find_element(By.ID,"sideBarOption-fundings").click()
        self.driver.find_element(By.XPATH,"//ul[@id='actionsToolbar']//li[@class='actionsToolbarItem newIcon']").click()
        select_funding_type= self.driver.find_element(By.ID,"ᐅtab_funding_newᐅfundingTypeId")
        select_funding_type.click()
        time.sleep(2)
        select = Select(select_funding_type)
        select.select_by_index(1)

        academi_year = self.driver.find_element(By.ID,"ᐅtab_funding_newᐅfundingToYearId")
        academi_year.click()
        time.sleep(2)
        select_academic_year = Select(academi_year)
        select_academic_year.select_by_value("12")
        '''Save the Data'''
        self.driver.find_element(By.XPATH,"//a[@class='formBuilderSave' and @title='Save']").click()
        time.sleep(1)
        message = "The new entry has been added successfully."
        expected_mes = self.driver.find_element(By.XPATH,"//div[@class='message' and contains(@id,'statusMessage')]")
        assert expected_mes.text == message
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//div[contains(@id,'mainTab_tablist_tab_funding')]//span[@class='dijitTabCloseButton']").click()



