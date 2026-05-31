import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from authPage_shop import AuthPage_shop
from mainPage_shop import MainPage_shop
from cartPage_shop import CartPage_shop
from checkoutPage_shop import CheckoutPage_shop


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации драйвера Firefox,
    открытия страницы интернет-магазина и последующего завершения работы.
    :yield: WebDriver — настроенный экземпляр драйвера Selenium.
    """
    firefox_options = Options()
    firefox_options.binary_location = \
        r"C:\Program Files\Mozilla Firefox\firefox.exe"
    service = FirefoxService(
        executable_path=r"C:\IULIYA\Обучение\Скайпро\geckodriver.exe"
    )
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Авторизация и добавление товаров в корзину")
@allure.description("Тестирование операции по добавлению товаров в корзину")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
   Тест проверяет получение итоговой суммы добавленных в корзину товаров.
   Шаги теста:
       1. Авторизация пользователя
       2. Добавление трех товаров в корзину
       3. Оформление заказа
       4. Получение общей суммы заказа
   """

    with allure.step("Авторизоваться на сайте: ввести username и password"):
        auth_page = AuthPage_shop(driver)
        auth_page.set_username()
        auth_page.set_password()
        auth_page.click_login_button()

    with allure.step("Добавить 3 товара в корзину"):
        main_page = MainPage_shop(driver)
        main_page.add_to_cart_sauce_labs_backpack()
        main_page.add_to_cart_sauce_labs_bolt_tshirt()
        main_page.add_to_cart_sauce_labs_onesie()

    with allure.step("Перейти на страницу корзины и нажать checkout"):
        cart_page = CartPage_shop(driver)
        cart_page.open().checkout_button()

    with allure.step("Оформить заказ: заполнить поля first_name, "
                     "last_name и postal_code"):
        checkout_page = CheckoutPage_shop(driver)
        checkout_page.first_name()
        checkout_page.last_name()
        checkout_page.postal_code()
        checkout_page.continue_button()

    with allure.step("Получить итоговую сумму заказа"):
        total_label = driver.find_element(By.CLASS_NAME, "summary_total_label")
        actual_result = total_label.text
        expected_result = "Total: $58.29"

    with allure.step("Проверить результат вычисления"):
        assert actual_result == expected_result, \
            f"Ошибка! Ожидалось {expected_result}, получено {actual_result}"

    print(f"✅Тест пройден! Итоговая сумма: {actual_result}")
