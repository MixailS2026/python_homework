from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # Использование find_elements для поиска всех элементов с тегом <a>
    links = driver.find_elements(By.TAG_NAME, "a")

    # len() возвращает количество элементов в списке для проверки
    assert len(links) == 9

    # Использование цикла для проверки отображения всех элементов
    for link in links:
        assert link.is_displayed()

    # Использование индекса [0] для проверки первой ссылки
    first_link_text = links[0].text
    assert "1" in first_link_text

    driver.quit()
