
from Keywords.LoginLogoutPage import Login_Logout
from Lib.BasePage import BasePage



class Test_Login(BasePage):

    def test_login(self):
       login_logout = Login_Logout(self.driver)
       login_logout.login()
       login_logout.logout()
        
