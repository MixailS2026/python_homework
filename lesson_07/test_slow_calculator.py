from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage


def test_slow_calculator():
    # Создание и настройка драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Создание и использование объекта страницы
        calculator_page = SlowCalculatorPage(driver)
        delay = 45

        calculator_page.open()
        calculator_page.set_delay(delay)
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

        actual_result = calculator_page.get_result("15", delay)

        # Проверка только на уровне теста
        assert actual_result == "15", (
            f"Ожидался результат '15', но получено: '{actual_result}'"
        )
    finally:
        # Закрытие драйвера
        driver.quit()
