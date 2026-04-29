import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    waiter = WebDriverWait(driver, 60)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

        search_field = driver.find_element(By.ID, "delay")
        search_field.clear()
        search_field.send_keys("45")

        element_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        element_7.click()

        element_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        element_plus.click()

        element_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        element_8.click()

        element_equal = driver.find_element(By.XPATH, "//span[text()='=']")
        element_equal.click()

        start_time = time.time()

        result = waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.screen')))
        waiter.until(lambda d: result.text == "15")

        end_time = time.time()
        wait_time = end_time - start_time

        assert 43 <= wait_time <= 47, \
            f"Результат появился за {wait_time:.1f} секунд, а должен был за 45"

        actual_result = result.text
        expected_result = "15"

        assert actual_result == expected_result, \
            f"Ошибка! Ожидалось {expected_result}, получено {actual_result}"

        print(f"✅ 7 + 8 = {actual_result} (появилось за {wait_time:.1f} сек)")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
