from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By

# HW_1, 4

# @when('Search for {search_text}')
# def search_product(context, search_text):
#     context.search_text = search_text
#     context.driver.find_element(By.ID, "search").send_keys(search_text)
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)
#
# @then('Verify search worked {expected_result}')
# def verify_search_worked(context, expected_result):
#     #expected_text = search_text
#     actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
#     assert expected_result in actual_text, f"Error, Expected: {expected_result} not in Actual: {actual_text}"

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SEARCH_FIELD = (By.ID, "search")
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

@when('Search for {search_text}')
def search_product(context, search_text):
    # context.search_text = search_text
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_text)
    # context.driver.find_element(*SEARCH_BTN).click()
    # sleep(1)
    context.app.header.search_product()

@then('Verify search worked for {expected_result}')
def verify_search_worked(context, expected_result):
    # actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text.lower()
    # assert expected_result.lower() in actual_text, f"Error: Expected '{expected_result}' not found in Actual '{actual_text}'"

    context.app.search_result_page.verify_search_worked()

