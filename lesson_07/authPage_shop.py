from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage_shop:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def set_username(self):
        username = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "user-name")))
        username.clear()
        username.send_keys("standard_user")

    def set_password(self):
        password = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "password")))
        password.clear()
        password.send_keys("secret_sauce")

    def click_login_button(self):
        login = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "login-button")))
        login.click()
