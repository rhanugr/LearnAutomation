from Keywords.LoginLogoutPage import LoginLogout
from Lib.BasePage import BasePage



class Test_Login(BasePage):

    def test_login(self):
       login_logout = LoginLogout(self.driver)
       login_logout.login()
       login_logout.logout()
        
