from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    service = Service(r"C:\IULIYA\Обучение\Скайпро\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    waiter = WebDriverWait(driver, 4)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    first_name = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="first-name"]')))
    first_name.send_keys('Иван')

    last_name = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="last-name"]')))
    last_name.send_keys('Петров')

    address = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="address"]')))
    address.send_keys('Ленина, 55-3')

    e_mail = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="e-mail"]')))  # ✅ e-mail, не e_mail
    e_mail.send_keys('test@skypro.com')

    phone = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="phone"]')))
    phone.send_keys('+7985899998787')

    zip_code = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="zip-code"]')))
    zip_code.send_keys('')  # Пустое поле

    city = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="city"]')))
    city.send_keys('Москва')

    country = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="country"]')))
    country.send_keys('Россия')

    job_position = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="job-position"]')))  # ✅ job-position
    job_position.send_keys('QA')

    company = waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[name="company"]')))
    company.send_keys('SkyPro')

    # Отправка формы
    submit = waiter.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[@type="submit"]')))
    submit.click()

    # Проверка валидации
    waiter.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.alert-danger')))

    # Проверка zip-code (должен быть красным)
    zip_code_div = waiter.until(EC.visibility_of_element_located(
        (By.ID, 'zip-code')))
    assert 'alert-danger' in zip_code_div.get_attribute('class'), \
        'Поле zip code не подсвечено красным'

    # Проверка остальных полей (должны быть зелеными)
    fields_to_check = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                       'city', 'country', 'job-position', 'company']

    for field_id in fields_to_check:
        field_div = driver.find_element(By.ID, field_id)
        class_attr = field_div.get_attribute('class')
        assert 'alert-success' in class_attr, (
            f'Поле {field_id} не подсвечено зеленым. Класс: {class_attr}')

    print("✅Все проверки пройдены успешно!")
    driver.quit()
