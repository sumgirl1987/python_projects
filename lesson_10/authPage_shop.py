import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage_shop:
    """
    Класс Page Object для страницы авторизации интернет-магазина.
    Содержит методы для ввода логина, пароля и нажатия кнопки входа.
    """
    def __init__(self, driver):
        """
        Конструктор класса AuthPage_shop.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Ввести имя пользователя")
    def set_username(self):
        """
        Вводит имя пользователя в поле авторизации.
        Используется стандартный пользователь 'standard_user'.
        """
        username = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "user-name")))
        username.clear()
        username.send_keys("standard_user")

    @allure.step("Ввести пароль")
    def set_password(self):
        """
        Вводит пароль в поле авторизации.
        Используется стандартный пароль 'secret_sauce'.
        """
        password = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "password")))
        password.clear()
        password.send_keys("secret_sauce")

    @allure.step("Нажать на кнопку Login")
    def click_login_button(self):
        """
        Нажимает кнопку 'Login' для входа в систему.
        """
        login = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "login-button")))
        login.click()
