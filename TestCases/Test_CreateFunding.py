import logging
import time

from Keywords.CreateFundingPage import CreateFunding
from Keywords.LoginLogoutPage import Login_Logout
from Lib.BasePage import BasePage



class Test_CreateFund(BasePage):

    def test_verify_funding(self):
        logging.info("Create a Funding")
        loginlogout = Login_Logout(self.driver)
        loginlogout.login()
        '''Create Funding'''
        funding = CreateFunding(self.driver)
        funding.test_funding()

        time.sleep(10)
        loginlogout.logout()
