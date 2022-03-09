from Keywords.CommonMethods import Common
from Keywords.LoginLogoutPage import Login
from Keywords.Settings import Settings_Administration
from Lib.BasePage import BasePage


class Test_AcademicPeriod(BasePage):

    def test_academic_period_creation(self):
        setting = Settings_Administration(self.driver)
        login = Login(self.driver)
        login.login()
        setting.academic_periods()

        Common(self.driver).new(self)
        Common(self.driver).close(self)

        Common(self.driver).close(self)
        login.logout()
