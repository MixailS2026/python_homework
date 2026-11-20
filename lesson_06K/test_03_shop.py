from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://saucedemo.com")

    #  Авторизуемся как standard_user с использованием ожидания появления полей
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем в корзину выбранные товары (ждем кликабельности первой кнопки)
    backpack_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    backpack_btn.click()
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout (ждем появления кнопки на новой странице)
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # 6. Заполняем форму своими данными
    first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name.send_keys("Михаил")
    
    driver.find_element(By.ID, "last-name").send_keys("Шарамчевский")
    driver.find_element(By.ID, "postal-code").send_keys("65603")

    # 7. Нажимаем кнопку Continue
    driver.find_element(By.ID, "continue").click()

    # 8. Читаем со страницы итоговую стоимость (Total) с ожиданием её появления
    total_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    # 9. Проверяем, что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29", f"Неожиданная сумма: {total_text}"

    driver.quit()
