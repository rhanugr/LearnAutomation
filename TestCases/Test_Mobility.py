from Keywords.LoginLogoutPage import TestLogin
from Keywords.Mobility import Mobility
from Lib.BasePage import BasePage

class TestMobility(BasePage):
    def test_mobility(self):
        mob = Mobility(self.driver)
        login_logout = TestLogin(self.driver)
        login_logout.login()
        mob.mobility()
        str = "  Jtest"
        print(str.strip())
        login_logout.logout()
