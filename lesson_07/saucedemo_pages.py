from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        self.wait = WebDriverWait(driver, 20)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        self.wait.until(
            EC.presence_of_element_located(
                self.username_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.cart_link = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def add_item_to_cart(self, item_id: str):
        button_locator = (By.ID, f"add-to-cart-{item_id}")
        self.wait.until(EC.element_to_be_clickable(button_locator)).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_button)).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (
            By.CSS_SELECTOR, "[data-test='total-label']")

    def fill_shipping_info(
            self,
            first_name: str,
            last_name: str,
            postal_code: str
    ):
        self.wait.until(
            EC.presence_of_element_located(
                self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input
        ).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_text(self) -> str:
        return self.wait.until(
            EC.presence_of_element_located(self.total_label)
        ).text
