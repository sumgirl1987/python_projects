import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage_shop:
    """
    Класс Page Object для страницы корзины.
    Содержит метод для нажатия кнопки оформления заказа.
    """
    def __init__(self, driver):
        """
        Конструктор класса CartPage_shop.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Открыть страницу корзины")
    def open(self):
        """Открывает страницу корзины прямым переходом по URL"""
        self.driver.get("https://www.saucedemo.com/cart.html")
        return self

        # self.driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажать на кнопку Checkout")
    def checkout_button(self):
        """Нажимает кнопку 'Checkout' для перехода к оформлению заказа"""
        checkout_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "checkout")))
        checkout_button.click()
