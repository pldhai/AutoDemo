import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.loginPage import LoginPage
from pages.homePage import HomePage

# @pytest.fixture(autouse=True, scope="function")
# def setup_fixture():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield 
#     driver.close()
#     driver.quit()
#     print("1 Test completed")

'''
TC01: Open login page successfully
1. Open browser - chrome
2. naviagte to url "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
3. check login button is exist
'''

def test_open_login_page():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # assert driver.find_element(by=By.CSS_SELECTOR, value=".oxd-button").is_displayed() == True
    login = LoginPage(driver)
    assert login.find_login_button() == True
    time.sleep(2)
    driver.quit()

'''
TC02: Login successfully with valid username and password
1. Open browser - chrome
2. naviagte to url "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
3. enter username
4. enter password
5. click login
6. check current user's name existed
7. logout
'''
def test_login_valid():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    homepage = HomePage(driver)
    assert homepage.check_user_name() == True
    homepage.click_user_dropdown()
    homepage.click_logout()
    time.sleep(5)
    driver.quit()



'''
TC03: Login failed with invalid username and password
1. Open browser - chrome
2. naviagte to url "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
3. enter invalid username
4. enter password
5. check alert 
'''

def test_login_invalid_username():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(driver)
    login.enter_username("Admin111")
    login.enter_password("admin123")
    login.click_login()
    assert login.find_alert() == True
    time.sleep(2)
    driver.quit()