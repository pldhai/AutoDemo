from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_css = ".oxd-button"
        self.alert_css = ".oxd-alert"

    def enter_username(self, username):
        self.driver.find_element(by=By.NAME, value=self.username_textbox_name).clear()
        self.driver.find_element(by=By.NAME, value=self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by=By.NAME, value=self.password_textbox_name).clear()
        self.driver.find_element(by=By.NAME, value=self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.login_button_css).click()
    
    def find_login_button(self):
        button_display = self.driver.find_element(by=By.CSS_SELECTOR, value=self.login_button_css).is_displayed()
        return button_display

    def find_alert(self):
        alert_display = self.driver.find_element(by=By.CSS_SELECTOR, value=self.alert_css).is_displayed()
        return alert_display
        