from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage_shop():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def add_to_cart_sauce_labs_backpack(self):
        backpack = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack.click()

    def add_to_cart_sauce_labs_bolt_tshirt(self):
        bolt_tshirt = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        bolt_tshirt.click()

    def add_to_cart_sauce_labs_onesie(self):
        onesie = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie.click()
