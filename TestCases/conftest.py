import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def set_up(request):
    chrome_driver_path = "C:/JavaSeln/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(100)
    # driver.minimize_window()
    driver.get("https://huberlin-bo.staging.moveon4.com/")
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
    # menu = driver.find_element(By.XPATH, "//*[@role='presentation' and contains(text(),'Mobility')]")
    # menu.click()