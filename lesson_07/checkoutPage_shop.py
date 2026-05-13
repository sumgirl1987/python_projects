from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage_shop():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def first_name(self):
        first_name = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")))
        first_name.clear()
        first_name.send_keys("Юлия")

    def last_name(self):
        last_name = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "last-name")))
        last_name.clear()
        last_name.send_keys("Соколова")

    def postal_code(self):
        postal_code = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "postal-code")))
        postal_code.clear()
        postal_code.send_keys("195257")

    def continue_button(self):
        continue_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue")))
        continue_button.click()
