from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage_calc:
    def __init__(self, driver):
        """
        Конструктор класса MainPage_calc.
        :param driver: WebDriver — объект драйвера Selenium.
        """
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
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param value: int — время задержки в секундах.
        :return: self — возвращает экземпляр класса для цепочки вызовов.
        """
        search_field = self.wait.until(
            EC.element_to_be_clickable(self.delay_field_locator)
        )
        search_field.clear()
        search_field.send_keys(str(value))
        return self

    def click_seven(self):
        """Нажимает на кнопку "7" на калькуляторе.
        :return: self — возвращает экземпляр класса для цепочки вызовов.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_7_locator)
        )
        button.click()
        return self

    def click_eight(self):
        """Нажимает на кнопку "8" на калькуляторе.
        :return: self — возвращает экземпляр класса для цепочки вызовов.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_8_locator)
        )
        button.click()
        return self

    def click_plus(self):
        """Нажимает на кнопку "+" на калькуляторе.
        :return: self — возвращает экземпляр класса для цепочки вызовов.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_plus_locator)
        )
        button.click()
        return self

    def click_equal(self):
        """Нажимает на кнопку "=" на калькуляторе.
        :return: self — возвращает экземпляр класса для цепочки вызовов.
        """
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_equal_locator)
        )
        button.click()
        return self

    def get_result(self, expected="15"):
        """
        Возвращает текущий результат с экрана калькулятора.
        :param expected: str — ожидаемый результат (по умолчанию "15").
        :return: str — текст результата на экране калькулятора.
        """
        # Ждем, пока на экране не появится expected значение
        self.wait.until(
            lambda d: d.find_element(*self.screen_locator).text == expected
        )
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.screen_locator)
        )
        return result_element.text

    def calculate_7_plus_8(self, delay=45):
        """Выполняет вычисление 7+8 с задержкой
        :param delay: int — время задержки в секундах.
        :return: str — текст результата на экране калькулятора.
        """
        self.set_delay(delay)
        self.click_seven()
        self.click_plus()
        self.click_eight()
        self.click_equal()
        return self.get_result()
