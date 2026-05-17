from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage_calc:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

        # Локаторы
        self.delay_field_locator = (By.ID, "delay")
        self.button_7_locator = (By.XPATH, "//span[text()='7']")
        self.button_8_locator = (By.XPATH, "//span[text()='8']")
        self.button_plus_locator = (By.XPATH, "//span[text()='+']")
        self.button_equal_locator = (By.XPATH, "//span[text()='=']")
        self.screen_locator = (By.CSS_SELECTOR, 'div.screen')

    def set_delay(self, value):
        """Устанавливает задержку"""
        search_field = self.wait.until(
            EC.element_to_be_clickable(self.delay_field_locator)
        )
        search_field.clear()
        search_field.send_keys(str(value))
        return self

    def click_seven(self):
        """Нажимает кнопку 7"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_7_locator)
        )
        button.click()
        return self

    def click_eight(self):
        """Нажимает кнопку 8"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_8_locator)
        )
        button.click()
        return self

    def click_plus(self):
        """Нажимает кнопку +"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_plus_locator)
        )
        button.click()
        return self

    def click_equal(self):
        """Нажимает кнопку ="""
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_equal_locator)
        )
        button.click()
        return self

    def get_result(self, expected="15"):
        """Получает результат, ожидая конкретное значение"""
        # Ждем, пока на экране не появится expected значение
        self.wait.until(
            lambda d: d.find_element(*self.screen_locator).text == expected
        )
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.screen_locator)
        )
        return result_element.text

    def calculate_7_plus_8(self, delay=45):
        """Выполняет вычисление 7+8 с задержкой"""
        self.set_delay(delay)
        self.click_seven()
        self.click_plus()
        self.click_eight()
        self.click_equal()
        return self.get_result()
