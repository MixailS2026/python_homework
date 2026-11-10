from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru")

    # Установите cookie пользователя 1
    cookie_user_1 = {
        'name': 'SESSION',
        'value': 'NmI5YzA1MDItMTA1Zi00Zjc0LWE4ZWItNzc4MDAxMGJmN2Uy',
        'domain': 'gitflic.ru'
    }
    driver.add_cookie(cookie_user_1)

    # Обновите страницу
    driver.refresh()

    # Перейдите на страницу профиля пользователя 1
    driver.get("https://gitflic.ru/user/mixail1")

    # Сохраните текущий URL пользователя 1
    url_user_1 = driver.current_url
    print(f"URL Пользователя 1: {url_user_1}")

    # Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # Установите cookie пользователя 2
    cookie_user_2 = {
        'name': 'SESSION',
        'value': 'YzFjMzMwZDctODNjOC00NTIzLTg0OTktYzcwZTQxNWQyODll',
        'domain': 'gitflic.ru'
    }
    driver.add_cookie(cookie_user_2)

    # обновите страницу
    driver.refresh()

    # Перейдите на страницу профиля пользователя 2
    driver.get("https://gitflic.ru/user/mixail2")

    # Сохраните текущий URL пользователя 2
    url_user_2 = driver.current_url
    print(f"URL Пользователя 2: {url_user_2}")

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user_1 != url_user_2, (
        f"ОШИБКА: URL пользователей совпадают! ({url_user_1})"
    )

    driver.quit()
