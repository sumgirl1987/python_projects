from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_successful_purchase():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        username.clear()
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys("secret_sauce")

        login = driver.find_element(By.ID, "login-button")
        login.click()

        add_to_cart_sauce_labs_backpack = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_sauce_labs_backpack.click()

        add_to_cart_sauce_labs_bolt_tshirt = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_to_cart_sauce_labs_bolt_tshirt.click()

        add_to_cart_sauce_labs_onesie = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")
        add_to_cart_sauce_labs_onesie.click()

        cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
        cart.click()

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        first_name = driver.find_element(By.ID, "first-name")
        first_name.clear()
        first_name.send_keys("Юлия")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.clear()
        last_name.send_keys("Соколова")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.clear()
        postal_code.send_keys("195257")

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        total_label = driver.find_element(By.CLASS_NAME, "summary_total_label")
        actual_result = total_label.text
        expected_result = "Total: $58.29"

        assert actual_result == expected_result, \
            f"Ошибка! Ожидалось {expected_result}, получено {actual_result}"

        print(f"✅Тест пройден! Итоговая сумма: {actual_result}")

    finally:
        driver.quit()

    if __name__ == "__main__":
        test_successful_purchase()
