from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, "search").send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)

@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert expected_text in actual_text, f"Error, Expected: {expected_text} not in Actual: {actual_text}"

