import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from authPage_shop import AuthPage_shop
from mainPage_shop import MainPage_shop
from cartPage_shop import CartPage_shop
from checkoutPage_shop import CheckoutPage_shop


@pytest.fixture()
def driver():
    service = FirefoxService(
        r"C:\IULIYA\Обучение\Скайпро\geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get(
        "https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    auth_page = AuthPage_shop(driver)
    auth_page.set_username()
    auth_page.set_password()
    auth_page.click_login_button()

    main_page = MainPage_shop(driver)
    main_page.add_to_cart_sauce_labs_backpack()
    main_page.add_to_cart_sauce_labs_bolt_tshirt()
    main_page.add_to_cart_sauce_labs_onesie()

    cart_page = CartPage_shop(driver)
    cart_page.checkout_button()

    checkout_page = CheckoutPage_shop(driver)
    checkout_page.first_name()
    checkout_page.last_name()
    checkout_page.postal_code()
    checkout_page.continue_button()

    total_label = driver.find_element(By.CLASS_NAME, "summary_total_label")
    actual_result = total_label.text
    expected_result = "Total: $58.29"

    assert actual_result == expected_result, \
        f"Ошибка! Ожидалось {expected_result}, получено {actual_result}"

    print(f"✅Тест пройден! Итоговая сумма: {actual_result}")
