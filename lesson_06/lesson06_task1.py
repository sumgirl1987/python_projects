from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get('http://uitestingplayground.com/ajax')

blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
blue_button.click()

waiter = WebDriverWait(driver, 16)

element = waiter.until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success'))
)

print(f'\"{element.text}\"')

driver.quit()
