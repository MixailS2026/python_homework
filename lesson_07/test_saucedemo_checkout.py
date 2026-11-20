from selenium import webdriver
from saucedemo_pages import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_saucedemo_checkout():
    # Создание и настройка драйвера
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        # 1. Авторизация
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Добавление товаров и переход в корзину
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        inventory_page.add_item_to_cart("sauce-labs-onesie")
        inventory_page.go_to_cart()

        # 3. Переход к оформлению заказа
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        # 4. Заполнение данных и получение итоговой суммы
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping_info("Михаил", "Шарамчевский", "65603")
        total_text = checkout_page.get_total_text()

        # 5. Проверка итоговой суммы
        assert total_text == "Total: $58.29", (
            f"Неожиданная сумма: {total_text}"
        )

    finally:
        # Закрытие драйвера
        driver.quit()
