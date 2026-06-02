import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage_shop:
    """
    Класс Page Object для страницы оформления заказа.
    Содержит методы для ввода имени, фамилии, почтового индекса и
    нажатия кнопки входа.
    """
    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage_shop.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Ввести имя")
    def first_name(self):
        """
        Вводит имя пользователя в поле 'First Name'.
        Используется значение "Юлия".
        """
        first_name = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")))
        first_name.clear()
        first_name.send_keys("Юлия")

    @allure.step("Ввести фамилию")
    def last_name(self):
        """
        Вводит фамилию пользователя в поле 'Last Name'.
        Используется значение "Соколова".
        """
        last_name = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "last-name")))
        last_name.clear()
        last_name.send_keys("Соколова")

    @allure.step("Ввести почтовый индекс")
    def postal_code(self):
        """
        Вводит почтовый индекс в поле 'Zip/Postal Code'.
        Используется значение "195257".
        """
        postal_code = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "postal-code")))
        postal_code.clear()
        postal_code.send_keys("195257")

    @allure.step("Нажать на кнопку Continue")
    def continue_button(self):
        """
        Нажимает кнопку 'Continue' для перехода к странице обзора заказа
        (Checkout: Overview).
        """
        continue_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue")))
        continue_button.click()
