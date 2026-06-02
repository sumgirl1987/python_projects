import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from mainPage_calc import MainPage_calc


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации драйвера Chrome,
    открытия страницы калькулятора и последующего завершения работы.
    :yield: WebDriver — настроенный экземпляр драйвера Selenium.
    """
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@allure.title("Тестирование операции сложения на калькуляторе")
@allure.description("Проверка операции сложения на калькуляторе "
                    "с настраиваемой задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет вычисление 7 + 8 на калькуляторе с задержкой 45 секунд.
    Шаги теста:
        1. Настройка задержки 45 секунд
        2. Нажатие кнопок 7, +, 8
        3. Замер времени до нажатия "="
        4. Нажатие "=" и ожидание результата "15"
        5. Замер времени после получения результата
        6. Проверка времени ожидания (должно быть 43-47 секунд)
        7. Проверка результата (должно быть "15")

    :param driver: WebDriver — экземпляр драйвера от фикстуры
    """

    with allure.step("Открыть калькулятор и настроить задержку"):
        page = MainPage_calc(driver)
        page.set_delay(45)

    with allure.step("Выполнить вычисление: 7 + 8"):
        page.click_seven()
        page.click_plus()
        page.click_eight()

    with allure.step("Замер времени ДО нажатия ="):
        start_time = time.time()

    with allure.step("Нажать ="):
        page.click_equal()

    # Ожидаем, что текст станет "15"
    WebDriverWait(driver, 45).until(
        lambda d: d.find_element(By.CSS_SELECTOR, 'div.screen').text == "15"
    )

    with allure.step("Замер времени ПОСЛЕ нажатия ="):
        end_time = time.time()

    with allure.step("Определяем разницу во времени ПОСЛЕ и ДО"):
        wait_time = end_time - start_time

    with allure.step("Получаем результат после ожидания 15"):
        actual_result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        expected_result = "15"

    with allure.step("Проверить время получения результата"):
        assert 43 <= wait_time <= 47, \
            f"Результат появился за {wait_time:.1f} секунд, а должен был за 45"

    with allure.step("Проверить результат вычисления"):
        assert actual_result == expected_result, \
            f"Ошибка! Ожидалось {expected_result}, получено {actual_result}"

    print(f"✅ 7 + 8 = {actual_result} (появилось за {wait_time:.1f} сек)")
