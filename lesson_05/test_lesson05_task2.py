from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Сохраняем начальный URL для последующего сравнения
    initial_url = driver.current_url

    driver.maximize_window()
    sleep(5)

    # Находим поле ввода custname и вводим имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Михаил")
    sleep(10)

    # Находим кнопку Submit по тексту и кликаем на нее
    submit_but = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
    )

    submit_but.click()
    sleep(5)

    # Проверяем, что текущий URL изменился (не равен начальному)
    assert driver.current_url != initial_url, (
        f"Переход не произошел! URL остался прежним: {initial_url}"
    )

    driver.quit()
