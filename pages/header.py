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
    cart_empty_text = 'Your cart is empty'

    def input_text(self, param, param1):
        pass

    def search_product(self, search_text):
        self.input_text(search_text, '*self.SEARCH_FIELD')
        self.click(self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.wait_for_element_click(self.CART_ICON)
        self.wait_for_element(self.CART_ICON)

    def shopping_cart(self):
        # context.driver.find_element(By.XPATH, "//a[@aria-label='cart 0 items']").click()
        self.find_element(*self.CART_ICON).click()
        sleep(2)

    def verify_empty_shopping_cart(self):
        self.verify_text1(self.cart_empty_text, self.SHOPPING_CART_IS_EMPTY_MSG)
        print("Verify cart Empty Test Passed")

    def verify_cart_opened(self):
        self.verify_url('https://www.target.com/cart')
        print("Cart Opened Test Passed")

