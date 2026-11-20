from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation_edge():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 20)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Ожидаем загрузки полей и заполняем форму значениями
    wait.until(EC.presence_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # 2. Нажатие кнопки Submit
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # 3. Ожидаем, пока применится валидация (ждем появления класса на одном из элементов результатов)
    # На этом сайте после отправки элементы результатов получают ID, соответствующие именам полей
    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    # Проверка, что пустое поле Zip code подсвечено красным
    zip_code_result = driver.find_element(By.ID, "zip-code")
    zip_class = zip_code_result.get_attribute("class")
    assert "alert-danger" in zip_class or "is-invalid" in zip_class, "Поле Zip code должно быть подсвечено красным"

    # 4. Проверка, что остальные поля подсвечены зеленым
    other_fields_ids = [
        "first-name", "last-name", "address", "e-mail", 
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in other_fields_ids:
        field_result = driver.find_element(By.ID, field_id)
        field_class = field_result.get_attribute("class")
        assert "alert-success" in field_class or "is-valid" in field_class, f"Поле {field_id} должно быть подсвечено зеленым"

    driver.quit()
