from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: int):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, value: str):
        button_locator = (By.XPATH, f"//span[text()='{value}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, expected_result: str, timeout: int) -> str:
        wait = WebDriverWait(self.driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(self.screen, expected_result)
        )

        return self.driver.find_element(*self.screen).text
