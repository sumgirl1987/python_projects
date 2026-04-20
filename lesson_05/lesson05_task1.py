from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoAlertPresentException

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")
sleep(2)
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-test")
blue_button.click()

try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alert принят")
except NoAlertPresentException:
    print("Alert не появился")

print("Скрипт успешно отработал")

driver.quit()
