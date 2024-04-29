from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.user_dropdown_css = ".oxd-userdropdown-name"
        self.logout_link_text = "Logout"
        self.dashboard_header = ""

    def click_user_dropdown(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.user_dropdown_css).click()

    def click_logout(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.logout_link_text).click()

    def check_user_name(self):
        current_user_name = self.driver.find_element(by=By.CSS_SELECTOR, value=self.user_dropdown_css).is_displayed()
        return current_user_name
        


