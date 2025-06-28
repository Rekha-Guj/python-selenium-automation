from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')

    def input_text(self, param, param1):
        pass

    def search_product(self):
        self.input_text('tea', '*self.SEARCH_FIELD')
        self.click(self.SEARCH_BTN)
        sleep(10)

