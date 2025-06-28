from encodings.punycode import selective_find

from pages.base_page import Page

from selenium.webdriver.common.by import By

class SearchResultPage(Page):

    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_worked(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text.lower()
        assert 'tea' in actual_text, f"Error: Expected '{tea}' not found in Actual '{actual_text}'"



