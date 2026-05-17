import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from mainPage_calc import MainPage_calc


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    page = MainPage_calc(driver)
    page.set_delay(45)
    page.click_seven()
    page.click_plus()
    page.click_eight()

    # Замер времени ДО нажатия "="
    start_time = time.time()

    page.click_equal()

    # Ожидаем, что текст станет "15"
    WebDriverWait(driver, 45).until(
        lambda d: d.find_element(By.CSS_SELECTOR, 'div.screen').text == "15"
    )

    end_time = time.time()
    wait_time = end_time - start_time

    # Получаем результат после ожидания
    actual_result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    expected_result = "15"

    # Проверка времени
    assert 43 <= wait_time <= 47, \
        f"Результат появился за {wait_time:.1f} секунд, а должен был за 45"

    # Проверка результата
    assert actual_result == expected_result, \
        f"Ошибка! Ожидалось {expected_result}, получено {actual_result}"

    print(f"✅ 7 + 8 = {actual_result} (появилось за {wait_time:.1f} сек)")
