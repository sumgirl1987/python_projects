import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage_shop:
    """
    Класс Page Object для главной страницы интернет-магазина.
    Содержит методы для добавления товаров в корзину.
    """
    def __init__(self, driver):
        """
        Конструктор класса MainPage_shop.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    @allure.step("Добавить товар Sauce Labs Backpack в корзину")
    def add_to_cart_sauce_labs_backpack(self):
        """
        Добавляет товар 'Sauce Labs Backpack' в корзину.
        """
        backpack = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack.click()

    @allure.step("Добавить товар Sauce Labs Bolt T-Shirt в корзину")
    def add_to_cart_sauce_labs_bolt_tshirt(self):
        """Sauce Labs Bolt T-ShirtSauce labs bolt T-Shirt' в корзину.
        """
        bolt_tshirt = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        bolt_tshirt.click()

    @allure.step("Добавить товар Sauce Labs Onesie в корзину")
    def add_to_cart_sauce_labs_onesie(self):
        """
        Добавляет товар 'Sauce Labs Onesie' в корзину.
        """
        onesie = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie.click()
