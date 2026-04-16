from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)

search_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_input.send_keys("12345")
sleep(2)

search_input.clear()
sleep(2)

search_input.send_keys("54321")
sleep(2)

driver.quit()
