from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ALL_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    SHOPPING_CART_IS_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def input_text(self, param, param1):
        pass

    def search_product(self):
        self.input_text('tea', '*self.SEARCH_FIELD')
        self.click(self.SEARCH_BTN)
        sleep(10)

    def shopping_cart(self):
        # context.driver.find_element(By.XPATH, "//a[@aria-label='cart 0 items']").click()
        self.find_element(*self.CART_ICON).click()
        sleep(2)

    def verify_empty_shopping_cart(self):
        expected_text2 = 'Your cart is empty'
        actual_text2 = self.find_element(*self.SHOPPING_CART_IS_EMPTY_MSG).text
        assert expected_text2 in actual_text2, f'error, expected {expected_text2}, not in {actual_text2}'
        sleep(2)
        print("Test Passed")