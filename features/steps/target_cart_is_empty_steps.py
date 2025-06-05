from behave import *
from selenium.webdriver.common.by import By
from time import sleep

@given('Target main page is open')
def step_impl(context):
    context.driver.get('https://target.com')
    sleep(1)

@when('Clicked on Shopping cart icon')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@aria-label='cart 0 items']").click()
    sleep(2)

@then('Verify that the shopping cart is empty')
def step_impl(context):
    expected_text2 = 'Your cart is empty'
    actual_text2 = context.driver.find_element(By.XPATH, "//h1[@class='styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh']").text
    assert expected_text2 in actual_text2, f'error, expected {expected_text2}, not in {actual_text2}'
    sleep(1)
    print("Test Passed")