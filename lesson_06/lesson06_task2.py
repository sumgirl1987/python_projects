from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get('http://uitestingplayground.com/textinput')

MyButton = driver.find_element(By.CSS_SELECTOR, 'input.form-control')

MyButton.send_keys('SkyPro')

blue_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
blue_button.click()

print(f'\"{blue_button.text}\"')

driver.quit()
