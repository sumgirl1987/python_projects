from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage_shop():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout_button(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "checkout")))
        checkout_button.click()
