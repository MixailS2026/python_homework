from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()    
    wait = WebDriverWait(driver, 50)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле ввода по локатору #delay вводим значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажимаем на кнопки: 7 + 8 =
    # Кнопки реализованы через теги span, находим их по тексту
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Локатор окна с результатом калькулятора
    screen_locator = (By.CLASS_NAME, "screen")

    # Ждем, пока внутри элемента .screen появится текст "15"
    wait.until(EC.text_to_be_present_in_element(screen_locator, "15"))

    #  Проверяем (assert), что в окне отобразился результат 15
    result_text = driver.find_element(*screen_locator).text
    assert result_text == "15", f"Ожидался результат 15, но отобразилось: '{result_text}'"

    driver.quit()
