import logging

from Keywords.LoginLogoutPage import Login
from Keywords.Mobility import Mobility
from Lib.BasePage import BasePage

class TestMobility(BasePage):
    def test_mobility(self):
        mob = Mobility(self.driver)
        login_logout = Login(self.driver)
        login_logout.login()
        mob.mobility()
        str = "  Jtest"
        print(str.strip())
        login_logout.logout()
        print("Logger")