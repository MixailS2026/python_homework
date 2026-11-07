from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Открываем страницу
    base_url = "https://httpbin.qa-territory.online"
    driver.get(base_url)
    sleep(5)

    # 2. Находим и кликаем на ссылку "HTML Form"
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()
    sleep(5)

    # 3. Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url
    sleep(5)

    # 4. Возвращаемся назад на главную страницу
    driver.back()

    # 5. Проверяем, что вернулись на исходный URL
    assert (driver.current_url == base_url
            or driver.current_url == f"{base_url}/")
    sleep(5)

    driver.quit()
