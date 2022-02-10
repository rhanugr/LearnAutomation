from selenium.webdriver.common.by import By


class Login_Logout():
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        self.driver.find_element(By.NAME, "username").send_keys("support@moveon4.com")
        self.driver.find_element(By.NAME, "password").send_keys("Moveon@30000")
        self.driver.find_element(By.NAME, "label_button_login").click()
        user_login= self.driver.find_element(By.ID,"loginDetails").text
        assert user_login == "surname_1, firstname_1"

    def logout(self):
            self.driver.find_element(By.ID, "logout").click()
