from Keywords.LoginLogoutPage import Login
from Lib.BasePage import BasePage



class Test_Login(BasePage):

    def test_login(self):
       login_logout = Login(self.driver)
       login_logout.login()
       login_logout.logout()
        
